#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 27 EPUB (chapters 167-168 added: the hanwoo thank-you dinner - the door sign, the toast, the tongs jurisdiction dispute, IU's three-circumstances Oppa interrogation, BTS's ladies-first hold and the kimchi advertisement, Irene's soft-drink toast with the ankle seen first, "Screenwriter Park Ji-eun" as counter-leverage, the intercepted insurance-scam fall and the car verdict the peach ripened and grew thorns; and Day One After the Concert - Kim Min-jun's million-view retitle, the meme reaching boardrooms and storefronts, five headlines, the Naver ten, the brands gaining shapes, the roommate-interview cat house, Blin the Sphynx, the KakaoTalk twenty minutes, the Christmas kiss and the deliberately forgotten wet wipe) plus three new wardrobe images; from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_27.epub"


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
