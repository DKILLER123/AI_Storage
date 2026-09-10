# -*- coding: utf-8 -*-
"""Fix pass V4 - part 3: Jeanie Buss card + hangul-normalize the four new cards' rows."""
import io, re, shutil

OEBPS = '/home/user/work/epub_src/OEBPS/'
def rd(p): return io.open(p, encoding='utf-8').read()
def wr(p, s): io.open(p, 'w', encoding='utf-8').write(s)

# ---- 0) stage Jeanie Buss portrait (getty via yahoo listing, in-arena portrait) ----
shutil.copy('/home/user/image-search/jeanie-buss-los-angeles-lakers-president-1.jpg',
            OEBPS + 'images/jeanie-buss.jpg')
print('jeanie-buss.jpg staged')

# ---- 1) characters.xhtml: normalize the four tables to Name/Post/Role + hangul ----
p = OEBPS + 'text/characters.xhtml'
s = rd(p)
subs = [
 (u'<tr><th>Name</th><td>James Harden</td></tr>\n'
  u'          <tr><th>Team</th><td>Houston Rockets</td></tr>\n'
  u'          <tr><th>No.</th><td>13</td></tr>\n'
  u'          <tr><th>Role</th><td>Real · the bearded engineer of the upset</td></tr>',
  u'<tr><th>Name</th><td>James Harden (제임스 하든)</td></tr>\n'
  u'          <tr><th>Post</th><td>Shooting guard · Houston Rockets</td></tr>\n'
  u'          <tr><th>Role</th><td>The bearded engineer of the upset</td></tr>'),
 (u'<tr><th>Name</th><td>Dwight Howard</td></tr>\n'
  u'          <tr><th>Team</th><td>Houston Rockets</td></tr>\n'
  u'          <tr><th>No.</th><td>12</td></tr>\n'
  u'          <tr><th>Role</th><td>Real · the elbow that started everything</td></tr>',
  u'<tr><th>Name</th><td>Dwight Howard (드와이트 하워드)</td></tr>\n'
  u'          <tr><th>Post</th><td>Centre · Houston Rockets</td></tr>\n'
  u'          <tr><th>Role</th><td>The elbow that started everything</td></tr>'),
 (u'<tr><th>Name</th><td>Adam Levine</td></tr>\n'
  u'          <tr><th>Band</th><td>Maroon 5</td></tr>\n'
  u'          <tr><th>Wife</th><td>Behati Prinsloo</td></tr>\n'
  u'          <tr><th>Role</th><td>Real · courtside friend, reluctant bodyguard</td></tr>',
  u'<tr><th>Name</th><td>Adam Levine (애덤 리바인)</td></tr>\n'
  u'          <tr><th>Post</th><td>Frontman · Maroon 5</td></tr>\n'
  u'          <tr><th>Role</th><td>The one who held him back</td></tr>'),
 (u'<tr><th>Name</th><td>Behati Prinsloo</td></tr>\n'
  u'          <tr><th>Husband</th><td>Adam Levine</td></tr>\n'
  u'          <tr><th>Label</th><td>Victoria’s Secret</td></tr>\n'
  u'          <tr><th>Role</th><td>Real · the other half of the defensive line-up</td></tr>',
  u'<tr><th>Name</th><td>Behati Prinsloo (베하티 프린슬루)</td></tr>\n'
  u'          <tr><th>Post</th><td>Model · Victoria’s Secret</td></tr>\n'
  u'          <tr><th>Role</th><td>The other half of the defensive line-up</td></tr>'),
]
for old, new in subs:
    assert s.count(old) == 1, ('row sub', old[:60])
    s = s.replace(old, new, 1)

# Jeanie Buss card, inserted right before the James Harden card
jeanie_card = u'''    <div class="char-card">
      <div class="char-infobox">
        <div class="ci-name"><a href="#chr-jeanie-buss">Jeanie Buss</a></div>
        <div class="ci-photo"><img src="../images/jeanie-buss.jpg" alt="Portrait of Jeanie Buss"/></div>
        <p class="ci-caption">The boss of the building.</p>
        <table class="ci-table">
          <tr><th>Name</th><td>Jeanie Buss (지니 버스)</td></tr>
          <tr><th>Post</th><td>President · Los Angeles Lakers</td></tr>
          <tr><th>Role</th><td>The handshake that became a partnership conversation</td></tr>
        </table>
      </div>
      <div class="char-bio">
        <h3>The Woman Who Owns the Building</h3>
        <p>The Lakers’ president comes over at the end of a rehearsal to shake a stranger’s hand and take one photo together — then her assistant follows Baek Eun-ah out with a business card and a suggestion of partnership talks worth having later. In her building, even a comeback rehearsal is business, and the business keeps its manners.</p>
      </div>
    </div>

'''
anchor = '<div class="ci-name"><a href="#chr-james-harden">James Harden</a></div>'
assert s.count(anchor) == 1
s = s.replace(anchor, jeanie_card + anchor, 1)

