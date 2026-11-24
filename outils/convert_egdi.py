#!/usr/bin/env python3
"""Prépare la carte géologique européenne au 1/1 000 000 (EGDI, EuroGeoSurveys, CC BY 4.0)
pour l'application : simplification, passage en longitude/latitude, découpage en carreaux de 2° × 2°.

Usage : python3 convert_egdi.py sources/GeologicUnitView.gpkg ../geol1m-eu
Aucune bibliothèque externe : lecture SQLite + WKB, projection Lambert conique (EPSG:3034) écrite ici.
"""
import sqlite3, struct, math, json, sys, os, collections

# ---------- Projection ETRS89 / LCC Europe (EPSG:3034) -> longitude/latitude ----------
A, F = 6378137.0, 1 / 298.257222101
E2 = F * (2 - F); EE = math.sqrt(E2)
LAT1, LAT2, LAT0, LON0 = (math.radians(v) for v in (35, 65, 52, 10)); X0, Y0 = 4000000.0, 2800000.0
def _m(p): return math.cos(p) / math.sqrt(1 - E2 * math.sin(p) ** 2)
def _t(p): s = math.sin(p); return math.tan(math.pi / 4 - p / 2) / ((1 - EE * s) / (1 + EE * s)) ** (EE / 2)
N = (math.log(_m(LAT1)) - math.log(_m(LAT2))) / (math.log(_t(LAT1)) - math.log(_t(LAT2)))
FF = _m(LAT1) / (N * _t(LAT1) ** N)
R0 = A * FF * _t(LAT0) ** N
def fwd(lon, lat):
    r = A * FF * _t(math.radians(lat)) ** N; th = N * (math.radians(lon) - LON0)
    return X0 + r * math.sin(th), Y0 + R0 - r * math.cos(th)
def inv(x, y):
    dx, dy = x - X0, R0 - (y - Y0); r = math.copysign(math.hypot(dx, dy), N); th = math.atan2(dx, dy)
    t = (r / (A * FF)) ** (1 / N); p = math.pi / 2 - 2 * math.atan(t)
    for _ in range(8):
        s = math.sin(p); p = math.pi / 2 - 2 * math.atan(t * ((1 - EE * s) / (1 + EE * s)) ** (EE / 2))
    return math.degrees(th / N + LON0), math.degrees(p)

