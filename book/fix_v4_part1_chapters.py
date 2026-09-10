# -*- coding: utf-8 -*-
"""Fix pass V4 - part 1: chapter content edits (ch125/126/127)."""
import re, io, sys

TEXT = '/home/user/work/epub_src/OEBPS/text/'

def rd(f):
    return io.open(f, encoding='utf-8').read()

def wr(f, s):
    io.open(f, 'w', encoding='utf-8').write(s)

def once(text, old, new, label):
    n = text.count(old)
    assert n == 1, 'ONCE FAIL %s: found %d' % (label, n)
    return text.replace(old, new)

def ntimes(text, old, new, n, label):
    c = text.count(old)
    assert c == n, 'NTIMES FAIL %s: found %d want %d' % (label, c, n)
    return text.replace(old, new)

def A(frag, img, disp):
    return ('<a class="chr-inline" href="character-intro.xhtml#chr-%s">'
            '<span class="chr-peek"><img src="../images/%s" alt=""/></span>%s</a>'
            % (frag, img, disp))

# name fragments used repeatedly
BS  = A('baek-sion', 'baek-sion.jpg', 'Baek Si-on')
BE  = A('baek-eunah', 'eun-ah.jpg', 'Baek Eun-ah')
PJ  = A('park-jihun', 'park-jihun.jpg', 'Park Ji-hun')
KB  = A('kobe-bryant', 'kobe-bryant.jpg', 'Kobe')
JH  = A('baek-jeonghun', 'baek-jeonghun.jpg', 'Baek Jeong-hun')
CJR = A('choi-jinri', 'sulli.jpg', 'Choi Jin-ri')
AL  = A('adam-levine', 'adam-levine.jpg', 'Adam Levine')
BEP = A('behati', 'behati-prinsloo.jpg', 'Behati Prinsloo')
HA  = A('james-harden', 'james-harden.jpg', 'James Harden')
DW  = A('dwight-howard', 'dwight-howard.jpg', 'Dwight Howard')

print('== CH125 ==')
s = rd(TEXT + 'chapter-125.xhtml')

# ---- 1) Yoon Hye-ja / Choi Jin-ri unread chat blocks ----
old = (
    u'    <p>%s</p>\n'
    u'\n'
    u'    <p>%s</p>\n'
    u'\n'
    u'    <p>Both were replies to the safe-arrival messages %s had sent them, separately, the moment he landed in Los Angeles.</p>\n'
    % (A('yoon-hyeja', 'yoon-hyeja.jpg', 'Yoon Hye-ja') + ' had sent \u201cGet some rest.\u201d',
       CJR + ' had sent \u201cGlad you made it! Get some rest~ take care!\u201d',
       BS))
assert old in s, 'ch125 chat old missing'
new = (
    u'    <div class="chat-container">\n'
    u'      <p class="chat-header">KakaoTalk \u00b7 Yoon Hye-ja</p>\n'
    u'      <p class="chat-name">Yoon Hye-ja</p>\n'
    u'      <p class="chat-bubble chat-received">Get some rest.</p>\n'
    u'      <p class="chat-clear"/>\n'
    u'    </div>\n'
    u'\n'
    u'    <div class="chat-container">\n'
    u'      <p class="chat-header">KakaoTalk \u00b7 Choi Jin-ri</p>\n'
    u'      <p class="chat-name">Choi Jin-ri</p>\n'
    u'      <p class="chat-bubble chat-received">Glad you made it! Get some rest~ take care!</p>\n'
    u'      <p class="chat-clear"/>\n'
    u'    </div>\n'
    u'\n'
    u'    <p>Both were replies to the safe-arrival messages %s had sent them, separately, the moment he landed in Los Angeles.</p>\n' % BS)
s = s.replace(old, new, 1)

