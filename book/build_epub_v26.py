#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 26 EPUB (chapters 165-166 added: the thank-you concert in full - the crowd singing Legend over the headliner, the hush gesture, Sign of the Times as a programmed cooldown, the audience cam ride with Sulli caught in the down coat, Red Velvet's Chu~? tribute and Happiness with the director's Irene doctrine, BTS Danger and seven names, IU's bunny ears and the guitar reply-version of Way Back Home, Friday, the single-people duet, Can't Take My Eyes Off You, the deep bow, the mother-son receipt-length reunion backstage, and the Red Velvet van call that reprices a rookie) plus three new wardrobe images; from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_26.epub"


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
    print("mimetype stored?", zipfile.ZipInfo.from_file(OUT) is not None and True)
    # check compression of mimetype
    for info in zf.infolist()[:3]:
        print(info.filename, "compress_type", info.compress_type)
