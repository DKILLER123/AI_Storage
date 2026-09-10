# -*- coding: utf-8 -*-
"""Fix pass V4 - part 2: character intros + characters page + manifest."""
import io, re

OEBPS = '/home/user/work/epub_src/OEBPS/'
def rd(p): return io.open(p, encoding='utf-8').read()
def wr(p, s): io.open(p, 'w', encoding='utf-8').write(s)

# ---------- ci entries (character-intro.xhtml), appended in first-appearance order ----------
ci_entries = u'''\
      <div class="char-intro" id="ci-james-harden">
        <div class="chi-photo"><img src="../images/james-harden.jpg" alt="Portrait of James Harden"/></div>
        <div class="chi-body">
          <p class="chi-name"><a href="#chr-james-harden">James Harden</a></p>
          <p class="chi-role">Guard \u00b7 Houston Rockets</p>
          <p class="chi-meta">Real \u00b7 October 2014 \u00b7 the visitors\u2019 tunnel</p>
          <p class="chi-desc">The Beard with two drives and a drawn foul who reminds twenty thousand people that Kobe\u2019s comeback night is not a documentary. He plans the upset from the mouth of the tunnel and does not plan on losing.</p>
        </div>
      </div>

      <div class="char-intro" id="ci-dwight-howard">
        <div class="chi-photo"><img src="../images/dwight-howard.jpg" alt="Portrait of Dwight Howard"/></div>
        <div class="chi-body">
          <p class="chi-name"><a href="#chr-dwight-howard">Dwight Howard</a></p>
          <p class="chi-role">Centre \u00b7 Houston Rockets</p>
          <p class="chi-meta">Real \u00b7 October 2014 \u00b7 the elbow at the centre of everything</p>
          <p class="chi-desc">Elbows out, hands spread, grinning wider the louder the boos get. His defensive rebound starts the fight, and his elbow \u2014 swung from two hundred and sixty pounds away \u2014 is what nearly ends Baek Si-on\u2019s night.</p>
        </div>
      </div>

      <div class="char-intro" id="ci-adam-levine">
        <div class="chi-photo"><img src="../images/adam-levine.jpg" alt="Portrait of Adam Levine"/></div>
        <div class="chi-body">
          <p class="chi-name"><a href="#chr-adam-levine">Adam Levine</a></p>
          <p class="chi-role">Frontman \u00b7 Maroon 5</p>
          <p class="chi-meta">Real \u00b7 courtside, VIP row one</p>
          <p class="chi-desc">The frontman who calls Baek Si-on\u2019s pre-game show the best he has seen all year, presses a demo into his ear and asks him for a video idea \u2014 then spends the rest of the night physically keeping the same singer away from Dwight Howard.</p>
        </div>
      </div>

      <div class="char-intro" id="ci-behati">
        <div class="chi-photo"><img src="../images/behati-prinsloo.jpg" alt="Portrait of Behati Prinsloo"/></div>
        <div class="chi-body">
          <p class="chi-name"><a href="#chr-behati">Behati Prinsloo</a></p>
          <p class="chi-role">Victoria\u2019s Secret model \u00b7 Adam\u2019s wife</p>
          <p class="chi-meta">Real \u00b7 the one Adam calls Little Pumpkin</p>
          <p class="chi-desc">The Victoria\u2019s Secret model who reaches across her husband to press down the same singer\u2019s other arm \u2014 and then calls the whole near-death moment \u201csweet.\u201d</p>
        </div>
      </div>

'''

# ---------- chr modal blocks ----------
def modal(mid, img, disp, href):
    return (
        u'    <div class="chr-modal" id="%s">\n'
        u'      <a class="chr-backdrop" href="%s" aria-label="Close"></a>\n'
        u'      <div class="chr-shot">\n'
        u'        <a class="chr-close" href="%s" aria-label="Close">\u2715</a>\n'
        u'        <img src="../images/%s" alt="%s"/>\n'
        u'        <span class="chr-caption">%s</span>\n'
        u'      </div>\n'
        u'    </div>\n'
        % (mid, href, href, img, disp, disp))

modals_intro = (
    modal('chr-james-harden', 'james-harden.jpg', 'James Harden', '#character-intro') +
    modal('chr-dwight-howard', 'dwight-howard.jpg', 'Dwight Howard', '#character-intro') +
    modal('chr-adam-levine', 'adam-levine.jpg', 'Adam Levine', '#character-intro') +
    modal('chr-behati', 'behati-prinsloo.jpg', 'Behati Prinsloo', '#character-intro'))

# ---------- characters.xhtml cards ----------
card = u'''\
    <div class="char-card">
      <div class="char-infobox">
        <div class="ci-name"><a href="#%s">%s</a></div>
        <div class="ci-photo"><img src="../images/%s" alt="Portrait of %s"/></div>
        <p class="ci-caption">%s</p>
        <table class="ci-table">
%s
        </table>
      </div>
      <div class="char-bio">
        <h3>%s</h3>
        <p>%s</p>
      </div>
    </div>

'''

def rows(*pairs):
    return ''.join(u'          <tr><th>%s</th><td>%s</td></tr>\n' % (k, v) for k, v in pairs)

