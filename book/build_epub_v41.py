"""Build the Version 41 EPUB (chapters 195-196 added: Europe's map stamped at the O2 with an award that cannot be won by fan votes - so the Korean fans can finally sleep; a double champion who thanks his cat, his guitar tech and a fried-chicken shop; a buffet that explains the industrial revolution; a hummed rhythm disdained by its own author and matched, instantly, to the most terrifying cash machine not yet assembled; Billboard Thief versus King of the Dead Drafts; a trophy photographed as garnish, pasta beside it, second thing first; a guitar custody explained in six words; then March's monster highway, a passportless farewell on the radio, a dethroned chart and a Busan auntie's one-bowl diagnosis; and Cindy's first morning, lost by inches to one hot chocolate, two support vans and a card inside a script; also the location-stamp ls-time redesigned from a capsule to a self-growing box so the contents can never leave) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_41.epub"


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
