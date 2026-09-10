# -*- coding: utf-8 -*-
# Phone-call conversion pass: ch169 Adam call + ch156 Lee Seon-ho return call.
# Splices prose dialogue-line scenes into single .phone-call blocks (pc-head/pc-them/pc-me/pc-note).
# Also repairs ch156 orphaned subject: "<p>’s name was never spoken." -> "The young master’s name ..."
import io, sys

TEXT = 'epub_src/OEBPS/text/'

def splice(path, start_marker, end_marker, block, from_end=False):
    with io.open(path, 'r', encoding='utf-8') as f:
        t = f.read()
    i = t.find(start_marker)
    if i < 0:
        sys.exit('START NOT FOUND in ' + path)
    if from_end:
        j = t.rfind(end_marker)
    else:
        j = t.find(end_marker, i)
    if j < 0:
        sys.exit('END NOT FOUND in ' + path)
    j += len(end_marker)
    t2 = t[:i] + block + t[j:]
    with io.open(path, 'w', encoding='utf-8') as f:
        f.write(t2)
    print(path, 'spliced:', j - i, '->', len(block), 'chars')

# ---------------- ch169 ----------------
p169 = TEXT + 'chapter-169.xhtml'
start169 = '<p class="dialogue-line">“Hey.”</p>'
# end = final anchored Adam "……" paragraph of the scene (last occurrence in file)
end169 = '<p><a class="chr-inline" href="character-intro.xhtml#chr-adam-levine"><span class="chr-peek"><img src="../images/adam-levine.jpg" alt=""/></span>Adam</a>: “……”</p>'

block169 = '''<div class="phone-call">
      <p class="pc-head">Baek Si-on ← Adam Levine · the hotel, Los Angeles · incoming</p>
      <p class="pc-me">Hey.</p>
      <p class="pc-note">The first sentence through the line was direct.</p>
      <p class="pc-them">I hate you.</p>
      <p class="pc-note">Baek Si-on toweled his hair.</p>
      <p class="pc-me">Reason?</p>
      <p class="pc-note">Adam’s voice was thick with grievance.</p>
      <p class="pc-them">You’re asking me for a REASON?</p>
      <p class="pc-them">The idea YOU gave me at the Lakers game! The Sugar video — crashing newlyweds’ weddings!</p>
      <p class="pc-them">Do you know what we’ve been through this week?</p>
      <p class="pc-note">Baek Si-on ran the memory back. He remembered the video. In the finished cut, Maroon 5 bursts into a wedding, the curtain swings open, the bride screams, the groom freezes, the guests erupt — everybody thrills like Cupid has them all at syringe-point. Dreamlike. Frictionless. In his last life he’d watched the final cut and honestly assumed the shoot had gone the same way. Adam’s opening remarks suggested reality had other paperwork.</p>
      <p class="pc-me">It failed?</p>
      <p class="pc-them">Failed?</p>
      <p class="pc-note">Adam laughed once — the laugh of a man past that word.</p>
      <p class="pc-them">That word is too gentle.</p>
      <p class="pc-them">Wedding one: the groom decided I was the bride’s ex.</p>
      <p class="pc-them">He charged over asking why I was at his wedding.</p>
      <p class="pc-them">I said I came to sing.</p>
      <p class="pc-them">He said, who TOLD you to sing.</p>
      <p class="pc-note">Baek Si-on: ……</p>
      <p class="pc-note">Adam pressed on.</p>
      <p class="pc-them">Wedding two: bride happy, groom happy.</p>
      <p class="pc-them">The problem was the bride’s father.</p>
      <p class="pc-them">He thought we were a wedding-scam crew.</p>
      <p class="pc-them">That man pulled his BELT out.</p>
      <p class="pc-them">A belt, White. A BELT!</p>
      <p class="pc-note">Baek Si-on held it in. He failed to hold it in. One laugh escaped.</p>
      <p class="pc-note">Adam heard it and went up an octave in outrage.</p>
      <p class="pc-them">You’re LAUGHING?</p>
      <p class="pc-them">Do you know what went through my mind in that moment?</p>
      <p class="pc-them">I thought — so this is where a music career ends up. Being chased across a reception by a father-in-law with a belt.</p>
      <p class="pc-note">Baek Si-on asked:</p>
      <p class="pc-me">What brand?</p>
      <p class="pc-them">What?</p>
      <p class="pc-me">The belt.</p>
      <p class="pc-note">Adam went silent for two seconds.</p>
      <p class="pc-them">How would I know? All I knew at the time was that it HURT people.</p>
      <p class="pc-note">Baek Si-on said:</p>
      <p class="pc-me">In Asia, that scene usually comes with a Seven Wolves.</p>
      <p class="pc-them">What’s a Seven Wolves?</p>
      <p class="pc-me">A symbol of patriarchal authority.</p>
      <p class="pc-note">Adam: …… He understood nothing. But he understood, at some level, that Baek Si-on was enjoying this.</p>
      <p class="pc-them">Wedding three: security thought we were crashers.</p>
      <p class="pc-them">Wedding four: the PA was wired wrong — I opened my mouth and the mic was dead.</p>
      <p class="pc-them">Wedding five: we finally get going and the best man out-screams the bride and steals three shots.</p>
      <p class="pc-them">Wedding six: the groom’s mother cried so hard we thought she was moved. Turns out she thought the budget had busted again.</p>
      <p class="pc-note">Baek Si-on: ……</p>
      <p class="pc-me">Adam. Every failure gets cut.</p>
      <p class="pc-me">The audience only ever sees the ones that worked.</p>
      <p class="pc-me">They’ll see the door open, the band appear, the bride scream, the groom hug you, everyone cheer.</p>
      <p class="pc-me">They will not see the father-in-law’s belt.</p>
      <p class="pc-note">…… Adam was strangled into silence for a while. Then he sighed.</p>
      <p class="pc-them">Honestly, though — the two that worked, worked GREAT.</p>
      <p class="pc-note">Baek Si-on made the acknowledging sound.</p>
      <p class="pc-me">Then it’s fine.</p>
      <p class="pc-me">You were merely permitted to want to kill me during execution.</p>
      <p class="pc-me">You can decide again when you see the final cut.</p>
      <p class="pc-note">Adam laughed.</p>
      <p class="pc-them">Fine.</p>
      <p class="pc-them">If it actually blows up, I’ll hate you a little less.</p>
      <p class="pc-note">Baek Si-on said:</p>
      <p class="pc-me">If it blows up, you owe me dinner.</p>
      <p class="pc-them">You’re demanding MEALS now?</p>
      <p class="pc-me">Idea fee.</p>
      <p class="pc-note">…… Adam swore down the line — no real heat in it anywhere.</p>
      <p class="pc-note">Baek Si-on added:</p>
      <p class="pc-me">I’m doing a test show out here in a few days. Then possibly a full North American tour after.</p>
      <p class="pc-note">Adam perked up immediately. He knew perfectly well what it means for a Korean artist to tour America — it is not an Asian tour with longer flights.</p>
      <p class="pc-them">Seriously?</p>
      <p class="pc-me">If the test show lands, come play Sugar for audiences that don’t pull belts.</p>
      <p class="pc-note">Adam: ……</p>
    </div>'''

