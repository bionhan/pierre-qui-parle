"""Convertit toute la BD Charm-50 en fichiers JSON départementaux pour l'application.
Usage : python3 -I convert_all.py <dossier source> <dossier de sortie> [tolérance en m, défaut 20]
Le dossier source peut contenir les archives GEO050K_HARM_*.zip et/ou des dossiers déjà décompressés.
Produit un fichier <nom>.json par archive et un index.json (emprise et taille de chaque fichier)."""
import sys, os, re, json, zipfile, tempfile, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import convert

def find_layers(root):
    for d, _, files in os.walk(root):
        for f in files:
            if re.search(r'_S_FGEOL(_CGH)?_2154\.shp$', f, re.I) and '_CGH_' not in f.upper():
                yield os.path.join(d, f[:-4])

def name_of(base):
    m = re.search(r'GEO050K_HARM_(.+?)_S_FGEOL', os.path.basename(base), re.I)
    return 'dept_' + (m.group(1) if m else os.path.basename(base))

def bbox_of(path):
    d = json.load(open(path, encoding='utf-8')); q = d['q']
    bbs = [p[1] for p in d['polys']]
    return [min(b[0] for b in bbs) / q, min(b[1] for b in bbs) / q, max(b[2] for b in bbs) / q, max(b[3] for b in bbs) / q]

def run(src, out, tol=20.0):
    os.makedirs(out, exist_ok=True); index, tmp = [], None
    jobs = list(find_layers(src))
    zips = sorted(os.path.join(src, f) for f in os.listdir(src) if f.lower().endswith('.zip'))
    def do(base):
        name = name_of(base); dst = os.path.join(out, name + '.json')
        st = convert.convert(base, dst, tol)
        index.append({'name': name, 'file': name + '.json', 'bbox': [round(v, 5) for v in bbox_of(dst)], 'bytes': os.path.getsize(dst), 'formations': st['legend']})
        print('%-60s %6d polygones %5.1f Mo' % (name, st['polys'], st['json_mb']), flush=True)
    for base in jobs: do(base)
    for z in zips:
        tmp = tempfile.mkdtemp()
        try:
            with zipfile.ZipFile(z) as zf:
                keep = [n for n in zf.namelist() if re.search(r'_S_FGEOL_2154\.(shp|dbf|shx)$', n, re.I)]
                for n in keep:   # extraction à plat, sans suivre les chemins de l'archive
                    with zf.open(n) as a, open(os.path.join(tmp, os.path.basename(n)), 'wb') as b: shutil.copyfileobj(a, b)
            for base in find_layers(tmp): do(base)
        except Exception as e: print('ECHEC', os.path.basename(z), e, flush=True)
        finally: shutil.rmtree(tmp, ignore_errors=True)
    # fusion avec un index existant (traitement en plusieurs lots)
    ip = os.path.join(out, 'index.json')
    old = {e['name']: e for e in (json.load(open(ip, encoding='utf-8')) if os.path.exists(ip) else [])}
    old.update({e['name']: e for e in index})
    json.dump(sorted(old.values(), key=lambda e: e['name']), open(ip, 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    print(len(old), 'départements dans index.json ; total %.1f Mo' % (sum(e['bytes'] for e in old.values()) / 1e6))

if __name__ == '__main__':
    run(sys.argv[1], sys.argv[2], float(sys.argv[3]) if len(sys.argv) > 3 else 20.0)
