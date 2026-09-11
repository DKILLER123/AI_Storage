"""Build the Version 43 EPUB (chapters 199-200 added: a morning after that begins with a cat who scratches once and formally gives up, three minutes of emergency cosmetics, eyelashes that lined up in formation, birthday privileges deferred until departure; then the Gangnam Tax Office's red carpet that is not a privilege but brown-nosing, 3.2 billion won and a wooden frame, a deputy director's résumé quietly burnished; then CJ CheilJedang, Director Baek, three sample cups, Red Velvet and five fruit flavors where the group's structure becomes the product's structure, a text flown across an ocean - don't be too happy - and a sister in Los Angeles who used to lose sleep over two letters and now carries the quote request to their door; then a tax-office post with twenty-three likes that grew teeth in its sixteenth minute, estimate tables, one name worth second through sixth combined, a headline that mugs him on the way in and gilds him by the end, one person growing into a company; then a half self-made dinner audited by a cat, the word romance said out loud by accident, and a van outside 'Producers' where Jung Han-teuk commits one of the greatest judgment errors of his career - also chapter 195's chat bubbles re-seated: Baek Si-on left, received; Lee Ji-eun right, sent) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_43.epub"


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