# modal for Jeanie (characters page)
assert s.count('\n</body>\n</html>\n') == 1
jeanie_modal_chars = u'''    <div class="chr-modal" id="chr-jeanie-buss">
      <a class="chr-backdrop" href="#characters" aria-label="Close"></a>
      <div class="chr-shot">
        <a class="chr-close" href="#characters" aria-label="Close">✕</a>
        <img src="../images/jeanie-buss.jpg" alt="Jeanie Buss"/>
        <span class="chr-caption">Jeanie Buss</span>
      </div>
    </div>
'''
s = s.replace('\n</body>\n</html>\n', '\n' + jeanie_modal_chars + '\n</body>\n</html>\n', 1)
wr(p, s)
print('characters.xhtml: cards =', s.count('class="char-card"'), '| hangul rows ok')

# ---- 2) character-intro.xhtml: ci entry before James Harden + modal ----
p = OEBPS + 'text/character-intro.xhtml'
s = rd(p)
ci_jeanie = u'''      <div class="char-intro" id="ci-jeanie-buss">
        <div class="chi-photo"><img src="../images/jeanie-buss.jpg" alt="Portrait of Jeanie Buss"/></div>
        <div class="chi-body">
          <p class="chi-name"><a href="#chr-jeanie-buss">Jeanie Buss</a></p>
          <p class="chi-role">President · Los Angeles Lakers</p>
          <p class="chi-meta">Real · Staples Center · the afternoon before the opener</p>
          <p class="chi-desc">The president who ends a stranger’s rehearsal by walking over to shake his hand, take one photo, and send her assistant after his sister with a business card. Partnership talks, she notes, are worth having later.</p>
        </div>
      </div>

'''
anchor = '<div class="char-intro" id="ci-james-harden">'
assert s.count(anchor) == 1
s = s.replace(anchor, ci_jeanie + anchor, 1)
jeanie_modal_intro = u'''    <div class="chr-modal" id="chr-jeanie-buss">
      <a class="chr-backdrop" href="#character-intro" aria-label="Close"></a>
      <div class="chr-shot">
        <a class="chr-close" href="#character-intro" aria-label="Close">✕</a>
        <img src="../images/jeanie-buss.jpg" alt="Jeanie Buss"/>
        <span class="chr-caption">Jeanie Buss</span>
      </div>
    </div>
'''
assert s.count('\n</body>\n</html>\n') == 1
s = s.replace('\n</body>\n</html>\n', '\n' + jeanie_modal_intro + '\n</body>\n</html>\n', 1)
wr(p, s)
print('character-intro.xhtml updated')

# ---- 3) chapter-125.xhtml: hover anchors for Jeanie Buss / Jeanie ----
p = OEBPS + 'text/chapter-125.xhtml'
s = rd(p)
def A(disp, frag, img):
    return ('<a class="chr-inline" href="character-intro.xhtml#%s">'
            '<span class="chr-peek"><img src="../images/%s" alt=""/></span>%s</a>'
            % (frag, img, disp))
A_JB = A('Jeanie Buss', 'chr-jeanie-buss', 'jeanie-buss.jpg')
A_Jeanie = A('Jeanie', 'chr-jeanie-buss', 'jeanie-buss.jpg')
subs = [
 ('When he was done, Jeanie Buss, the Lakers’ president, came over to shake his hand.',
  'When he was done, %s, the Lakers’ president, came over to shake his hand.' % A_JB),
 ('Jeanie’s assistant asked for', '%s’s assistant asked for' % A_Jeanie),
]
for old, new in subs:
    assert s.count(old) == 1, ('ch125', old[:40])
    s = s.replace(old, new, 1)
wr(p, s)
print('chapter-125.xhtml anchored x2; chr-inline =', s.count('chr-inline'))

# ---- 4) content.opf manifest ----
p = OEBPS + 'content.opf'
s = rd(p)
pat = re.compile(r'    <item id="img-jeanie-buss"[^>]*/>')
assert not pat.search(s), 'already present'
anchor_item = '    <item id="img-behati-prinsloo" href="images/behati-prinsloo.jpg" media-type="image/jpeg"/>\n'
assert s.count(anchor_item) == 1
s = s.replace(anchor_item, anchor_item + '    <item id="img-jeanie-buss" href="images/jeanie-buss.jpg" media-type="image/jpeg"/>\n', 1)
wr(p, s)
print('content.opf image items =', s.count('media-type="image/'))
print('DONE PART 3')
