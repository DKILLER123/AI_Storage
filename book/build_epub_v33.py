#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 33 EPUB (chapters 179-180 added: I'll be there to save the day - the Temple Theatre on New Year's Eve, a TIME deputy editor's headline born in the third row, the scalper-coconut-water joke, the whole catalogue in one night, the cover-request game, a Furious 7 promise with one condition, a splice no studio approved, the a cappella drop, a Superman heard by exactly one person, an administrative-process heart, a countdown shouted into a phone camera, 2015 arriving in gold confetti, dumplings for ticket stubs, and the poisoning headline already typeset in Scooter's head; then the four-leaf clover gets the final say - army stew in Koreatown, a physics lecture that answers the wrong question, two afternoon tickets to Canada, an unfilial cap nailed down, a schedule that dies in a manager's throat, the Under Armour drop melting Melrose Avenue, does eating count, and a Beverly Hills lawn that declines to testify until it produces the fourth leaf) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_33.epub"


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
