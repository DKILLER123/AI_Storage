#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
apply_name_previews.py
Re-applies the book's hover-name linking scheme to the newest chapter files.

Faithful to the established behaviour observed across chapters 1-116:
  * A registered person's display name (and short aliases) becomes
        <a class="chr-inline" href="character-intro.xhtml#chr-SLUG"><span
        class="chr-peek"><img src="../images/SLUG.jpg" alt=""/></span>NAME</a>
  * Wrapping happens ONLY in plain text runs whose ancestor chain carries
    class tokens from the allowed set {"dialogue-line","thought",
    "page-wrapper"} (or no class at all).  Everything inside styled
    containers (location-stamp, chat-*, comment-*, highlight-block,
    facetime, phone-call, char-intro, metric/billboard/news blocks, lyric
    lines, etc.) is left untouched, exactly as in the existing chapters.
  * "Never wrap" inside any <a>, <title>, h1 or the document head.
  * Longest alias first; no re-wrapping of already-consumed spans.
"""
import re
import glob
import collections
import sys
import os

TEXT_DIR = "/home/user/work/epub_src/OEBPS/text"
MANUAL_ADD = {
    "LeBron James": "character-intro.xhtml#chr-lebron-james",
    "LeBron": "character-intro.xhtml#chr-lebron-james",
    "Rich Paul": "character-intro.xhtml#chr-rich-paul",
}
# Any class token encountered in an ancestor that is NOT in this set blocks
# wrapping.  Keep in sync with observed in-book behaviour.
ALLOWED_ANCESTOR_CLASSES = {"dialogue-line", "thought", "page-wrapper"}
# Whole names that must never receive hover links — including any alias
# that happens to be a substring of them (e.g. "Ji-eun" inside the real
# screenwriter "Park Ji-eun", who is non-rostered and stays plain text).
PROTECTED = {"Park Ji-eun"}


def build_image_map():
    """modal id -> portrait filename, read from the roster pages."""
    imap = {}
    for page in ("character-intro.xhtml", "characters.xhtml"):
        p = os.path.join(TEXT_DIR, page)
        if not os.path.exists(p):
            continue
        a = open(p, encoding="utf-8").read()
        for m in re.finditer(
            r'<div class="chr-modal" id="(chr-[^"]+)"(.*?)<img src="\.\./images/([^"]+)"',
            a,
            re.S,
        ):
            imap.setdefault(m.group(1), m.group(3))
    return imap


def build_alias_map():
    counter = collections.Counter()
    for fn in glob.glob(os.path.join(TEXT_DIR, "chapter-*.xhtml")):
        base = os.path.basename(fn)
        m = re.match(r"chapter-(\d+)\.xhtml", base)
        if not m:
            continue
        n = int(m.group(1))
        if n >= 117:  # the newest files are the target, not a source
            continue
        with open(fn, encoding="utf-8") as fh:
            h = fh.read()
        for am in re.finditer(
            r'<a class="chr-inline" href="([^"]+?)"[^>]*>(?:<[^>]+>)*([^<]+)</a>', h
        ):
            counter[(am.group(2).strip(), am.group(1))] += 1
    best = {}
    for (txt, href), c in counter.items():
        txt = txt.strip()
        if not txt:
            continue
        if txt not in best or c > best[txt][1]:
            best[txt] = (href, c)
    aliases = {txt: href for txt, (href, _c) in best.items()}
    aliases.update(MANUAL_ADD)
    return aliases


def wrap_text_run(text, aliases, imap, out):
    """Append `text` to out, replacing longest-first alias occurrences."""
    if not text:
        return
    if not aliases:
        out.append(text)
        return
    keys = sorted(aliases, key=len, reverse=True)
    i = 0
    n = len(text)
    while i < n:
        # protected compound names are copied verbatim (no inner alias match)
        protected_hit = None
        for ph in PROTECTED:
            if text.startswith(ph, i):
                protected_hit = ph
                break
        if protected_hit:
            out.append(protected_hit)
            i += len(protected_hit)
            continue
        matched = None
        # pick the longest alias that matches at i (keys pre-sorted by length)
        for k in keys:
            if text.startswith(k, i):
                # boundary: previous char must not be word char or hyphen
                prev = text[i - 1] if i > 0 else ""
                nxt = text[i + len(k)] if i + len(k) < n else ""
                if prev and (prev.isalnum() or prev == "-"):
                    continue
                if nxt and (nxt.isalnum() or nxt == "-"):
                    continue
                matched = k
                break
        if matched:
            mid = aliases[matched].rsplit("#", 1)[-1]
            img = imap.get(mid, (mid[4:] if mid.startswith("chr-") else mid) + ".jpg")
            out.append(
                '<a class="chr-inline" href="{0}"><span class="chr-peek">'
                '<img src="../images/{1}" alt=""/></span>{2}</a>'.format(
                    aliases[matched], img, matched
                )
            )
            i += len(matched)
        else:
            out.append(text[i])
            i += 1


def process(fn, aliases, imap):
    with open(fn, encoding="utf-8") as fh:
        h = fh.read()
    out = []
    # stack of (is_blocking, in_anchor, in_head)
    stack = []  # entries: dict(class_tokens, tag)
    i = 0
    n = len(h)
    while i < n:
        ch = h[i]
        if ch == "<":
            # find tag end, respecting comments
            if h.startswith("<!--", i):
                j = h.find("-->", i + 4)
                j = n if j == -1 else j + 3
                out.append(h[i:j])
                i = j
                continue
            j = h.find(">", i)
            j = n if j == -1 else j + 1
            tag = h[i + 1:j - 1].strip()
            # closing tag?
            if tag.startswith("/"):
                name = tag[1:].split()[0].lower()
                if name in ("title", "head"):
                    pass
                for k in range(len(stack) - 1, -1, -1):
                    if stack[k][0] == name:
                        del stack[k:]
                        break
            elif not tag.endswith("/") and not tag.startswith("!"):
                name = tag.split()[0].lower()
                # find class attr in this raw chunk
                cls = ""
                cm = re.search(r'class\s*=\s*"([^"]*)"', h[i:j])
                if cm:
                    cls = cm.group(1)
                stack.append((name, set(cls.split())))
            out.append(h[i:j])
            i = j
            continue
        # text character
        # determine blocking state
        in_anchor = any(t == "a" for t, _ in stack)
        blocking = False
        for name, classes in stack:
            if name in ("title", "head", "script", "style"):
                blocking = True
                break
            if classes:
                # block if any class token is not allowed
                extra = classes - ALLOWED_ANCESTOR_CLASSES
                if extra:
                    blocking = True
                    break
        if blocking or in_anchor:
            # consume whole text run verbatim
            j = i
            while j < n and h[j] != "<":
                j += 1
            out.append(h[i:j])
            i = j
            continue
        # gather text run
        j = i
        while j < n and h[j] != "<":
            j += 1
        run = h[i:j]
        wrap_text_run(run, aliases, imap, out)
        i = j
    result = "".join(out)
    with open(fn, "w", encoding="utf-8") as fh:
        fh.write(result)
    return result


def main():
    aliases = build_alias_map()
    imap = build_image_map()
    print("alias tokens:", len(aliases), "| portrait map:", len(imap))
    chapters = [int(a) for a in sys.argv[1:] if a.isdigit() and not a.startswith("-")]
    if not chapters:
        chapters = list(range(117, 125))
    targets = [os.path.join(TEXT_DIR, f"chapter-{n}.xhtml") for n in chapters]
    for fn in targets:
        if not os.path.exists(fn):
            print("missing", fn)
            continue
        process(fn, aliases, imap)
        txt = open(fn, encoding="utf-8").read()
        c = len(re.findall(r'class="chr-inline"', txt))
        print(os.path.basename(fn), "anchors:", c)
    # report remaining candidate names never wrapped (debug)
    if "--debug" in sys.argv:
        neww = {}
        for fn in targets:
            txt = open(fn, encoding="utf-8").read()
            for name in sorted(aliases, key=len, reverse=True):
                if re.search(r"(?<![A-Za-z0-9-])" + re.escape(name) + r"(?![A-Za-z0-9-])", txt):
                    neww.setdefault(name, 0)
                    neww[name] += txt.count(name)
        print("debug: aliases whose literal still appears anywhere:", len(neww))


if __name__ == "__main__":
    main()
