#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Anchor-wrap pass for V29 (ch171-172), per SKILL.md §4 mechanics.

Wraps carded-name mentions in CLASSLESS <p> and <p class="dialogue-line">
paragraphs only. Longest-first alternation, skips matches that overlap an
existing chr-inline anchor, possessives/suffixes stay outside the anchor
(lookahead (?![\\w-])). Display rows (pc-*, chat-*, nd-*, sv-*, ls-*, nv-*,
lb-*, al-*, fb-*, comment-*) are never touched.
"""
import re

FORMS = [
    # (form, chr-id, image) — longest-first
    ("Baek Si-on",    "chr-baek-sion",     "baek-sion.jpg"),
    ("Baek Eun-ah",   "chr-baek-eunah",    "eun-ah.jpg"),
    ("Scooter Braun", "chr-scooter-braun", "scooter-braun.jpg"),
    ("Jeong Han-teuk","chr-jeong-hanteuk", "han-teuk.jpg"),
    ("Choi Jin-ri",   "chr-choi-jinri",    "sulli.jpg"),
    ("Yoon Hye-ja",   "chr-yoon-hyeja",    "yoon-hyeja.jpg"),
    ("Wiz Khalifa",   "chr-wiz-khalifa",   "wiz-khalifa.jpg"),
    ("Charlie Puth",  "chr-charlie-puth",  "charlie-puth.jpg"),
    ("Kim Jae-wook",  "chr-kim-jaewook",   "kim-jaewook.jpg"),
    ("Lee Joon-ik",   "chr-lee-joonik",    "lee-joonik.jpg"),
    ("Goo Hara",      "chr-goo-hara",      "goo-hara.jpg"),
    ("Son Nam-won",   "chr-son-namwon",    "son-nam-won.jpg"),
    ("Bong Joon-ho",  "chr-bong-joonho",   "bong-joonho.jpg"),
    ("LeBron James",  "chr-lebron-james",  "lebron-james.jpg"),
    ("Hara",          "chr-goo-hara",      "goo-hara.jpg"),
    ("Bong",          "chr-bong-joonho",   "bong-joonho.jpg"),
    ("LeBron",        "chr-lebron-james",  "lebron-james.jpg"),
    ("Joo-hyun",      "chr-irene",         "irene.jpg"),
    ("Irene",         "chr-irene",         "irene.jpg"),
    ("Lee Mi-kyung",   "chr-lee-mikyung",   "lee-mikyung.jpg"),
    ("Baek Jeong-hoon","chr-baek-jeonghoon","baek-jeonghoon.jpg"),
    ("Kevin Hart",     "chr-kevin-hart",    "kevin-hart.jpg"),
    ("Chang Byung-gyu", "chr-chang-byunggyu", "chang-byunggyu.jpg"),
    ("Yeon Sang-ho",   "chr-yeon-sangho",   "yeon-sangho.jpg"),
    ("Seul-gi",        "chr-seulgi",        "seulgi.jpg"),
    ("Seung-wan",      "chr-wendy",         "wendy.jpg"),
    ("Joy",            "chr-joy",           "joy.jpg"),
    ("Yeri",           "chr-yeri",          "yeri.jpg"),
    ("Park Sang-min",  "chr-park-sangmin",  "park-sangmin.jpg"),
    ("Jeong-hoon",     "chr-baek-jeonghoon","baek-jeonghoon.jpg"),
    ("Mi-kyung",       "chr-lee-mikyung",   "lee-mikyung.jpg"),
    ("Kevin",          "chr-kevin-hart",    "kevin-hart.jpg"),
    ("James Corden",   "chr-james-corden",  "james-corden.jpg"),
    ("Jung Jae-joon",  "chr-jung-jae-joon", "jung-jae-joon.jpg"),
    ("Corden",         "chr-james-corden",  "james-corden.jpg"),
    ("Jae-joon",       "chr-jung-jae-joon", "jung-jae-joon.jpg"),
    ("Ariana Grande", "chr-ariana-grande", "ariana-grande.jpg"),
    ("Behati Prinsloo","chr-behati",       "behati-prinsloo.jpg"),
    ("Justin Bieber", "chr-justin-bieber", "justin-bieber.jpg"),
    ("Ariana",        "chr-ariana-grande", "ariana-grande.jpg"),
    ("Behati",        "chr-behati",        "behati-prinsloo.jpg"),
    ("Justin",        "chr-justin-bieber", "justin-bieber.jpg"),
    ("Lee Ji-eun",    "chr-lee-ji-eun",    "iu.jpg"),
    ("Kobe Bryant",   "chr-kobe-bryant",   "kobe-bryant.jpg"),
    ("Taylor Swift",  "chr-taylor",        "taylor-swift.jpg"),
    ("Park Ji-hun",   "chr-park-jihun",    "park-jihun.jpg"),
    ("Adam Levine",   "chr-adam-levine",   "adam-levine.jpg"),
    ("Scooter",       "chr-scooter-braun", "scooter-braun.jpg"),
    ("Jin-ri",        "chr-choi-jinri",    "sulli.jpg"),
    ("Eun-ah",        "chr-baek-eunah",    "eun-ah.jpg"),
    ("Wiz",           "chr-wiz-khalifa",   "wiz-khalifa.jpg"),
    ("Charlie",       "chr-charlie-puth",  "charlie-puth.jpg"),
    ("Puth",          "chr-charlie-puth",  "charlie-puth.jpg"),
    ("Jae-wook",      "chr-kim-jaewook",   "kim-jaewook.jpg"),
    ("Hye-ja",        "chr-yoon-hyeja",    "yoon-hyeja.jpg"),
    ("Kobe",          "chr-kobe-bryant",   "kobe-bryant.jpg"),
    ("Taylor",        "chr-taylor",        "taylor-swift.jpg"),
    ("Adam",          "chr-adam-levine",   "adam-levine.jpg"),
]
ALT = "|".join(re.escape(f) for f, _, _ in FORMS)
LOOKUP = {f: (i, img) for f, i, img in FORMS}
# only classless <p> or dialogue-line
PARA = re.compile(r'<p( class="dialogue-line")?>(.*?)</p>', re.S)
NAME_RE = re.compile(r'(?<![\w-])(' + ALT + r')(?![\w-])')

def wrap_segment(seg):
    out, last = [], 0
    for m in NAME_RE.finditer(seg):
        out.append(seg[last:m.start()])
        cid, img = LOOKUP[m.group(1)]
        out.append(
            f'<a class="chr-inline" href="character-intro.xhtml#{cid}">'
            f'<span class="chr-peek"><img src="../images/{img}" alt=""/></span>'
            f'{m.group(1)}</a>'
        )
        last = m.end()
    out.append(seg[last:])
    return "".join(out)

def wrap_para(inner):
    # split around existing anchors; wrap only outside them
    parts = re.split(r'(<a class="chr-inline".*?</a>)', inner, flags=re.S)
    return "".join(p if p.startswith('<a class="chr-inline') else wrap_segment(p) for p in parts)

def wrap_file(path):
    src = open(path, encoding="utf-8").read()
    count = [0]

    def repl(m):
        cls, inner = m.group(1), m.group(2)
        # skip if paragraph is a display row (paranoia guard)
        if cls is None:  # classless
            new = wrap_para(inner)
        else:
            new = wrap_para(inner)
        if new != inner:
            count[0] += len(re.findall(r'class="chr-inline"', new)) - len(re.findall(r'class="chr-inline"', inner))
        return f'<p{cls or ""}>{new}</p>'

    out = PARA.sub(repl, src)
    open(path, "w", encoding="utf-8").write(out)
    print(f"{path}: +{count[0]} anchors")

import sys
for f in sys.argv[1:] or ["chapter-171.xhtml", "chapter-172.xhtml"]:
    wrap_file(f)
