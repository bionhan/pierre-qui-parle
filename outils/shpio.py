"""Lecture minimale de shapefile (polygones) + DBF, et conversion Lambert-93 -> WGS84. Sans dépendance."""
import struct, math

def read_dbf(path, encoding='latin-1'):
    with open(path, 'rb') as f:
        hdr = f.read(32); n, hlen, rlen = struct.unpack('<IHH', hdr[4:12])
        fields = []
        while True:
            d = f.read(32)
            if d[0] == 0x0D: break
            fields.append((d[:11].split(b'\0')[0].decode('ascii'), chr(d[11]), d[16]))
        f.seek(hlen); rows = []
        for _ in range(n):
            rec = f.read(rlen); pos = 1; row = {}
            for name, typ, ln in fields:
                row[name] = rec[pos:pos+ln].decode(encoding, 'replace').strip(); pos += ln
            rows.append(row)
    return fields, rows

def read_shp_polygons(path):
    """Renvoie pour chaque enregistrement une liste d'anneaux [(x, y), ...] (None si forme vide)."""
    out = []
    with open(path, 'rb') as f:
        f.seek(100)
        while True:
            h = f.read(8)
            if len(h) < 8: break
            clen = struct.unpack('>i', h[4:])[0] * 2
            rec = f.read(clen); st = struct.unpack('<i', rec[:4])[0]
            if st == 0: out.append(None); continue
            assert st in (5, 15, 25), st
            nparts, npts = struct.unpack('<ii', rec[36:44])
            parts = list(struct.unpack('<%di' % nparts, rec[44:44+4*nparts])) + [npts]
            base = 44 + 4*nparts
            pts = struct.unpack('<%dd' % (2*npts), rec[base:base+16*npts])
            out.append([[(pts[2*i], pts[2*i+1]) for i in range(parts[k], parts[k+1])] for k in range(nparts)])
    return out

# Lambert-93 (RGF93, ellipsoïde GRS80) -> longitude, latitude en degrés
_N, _C, _XS, _YS, _E, _L0 = 0.7256077650532670, 11754255.426096, 700000.0, 12655612.049876, 0.0818191910428158, math.radians(3)
def l93_to_wgs(x, y):
    r = math.hypot(x - _XS, y - _YS); g = math.atan((x - _XS) / (_YS - y))
    lon = _L0 + g / _N; iso = -math.log(abs(r / _C)) / _N
    lat = 2 * math.atan(math.exp(iso)) - math.pi / 2
    for _ in range(8):
        es = _E * math.sin(lat)
        lat = 2 * math.atan(((1 + es) / (1 - es)) ** (_E / 2) * math.exp(iso)) - math.pi / 2
    return math.degrees(lon), math.degrees(lat)
