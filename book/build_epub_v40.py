"""Build the Version 40 EPUB (chapters 193-194 added: a watchdog delegation at a fashion-week backstage - work self-managing, food self-hunting, actresses denied; a brand dinner exited on the grounds of a lesson; a dress code no teacher's union would certify; a syllabus in four bullets; a student too fast to teach; Cindy's demo take one and the remix that made it colder; knives held in her own hand; she is a character, you are a living person; two kisses timed to a metronome at sixty-seven BPM; a file renamed into a contradiction on purpose; a bridge that dropped half a key; then SIXTEEN on a JYP desk, a queue-jump filed with perfect confidence, the word Dream scribbled on a back cover, a morning that remembered temperature, a 1.2-meter case with numbered labels, a 1962 Gibson J-160E insured at two and a half million dollars, a half-century of British temptation declined, one string plucked once, and Three Bears under serious consideration) from epub_src (mimetype stored first)."""
import os, zipfile, time

SRC = "/home/user/work/epub_src"
OUT = "Seoul_Starting_With_Debt_Collection__Version_40.epub"


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
