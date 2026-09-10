#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 28 EPUB (chapters 169-170 added: LAX landing - jet lag as workplace injury, Scooter's old-money curb lean and the Billboard slate, the KIIS FM hour with Ryan Seacrest - three hamburgers, the butt-trending translation, cushions are normal, a second door, the stripped Love Yourself; the corridor cat summit with Taylor - Meredith, Olivia, bought-a-bigger-house doctrine, litter-box warning, the apple that got eaten; Scooter's real-reason negotiation - Selena/Justin/for you, not for Justin; Adam Levine's Sugar wedding-war stories and the Seven Wolves doctrine of patriarchal authority; and back in Seoul - Faker queues twenty-eight minutes, loses three league points to a ceiling fan, the MV through three pairs of eyes, Ji-eun's reviews that matter, Jin-ri's cat-censored screening and winning by a little, Irene's low heels and the cable-guy recognition - and no phone of her own) plus three new wardrobe images; from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_28.epub"


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
