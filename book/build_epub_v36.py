#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 36 EPUB (chapters 185-186 added: chaebols can't picket, but movies can fire - a farewell kept small at the security line, an Asian tyrant training an army, locusts at the ticket gate answered by thirty-six shows, a two-thousand-dollar stub in a VIP row, Corden's perfectly timed crack-up and the refund, CJ's sixty percent of a drink, the MAMA debt repaid with a joint venture, a hit list whose No. 1 is a certain teacher, and a backstage toast poured from a three-dollar sports drink; then forbidden from increasing America's GDP with your life - Kevin Hart and the booster seat, Charlie Puth handed twenty thousand people and a two-week deadline for a desert opening its eyes, a producer discovering geopolitics, Silicon Valley discussing retention rates, Vancouver singing Korean over the PA, a Russian doll of a risk list, three fansite masters flown fourteen hours to be grounded by their own idol, and the post that made the hot list before Korea woke up) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_36.epub"


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
