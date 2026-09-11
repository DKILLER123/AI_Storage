#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 32 EPUB (chapters 177-178 added: one album, two crowns, one step away - the RIAA platinum that crowns a human album, a screen that leads Korea by the hand to the front row, a DC emergency muster, Uptown Funk vs Love Yourself at Nos. 1 and 2, an Insight op-ed on the Grammy's regret, a trans-Pacific inspection tour of the New Year's Eve test show, the emotional-debt ledger, a KBS seniority plan flipped on its head, a spiral rescued by a tsundere's four words, Train to Busan signed; then trying to please people is exhausting - forty minutes early at Incheon, an invitation built from flimsy excuses, warm water copied in first class, thirteen hours of expert silence, permission to stop trying, fan gift bags that can fill a stomach, a perfect logic loop, a hotel downgraded to the wrong chain, and a whisper no one hears) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_32.epub"


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
