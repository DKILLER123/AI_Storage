#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the Version 29 EPUB (chapters 171-172 added: the play count that goes to war for its country - a portal newsroom refuses a bare crown and bolts on Nicki Minaj and Taylor Swift qualifiers, the 7:46 a.m. push conscripts the morning commute, KBS breakfast TV and a gimbap uncle, IU's 99+ red morning and the Gucci Milan invitation with the ELLE Korea February cover, a three-word thank-you that spends the night unread; then Los Angeles - Kobe's forty-minute lunch authorization, and in Newport Coast the five-million-dollar Pepsi cash contract dies quietly beside the grill, BodyArmor equity signed for dessert, a steak race with no rules, Gi-Gi's Lakers audition, and a manager who stitches his wounds then haggles for extra points) plus the new BodyArmor bottle image; from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_29.epub"


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
