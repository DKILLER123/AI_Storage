#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 30 EPUB (chapters 173-174 added: the highest-value steal in history - a Christmas special shot with three props and a twelve-percent smile, the league borrows a singer for Lakers-Bulls without Kobe, Scooter is pulled off to Justin's trouble, the Dubai-trap timeline unfurls with a memo to Dispatch's Director Lim, a frozen bronze Jordan, the United Center opening of Legend, Wiz Khalifa's Furious 7 heartbreak, the See You Again demo in one earbud, the favor-chain meditation, the BodyArmor side-deal, and the eyebrow identification feature; then crying counts toward the clock - Charlie Puth's two papers and one pepper spray, an SB Projects card at the door, the UA gift bag with tags on, four Christmas chat threads across three time zones, the steak that stayed untouched, a twenty-minute meeting with its own arithmetic, five hundred thousand dollars against fifty thousand, the song and the person negotiated separately, and a stomach that betrayed three secrets) plus the new UA gift flat-lay wardrobe image; from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_30.epub"


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