# ---------- Lecture WKB (GeoPackage) ----------
def rings_of(blob):
    flags = blob[3]; env = (flags >> 1) & 7; off = 8 + [0, 32, 48, 48, 64][env]
    out = []
    def geom(o):
        bo = '<' if blob[o] == 1 else '>'; t = struct.unpack(bo + 'I', blob[o + 1:o + 5])[0]; o += 5
        base = t % 1000; dim = 3 if (t // 1000) in (1, 2) else 4 if t // 1000 == 3 else 2
        if base == 3:  # Polygon
            n = struct.unpack(bo + 'I', blob[o:o + 4])[0]; o += 4; poly = []
            for _ in range(n):
                k = struct.unpack(bo + 'I', blob[o:o + 4])[0]; o += 4
                v = struct.unpack(bo + 'd' * (k * dim), blob[o:o + 8 * k * dim]); o += 8 * k * dim
                poly.append([(v[i], v[i + 1]) for i in range(0, len(v), dim)])
            out.append(poly); return o
        if base in (6, 12, 7):  # MultiPolygon, MultiSurface, GeometryCollection
            n = struct.unpack(bo + 'I', blob[o:o + 4])[0]; o += 4
            for _ in range(n): o = geom(o)
            return o
        if base == 10:  # CurvePolygon : on prend les sommets des courbes (rendu au 1/1M suffisant)
            n = struct.unpack(bo + 'I', blob[o:o + 4])[0]; o += 4; poly = []
            for _ in range(n):
                pts = []; o = curve(o, pts); poly.append(pts)
            out.append(poly); return o
        raise ValueError('type %d' % t)
    def curve(o, pts):
        bo = '<' if blob[o] == 1 else '>'; t = struct.unpack(bo + 'I', blob[o + 1:o + 5])[0]; o += 5; base = t % 1000
        dim = 3 if (t // 1000) in (1, 2) else 4 if t // 1000 == 3 else 2
        if base in (2, 8):
            k = struct.unpack(bo + 'I', blob[o:o + 4])[0]; o += 4
            v = struct.unpack(bo + 'd' * (k * dim), blob[o:o + 8 * k * dim]); o += 8 * k * dim
            pts.extend((v[i], v[i + 1]) for i in range(0, len(v), dim)); return o
        if base == 9:
            n = struct.unpack(bo + 'I', blob[o:o + 4])[0]; o += 4
            for _ in range(n): o = curve(o, pts)
            return o
        raise ValueError('courbe %d' % t)
    geom(off); return out

# ---------- Simplification (Douglas-Peucker, en mètres) ----------
def dp(pts, tol):
    if len(pts) < 5: return pts
    keep = [False] * len(pts); keep[0] = keep[-1] = True; st = [(0, len(pts) - 1)]; t2 = tol * tol
    while st:
        a, b = st.pop(); ax, ay = pts[a]; bx, by = pts[b]; dx, dy = bx - ax, by - ay; L = dx * dx + dy * dy; best, bi = -1, -1
        for i in range(a + 1, b):
            px, py = pts[i]
            if L == 0: d = (px - ax) ** 2 + (py - ay) ** 2
            else:
                u = max(0, min(1, ((px - ax) * dx + (py - ay) * dy) / L)); d = (ax + u * dx - px) ** 2 + (ay + u * dy - py) ** 2
            if d > best: best, bi = d, i
        if best > t2: keep[bi] = True; st += [(a, bi), (bi, b)]
    return [p for p, k in zip(pts, keep) if k]
def area(r): return abs(sum(r[i][0] * r[i - 1][1] - r[i - 1][0] * r[i][1] for i in range(len(r)))) / 2

# ---------- Découpage d'un anneau par un rectangle (Sutherland-Hodgman) ----------
def clip(ring, x0, y0, x1, y1):
    def cut(pts, inside, inter):
        out = []
        for i in range(len(pts)):
            p, q = pts[i - 1], pts[i]; pi, qi = inside(p), inside(q)
            if qi:
                if not pi: out.append(inter(p, q))
                out.append(q)
            elif pi: out.append(inter(p, q))
        return out
    def ix(x): return lambda p, q: (x, p[1] + (q[1] - p[1]) * (x - p[0]) / (q[0] - p[0]))
    def iy(y): return lambda p, q: (p[0] + (q[0] - p[0]) * (y - p[1]) / (q[1] - p[1]), y)
    pts = ring
    for inside, inter in ((lambda p: p[0] >= x0, ix(x0)), (lambda p: p[0] <= x1, ix(x1)), (lambda p: p[1] >= y0, iy(y0)), (lambda p: p[1] <= y1, iy(y1))):
        if not pts: break
        pts = cut(pts, inside, inter)
    return pts

def short(uri):
    return (uri or '').rstrip('/').split('/')[-1] if uri and 'nil' not in uri else ''

def main(src, dst, tol=120.0, minarea=4e4, q=1e4, step=2):
    os.makedirs(dst, exist_ok=True)
    c = sqlite3.connect(src)
    tiles = collections.defaultdict(list)   # (lat, lon) -> [(legend key, rings)]
    legend = {}; n = 0; kept = 0
    for blob, lit, age, oa, ya, nold, nyoung, name, descr, country in c.execute(
            "select geom, representativelithology_uri, representativeage_uri, representativeolderage_uri_href, representativeyoungerage_uri_href, numericolderage, numericyoungerage, name, description, country from GeologicUnitView"):
        n += 1
        if not blob: continue
        d = (descr or '').strip()
        # beaucoup de « descriptions » ne sont que des identifiants internes : on ne garde qu'un vrai texte (plusieurs mots)
        if len(d) < 12 or len(d.split()) < 3 or d.startswith('{'): d = ''
        try: no = float(nold) if nold not in (None, '', 'unknown') else None
        except ValueError: no = None
        try: ny = float(nyoung) if nyoung not in (None, '', 'unknown') else None
        except ValueError: ny = None
        key = (short(lit), short(age), short(oa), short(ya), no, ny, d[:220], (country or '').split('-')[0].split('_')[0].upper()[:2])
        li = legend.setdefault(key, len(legend))
        for poly in rings_of(blob):
            rings = []
            for r in poly:
                r = dp(r, tol)
                if len(r) >= 4 and area(r) >= minarea: rings.append([inv(x, y) for x, y in r])
            if not rings: continue
            xs = [p[0] for p in rings[0]]; ys = [p[1] for p in rings[0]]
            for la in range(math.floor(min(ys) / step) * step, math.floor(max(ys) / step) * step + 1, step):
                for lo in range(math.floor(min(xs) / step) * step, math.floor(max(xs) / step) * step + 1, step):
                    cr = []
                    for r in rings:
                        cc = clip(r, lo, la, lo + step, la + step)
                        if len(cc) >= 3: cr.append(cc)
                    if cr: tiles[(la, lo)].append((li, cr)); kept += 1
        if n % 20000 == 0: print(n, 'unités lues', file=sys.stderr)
    keys = [None] * len(legend)
    for k, i in legend.items(): keys[i] = k
    index = []; total = 0
    for (la, lo), items in sorted(tiles.items()):
        used = sorted({li for li, _ in items}); remap = {li: j for j, li in enumerate(used)}
        polys = []
        for li, rings in items:
            enc = []; bx0 = by0 = 1e18; bx1 = by1 = -1e18
            for r in rings:
                flat = []; px = py = 0
                for x, y in r:
                    X, Y = round(x * q), round(y * q)
                    if flat and X == px and Y == py: continue
                    flat += [X - px, Y - py]; px, py = X, Y
                    bx0, by0, bx1, by1 = min(bx0, X), min(by0, Y), max(bx1, X), max(by1, Y)
                if len(flat) >= 6: enc.append(flat)
            if enc: polys.append([remap[li], [bx0, by0, bx1, by1], enc])
        if not polys: continue
        name = 'eu_%s%02d%s%03d' % ('n' if la >= 0 else 's', abs(la), 'e' if lo >= 0 else 'w', abs(lo))
        data = {'source': 'EGDI 1:1M pan-european surface geology (EuroGeoSurveys, CC BY 4.0)', 'q': q, 'tol_m': tol,
                'legend': [list(keys[li]) for li in used], 'polys': polys}
        txt = json.dumps(data, separators=(',', ':'), ensure_ascii=False)
        open(os.path.join(dst, name + '.json'), 'w', encoding='utf-8').write(txt); total += len(txt)
        index.append({'name': name, 'bbox': [lo, la, lo + step, la + step]})
    json.dump(index, open(os.path.join(dst, 'index.json'), 'w'), separators=(',', ':'))
    print('%d unités, %d morceaux, %d carreaux, %.1f Mo' % (n, kept, len(index), total / 1e6), file=sys.stderr)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
