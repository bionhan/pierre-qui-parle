"""BD Charm-50 (couche S_FGEOL d'un département) -> fichier JSON compact pour l'application.
Usage : python3 -I convert.py <chemin sans extension de ..._S_FGEOL_2154> <sortie.json> [tolérance en m, défaut 20]"""
import sys, json, gzip, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import shpio

def simplify(pts, tol):
    """Douglas-Peucker itératif sur un anneau fermé (coordonnées en mètres)."""
    n = len(pts)
    if tol <= 0 or n < 5: return pts
    keep = [False] * n; keep[0] = keep[n-1] = True
    # un anneau fermé a ses deux extrémités confondues : on ancre aussi le point le plus éloigné du départ
    far = max(range(n), key=lambda i: (pts[i][0]-pts[0][0])**2 + (pts[i][1]-pts[0][1])**2); keep[far] = True
    stack = [(0, far), (far, n-1)]; t2 = tol * tol
    while stack:
        a, b = stack.pop()
        if b - a < 2: continue
        ax, ay = pts[a]; bx, by = pts[b]; dx, dy = bx-ax, by-ay; L = dx*dx + dy*dy
        best, bi = -1.0, -1
        for i in range(a+1, b):
            px, py = pts[i]
            if L == 0: d = (px-ax)**2 + (py-ay)**2
            else:
                t = max(0.0, min(1.0, ((px-ax)*dx + (py-ay)*dy) / L))
                d = (px-ax-t*dx)**2 + (py-ay-t*dy)**2
            if d > best: best, bi = d, i
        if best > t2: keep[bi] = True; stack += [(a, bi), (bi, b)]
    out = [p for p, k in zip(pts, keep) if k]
    return out if len(out) >= 4 else pts

def cmyk_hex(c, m, y, k):
    f = lambda v: round(255 * (1 - v/100) * (1 - k/100))
    return '#%02x%02x%02x' % (f(c), f(m), f(y))

def convert(src, dst, tol=20.0):
    _, rows = shpio.read_dbf(src + '.dbf'); shapes = shpio.read_shp_polygons(src + '.shp')
    assert len(rows) == len(shapes)
    legend, index, polys, npts_in, npts_out = [], {}, [], 0, 0
    Q = 1e5   # quantification : 1e-5 degré, soit environ 1 m
    for row, rings in zip(rows, shapes):
        if not rings: continue
        key = (row['NOTATION'], row['DESCR'])
        if key not in index:
            index[key] = len(legend)
            legend.append([row['NOTATION'], row['DESCR'], cmyk_hex(*(float(row[k] or 0) for k in ('C_FOND', 'M_FOND', 'J_FOND', 'N_FOND')))])
        enc, bb = [], [1e9, 1e9, -1e9, -1e9]
        for ring in rings:
            npts_in += len(ring); s = simplify(ring, tol); npts_out += len(s)
            flat, px, py = [], 0, 0
            for x, y in s:
                lon, lat = shpio.l93_to_wgs(x, y); qx, qy = round(lon * Q), round(lat * Q)
                flat += [qx - px, qy - py]; px, py = qx, qy     # codage par différences
                bb = [min(bb[0], qx), min(bb[1], qy), max(bb[2], qx), max(bb[3], qy)]
            enc.append(flat)
        polys.append([index[key], bb, enc])
    data = {'source': 'BRGM, BD Charm-50 (Licence Ouverte)', 'q': Q, 'tol_m': tol, 'legend': legend, 'polys': polys}
    raw = json.dumps(data, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    open(dst, 'wb').write(raw)
    return dict(polys=len(polys), legend=len(legend), pts_in=npts_in, pts_out=npts_out, json_mb=len(raw)/1e6, gz_mb=len(gzip.compress(raw, 9))/1e6)

if __name__ == '__main__':
    print(convert(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 20.0))