# ---- 2) wardrobe-block: Tom Ford suits scene ----
start_marker = '<p>The next morning, the Tom Ford brand PR delivered the suits to the hotel suite.</p>'
end_marker = '<p>Her worldview had already been rebuilt, once, by the Dubai royal family.</p>'
i0 = s.index(start_marker)
i1 = s.index(end_marker) + len(end_marker)
old_region = s[i0:i1]
assert old_region.count('<p>') > 10
wardrobe = (
    u'    <p>The next morning, the Tom Ford brand PR delivered the suits to the hotel suite \u2014 three of them in all, plus two spare shirts, ties, cufflinks, and dress shoes.</p>\n'
    u'\n'
    u'    <p>The brand PR was extremely courteous.</p>\n'
    u'\n'
    u'    <p>So courteous that %s wondered if they had come to pledge allegiance rather than deliver clothing. After all, %s was no longer merely Korea\u2019s Venice-winning actor.</p>\n'
    u'\n'
    u'    <div class="wardrobe-block">\n'
    u'      <p class="wd-header">Game-night suits \u00b7 Tom Ford <span class="wd-tag">delivered to the suite</span></p>\n'
    u'      <div class="wd-item"><span class="wd-label">1 \u00b7 Black</span><span class="wd-effect">The plainest read \u2014 a slab of darkness that disappears into any crowd.</span></div>\n'
    u'      <div class="wd-item"><span class="wd-label">2 \u00b7 Dark grey</span><span class="wd-effect">One degree softer than the black, considered rather than ceremonial.</span></div>\n'
    u'      <div class="wd-item"><span class="wd-label">3 \u00b7 The choice \u2014 midnight blue</span><span class="wd-effect">The suit %s settled on after going through all three one at a time \u2014 worn with a white shirt and the platinum pair of cufflinks the brand had sent over. Under a white follow spot it would read as near-black on camera anyway.</span></div>\n'
    u'      <p class="wd-note">After %s tried it on, %s circled him once and pulled twice at the shoulders and the back: \u201cNo alterations.\u201d For the wrist, a far more understated black-strap watch \u2014 the Patek Philippe 5208P stayed in its box. Tonight he was singing for %s, not measuring wristwatches against a Russian head of state. %s looked at that \u201cfar more understated\u201d watch and fell silent for a moment. In her book, nothing north of ten million won had any business being called understated. But fine \u2014 her worldview had already been rebuilt, once, by the Dubai royal family.</p>\n'
    u'    </div>\n' % (BE, BS, PJ, BS, PJ, KB, BE))
s = s[:i0] + wardrobe + s[i1:]

# ---- 3) live-stage broadcast card (TNT commentator, close of opener) ----
old = (
    u'    <p>The TNT broadcast held on his back for two seconds.</p>\n'
    u'\n'
    u'    <p>\u201cWhat a way to open a season!\u201d the commentator said.</p>\n')
assert s.count(old) == 1
new = (
    u'    <div class="live-stage">\n'
    u'      <p class="ls-header">TNT \u00b7 Staples Center \u00b7 Lakers season opener \u00b7 LIVE</p>\n'
    u'      <p class="ls-scene">The broadcast holds on his back for two seconds as he walks toward the sideline, handing the floor back to the people it truly belongs to.</p>\n'
    u'      <p class="ls-line">\u201cWhat a way to open a season!\u201d</p>\n'
    u'    </div>\n')
s = s.replace(old, new, 1)

# ---- 4) music-player for the Sugar demo ----
old = (
    u'    <p class="lyric-line">Sugar\u2014</p>\n'
    u'\n'
    u'    <p class="lyric-line">Yes please\u2014</p>\n'
    u'\n'
    u'    <p class="lyric-line">Won\u2019t you come and put it down on me\u2014</p>\n')
assert s.count(old) == 1, 'sugar lyric block not found'
new = (
    u'    <div class="music-player">\n'
    u'      <span class="mp-art">\u266a</span>\n'
    u'      <p class="mp-title">Sugar</p>\n'
    u'      <p class="mp-artist">Maroon 5 \u00b7 unreleased demo \u00b7 one earbud in Baek Si-on\u2019s right ear</p>\n'
    u'      <div class="mp-trackbar"><span class="filled"/></div>\n'
    u'      <p class="mp-lyric">Sugar\u2014</p>\n'
    u'      <p class="mp-lyric">Yes please\u2014</p>\n'
    u'      <p class="mp-lyric">Won\u2019t you come and put it down on me\u2014</p>\n'
    u'    </div>\n')
s = s.replace(old, new, 1)

wr(TEXT + 'chapter-125.xhtml', s)
print('ch125 structural edits ok')

print('== CH126 ==')
s = rd(TEXT + 'chapter-126.xhtml')

