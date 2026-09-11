"""Build the Version 37 EPUB (chapters 187-188 added: TIME filed him between the Wall Street Journal and The Economist and three fansite masters bought out an airport bookstore; Lee Ji-eun did English reading practice for five minutes and smuggled the red border into her bag; the luxury queue was told the market must stay liquid; Chicago heard ninety seconds of See You Again before the world and applauded in the wrong silence; Toronto watched its most famous son harmonize on another man's chorus and get told he just sang it; a salad eaten under armed guard; a Charlie Puth research trip that touched sand and champagne in equal measure and renamed a demo SW Baek, renamed back on the spot; Desert Rose approved, Starboy paired to Doha; an Arabian horse declined for lack of a stable; a diplomatic-incident prevention program; and five hundred thousand dollars politely not taken in the name of art; plus the Vancouver chorus finally set down in its own box) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_37.epub"


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