cards = ''
cards += card % ('chr-james-harden', 'James Harden', 'james-harden.jpg', 'James Harden',
    'The Beard who plans the upset.',
    rows(('Name', 'James Harden'), ('Team', 'Houston Rockets'), ('No.', '13'),
         ('Role', 'Real \u00b7 the bearded engineer of the upset')),
    'The Upset, Planned in the Tunnel',
    'Two drives, a drawn foul, and a message delivered from the visitors\u2019 tunnel: tonight is not Kobe\u2019s documentary. Harden watches the coronation and talks about torching it \u2014 and by the fourth quarter, the only thing between him and the script is a Korean singer in a borrowed suit.')
cards += card % ('chr-dwight-howard', 'Dwight Howard', 'dwight-howard.jpg', 'Dwight Howard',
    'The centre at the centre of the storm.',
    rows(('Name', 'Dwight Howard'), ('Team', 'Houston Rockets'), ('No.', '12'),
         ('Role', 'Real \u00b7 the elbow that started everything')),
    'The Elbow and the Grin',
    'He boxes out, grabs boards, protects the rim, and grins wider the louder the building boos. The defensive rebound is clean; the elbow that follows is not \u2014 and from the sideline, a singer in a midnight-blue suit decides the whole thing is his business.')
cards += card % ('chr-adam-levine', 'Adam Levine', 'adam-levine.jpg', 'Adam Levine',
    'The one who held him back.',
    rows(('Name', 'Adam Levine'), ('Band', 'Maroon 5'), ('Wife', 'Behati Prinsloo'),
         ('Role', 'Real \u00b7 courtside friend, reluctant bodyguard')),
    'The One Who Held Him Back',
    'He liked the pre-game show enough to ask its singer for a video idea, and he likes him well enough to spend the whole fight physically preventing him from charging an NBA centre. \u201cOne elbow from him and he\u2019ll elbow you straight back to Korea!\u201d')
cards += card % ('chr-behati', 'Behati Prinsloo', 'behati-prinsloo.jpg', 'Behati Prinsloo',
    'Little Pumpkin.',
    rows(('Name', 'Behati Prinsloo'), ('Husband', 'Adam Levine'), ('Label', 'Victoria\u2019s Secret'),
         ('Role', 'Real \u00b7 the other half of the defensive line-up')),
    'Little Pumpkin',
    'She snaps out of her daze to grab the other arm, listens to a rock singer explain loyalty, and delivers the evening\u2019s only true verdict: \u201cBut sweet.\u201d')

modals_chars = (
    modal('chr-james-harden', 'james-harden.jpg', 'James Harden', '#characters') +
    modal('chr-dwight-howard', 'dwight-howard.jpg', 'Dwight Howard', '#characters') +
    modal('chr-adam-levine', 'adam-levine.jpg', 'Adam Levine', '#characters') +
    modal('chr-behati', 'behati-prinsloo.jpg', 'Behati Prinsloo', '#characters'))

# ================= character-intro.xhtml =================
p = OEBPS + 'text/character-intro.xhtml'
s = rd(p)
marker = '<!-- ===== Pure-CSS lightboxes: each shows ONLY the character\'s portrait ===== -->'
assert s.count(marker) == 1, 'ci marker'
idx = s.index(marker)
# insert ci entries right before the ci-index close (the "    </div>" line preceding marker)
pre = s[:idx]
close_pos = pre.rfind('\n    </div>')
assert close_pos != -1
s = pre[:close_pos] + '\n' + ci_entries + pre[close_pos:] + s[idx:]
# append modals before </body>
assert s.count('\n</body>\n</html>\n') == 1
s = s.replace('\n</body>\n</html>\n', '\n' + modals_intro + '\n</body>\n</html>\n', 1)
wr(p, s)
print('character-intro.xhtml updated; chr-ids now =', s.count('id="chr-'))

# ================= characters.xhtml =================
p = OEBPS + 'text/characters.xhtml'
s = rd(p)
# insert new char-cards immediately before the first chr-modal line (after the last card)
mm = s.index('    <div class="chr-modal" id="chr-baek-sion">')
s = s[:mm] + '\n' + cards + s[mm:]
assert s.count('\n</body>\n</html>\n') == 1
s = s.replace('\n</body>\n</html>\n', '\n' + modals_chars + '\n</body>\n</html>\n', 1)
wr(p, s)
print('characters.xhtml updated; char-card count =', s.count('class="char-card"'))

# ================= content.opf manifest =================
p = OEBPS + 'content.opf'
s = rd(p)
pat = re.compile(r'    <item id="img-rich-paul"[^>]*/>\n')
assert len(pat.findall(s)) == 1, 'img-rich-paul item'
add = ''.join(
    u'    <item id="img-%s" href="images/%s.jpg" media-type="image/jpeg"/>\n' % (n, n)
    for n in ['james-harden', 'dwight-howard', 'adam-levine', 'behati-prinsloo'])
s = pat.sub(lambda m: m.group(0) + add, s, count=1)
wr(p, s)
print('content.opf image items now =', s.count('media-type="image/'))

print('DONE PART 2')