# ---- 1) live-stage broadcast card (TNT cut + commentators) ----
i0 = s.index('<p>The director froze for a second.</p>')
i1 = s.index(u'\u201cLooks like he\u2019s trying to rescue him from Dwight Howard!\u201d</p>') + len(u'\u201cLooks like he\u2019s trying to rescue him from Dwight Howard!\u201d</p>')
old_region = s[i0:i1]
assert old_region.count('<p') >= 11, 'ch126 bcast region size'
ls = (
    u'    <p>The director froze for a second.</p>\n'
    u'\n'
    u'    <p>Then instinct beat judgment.</p>\n'
    u'\n'
    u'    <p>Cut.</p>\n'
    u'\n'
    u'    <p>The big screen switched.</p>\n'
    u'\n'
    u'    <div class="live-stage">\n'
    u'      <p class="ls-header">TNT \u00b7 Staples Center \u00b7 LIVE</p>\n'
    u'      <p class="ls-scene">On the floor, %s and Howard \u2014 being separated by referees and teammates \u2014 vanish from the frame. In their place, the sideline: the Maroon 5 frontman with an Asian man in a Tom Ford suit in a death grip, the Victoria\u2019s Secret model pressing down on his other arm. Both their faces read \u201cplease sit down.\u201d His reads \u201clet me go, I\u2019m going.\u201d</p>\n'
    u'      <p class="ls-line">\u201cWait \u2014 is Adam Levine trying to stop Baek Si-on?\u201d</p>\n'
    u'      <p class="ls-line">\u201cLooks like he\u2019s trying to rescue him from Dwight Howard!\u201d</p>\n'
    u'      <p class="ls-note">The whole building blinked first \u2014 then laughter and screaming blew up together. Even the commentators were lost for a second.</p>\n'
    u'    </div>\n' % KB)
s = s[:i0] + ls + s[i1:]

# ---- 2) interview-block for the media Q&A ----
i0 = s.index(u'<p>The reporter\u2019s tone was very polite.</p>')
i1 = s.index(u'\u201cPublic figures aren\u2019t allowed to have friends? If a person can watch a friend get hit and feel nothing, that isn\u2019t rationality. That\u2019s cold blood.\u201d</p>') + len(u'\u201cPublic figures aren\u2019t allowed to have friends? If a person can watch a friend get hit and feel nothing, that isn\u2019t rationality. That\u2019s cold blood.\u201d</p>')
old_region = s[i0:i1]
assert old_region.count('<p') >= 25
block = (
    u'    <p>The reporter\u2019s tone was very polite.</p>\n'
    u'\n'
    u'    <p>But the question was anything but.</p>\n'
    u'\n'
    u'    <p>The atmosphere in the room changed instantly. Director %s\u2019s brow furrowed. The agent standing at the side of the stage tightened.</p>\n'
    u'\n'
    u'    <p>The question was sharp.</p>\n'
    u'\n'
    u'    <p>And the malice ran deep.</p>\n'
    u'\n'
    u'    <p>He was not asking about %s alone. He had tied together the violence of the Green Bottle Fly role, %s\u2019s real-life conduct, and %s\u2019s working relationship with him.</p>\n'
    u'\n'
    u'    <p>If %s said \u201cI don\u2019t know,\u201d that was evasion. If she said \u201che shouldn\u2019t have,\u201d the media would write \u201cSulli also thinks Baek Si-on lost control.\u201d</p>\n'
    u'\n'
    u'    <p>Down in the audience, silence.</p>\n'
    u'\n'
    u'    <p>But the camera flashes had already started popping, early.</p>\n'
    u'\n'
    u'    <p class="sfx-line">Click.</p>\n'
    u'\n'
    u'    <p class="sfx-line">Click.</p>\n'
    u'\n'
    u'    <p class="sfx-line">Click.</p>\n'
    u'\n'
    u'    <p>%s turned his head and gave %s a look. His meaning was clear \u2014 you don\u2019t have to answer. The press-conference host also had a smooth exit line ready.</p>\n'
    u'\n'
    u'    <p>But %s looked the reporter straight in the eye:</p>\n'
    u'\n'
    u'    <div class="interview-block">\n'
    u'      <p class="iv-kicker">Green Bottle Fly media preview \u00b7 press Q&amp;A \u00b7 the last question</p>\n'
    u'      <p class="iv-q">\u201cA little while ago, Baek Si-on-ssi appeared to try to rush into a conflict zone at an NBA game, and it has caused considerable controversy. Some argue this is a kind of real-life extension of the violent role he plays in Green Bottle Fly. As an actor who co-stars with Baek Si-on-ssi in this film and shares a great many scenes with him \u2014 how do you view his conduct in front of the overseas broadcast cameras? Do you think he lacks the restraint a public figure ought to have?\u201d</p>\n'
    u'      <p class="iv-a">\u201cHave you watched the full video?\u201d</p>\n'
    u'      <p class="iv-q">\u201cI\u2026 saw the news screenshots and the related coverage.\u201d</p>\n'
    u'      <p class="iv-a">\u201cSo you\u2019re taking things out of context. That\u2019s fine \u2014 but let me ask you: if your friend were being beaten in front of you, would you sit there and not move?\u201d</p>\n'
    u'      <p class="iv-q">\u201cBut he\u2019s a public figure\u2014\u201d</p>\n'
    u'      <p class="iv-a">\u201cPublic figures aren\u2019t allowed to have friends? If a person can watch a friend get hit and feel nothing, that isn\u2019t rationality. That\u2019s cold blood.\u201d</p>\n'
    u'    </div>\n' % (JH, BS, BS, CJR, CJR, JH, CJR, CJR))
