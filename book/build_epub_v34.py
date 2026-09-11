#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 34 EPUB (chapters 181-182 added: give the ankle a vacation - a midnight knock that asks one ordinary question, an invitation that sounds like third-rate cinema, don't fight me for clothes, the Billboard update that robs the Federal Reserve with a burlap sack, an interview outline cut from thirty to ten, a special report that stops four girls mid-chew, one parcel addressed by S.W Studio, a card that says give the ankle a vacation, a sold-out Gangnam pop-up, and a verdict that accepts no appeal; then rarer than the aurora, you - a scarf surrendered at the airstair, a trash can of great bearing, a snow war at the edge of centuries-old pines, hot water that would lose its dignity, the disappointment permitted to hurt, a four-leaf clover that will not wilt, a two-in-the-morning security log that was never filed, a clasp hotter than any heat pack, the green curtain that made the whole night step aside, a kiss interrupted by physics and then avenged, and the lie at minus thirty) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_34.epub"


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
