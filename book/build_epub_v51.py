"""Build the Version 51 EPUB (chapters 213-214 added: a coffee-house piano nobody was asked to silence, a bench one fist wide, a director who stopped drinking his coffee mid-sip, ten million dollars and a union-minimum fee, a video that leaked anyway, three condemned Tom Fords and one resurrected brief, an examiner who says it with lamplight, a waistband logo open for retail, and a swap of songs between two geniuses with no taste between them) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_51.epub"


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
