# -*- coding: utf-8 -*-
"""Card-builder helper for the V11 character-intro pass.

Payload source: /home/user/work/payload40.json (extracted from
character-intro.xhtml page cards: name, role, meta, desc, img).
"""
import json, html, re

_PAYLOAD = json.load(open('/home/user/work/payload40.json', encoding='utf-8'))


def card(slug, page_name=None):
    """Return the in-text `.char-intro` card HTML for a page slug.

    Mirrors the exact markup used by published chapters (e.g. ch04/05):
    a wrapper div with chi-photo / chi-body and chi-name / chi-role /
    chi-meta / chi-desc paragraphs.  chi-name is plain text (no anchor),
    exactly like existing in-text cards.
    """
    p = _PAYLOAD[slug]
    name = p['name'] if page_name is None else page_name
    img = p['img']
    role = p['role']
    meta = p['meta']
    desc = p['desc']
    esc = lambda s: (s.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;'))
    out = []
    out.append('    <div class="char-intro">')
    out.append(f'      <div class="chi-photo"><img src="../images/{img}" alt="{esc(name)}"/></div>')
    out.append('      <div class="chi-body">')
    out.append(f'        <p class="chi-name">{esc(name)}</p>')
    out.append(f'        <p class="chi-role">{esc(role)}</p>')
    out.append(f'        <p class="chi-meta">{esc(meta)}</p>')
    out.append(f'        <p class="chi-desc">{esc(desc)}</p>')
    out.append('      </div>')
    out.append('    </div>')
    return '\n'.join(out)


def find_para(text, needle):
    """Return (start,end) of the <p>…</p> block containing `needle`."""
    pstart = text.rfind('<p', 0, text.find(needle))
    if pstart == -1:
        return None
    pend = text.find('</p>', text.find(needle))
    if pend == -1:
        return None
    return pstart, pend + len('</p>')


def para_span(text, needle, start=0):
    """Index span of the first <p> block containing `needle` at/after `start`."""
    i = text.find(needle, start)
    if i < 0:
        return None
    p0 = text.rfind('<p', 0, i)
    if p0 < 0:
        p0 = 0
    p1 = text.find('</p>', i)
    if p1 < 0:
        return None
    return (p0, p1 + 4)


def extract_char_intro(text, start):
    """Given index of '<div class="char-intro">', return (end, html)."""
    s = text.find('>', text.find('<div class="char-intro"', start)) + 1
    depth = 1
    i = s
    while i < len(text) and depth:
        op = text.find('<div', i)
        cl = text.find('</div>', i)
        if cl == -1:
            break
        if op != -1 and op < cl:
            depth += 1
            i = text.find('>', op) + 1
        else:
            depth -= 1
            i = cl + 6
    return (i, text[start:i])


def remove_card_by_img(text, imgfile):
    """Delete the whole .char-intro card whose chi-photo uses imgfile."""
    needle = f'<img src="../images/{imgfile}"'
    while True:
        st = text.find('<div class="char-intro">')
        found_at = None
        # walk each card and check img inside
        pos = 0
        out = text
        removed = False
        while True:
            st = text.find('<div class="char-intro">', pos)
            if st == -1:
                break
            end, block = extract_char_intro(text, st)
            if needle in block:
                out = text[:st] + text[end:]
                removed = True
                break
            pos = end
        return (out, removed)


def insert_after(text, pos, block):
    return text[:pos] + '\n\n' + block + '\n' + text[pos:]