# ---------------- ch156 ----------------
p156 = TEXT + 'chapter-156.xhtml'
start156 = '<p class="dialogue-line">“Young Master. You were looking for me.”</p>'
end156 = '<p class="dialogue-line">“Some other day, on my father’s behalf — I’ll buy you a proper cup of tea.”</p>'

block156 = '''<div class="phone-call">
      <p class="pc-head">Shin Hyung-kwan ← Lee Seon-ho · the MAMA control room · incoming</p>
      <p class="pc-me">Young Master. You were looking for me.</p>
      <p class="pc-note">The other end was quiet for a beat. Then a young man’s voice came through, mild as milk.</p>
      <p class="pc-them">Director Shin, you’ve got the wrong person, I think.</p>
      <p class="pc-them">In this company, you’re the elder. The department head. I’m a lowly assistant manager in the sugar division — for you to call me ‘young master’…</p>
      <p class="pc-note">Shin Hyung-kwan’s cold sweat arrived on schedule.</p>
      <p class="pc-note">The whole CJ Group knew who this was. The young man carrying the business card of an “assistant manager” was the chairman’s eldest son — the single, unambiguous heir to the empire.</p>
      <p class="pc-me">No, no — you honor me too much.</p>
      <p class="pc-me">What are your instructions?</p>
      <p class="pc-note">A small laugh from the other end.</p>
      <p class="pc-them">Instructions? Nothing so grand.</p>
      <p class="pc-them">Just a junior colleague in the field, reporting a little difficulty at work.</p>
      <p class="pc-note">The young master’s name was never spoken. He didn’t need it. Lee Seon-ho sighed — a real sigh, performed at the exact resonance of a junior employee genuinely worried about his KPI.</p>
      <p class="pc-them">I’ve recently been handling global marketing data for the sugar division.</p>
      <p class="pc-them">Mr. Baek Si-on is our newly signed endorser. He’s supposed to help pull up our North America business.</p>
      <p class="pc-them">But just now I heard that Mr. Baek is upset over something at MAMA, and that it might affect future cooperation.</p>
      <p class="pc-note">Shin Hyung-kwan opened his mouth. Nothing came out.</p>
      <p class="pc-note">Lee Seon-ho kept going, unhurried:</p>
      <p class="pc-them">You’re an elder of this group — you’ve watched CJ grow since the beginning. You understand our situation better than anyone.</p>
      <p class="pc-them">Father is where he is. Aunt is in the States. The whole group is walking a wire, and the wire doesn’t take gusts.</p>
      <p class="pc-them">So teach me: if one trophy makes Mr. Baek stop working, and CJ’s market cap evaporates by several trillion tomorrow — what do I tell the shareholders? And what do I tell my father, from where he is?</p>
      <p class="pc-note">Shin Hyung-kwan: ……</p>
      <p class="pc-note">The control room roared around him — cued graphics, talking heads, a stage manager shouting about a rundown change — and yet in his ears the whole room reduced to one phrase on a loop: <em>market cap, several trillion.</em></p>
      <p class="pc-note">Wait.</p>
      <p class="pc-note">Wasn’t this about Lee Ji-eun?</p>
      <p class="pc-note">How had it become about Baek Si-on? How had it become about CheilJedang’s market cap? How had defending Mnet’s rules, one phone call ago, turned him into the risk source of the group’s entire global business?</p>
      <p class="pc-note">He hurried to explain:</p>
      <p class="pc-me">No — no, it’s not like that.</p>
      <p class="pc-me">Yo— Assistant Manager Lee. We have treated Mr. Baek Si-on with the utmost seriousness.</p>
      <p class="pc-me">He was given the opening stage. The center of the artist seating. The camera time — generous, you can check the rundown.</p>
      <p class="pc-me">When he asked for chairs for T-ara just now, we moved without one word of argument.</p>
      <p class="pc-me">If his album release hadn’t fallen after the voting cutoff, the three grand prizes were — frankly — being prepared for him anyway.</p>
      <p class="pc-note">It came out in one breath — so fast that several staff members at the neighboring desks developed sudden, total deafness while staring very hard at their screens.</p>
      <p class="pc-them">Is that so.</p>
      <p class="pc-note">On the other end, Lee Seon-ho pressed two fingers to his temple.</p>
      <p class="pc-note">Not one lamp in this entire generation of old guard burned anything but oil. When Lee Myung-han had called, the story arrived pre-seasoned to “CJ stock limit-down by tomorrow’s bell.” Having now seen the raw material himself, Lee Seon-ho could report: the underlying incident was nowhere near that grave. And every single person who touched it shoved it one degree closer to grave anyway. That was CJ’s internal weather system. Four dozen managers in their late forties, each privately convinced he was the one irreplaceable pillar of the group — while the “assistant manager of the sugar division,” whose actual daily job was walking between those pillars keeping them from toppling in the same direction at once, aged one year per quarter.</p>
      <p class="pc-note">Worse than prison, honestly. Prison doesn’t make you mediate your own subordinates.</p>
      <p class="pc-them">In any case — I’d like this event managed sensibly, Director Shin.</p>
      <p class="pc-them">If a trophy allocation creates feelings on Mr. Baek’s side, which then touches the sugar division’s global endorsement and tvN’s broadcast contract…</p>
      <p class="pc-note">He let the sentence stop and stand there.</p>
      <p class="pc-them">That kind of chain reaction is beyond what one assistant manager can absorb.</p>
      <p class="pc-note">Shin Hyung-kwan heard every word that wasn’t said. The meaning came through clean as a stage direction: <em>if CJ ENM wants to fight, fight with the doors closed. Don’t put it in front of partners and capital markets. And do not splash grease on the sugar division’s global endorsement.</em></p>
      <p class="pc-note">Lee Seon-ho was not out to demonstrate brilliant leadership in a storm season. He wanted exactly one thing: stability. No incidents. No embarrassments. No version of the future where his father and his aunt came home, pointed at him, and said: <em>Lee Seon-ho — you couldn’t even manage one small awards show?</em></p>
      <p class="pc-note">Shin Hyung-kwan was nodding before he knew it. The phone couldn’t see him. His voice could, and the spine in the voice had folded.</p>
      <p class="pc-me">Understood. I’ll re-coordinate the remaining awards immediately.</p>
      <p class="pc-note">Lee Seon-ho asked:</p>
      <p class="pc-them">Won’t that break the rules of your bureau?</p>
      <p class="pc-note">The probe was audible. Shin Hyung-kwan hurried over it:</p>
      <p class="pc-me">You flatter me by asking.</p>
      <p class="pc-me">At CJ, your — that is, the group’s interest is the only rule there is.</p>
      <p class="pc-note">A small laugh.</p>
      <p class="pc-them">Then thank you for the trouble, Director Shin.</p>
      <p class="pc-them">Some other day, on my father’s behalf — I’ll buy you a proper cup of tea.</p>
    </div>'''

splice(p169, start169, end169, block169, from_end=True)
splice(p156, start156, end156, block156)
print('DONE')