s = s[:i0] + block + s[i1:]

# ---- 3) chat-container direction fixes (Jin-ri's phone: header=Baek Si-on, name self) ----
# Convert only chat containers whose header is "KakaoTalk · Choi Jin-ri" but whose
# messages are SENT (chat-sent) by Choi Jin-ri from her own phone.
def fix_jinri_phone_chats(s):
    # process containers one by one
    out = []
    pos = 0
    pat = re.compile(r'<div class="chat-container">.*?</div>', re.S)
    cnt = 0
    for m in pat.finditer(s):
        seg = m.group(0)
        if ('chat-header\">KakaoTalk \u00b7 Choi Jin-ri<' in seg
                and 'chat-bubble chat-sent' in seg
                and 'chat-name self' not in seg):
            seg = seg.replace('<p class="chat-header">KakaoTalk \u00b7 Choi Jin-ri</p>',
                              '<p class="chat-header">KakaoTalk \u00b7 Baek Si-on</p>')
            seg = seg.replace('<p class="chat-name">Choi Jin-ri</p>',
                              '<p class="chat-name self">Choi Jin-ri</p>')
            cnt += 1
        out.append((m.start(), m.end(), seg))
    if cnt == 0:
        raise RuntimeError('no jinri chat containers fixed in ch126')
    # rebuild
    res = []
    last = 0
    for a, b, seg in out:
        res.append(s[last:a]); res.append(seg); last = b
    res.append(s[last:])
    return ''.join(res), cnt
s, c = fix_jinri_phone_chats(s)
print('ch126 jinri chat containers fixed:', c)
assert c == 6, c

wr(TEXT + 'chapter-126.xhtml', s)
print('ch126 structural edits ok')

print('== CH127 ==')
s = rd(TEXT + 'chapter-127.xhtml')

# ---- chat direction fixes (3 draft blocks from Jin-ri's phone) ----
s, c = fix_jinri_phone_chats(s)
assert c == 3, ('ch127 fixed', c)
print('ch127 jinri chat containers fixed:', c)

# ---- trend-block for the iTunes/Spotify/YouTube wave ----
i0 = s.index('<p>United States.</p>')
i1 = s.index('The comment section of the official YouTube music video was adding new comments at a pace not seen since the day of the S4 World Championship final.</p>') + len('The comment section of the official YouTube music video was adding new comments at a pace not seen since the day of the S4 World Championship final.</p>')
old_region = s[i0:i1]
assert old_region.count('<p>') == 7, old_region.count('<p>')
trend = (
    u'    <div class="trend-block">\n'
    u'      <p class="tr-header">iTunes multi-country \u00b7 the morning after #TomFordGangster</p>\n'
    u'      <p class="tr-rank">United States \u2014 <span class="tr-work">Legend</span> <span class="tr-hot">climbing</span></p>\n'
    u'      <p class="tr-rank">Canada \u2014 <span class="tr-work">Legend</span> <span class="tr-hot">climbing</span></p>\n'
    u'      <p class="tr-rank">Australia \u2014 <span class="tr-work">Legend</span> <span class="tr-hot">climbing</span></p>\n'
    u'      <p class="tr-rank">United Kingdom \u2014 <span class="tr-work">Legend</span> <span class="tr-hot">climbing</span></p>\n'
    u'      <p class="tr-note">Even a few East Asian markets, which usually reacted far less strongly to an English rock anthem, saw \u201cLegend\u201d shoved from below and climbing again. Spotify\u2019s real-time plays were climbing too \u2014 and the official MV\u2019s comment section was adding new comments at a pace not seen since the day of the S4 World Championship final.</p>\n'
    u'    </div>\n')
