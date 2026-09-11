#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 35 EPUB (chapters 183-184 added: a moving city's GDP - a fake sleep that fools nobody, Pierre's Yellowknife confession, a handshake and a hand held through two gloves at the airstair, Schrodinger's necklace, a hotel bed renovated into a disaster zone, the Goo Hara video debrief that certifies a heart-arsonist, Exhibit No. 1, five percent of BodyArmor and the whole of Asia with Kobe driving, fourteen cities bidding for a mobile stimulus package, and the commendation banner Scooter declines in favor of cash; then the one-upmanship of oil money - a tour grid engineered like a machine, scalper economics answered with more shows, Justin Bieber calling three times, Dubai and Doha bidding identical millions forty minutes apart, twenty-eight shows becoming thirty-two, the Sugar belt that never swung, you won't need to talk, a syllable that arrives notarized, Nobu Malibu and a girl introduced as a lucky charm, the most romantic thing he ever said to Wiz was I'm a finished product, love lines filing themselves as small talk in English, Blin doesn't need to think, and the survival instinct of a focused front seat) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_35.epub"


def add(zf, path, arc, compress):
    with open(path, "rb") as fh:
        data = fh.read()
    zi = zipfile.ZipInfo(arc, date_time=time.localtime(os.path.getmtime(path))[:6])
    zi.compress_type = zipfile.ZIP_STORED if not compress else zipfile.ZIP_DEFLATED
    zi.external_attr = 0o644 << 16
    zf.writestr(zi, data)


with zipfile.ZipFile(OUT, "w", allowZip64=True) as zf:
    # mimetype must be first and stored
    add(zf, os.path.join(SRC, "mimetype"), "mimetype", False)
    for root, dirs, files in os.walk(SRC):
        dirs.sort()
        files.sort()
        for fn in files:
            full = os.path.join(root, fn)
            rel = os.path.relpath(full, SRC).replace(os.sep, "/")
            if rel == "mimetype":
                continue
            if fn.startswith(".") or fn.endswith(("~", ".pyc")):
                continue
            add(zf, full, rel, True)

size = os.path.getsize(OUT)
print("built", OUT, size, "bytes")
with zipfile.ZipFile(OUT) as zf:
    names = zf.namelist()
    print("entries:", len(names))
    print("first three:", names[:3])
    tops = sorted({n.split("/")[0] for n in names})
    print("top level:", tops)
    for info in zf.infolist()[:3]:
        print(info.filename, "compress_type", info.compress_type)
