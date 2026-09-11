"""Build the Version 38 EPUB (chapters 189-190 added: an ESPN push alert stops a tour machine that cannot stop; a thermos of samgyetang argued into a patient and a fist tapped once - the day Kobe retires, they pull one big job; fifteen thousand seven hundred quiet bitcoins filed under digital assets; Dubai opens its eyes to Desert Rose and a wall of vinyl called a little; one of seven cars accepted with a public relations cardiac event in mind; Doha answers with Starboy and the Gibson that wrote music history; then a zombie boot camp, a seven-in-the-world car learning to be parked, a safekeeping negotiation with one sentence said too honestly into a phone, a translation too accurate to rebut, a brick doctrine, and a realist road picture at golden hour; plus the long-missing in-text debut cards for Lee Mi-kyung and Kevin Hart folded in) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_38.epub"


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