s = s[:i0] + trend + s[i1:]

wr(TEXT + 'chapter-127.xhtml', s)
print('ch127 structural edits ok')

# ============================================================
# Anchor pass: insert chr-inline hover anchors on plain <p> prose
# ============================================================
TOKENS = [
    (re.compile(r'Adam Levine'), 'adam-levine', 'adam-levine.jpg', 'Adam Levine'),
    (re.compile(r'Dwight Howard'), 'dwight-howard', 'dwight-howard.jpg', 'Dwight Howard'),
    (re.compile(r'James Harden'), 'james-harden', 'james-harden.jpg', 'James Harden'),
    (re.compile(r'Little Pumpkin'), 'behati', 'behati-prinsloo.jpg', 'Little Pumpkin'),
    (re.compile(r'Behati'), 'behati', 'behati-prinsloo.jpg', 'Behati'),
    (re.compile(r'Dwight'), 'dwight-howard', 'dwight-howard.jpg', 'Dwight'),
    (re.compile(r'Harden'), 'james-harden', 'james-harden.jpg', 'Harden'),
    (re.compile(r'Howard'), 'dwight-howard', 'dwight-howard.jpg', 'Howard'),
    (re.compile(r'Adam'), 'adam-levine', 'adam-levine.jpg', 'Adam'),
]

def anchorize_line(line, stats):
    # only plain <p> paragraphs (no class attr)
    m = re.match(r'^(\s*<p>)(.*)(</p>)\s*$', line, re.S)
    if not m:
        return line, stats
    indent, body, close = m.group(1), m.group(2), m.group(3)
    # split body into tag/text pieces; skip text inside existing <a>
    pieces = re.split(r'(<[^>]+>)', body)
    out = []
    in_anchor = 0
    for pc in pieces:
        if pc.startswith('<a '):
            in_anchor += 1
            out.append(pc)
            continue
        if pc.startswith('</a>'):
            in_anchor -= 1
            out.append(pc)
            continue
        if in_anchor > 0 or pc.startswith('<') or pc.startswith('</'):
            out.append(pc)
            continue
        # text piece: replace tokens, skip ones inside curly quotes
        # build list of replacements (pos,len,frag,img,disp)
        rl = []
        for rx, frag, img, disp in TOKENS:
            for mm in rx.finditer(pc):
                # skip if inside quoted speech (“...”)
                pre = pc[:mm.start()]
                if pre.rfind(u'\u201c') > pre.rfind(u'\u201d'):
                    continue
                rl.append((mm.start(), mm.end() - mm.start(), frag, img, disp))
        rl.sort()
        # drop overlaps
        filtered = []
        for t in rl:
            if filtered and t[0] < filtered[-1][0] + filtered[-1][1]:
                continue
            filtered.append(t)
        for t in filtered:
            pos, ln, frag, img, disp = t
            stats.setdefault(frag, 0)
            stats[frag] += 1
        # rebuild
        buf = []
        last = 0
        for pos, ln, frag, img, disp in filtered:
            buf.append(pc[last:pos])
            buf.append(A(frag, img, disp))
            last = pos + ln
        buf.append(pc[last:])
        out.append(''.join(buf))
    return indent + ''.join(out) + close, stats

for fname in ['chapter-125.xhtml', 'chapter-126.xhtml', 'chapter-127.xhtml']:
    lines = rd(TEXT + fname).split('\n')
    stats = {}
    new_lines = []
    for ln in lines:
        nl, stats = anchorize_line(ln, stats)
        new_lines.append(nl)
    wr(TEXT + fname, '\n'.join(new_lines))
    print(fname, 'anchors:', stats)

print('DONE')
