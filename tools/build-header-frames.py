#!/usr/bin/env python3
"""
Rigenera l'array `FRAMES` (data-URI base64 dei frame dell'header) dentro index.html
a partire dagli SVG in assets/header/CAMP_XX.svg.

Uso:
    python3 tools/build-header-frames.py

I file vengono ordinati per numero (CAMP_00, CAMP_01, ...). L'array esistente
`var FRAMES=[ ... ];` nel motore "HEADER LOOP" di index.html viene sostituito.
Le slide restano identiche: qui si aggiorna solo cosa viene mostrato nel loop.
"""
import base64, os, re, sys, glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEADER_DIR = os.path.join(ROOT, "assets", "header")
INDEX = os.path.join(ROOT, "index.html")

def main():
    files = sorted(glob.glob(os.path.join(HEADER_DIR, "CAMP_*.svg")))
    if not files:
        sys.exit(f"Nessun CAMP_*.svg trovato in {HEADER_DIR}")
    uris = []
    for p in files:
        b = open(p, "rb").read()
        uris.append("data:image/svg+xml;base64," + base64.b64encode(b).decode())
    frames_js = "var FRAMES=[\n" + ",\n".join('"' + u + '"' for u in uris) + "\n];"

    html = open(INDEX, encoding="utf8").read()
    anchor = html.find("HEADER LOOP (push up")
    if anchor == -1:
        sys.exit("Motore 'HEADER LOOP' non trovato in index.html")
    s = html.find("var FRAMES=[", anchor)
    e = html.find("\n];", s)
    if s == -1 or e == -1:
        sys.exit("Array FRAMES non trovato in index.html")
    e += len("\n];")
    html = html[:s] + frames_js + html[e:]
    open(INDEX, "w", encoding="utf8").write(html)
    print(f"OK — {len(uris)} frame incorporati in index.html:")
    for p in files:
        print("  ", os.path.basename(p))

if __name__ == "__main__":
    main()
