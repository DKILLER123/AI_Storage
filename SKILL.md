# SKILL.md — Skills for Producing the *Seoul: Starting With Debt Collection From the Nation's Little Sister* EPUB

> Reusable, de-duplicated skills used to author, fix, QA, and package this webnovel's EPUB (currently through ch154, V20).
> Use this file as the operating manual for every future chapter batch. House rules are mandatory, not stylistic.

---

## 1. Project Layout & Pipeline

| Item | Location |
|---|---|
| EPUB source root | `/home/user/work/epub_src/OEBPS/` |
| Chapter XHTML | `OEBPS/text/chapter-NNN.xhtml` (full standalone XHTML + wrapper) |
| Package & nav | `OEBPS/content.opf`, `OEBPS/nav.xhtml`, `OEBPS/toc.ncx` |
| Stylesheet | `OEBPS/styles/stylesheet.css` (~575 classes, all components predefined) |
| Character intro page (hover targets) | `OEBPS/text/character-intro.xhtml` (`id="chr-…"` per person) |
| Portrait images | `OEBPS/images/` (referenced by anchors and the manifest) |
| Raw chapter text (Chinese) | `/home/user/raw/chapter-NNN.txt` — archive every batch here |
| Build scripts | `/home/user/book/build_epub_vN.py` (V20 is current) |
| Worklog | `/home/user/worklog.md` — append one `§NN` entry per delivered pass |
| Deliverable | `/home/user/Seoul_Starting_With_Debt_Collection__Version_N.epub` |

**Pipeline order (never skip):** draft chapter file(s) → XML-validate → style-block audit → anchor pass → registration (opf/nav/ncx) → full QA suite → build → epubcheck → clean old versions → worklog + SKILL.md update → present.

---

## 2. Translation & Prose Standards

- **Unabridged translation.** Every scene beat in the raw must appear. Add enrichment/research (real-world chart/history/music facts, culturally accurate texture) only where context is thin, and keep it consistent with the book's alternate-2014 framing. Never invent events that contradict the raw.
- **House address/honorifics:** "Oppa" for Eun-ah→Si-on, `sunbae`, `-ssi` as established; preserve the book's existing romanizations and character-name forms (see §4 table).
- **House canon lyrics are frozen:** `Legend` = "Here we go, here we go— / … / Won't stop till we're legends—" etc. Do not paraphrase established lyrics.
- **Curly typography only:** no straight apostrophes or quotes in prose; zero CJK/fullwidth leftovers. Use `’` `“` `”` and `——`-style emphasis with spaced em dashes (` — `) as the book does. Silence lines use the `“……”` dialogue-line convention.
- **Document naming:** each chapter gets `Chapter One Hundred N…` numbering + a distinctive English title; the `<title>`, `<h1>`, nav `<a>`, and NCX label must match exactly.

---

## 3. Style-Block Vocabulary (context → component)

Match each in-verse context to an existing CSS component. If a scene is a *display artifact* (screen, post, headline, chat, chart, broadcast), it must be a block — never flat prose.

| Context | Component | Key child classes |
|---|---|---|
| Music/song playback or demo | `.music-player` | `mp-art`, `mp-title`, `mp-artist`, `mp-trackbar .filled`, `mp-lyric` |
| Chart result | `.billboard-chart` | `bb-kicker`, `bb-title`, `bb-artist`, `bb-rank`, `bb-note` |
| Social / viral callout | `.highlight-block` | `hl-kicker`, `hl-tag`, `hl-rank` |
| A posted tweet/social post | `.official-post` | `op-band`, `op-handle`, `op-body`, `op-meta` |
| TV/radio/live broadcast or stream | `.live-stage` | `ls-header`, `ls-scene`, `ls-line`, `ls-note` |
| Screen/UI/player/window contents | `.screen-view` | `sv-header`, `sv-scene`, `sv-line`, `sv-caption`, `sv-note` |
| News headline/dispatch | `.news-digest` | `nd-source`, `nd-headline` |
| Chart/ranking list (search, charts) | `.trend-block` | `tr-header`, `tr-rank`, `tr-work`, `tr-hot`, `tr-note` |
| Naver-style realtime search | `.naver-search` | `nv-header`, `nv-row`, `nv-rank`, `nv-term`, `nv-note` |
| Comment threads | `.comment-thread` | `comment-header`, `comment-item`, `comment-user`, `comment-floor` |
| Press/magazine editorial card | `.magazine-block` | `mg-masthead`, `mg-title`, `mg-deck`, `mg-credit`, `mg-note` |
| Official statement | `.official-statement` | `os-masthead`, `os-title`, `os-clause`, `os-sign` |
| Media Q&A / interview | `.interview-block` | `iv-kicker`, `iv-q`, `iv-a`, `iv-note` |
| Album/product card | `.album-card` | `al-header`, `al-cover`, `al-title`, `al-line`, `al-release` |
| Voice-over pull quote | `.pullquote` | body `p`s, `.pq-glyph` (✦ divider), `.pq-cite` |
| Clothing/suit scene | `.wardrobe-block` | `wd-header`, `wd-item`, `wd-note` |
| Phone chat (KakaoTalk-style) | `.chat-container` | `chat-header`, `chat-name self` (sent) / `chat-received` (received), `chat-bubble chat-sent/chat-received`, `chat-clear` |
| Scene/location heading | `.location-stamp` | `ls-date`, `ls-time`, `ls-place`, `ls-sub`; section divider `scene-break` `✿ ✿ ✿` |

**Rules of thumb:** one component per distinct artifact; narration explaining an artifact stays in plain prose around it; do not force a block where plain narration fits (the §50 defect class was the reverse — context that belonged in blocks being left as prose).

---

## 4. Hover-Preview Anchors (the recurring high-impact rule)

Every carded character name must be **anchored on every mention** in narration paragraphs (classless `<p>`) and in `dialogue-line` paragraphs — not just the first mention. This was the single biggest fix in the review pass (ch128–130 went from ~20 to ~100 anchors each).

- **Anchor markup (must match house exactly):**
  ```html
  <a class="chr-inline" href="character-intro.xhtml#chr-baek-sion"><span class="chr-peek"><img src="../images/baek-sion.jpg" alt=""/></span>Baek Si-on</a>
  ```
- **Canonical name-form map** (form → `chr-` id → image; short forms anchor to the same target as full names):

  | Name forms used in prose | `character-intro.xhtml#` | image |
  |---|---|---|
  | Baek Si-on, Si-on | `chr-baek-sion` | `baek-sion.jpg` |
  | Baek Eun-ah, Eun-ah | `chr-baek-eunah` | `eun-ah.jpg` |
  | Scooter Braun, Scooter | `chr-scooter-braun` | `scooter-braun.jpg` |
  | Baek Jeong-hun, Jeong-hun | `chr-baek-jeonghun` | `baek-jeonghun.jpg` |
  | Jung Jae-joon, Jae-joon | `chr-jung-jae-joon` | `jung-jae-joon.jpg` |
  | Choi Jin-ri, Jin-ri, Sulli | `chr-choi-jinri` | `sulli.jpg` |
  | Lee Ji-eun, Ji-eun, IU | `chr-lee-ji-eun` | `iu.jpg` |
  | Jeong Han-teuk, Han-teuk | `chr-jeong-hanteuk` | `han-teuk.jpg` |
  | Yoon Hye-ja, Hye-ja | `chr-yoon-hyeja` | `yoon-hyeja.jpg` |
  | Park Ji-hun | `chr-park-jihun` | `park-jihun.jpg` |
  | Kobe, Kobe Bryant | `chr-kobe-bryant` | `kobe-bryant.jpg` |
  | LeBron, LeBron James | `chr-lebron-james` | `lebron-james.jpg` |
  | Adam, Adam Levine | `chr-adam-levine` | `adam-levine.jpg` |
  | Justin, Justin Bieber | `chr-justin-bieber` | `justin-bieber.jpg` |
  | Ari, Ariana Grande | `chr-ariana-grande` | `ariana-grande.jpg` |
  | Bong Joon-ho, Bong | `chr-bong-joonho` | `bong-joonho.jpg` |
  | Song Kang-ho | `chr-song-kangho` | `song-kangho.jpg` |
  | Lee Joon-ik | `chr-lee-joonik` | `lee-joonik.jpg` |
  | Bang Si-hyuk | `chr-bang-sihyuk` | `bang-sihyuk.jpg` |
  | Irene, Seul-gi/Kang Seul-gi, Seung-wan/Son Seung-wan, Soo-young/Park Soo-young | `chr-irene`, `chr-seulgi`, `chr-wendy`, `chr-joy` | `irene.jpg`, `seulgi.jpg`, `wendy.jpg`, `joy.jpg` |
  | BTS: Kim Nam-joon, Kim Seok-jin, Min Yoon-gi, Jung Ho-seok, Park Ji-min, Kim Tae-hyung, Jeon Jung-kook | `chr-kim-namjoon`, `chr-kim-seokjin`, `chr-min-yoongi`, `chr-jung-hoseok`, `chr-park-jimin`, `chr-kim-taehyung`, `chr-jeon-jungkook` | matching `kim-*.jpg` / `min-yoongi.jpg` / `jung-hoseok.jpg` / `park-jimin.jpg` / `jeon-jungkook.jpg` |

- **Where NOT to anchor:** inside UI/screen surfaces — `sv-*`, `nd-*`, `nv-*`, `comment-*`, `mp-*`, `ls-*`, `op-*`, `bb-*`, `chat-name`/headers, `location-stamp`, page titles. These render as third-party/display text.
- **Mechanics:** run one pass over each paragraph with a longest-first name-form alternation; skip any match that overlaps an existing `chr-inline` anchor (prevents nested/double anchors). Apply only to classless `<p>` and `dialogue-line`.
- **Possessives stay outside** the anchor: `<a …>Baek Si-on</a>’s`.
- **Cameo/media figures with no portrait card stay plain text** (never fabricate an anchor): Kevin Plank, Stephen Curry, Pharrell Williams, The Game, Bruno Mars, Kyu Sakamoto, Taylor Swift, Meghan Trainor, Shaq, Snoop, 50 Cent, Jeremy Lin, Harry Styles, Rag’n’Bone Man. New real people get cards only if a usable portrait exists and they become recurring cast (§50 rule).

---

## 5. Lyric Formatting

- All sung lyric lines live in `.music-player` cards as `<p class="mp-lyric">…</p>` — **never** as `dialogue-line` paragraphs. This includes short chorus/hook lines (e.g., five stacked hook lines are five consecutive `mp-lyric` rows inside one music-player block titled to the part, e.g. “the hook”).
- Wrap line text with a trailing em dash (`—`) as the book does; use `…` for omitted lines.
- Keep lyrics that are in-house canon exactly as previously established.

---

## 6. screen-view Alignment

- Within one `.screen-view`, rows that belong to the same column (filenames, tracklists, on-screen data) must use the **same** row class (`sv-line` for aligned rows, `sv-scene` for italic action captions, `sv-note` for a single dim closing remark).
- Don't mix `sv-scene`/`sv-line` for items of equal rank — that causes ragged indentation/colour (the exact defect flagged in review). A consistent list = `sv-header` + all `sv-line`.
- Use `sv-caption` (centred highlight) only for genuine on-screen captions/titles.

---

## 7. Registration Checklist (every delivered chapter)

1. `content.opf` — add `<item id="chNNN" href="text/chapter-NNN.xhtml" media-type="application/xhtml+xml"/>` in the manifest (after the previous chapter) **and** `<itemref idref="chNNN"/>` in the spine (after the previous chapter). New inline images also need a manifest `<item>` (`img-*`).
2. `nav.xhtml` — add the `<li><a href="text/chapter-NNN.xhtml">Chapter NNN …</a></li>` after the previous chapter's `<li>`.
3. `toc.ncx` — add `<navPoint id="np-K" playOrder="K">` after the previous chapter's navPoint, with the identical label text.
4. Verify nav/NCX/`<title>`/`<h1>` labels match exactly.

---

## 8. QA Suite (run every pass; no chapter ships without it)

- **XML well-formedness** for every touched file (minidom/ElementTree).
- **Anchor href audit:** every `character-intro.xhtml#chr-…` in all chapters resolves to an existing `id`; same for `characters.xhtml#…`. Report 0 missing.
- **Residual-plain audit:** in classless `<p>` + `dialogue-line`, zero unanchored carded-name mentions remain (name-form map from §4).
- **Nested-anchor check:** no `<a class="chr-inline"…>` inside another anchor.
- **CSS coverage:** every `class=` token in new chapters exists in `stylesheet.css`.
- **Image audit:** every `<img src="../images/…">` exists on disk **and** is listed in the OPF manifest.
- **Typography scan:** zero ASCII `'`/`"` and zero CJK/fullwidth in stripped chapter text; curly-quote balance per chapter (allow one decorative `pq-glyph` glyph inside `.pullquote` only).
- **epubcheck:** re-download `epubcheck-5.1.0.zip` if `/tmp` was wiped; run `java -jar epubcheck-5.1.0/epubcheck.jar <file>` — target **0 fatals / 0 errors / 0 warnings / 0 infos**.

---

## 9. Build, Versioning & Workspace Hygiene

- Build with the current `book/build_epub_vN.py` pattern: write `mimetype` first (stored, compress_type 0), then every other file under `epub_src` (deflated), excluding dotfiles. Keep the output path and docstring in sync with the new version.
- On-disk source must equal zip content for every touched file before declaring a version done.
- **Keep only the latest `.epub` in `/home/user`** — delete previous version files after the new build validates (user requirement).
- `epubcheck`, `fonts`, and any other dependency living in `/tmp` are NOT persisted; reinstall at the start of a session if missing.
- Every pass gets a `worklog.md` `§NN` entry (trigger, fixes, registrations, QA numbers, output identity, open items).
- Every new raw batch is archived to `/home/user/raw/chapter-NNN.txt` before translating.

---

## 10. Content-Accuracy Guards (2014 alternate-world frame)

- Real people, songs, releases, chart positions, and historical facts referenced in narration must be true for the in-verse date (e.g., Kyu Sakamoto’s "Sukiyaki" topping the US Hot 100 in 1963; AMAs dates; Music Bank broadcast day; Red Velvet promotion eras).
- Do not import post-2014 real-world events into 2014 narration (e.g., a demo titled "Sign of the Times" predating its real 2017 release is fine as in-verse songwriting, but do not reference the real-world song’s release or artist context).
- Keep the raw text’s fictional chart orders and numbers intact even where they differ from real charts.
- Where the raw’s historical shorthand is fuzzy (e.g., a "MacArthur" analogy), phrase it symbolically rather than asserting a wrong date.

---

## 11 · Scene Craft & Emotional Rhythm (interpersonal chapters)

High-drama, low-artifact chapters (drives, quiet rooms, phone calls) need the fewest *display* blocks — over-blocking shreds intimacy. Master these micro-rhythms instead:

- **Deadpan-exchange engine:** the house comedy/romance default is a laconic speaker (Baek Si-on) against a talkative one (Choi Jin-ri / Scooter Braun). Keep replies to one flat sentence; let the other character over-read them. E.g., "Sand." → she genuinely can't tell if it's a joke. Tension lives in the gap.
- **Bubble-pop beat:** let the warm character's mood visibly inflate, then deflate on a single flat line ("No need." / *pop*), then recover with a teasing counter ("Afraid you'd go broke."). Three beats: lift → prick → pivot.
- **The standoff stalemate** ("You go up first." / "You go first." × N): repeat the same two lines; break the loop with the softer character conceding after a counted pause (one/two/three seconds). The winner is the one who can wait.
- **Watching-until-safe beat:** character stays put until a concrete signal (a light coming on in the building) then leaves; narrate the rear-view mirror after-image. This says more than any line.
- **The instructive question** (Sulli: "do you know what a normal person should say?") — the character teaches the expected script; the other refuses it ("Then that's not it."). Reader supplies the warmth the flat speaker won't.
- **Off-screen hypothetical aside:** a narrator what-if starring an absent carded person (the Scooter "I'm the candle" aside) provides comic relief and reinforces established voices. Keep it short, clearly speculative, and anchored.
- **Gift scenes as character files:** the *content* of a gift (camel-milk chocolate, dates, saffron), the receiver's reaction order, and the giver's *stated* reason ("bought them to give away") all carry subtext. Vary the beat order to avoid formula.

## 12 · Character-Voice & Address Cheat-Sheet (recurring cast)

Speech DNA to preserve, plus binding address rules. Keep these stable across every chapter batch:

| Character | Voice traits | Fixed address patterns |
|---|---|---|
| Baek Si-on | Minimal replies, flat deadpan, literal answers, protective in actions not words | "Baek Si-on-ssi" (others); addresses Jeong-hun as "Uncle"; "Father-King" inside the film role |
| Choi Jin-ri (Sulli) | Bright, self-teasing, over-thinks his words, brave publicly | Called "Peach" by IU & Goo Hara; "Jin-ri"/"Jin-ri-ssi" elsewhere; calls Baek "Baek Si-on-ssi" when teasing; Eun-ah calls her "Jin-ri eonni" |
| Baek Eun-ah | Fast, loyal, comic narrator of Baek's love life, formal at work | "Oppa" → Baek Si-on; "eonni" → Jin-ri, IU |
| Scooter Braun | Negotiation theatre, bombastic, secretly fond | "Baek." direct address; calls himself the candle/highest-value asset |
| Goo Hara | Playful interrogation, affectionate elder, tour-hardened | Sulli calls her "eonni"; calls Sulli "Peach" / "Jin-ri" |
| Lee Ji-eun (IU) | Warm, low-key, sharp | Sulli calls her "Ji-eun eonni" (IU is older); she calls Sulli "Peach" |
| Song Kang-ho | Teasing sunbae, dry observational wit | "Sunbae" from Baek; jokes about the Crown Prince |
| Lee Joon-ik | Terse, deadpan, frames everything through the monitor | Baek calls him "Director" |

- **Age/order check for eonni/unnie:** IU (b.1993) & Hara (b.1991) are older than Sulli (b.1994) → they are her *eonni*; Eun-ah is younger than Jin-ri → Eun-ah says *eonni*. Verify birth-order before assigning; the wrong suffix breaks character.
- Nicknames (Peach) are not `chr-inline` anchor forms — leave unanchored.

## 13 · Additional Context→Block Mappings (call, film set, banners, notices)

Extends §3 with components encountered in the review/133–134 batches:

| Context | Component | Children & usage notes |
|---|---|---|
| Voice/video call (FaceTime/KakaoTalk video) | `.facetime` | `ft-bar` (call bar, auto green dot), `ft-party` (context line), `ft-me` (speaker's own bubbles, blue), `ft-them` (other party, italic green), `ft-note` (action); map POV: bubbles are labelled from the POV character's screen |
| Ambient crowd/murmur quotes | `.dialogue-block` | `dl-header`, `dl-line`, `dl-note`; perfect for court murmurs, lot whispers, launch-hall chatter |
| Ceremonial/performance moment | `.stage-block` | `st-header`, `st-scene`, `st-line`, `st-note` |
| Clapper/slate or standalone live cue | `.live-stage` | reuse `ls-header/ls-scene/ls-line` for broadcast/cue moments (ESPN-style live feed) |
| **Filmed scene being shot** (on-set performance, actor takes) | `.acting-block` | `ac-slate` (slate line: “scene twelve, camera two — take two”), `ac-heading`, `ac-cue` (standalone “Action” chip **or** inline speaker chip like `SADO`), `ac-direction` (blocking/camera), `ac-line` (performed spoken lines), `ac-note` (director/monitor read). House precedent ch02/08/11/13/83/112; applied ch134 take one/take two. |
| Box-office/scoreboard metric | `.box-office` | `bo-header`, `bo-title`, `bo-row` (`bo-label`+`bo-figure`), `bo-rank`, `bo-note` |
| Printed sign / support-truck / flyer | `.flyer-block` | `fl-band`, `fl-title`, `fl-when`, `fl-note` (dashed orange border, physical print feel) |
| Government/official notice | `.official-statement` | `os-masthead`, `os-title`, `os-clause`, `os-sign` |
| Government/search/news artifacts | `news-digest`, `naver-search`, `trend-block` | as §3 |

**Dramatic-take balance:** a *live* in-verse performance the audience is meant to feel (an acceptance speech, a concert) stays prose-first — never place display blocks inside that dramatic sequence. **But a scene being filmed for the in-verse movie is itself a production artifact** (actors on a set, clapper, repeated takes, director at the monitor): the performed dialogue must be carded as `.acting-block` rows (`ac-line` with `ac-cue` speaker chips, `ac-direction` blocking, `ac-slate`/`ac-heading`, `ac-note` monitor reads) — not flat `dialogue-line` prose (user-corrected in the V8 pass, ch134). Keep narration about the *crew* (director, lead actors, monitor) in prose around the block.

## 14 · Batch Research Discipline (deep context for every chapter)

Before/while translating each raw batch:

1. Archive the raw under `/home/user/raw/chapter-NNN.txt` immediately.
2. Research only the real-world facts the narration *will rest on*: period history, real people's 2014 contexts, release/chart/tour dates, venues, agencies. Log takeaways (and URLs) in the worklog's External Sources.
3. Keep the raw's **fictional** numbers, rankings, and timing intact even where real history differs.
4. Never import post-2014 real-world events into 2014 narration (no referencing a 2015 song release as a past event, etc.).
5. Use research to enrich, not to contradict: e.g., ground Goo Hara's "full houses in Japan" with the real KARA 3rd Japan Tour (Oct–Nov 2014); ground Sado history (Yeongjo r. 1724–1776; Sado made regent 1749; the rice-chest death, July 1762) but only state what the story needs.

## 15 · In-Verse Timeline Clock

Keep a running "now" while writing multi-chapter batches and record it in the worklog:
- Example clock: ch131 = morning after the Billboard #1 (Oct 30 2014 LA); ch132 = same day afternoon + Nov 1 Korea (Incheon 6:17 a.m., Sado kickoff, GBF premiere night, cake 21:00); ch133 = Nov 1 night 21:17 → Seoul→Jeonju drive → Seongbuk-gu → Sulli home 22:00+ (Hara call); ch134 = Nov 2 morning (Blue House #2, 120k first day, Sado court scene, trucks 11:21).
- Cross-check every `location-stamp`, "the same day/night/morning", and sleep budget (Baek's 4-hour sleep math in ch133) against this clock so nothing drifts.
- Anchor continuity devices the raw relies on: the borrowed uncle's car, the "no candles in America" callback, "bigger cake next time" paying off as the two support trucks arriving the very next morning.

## 16 · Prose QA Micro-Checks (in addition to §8)

- **No invented CSS sub-classes:** never introduce a class that does not exist (e.g., `mp-note` was flagged). If a block needs a stray observation, put it in a neighbouring existing class or move it outside the block as plain prose.
- **Anchor possessives/suffixes outside:** `</a>’s`, `</a>-ssi`, `</a> eonni`, `</a> sunbae` etc. — matches house convention (verified across the book).
- **Quote balance per <p>:** an unmatched `“` is acceptable only as the decorative `.pullquote` glyph; everything else should balance.
- **Read-aloud pass:** each chapter's dialogue should sound like its speaker (see §12) — check the deadpan lines are actually flat, the affectionate lines actually warm.

## 17 · Block-Strictness Regressions: Video Calls & Filmed Acting (V8 bugfix)

Two user-flagged regressions from the ch133/134 V7 delivery — do not repeat:

- **A voice/video call between two people is ALWAYS a `.facetime` block** (`ft-bar` + `ft-party` + alternating `ft-them`/`ft-me` bubbles + `ft-note` stage notes; POV is the on-screen character's). Never render a call as narrated prose or `dialogue-line` attribution. House precedent: ch116; fix applied: ch133 Hara video call → two `.facetime` blocks (KakaoTalk · video call bar, Japan hotel party line, news/press-conference callbacks inside bubbles).
- **On-set filmed acting is ALWAYS `.acting-block` carding.** Performed lines = `ac-line` rows with `ac-cue` speaker chips (`SADO`, `YEONGJO · OFF`, `MINISTER`); blocking/camera/mood = `ac-direction`; the slate ("scene twelve · camera two · take two") and take heading = `ac-slate`/`ac-heading`; a director/monitor beat that belongs to the take = `ac-note`. Never render the performed film lines as `.dialogue-line` prose with narration around them. Fix applied: ch134 Sado court scene, take one (full card) and take two (slate + heading under the crew banter, `Print one` retained as prose).
- **Row content in `ft-*` bubbles and `ac-*` rows stays plain** — like other UI/display surfaces (§4), no `chr-inline` anchors inside (verified ch133/134 = 0). Crew narration *around* the block stays normal anchored prose. In-film role names in `ac-cue` chips are role labels, not carded forms.
- After any block rework, re-run the full §8 QA suite plus per-chapter residual-plain and typography scans — a block conversion changes anchor counts (ch133: 126→95, ch134: 68→59, both from prose→block movement) and can hide leftover duplication.

## 18 · Dual-POV Comedy, Long-Take Continuity & Adaptation Discipline (ch135–136)

Applied while writing the Jeonju-set two-chapter arc (support trucks / Peach–IU misunderstanding / Sado retakes / saffron payoff):

- **Parallel-misconception engine:** when two characters each privately "prove" the same fact in their own favour (both women certain the stray glance was meant for *her*), write the two deductions as mirror-image passages with matching beats ("One hundred percent. Absolutely." beside "She was quite sure of it.") — same length, same certainty, opposite subjects. The narrator states both cannot win. Reader laughs at the geometry, not the jokes.
- **Enumeration-as-comedy:** a character's overwhelmed brain can be rendered as a numbered internal list (First / Second / Third — the strand that ties the knot), each item a short paragraph, ending in a distilled absurd question ("Simple, or not simple?"). Pairs well with the §11 deadpan engine when the flat speaker stays silent through the whole spiral.
- **A filmed performance spanning two chapters:** the "take" scenes (court take-one/take-two in ch134; side-hall take-one/take-two in ch135) stay in the same `.acting-block` grammar across chapter boundaries — `ac-slate` with scene/take, `ac-heading`, `Action` chip, performed lines as `ac-line` with `ac-cue` speaker chips (SADO / HONG BONG-HAN / EUNUCH), blocking & camera as `ac-direction`. When take two re-runs the same speech, do NOT repeat take one's `ac-line`s verbatim — compress into a direction ("the same speech from the top…") and card only the *new* beats (the eunuch's line, Sado's final line). Crew/director speech ("Cut", the tease, the monitor read) stays outside the block as prose/dialogue-line.
- **Set-comedy beat:** the AD/director "both staring professionally at the monitor, unable to hold it in" exit gag — keep the *crew* reaction as dialogue, and let the punchline land in a distance ("40 minutes") with a one-word button ("……").
- **Prop continuity:** an object carried across a chapter break (Jin-ri's coffee, IU's rubber-banded stub stack) can be the visual that carries the scene; reference it once, plainly, at each handoff.
- **Banner/artifact echo, not re-card:** if a display artifact (support-truck banner) was already carded as a `.flyer-block` in an earlier chapter, a later scene where a character *reads* it should echo the text in prose — do not emit a second identical flyer-block.
- **Adaptation discipline:** when a raw's throwaway joke contradicts established canon (Eun-ah "should be getting yelled at in an SM practice room" — she is S.W Studio's artist-management head, not a trainee), re-target the joke to the character's real life (her age vs her job) rather than importing the contradiction. Keep nicknames ("Peach") unanchored; anchor every carded-name mention inside prose and dialogue-line but never inside `ac-*`/`ft-*` rows (structural plain).
- **Scene numbers:** when the raw gives no slate number, extend the production's existing numbering by one (`scene thirteen` after ch134's `scene twelve`) and note the assumption in the worklog — a later raw may correct it.

## 19 · State-Ceremony Leverage, Single-Source News Beats & Silent-Scene Discipline (ch137–138)

Applied while writing the album-vocal-completion + Billboard-back-to-back + awards-day chapters:

- **The gifted vehicle as apology:** when a sponsor sat out a controversy (Hyundai's wait-and-see after the Lakers affair) and the artist then delivered commercially (Aslan's four-thousand-first-day launch, the share-price "effect"), the mending arrives as *hardware*, not words — a high-roof luxury nanny van "outside the gift clauses," delivered in person, with the folder already made out. Frame it in the manager's economic brain (she converts it to a price, then refuses to) and against the older vehicle the same team used to run (the second-hand Carnival's bump gag returns as the contrast for "this van is proof").
- **Single-source news beats:** a real one-week news event (Taylor Swift pulling her catalogue off Spotify on 2014-11-03 over the free tier) is a gift to a serial-number-one story — but render the *platform's* interest, not the artist's: the label-manager character (Scooter) reframes it as Spotify's need to "manufacture a new god," and the only person who can force an Asian name onto the board agenda is a Spotify shareholder. Keep the reported facts exact (the catalogue, the date, the stated reason) and the strategic spin invented.
- **"Sing it about yourself":** when a song's intended commissioner (LeBron's camp) goes cold, repurposing the track for its actual owner is canon-friendly if earlier chapters planted the demo's origin (ch128 wrote *King* for LeBron). Reuse the planted rationale, don't invent a new one.
- **Second-week reactions escalate the artifacts:** first-#1 reactions = shock/doubt/ecstasy; second-week = *no surprise*. Escalate the display surfaces accordingly (red-type headline digest, a forum where even the absurd posts are calm, a midnight official post with a punning echo line). One canon repeat (the Blue House's second telegram) reads as a joke precisely because it's a repeat.
- **A silent scene stays prose:** an on-set painting scene with no performed dialogue does not need `.acting-block` — keep the take's texture (brush, ink, monitor, "Cut") as plain prose; a comedy beat *inside* the take (a manager with a phone pressed to her mouth, forced to swallow a Billboard scream) is narration, not `ac-line`.
- **The state-ceremony lever:** the Korean Popular Culture and Arts Awards is government-backed, so lateness is a national-news crime; that pressure is what licenses the absurd escalation (a sponsor's helicopter + a police escort) and the comedy ("the brand value is achieving three-dimensional, multi-scenario linkage" → "Translate, please" → "They want to be on the news too").
- **Seniors' cover changes the optics:** the same act (arriving at an official ceremony in character costume) is "bad manners" alone but "a beautiful story" when a Song Kang-ho-level sunbae frames it ("Go wearing an actor's clothes") — state that rule explicitly as the scene's logic, then let the juniors accept.
- **Costume-dependency as a gag engine:** the stylist's panic over a costume/makeup change in transit (helicopter) generates both the real constraint (no dressing room on board, rotor wash) and the button line ("naked over Seoul").
- **QA habits this batch re-confirmed:** bare `????` dialogue (house, cf. ch128) is the replacement for a CJK 「？？？」; a draft-only class name (`nd-header`) must be swapped for the existing stylesheet pair (`nd-source`/`nd-headline`) — never invent CSS; film-title italics (`<em>Sado</em>`) are used inconsistently even inside shipped chapters (ch132 11/14, ch134 0/5), so keep the new chapters within that tolerance rather than normalizing the whole book.

## 20 · Character-Intro Parity, Phone-Call Discipline & Deep-Scan (V10 review → V11)

Applied while reconciling the Character Intros page with the text chapters and sweeping every call in the book into `.phone-call` blocks:

- **Audit cards by their image key, never by parsed name.** Each `.char-intro` card is uniquely identifiable by its `chi-photo` img file. Match on that file across `character-intro.xhtml` and every chapter to count in-text cards exactly once; a display-name parser is unreliable (the page says "(Victoria)" for Song Qian while ch24 cards her as "Song Qian (Victoria Song)", and card order vs page order can differ). Expect exactly one card per person.
- **First-ref ≠ first-appearance.** A naive "first anchor precedes the card" scan over-flags every mention (posters, referral conversations, inbox messages, comment threads, a name on a delivered document). Classify each flagged ref scene-by-scene: physical presence (in the room / on stage / hand-on-shoulder) vs mere mention. Cards belong at the first *physical* intro; a name heard-of-but-not-seen is a mention. Keep later anchors out of the carded chapter where the card covers the debut.
- **Card-placement beats:** insert the `.char-intro` block right after the paragraph where the character steps into the scene (not at scene start, not before their name is spoken); for ensemble walk-ons (a jury, a court audience, a flight), if no one physically enters (they appear only as a mass in an applause climax), card the reader's true introduction — the dossier/chapter list where their name + role paragraph appears — one card following each name paragraph; a person whose own body is their appearance (a manager introducing herself with a handshake) cards at that self-intro beat; if a character's first ref is an *inbox message* their card waits for the next chapter's physical debut.
- **Move, don't duplicate.** When a card sits in a chapter after the character's true physical debut, cut it there and insert the same card (page payload verbatim: role/meta/desc) at the debut. One card per person, always; a reviewer's complaint about the last entries of the page usually indicates the first-appearance cards *after* the big early-chapter clusters were skipped entirely, plus a few misplaced ones — fix all of them, not just the reported tail.
- **Live calls are `.phone-call`; silence is not.** A call is only *rendered* as a block when the caller speaks or replies are being negotiated through the line; a phone that merely rings, or "the doorbell through the receiver," or someone re-dialing a dead line, or listening to someone else's call is narration — do not block it. A call split across scenes (interior monologue / third-party aside in between) continues in *blocks* — a second `.phone-call` whose `pc-head` says "the same call, continued" — so every spoken exchange of one continuous call shares the block grammar; only genuinely separate future calls get fresh headers.
- **Deep-scan phrases.** To find untagged live calls run `grep` for `on the other end`, `through the receiver`, `the voice came through`, `pressed the phone`, `on the line`, then triage by reading context. Triaged false positives this book: ear in-ears, music through a monitor, a phone pressed between shoulder and ear (one-sided), people *near* the phone, calls a character *overhears*.
- **Wrapper mechanics (learned the hard way):** when converting prose dialogue into `pc-me`/`pc-them` rows, (1) strip any `<a><span class="chr-peek">…</span>NAME</a>` anchor inside the row text and keep the plain name — `pc-*`/`chat-*` rows are structural and must contain no `chr-inline` anchors (house rule; `<em>` is fine); (2) slice regions only at whole-`<p>` boundaries — cutting mid-paragraph desyncs the `<div>` nesting and breaks XML; (3) read dialogue text *after* removing the outer `<p …>` tag, or the `class="…"` attribute quotes get counted as quote characters and mis-split rows; (4) trim exactly `</p>` (4 chars) off the tail, or you chop the closing `.”`; (5) when a conversion corrupts a file, restore it from the last validated epub (`unzip` the `.epub`, pick `OEBPS/text/chapter-NNN.xhtml`) and re-wrap rather than patching.
- **Voice messages & calls with no dedicated class:** check the stylesheet first (`.voice` in this book means recording/audio prose, not voicemail). When nothing fits, reuse the message-thread component: `.chat-container` with `chat-header` ("NAME · voice message"), a received `.chat-bubble` reading "▸ Voice message — tap to play", `chat-name`/`chat-meta` ("arrived on the set · unread"), and put any *reveal* of its contents in the following `dialogue-line` prose. Never invent classes.
- **Run the screen/UI-adjacent audit every pass:** check all 138 chapters parse XML, no `.char-intro` nested inside another display block, no anchors inside `.phone-call`/`.facetime`/`.chat-container`/acting/live rows, and (for ch137-style scenes) that news digests name real, varied outlets — not one aggregator for every story.

## 21 · Always-On Deep Scan & Display-Block Density (V11 review → V12)

The reviewer's standing rules, encoded so no release ships without them: Deep Thinking and Deep Scan are always enabled, and a display moment earns a block even when its in-raw context is thin — the translator fills the surrounding context from the story's own logic rather than leaving it as plain prose.

- **Phone-screen artifacts are blocks.** A Billboard (or any chart) that a character sees *on a phone screen* is a `.billboard-chart` like any other; give it a kicker that marks the surface ("on the phone · 11:00 p.m., Korea time") so two charts of the same refresh (a desk scene and a phone scene) stay distinct. Never leave a screen artifact as three short punch paragraphs.
- **A played voice message gets its own state.** The notification ("▸ Voice message — tap to play", "arrived · unread") and the *played* content are two `.chat-container`s: after "she tapped the bubble," a second container headed "NAME · voice message · played on speaker" carries the spoken content as a received bubble with a duration ("▸ 0:07 · “…”") and a "now playing · …" meta. Only existing chat classes; no invented CSS.
- **Audit a call from ring to hang-up, not just its visible dialogue.** A call that starts ("his phone rang — NAME") and ends ("she hung up") with salon/music interludes in the middle is *one continuous call*; every spoken exchange of it belongs in block grammar. Wrap the whole thing as a chain of `.phone-call` blocks (first: "· on the phone"; rest: "· the same call, continued"), letting bridging prose (in-person exchanges, listening beats, analyses) live *between* blocks — the ch137/ch103 split-call pattern. Incoming orientation is `A ← B` (the person who rang in on the right), consistent with ch127/ch137.
- **Verify rewraps by normalized diff.** After restructuring a region, strip all tags/anchors and whitespace, then diff the plain text against the pre-edit file (apostrophe-style-insensitive). The only allowed differences are added block headers and row wrappers. This catches accidental word loss (e.g., a merged "Baek Eun-ah's voice came through the receiver." narration sentence that a naive row split would silently drop).
- **Deep scan the whole book, every pass, at the anchor/display level too.** Besides call phrases, sweep for `chr-inline` anchors inside every display row class (`.phone-call`, `.chat-container`, `.comment-thread`, `.official-post`, `.billboard-chart`, `.news-digest`, `.live-stage`, `.location-stamp`, `.comment-item`, …). Legacy stragglers get fixed even when they predate the current batch (ch126 live-stage, ch129 bb-artist) — strip the anchor, keep the display name, and prove with an epub-diff that nothing else changed.
- **When in doubt, block it.** A state ceremony's citation video, the bilingual SK tweet, an office KakaoTalk exchange, live-broadcast barrages — each is a `.official-post` / `.chat-container` / `.comment-thread` even if the raw only implies the surface. Then fill context (attached-photo meta, arrival times, subtitle runs) from canon.
- **`chat-name self` precedes every own-sent bubble.** In a `.chat-container`, the name row that labels the screen owner's outgoing message must be `<p class="chat-name self">` (right-aligned, matching the yellow `chat-sent` bubble); only the other party's name rows stay `<p class="chat-name">` before `chat-received`. When creating or rewrapping chat threads, run the bookwide check: walk each container's `chat-name → chat-bubble` pairs and flag any plain `chat-name` that feeds a `chat-sent`.
- **Live and state events are broadcast blocks.** A ceremony or presentation that the reader watches as a TV/stream feed belongs in `.live-stage` grammar — `ls-header` (event · live · venue), `ls-scene` for what the frame shows, `ls-note` for reactions/applause texture, `ls-line` for on-mic speech — with a live-comments `.comment-thread` right beside it (pinning, walking the steps, the handshake). This mirrors the NBA/TNT live-stage usage and turns a "he did X, she did Y" prose run into the broadcast it actually is.
- **Known legacy (left alone, do not regress):** ~2,661 straight apostrophes remain in older chapters (ch21–24 / ch76–80 era); new and edited content is curly-only per §2. A future normalization pass would touch dozens of files; do not silently "fix" those during a chapter pass.

## 22 · Corporate/Finance & Negotiation Chapters (ch141–142)

Applied to the KB-crisis-room / market-open / Hyundai-van batch:

- **An enterprise comedy chapter is the densest block chapter in the book.** Every surface the executives look at is a display artifact: the projector (`screen-view` per slide or per frame), the news push (`sfx-line` "Ding." + `news-digest`), the article photograph (own `screen-view`, `sv-caption` for the image's thesis line), branch LED / app splash / balance page (one `screen-view` each), the bottom-crawl ticker (`sv-line` rows, ALL-CAPS source labels), the broadcast desk (chained `live-stage`s), the retail forum (`comment-thread` with stock-forum handles), and hard numbers (`finance-block`). Slide exhibits that re-show artifacts already carded in an earlier chapter (SK tweet, convoy video, speech excerpt) stay **prose echoes** — §18 banner rule.
- **Chat POV follows the phone's owner.** Jin-ri's thread on her phone: her sends are `chat-name self`. The same night, IU's thread on HIS phone: his sends are `chat-name self`. Splitting a thread around narration beats = multiple containers headed "…· the same chat, continued" (§20's call-chaining, applied to chats). Bookwide `chat-name self → chat-sent` audit after any new thread.
- **A broadcast split across a scene break or a time jump continues in chained `live-stage` blocks** ("…· the same broadcast, continued"; "…· the late-morning recap"). Keep the raw's number gags verbatim (narration says ₩3.4 trillion; the announcer reads "3.8 trillion won" with a knotted tongue and converts to $3.2B).
- **`.finance-block` has exactly four children: `fb-header`, `fb-row`, `fb-label`, `fb-value`.** There is no `fb-note` — a stray observation after the numbers goes into prose following the block (same discipline as the old `mp-note` lesson). Use it for deal snapshots too ("the deal, as agreed inside a van").
- **Coincidence of nicknames:** 银冠世子 = **"Silver Crown Crown Prince"** (standing coinage — Jin-ri's texts, Naver #1, the Crown Prince Index gag). Keep double-"Crown" everywhere; the clunk is the joke.
- **Timeline smoothing (raw is loose, the book clock is not):** crossing/ceremony/premiere = Nov 8 (ch139–140); anything the raw calls "the next morning" after that night = Nov 9; AMAs 2014 = Nov 23, so "half a month to rehearse" lands ✓. Where a raw direction contradicts canon geography (Jin-ri's van "toward Gangnam" then "toward Seongbuk"), keep one clean direction that matches her established home.
- **Chaebol principals with no cards stay plain text** (Chung Eui-sun, Chung Ji-sun — 2014 titles verified: Hyundai Motor vice chairman; Hyundai Department Store Group). 堂哥 from Eun-ah is always "Oppa" (§12); chaebol fake-familiarity renders as "Si-on-ah" / "Ji-sun-ah"; 会长nim/副会长nim = "Chairman-nim" / "Vice Chairman-nim".
- **An imagined broadcast is still a broadcast block.** Eun-ah's vision of the AMAs stage is a `live-stage` headed "…· as she imagines it" — the §21 "when in doubt, block it" rule extends to interior rehearsals of public events. A watched choreo draft is a `screen-view` split at each banter beat; the lyric cue lands as `sv-caption` ("Long live the king." — first canonical appearance, ch142).

## 23 · Finance-Takeover & LA-Logistics Chapters (ch143–144)

Applied to the market-takeover week and the AMAs arrival:

- **A market week is a block-per-artifact parade.** Contract marks (`contract-block`: `ct-header`/`ct-clause`/`ct-figure`/`ct-note` — never cb-), store walls and big-screen takeovers (`screen-view` with `sv-caption` for the slogan), retail forums (`comment-thread`, one thread per news beat), chart refreshes (`billboard-chart` per week), corporate announcements (`official-post`, photo description in `op-meta`), hard numbers (`finance-block`, label/value rows), broadcast chains (`live-stage` → wall-board `screen-view` → `live-stage` continued → live-crawl `comment-thread`).
- **Image filenames are verified, never guessed.** Seo Eun-ju's portrait is `seo-eunju.jpg` (chr-seo-eunju) — a guessed `seo-eun-ju.jpg` passed every local audit and was caught only by epubcheck RSC-007. Always grep an existing chapter for the card's exact img path before writing a new anchor.
- **Carded lawyers anchor too.** Seo Eun-ju is carded (chr-seo-eunju): every prose/dialogue mention gets `chr-inline`. Chaebol principals (Chung, Koo Kwang-mo) and cameo names (Marc, Vincent, PSY, Dwight Howard, the dancers) stay plain; real names inside display rows stay plain (Kobe in the Times Square `screen-view`).
- **Coinages:** KOSPI亲爹 = **"KOSPI Daddy"**; 打投 = "organized voting"; 男儿膝下有黄金 = "beneath a man's knees, there is gold" (title adds "(Physically)"); 梭哈 = "go all in".
- **Scene numbering:** throne-hall Yeongjo scold = scene fourteen (extend-by-one rule, after ch135's scene thirteen). Crew monitor reads ("Good." / "One more.") live in `ac-note`; everything else about the leave request stays prose.
- **Raw-date wrinkles are kept, not engineered:** Spotify's Nov 21 10 a.m. push sits after a same-evening arrival in the raw; the arrival scene simply carries no date so the raw's own sequence stands. Do not "fix" such wrinkles by re-dating scenes.
- **Gold/bitcoin artifacts:** a bank lobby rate board is a `screen-view`; the Coinbase risk modal + ticker is a `screen-view` (YES/NO as `sv-caption`); ledgers (personal or deal) are `finance-block`s. Lobby greetings are a `dialogue-block`. Physical farce (the Four Seasons rack battle) stays prose — block only the sounds (`sfx-line`) and speech.

## 24 · Awards-Night Chapters (ch145–146)

Applied to AMAs day — couture politics, the red carpet, and the ceremony itself:

- **A fitting scene is a `wardrobe-block` scene.** One block per wardrobe decision: the three single-brand looks (Gucci / Tom Ford / Balmain as `wd-item` label+effect rows), the final three-house mashup, the KING stage outfit. Children: `wd-header` (+ `wd-tag` chip: fitting one / decision / stage), `wd-item`>`wd-label`+`wd-effect`, `wd-note`. The stylist's inspection (pinch the shoulder line, check the collar) stays prose between blocks.
- **A live stage performance is `stage-block` grammar** (`st-header`, `st-scene` for camera/staging, `st-line` for sung lines — frozen canon lyrics verbatim — `st-note` for crowd/analysis). Chain long performances in parts ("the KING stage · part one — the throne" / "part two — the walk"). Celebrity cut-away reactions and whispered gags sit OUTSIDE the stage blocks as a `dialogue-block` ("in the seats · …"); the Korean live-stream barrages are `comment-thread`s with **romanized handles only** (Hangul jamo/syllables count as CJK leftovers — the QA regex and the house rule both reject them).
- **A spoken Instagram post is an `official-post`** (op-band "NAME · Instagram", op-handle, op-body = caption verbatim, op-meta describing the photo/video). Scooter's "My boy. My girl." post included. A house-PA announcement over the arena speakers is a `live-stage` (ls-line rows). A nominee reel on the big screen is a `screen-view` (sv-line per nominee with the joke embedded, sv-note for the field's weight).
- **Winning beats stay prose-first:** the envelope, the hem-lift, the IKEA-crystal trophy gag, both speeches, the Selena/pocket-square sequence, and the kiss chain are narration + dialogue-lines — never boxed. Blocks carry the surfaces around them, not the emotion inside them (§13 dramatic-take balance).
- **Cameo discipline this batch:** carded = Baek Si-on, Eun-ah, Scooter, Ariana Grande, Park Ji-hun, Justin (Bieber) — anchor every prose/dialogue mention, including announcer calls ("Baek Si-on!") inside dialogue-lines. Plain = Taylor, Big Sean, Selena, Pharrell, John Legend, Diana Ross, Sam Smith, Luke Hemmings, Dan/5SOS/Imagine Dragons, Adrien, Marc, Vincent. Inside display rows everything is plain (Sean's pitch name-drops Justin inside a dialogue-line, which anchors; the same name would stay plain inside an ls-/st-/sv- row).
- **Coinages:** "Boss Baek" (stylist's address), "Ji-hun oppa", "the golden knee", "traffic tool" (Scooter's compliment), "handing out payroll" (Ariana on compliments). "Yo! Shiwen!" — Big Sean's mangled pronunciation — stays verbatim.
- **Real-AMAs-2014 anchors held:** Nokia Theatre, Nov 23; Blank Space opener; New Artist + Favorite Pop/Rock Male both won; The Heart Wants What It Wants premiered live; first-ever Dick Clark Award for Excellence → Taylor Swift, presented by Diana Ross (three million-plus first-week albums); "Happy" 10-week run; "All of Me" weddings. The vote-split-withheld joke ("bad for the emotional stability of a nation") is the chapter's narrator voice — keep.

## 25 · Wardrobe-Block Images & the Aftermath Chapters (ch147–148, V17)

- **THE WARDROBE-IMAGE RULE (standing):** every `wardrobe-block` carries an AI-generated image matched to the block's own `wd-effect` description, generated WITH the character's book portrait as the image reference so the face matches the cast. Embed as `<p class="wd-photo"><img src="../images/wardrobe-<char>-<look>.jpg" alt="…"/></p>` plus a one-line `<p class="wd-sub">` summary, placed after the `wd-item`s and before the `wd-note` (ch75 Venice pattern). Register every image in the OPF manifest (`img-wardrobe-…`). Naming: `wardrobe-sion-couture.jpg`, `wardrobe-sion-king-amas.jpg`, `wardrobe-sion-gucci-velvet.jpg`, `wardrobe-jinri-saffron.jpg`, `wardrobe-jinri-winter.jpg`. VIEW the portrait before prompting (face/hair/build) and VIEW the output before embedding — a look-alike is a defect.
- **Chat media rows use the house ▸ prefix** (ch120 voice-message precedent): photos are `▸ Photo — …`, stickers are `▸ Sticker — …`. NEVER literal emoji in bubbles (📷🤍 flagged and removed); ✿ scene-breaks and ♪ mp-art are house canon and exempt.
- **Viewer-side scenes mirror the broadcast:** a character watching a live event replays the event's blocks in miniature — her reactions prose-first, with her own artifacts blocked (the saffron morning as `wardrobe-block`; the burn-account like-spree as `checklist-block`; incoming barbs as `comment-thread`s; a number written on an apple as `screen-view`; the reply photo as a `chat-container` with ▸ rows).
- **Manager-side strategy is a `screen-view` transcript** (the Boss call: demote/promote/tag — "Listeners don't empathize with kings. They empathize with stories."), with the motive monologue (the tree, the hand over the fence) kept as prose. A chart flood is a `trend-block` (rank + work + note) plus forum `comment-thread` and `news-digest` headlines; a group-chat leak inside a client meeting is its own `screen-view` pair (projector + chat).
- **Coinages:** "saffron steeps in water, not in vinegar"; "the Baek Si-on system"; "died with purpose" (the apple); "fire extinguisher" (IU's self-diagnosis); "Little Apple" rendered as a `music-player` card with the forbidden-fruit misread as dialogue.
- **New names:** Jung Han-teul (IU's manager — plain text; do NOT confuse with the carded director Park Chan-wook); Zhang Jie (AMAs International Artist — plain cameo, the a-cappella lesson stays prose).

## 26 · The Dawn Landing, the Chance Engine, and the Night-Rain Incursion (ch149–150, V18)

- **CHAT-NAME RULE (locked by user fix):** `chat-name self` marks the ACCOUNT OWNER (the header's name) and is followed ONLY by `chat-sent` bubbles. Any incoming/received row — including media rows (`▸ Photo`) — uses PLAIN `chat-name`. Audit bookwide: grep `chat-name self` → next bubble must be `chat-sent`.
- **Every direct-quote phone call is a `.phone-call` block.** One call = one block; narration, interiority and scene beats go INSIDE as `pc-note` rows (long pc-notes are house canon — ch92 runs 500-char notes); continuation of the same call never opens a fresh unlabeled block. Indirect/summarized calls (no quoted lines) may stay prose. pc-head format: "A → B · time · context"; `→` is whitelisted house ASCII-plus.
- **Brand names never carry character anchors** (Under Armour is not Baek Si-on); glossary-locked plain names (Taylor, Moon Geun-young, Jung Han-teul) must not be "helpfully" carded — two such slips were caught pre-build in ch149/150. The anchor-wrap pass must compare the PARSED class name, not the raw attribute string (a `class="dialogue-line"` paragraph was skipped by a `group(1)=='dialogue-line'` bug — always capture the inner group).
- **Watching-a-set scenes mirror the film-set toolkit:** warm-patch placement and other prep rituals are `checklist-block`s; the costume moment is a `wardrobe-block` (+ generated image, per the standing rule) with wd-labels like "The robe"/"The feet"; crew-room chatter after a take is a `dialogue-block`; poll results are a `trend-block` (rank + name + melee line) with the comment floor as its own `comment-thread`.
- **Coinages:** "The Apple Killer" (Scooter's Korean nickname); "one arrow, many birds — nobody told the arrowhead"; "a personal triumphal arch" + "The Baek Si-on Effect, Traffic Edition" (the Seoul Plaza refusal); "declining to charge is already our conscience speaking" (Bang PD); "Senior Baek Si-on has given us another chance!" (the drill chant); "the suffering will be load-bearing"; "the dynasty's first central heating" (heat patches); "I pulled it."; "Everyone an arrowhead. No mocking anyone."; "A modal particle." (Jin-ri's mm); the buffer-state hedge ("firepower, distributed"); "Guests first. Everything else is logistics."
- **New names:** Park So-dam (carded, Royal Noble Consort Moon — the lecture-recall scene, "Keep that."); Moon Geun-young (PLAIN — no card; take seven's kicked Crown Princess); Bang Si-hyuk (carded; the fee exchange); the No. 9 "Legend" live-cut sidebar stays a `news-digest` ("The brothers are simply standing on me.").

## 27 · Taylor Carded, the Shoujo-Manga Opening, and the Industry Ground Flat (ch151–152, V19)

- **THE TAYLOR RULE (user-directed):** recurring main-cast figures must be visible BOTH as inline hover previews in chapter text AND on the Character Intro page. When a previously plain figure accumulates real recurring weight (Taylor: 12 chapters, the AMAs arc), promote them: generate the era-correct portrait, verify it visually, add `ci-<id>` card (real-name-counterpart meta in playful house idiom) + `chr-<id>` modal to `character-intro.xhtml` keeping cards/modals parity (now 70/70), manifest the image, and anchor mentions in all NEW chapters. Backfilling old chapters is offered, never silently churned. rv-cards already exist (chr-irene/seulgi/wendy/joy — real names Bae Joo-hyun / Kang Seul-gi / Son Seung-wan / Park Soo-young).
- **雪莉 = Sulli = Choi Jin-ri's stage name.** POV sections of people who only know her publicly (juniors, gossip) use "Sulli(-sunbaenim)"; narration uses "Choi Jin-ri". Her off-screen good deeds (the food truck, the recommendation) land on other POVs as dramatic irony — never explained by narration.
- **Multi-portrait generation:** group shots take every member's book portrait as reference, in left-to-right order matching the portraits; generated Korean signage comes out garbled — run one cleanup pass ("remove ALL text/signage") and re-verify faces survived it.
- **ASCII discipline additions:** "↔" is NOT house (use "→"); "≈" is NOT house (write "roughly/about" in words); "₩" IS house (ch120 canon) for won amounts (₩1 billion, ₩4 billion, ₩120,000).
- **Wrap-pass trap:** in `re.sub(…, def repl(m)), m.group(1)` is None (not '') for bare `<p>` — compare `(m.group(1) or '')`. Symptom: only dialogue-lines get wrapped (counts barely move); the residual audit catches it.
- **In-person conversations are never `.phone-call` blocks** — the van debrief is dialogue-line prose. phone-call is for actual calls, one block per call, narration inside as pc-note.
- **Coinages:** "the queue behind you has shoes on"; "vote-rigging — fan mobilization"; "Proof the brothers were still here"; "the optimized-away margin case"; "Fate, as a substance, is remarkably impolite"; "the whale falls, and ten thousand things feed"; "moral hostage-taking" (KBS); "Their pain is not my department."; "I already beautified them."; "Taylor has you surrounded."; "Romance. Not one bit of it."
- **New names:** Kim Tae-su (SM PR staffer, plain); Kwon Ji-yong stays plain (house precedent, ch92); Jamsil Olympic Stadium / Hwaseong Haenggung / Apgujeong for venues; “Chu~?” in curly quotes.

## 28 · The Wrap Party, the Pitch, and Hong Kong (ch153–154, V20)

- **KNOWN TRAP (bit twice):** Jung Han-teul is glossary-plain — never card him (ch150 AND ch154 drafts both sprouted jeong-hanteuk anchors). Also: **same-name people never share cards** — "Park Ji-eun" (the Producer writer) is NOT Lee Ji-eun (IU); the short-form wrap pattern ("Ji-eun") must not fire after "Park ". Two shipped ch121 anchors were unwrapped in V20. When auditing, grep `Park <a` bookwide.
- **User-directed chat style (ch152 precedent):** when a KakaoTalk exchange is the SCENE (not a cutaway), render it as a full `chat-container` continuing to the scene's exit line, and delete any prose paragraphs that duplicate the same lines. Owner = header name; the account owner's own name labels self rows.
- **News digests must vary their outlets** — never repeat one source across headlines in the same block (Billboard / Rolling Stone / Pitchfork / Variety pattern).
- **Canon anchors for the film arc:** the indie film is `<em>Green Bottle Fly</em>` (full) / "Green Fly" (short); Showbox = distributor; Baek Jeong-hun = uncle-director (carded); Yoon Hye-ja = Si-on's MOTHER (carded) — she financed Green Bottle Fly; Jung Jae-joon = producer (carded, did the original "Way Back Home" arrangement). Swearing spellings: "Ssi-bal"/"ssi-bal"/"Ssibal" (house).
- **In-person flirtation scenes get the wardrobe-block treatment even when "nothing happens"** — the incognito uniform IS the outfit of the scene (cap/flannel/earbud). Group-party looks (cream knit + jeans) likewise. Generated background signage: garbled text = redo; authentic foreign signage (HK neon in Chinese) = keep.
- **Coinages:** "Ten-Million Heroine/Leading Man/Lady"; "violence changing into a suit"; "a film is not a statement"; "That was education."; "the execution order for a movie"; "incognito the way lighthouses are"; "national-level classified material" (the room key); "filing paperwork against a hurricane" (Eun-ah); "the door had swung shut… everyone inside had seen what was outside."
- **New names:** Kim Tae-su was ch151; here: Lee Jong-won (IU's producer-teacher, plain), the Showbox distribution director (plain), Kim Tae-su-style staffers stay plain.

## §29 — MAMA-ceremony chapters (ch155–156, V21): stage names for groups, the CJ call tree, phone-call discipline

- **T-ara convention:** first appearance in ch155 — use the six STAGE names (Qri leader / Eunjung / Hyomin / Jiyeon / Boram / Soyeon), all plain, no cards; "the troll incident" stays vague per raw (departed member + tearful selfies), no real-name deep-dive. In-verse rapper 麻龙 = "Ma-ryong" (plain).
- **CJ/MAMA exec set (all plain, no cards):** Lee Myung-han (tvN president, ex-KBS <em>2 Days &amp; 1 Night</em>, 2011, "two SSR-tier cards" = Na Young-seok + Shin Won-ho), Shin Hyung-kwan (Mnet chief, CJ since '94, MKMF→MAMA), Lee Seon-ho (chairman's eldest son, sugar-division "assistant manager," father inside / aunt in the US). Nominees plain: Sunmi / HyunA / Ailee / Hyorin / Taeyang.
- **House song titles:** IU 'Meet Me on Friday' (full) / 'Friday' (list form), 'Sogyeokdong', 'Fly, Little Chick' (literal for 飞翔吧小鸡); 'Overdose', 'Touch My Body', 'Eyes, Nose, Lips'. "분猪肉" = "meat-sharing exercise" (ch152 coinage, reused).
- **Envelope-swap rendering (ch156):** "in plain black on white card stock, the card said: *HyunA.*" → announcement "—IU! Congratulations!" — keep both halves verbatim-adjacent; the professional director's cut to Si-on during the flap-open is the comedy beat.
- **.phone-call discipline held:** one block per call (Myung-han→Shin; Shin receiving Lee Seon-ho); pc-me/pc-them/pc-note rows; NO anchors inside pc rows; hang-up goes INSIDE the block ("Dud. The line went dead in his ear.").
- **In-person whisper/banter scenes stay dialogue-line prose** even when block-heavy would be tempting (Cindy coaching, joint interview) — display blocks reserved for the T-ara peanut-gallery huddles (`dialogue-block` with dl-header) and livestream reaction (`comment-thread`).
- **New coinages:** "front-line melon-patch sentries"; "settling the bill for the best spectator seats in the building"; "whether that was an accident, or careful"; "the King of Heaven's son. Different concept."; "Being judged seriously — that's the rarer thing."; "not-a-seating-issue into a-problem-we-are-solving-immediately."
- **Transcription discipline:** my ch155 archive had THREE slips vs the user message (分猪肉→"pork"; doubled 很快; collapsed 收视率 sentence) — diff raws against the message before drafting, every batch.

## §30 — the split-capture trap, the hole-audit battery, sv-line semantics, ch157–158 canon

- **FATAL TRAP (bit V21, shipped with 8 name-holes):** `re.split(r'<a class="chr-inline".*?</a>', body)` WITHOUT a capturing group DISCARDS the matches — pre-anchored names vanish tag-and-text. ALWAYS `re.split(r'(<a class="chr-inline".*?</a>)', body)` and treat odd indices as protected anchors. V18–V20 fine (group present); reimplementations must copy the group. Detect holes with the NEW standing battery, run before every build: (1) text-node `  ` double-space scan; (2) `<p…> [a-z]` leading-space scan; (3) `[a-z] , ` orphan-comma; (4) `[a-z] [?.,!;:]` space-before-punctuation (whitelist: curly-quote constructs, "Mr./No./vs." precede periods); (5) dangling-close-word paragraph-end scan (to/with/asked/said/and…</p>). Residual-audit alone CANNOT catch deletions — deleted names leave nothing to count.
- **sv-line semantics locked:** sv-line = ON-SCREEN TEXT (spoken lines on a screen, comments, barrages) — styled since V22 as a gold-bar broadcast chip (border-left #d4af37, gold→periwinkle gradient chip, gold glow, #f6ecc9). Never use sv-line for ordinary dialogue; that's what made it "look like normal dialogue" (user's own diagnosis). screen-view caption row = sv-caption; atmosphere rows = sv-note.
- **Hara/Jin-ri video calls = ONE .phone-call block per call** (pc-me = caller Jin-ri, pc-them = Hara), interior monologue folded into pc-note rows — same discipline as voice calls. KakaoTalk threads that ARE the scene = chat-container with owner's perspective: on Si-on's phone his rows are chat-name self + chat-sent, hers plain chat-name + chat-received.
- **ch157–158 canon:** the hug ("notice WAS given: I told you to stand up"; "Cindy doesn't need a reason."; the boomerang completes its arc); Jin-ri = saffron water + "kindness that doesn't have to step backward"; Hara's peach→kimchi law of sourness; 2012 chair-giving remembered ("Good things should be remembered." / "Scared, and did it anyway."); peace-offering geomungo video ("Crown Prince Sado's daily curriculum"); hot-search swap (OUT fan war / IN Taeyang follow); film title house form is <em>Sado</em> (NOT "The Throne"); "Silver Crown Crown Prince" (银冠世子, ch141 phrase reused); Jamsil finale: sixty thousand cushions, the coat as windbreak, "The wind picked up." — wind unchanged, coat gathered closer.
- **T-ara stays stage-name plain** (Soyeon's silent camera-check beat in ch157 — note-only dialogue-block with one whispered line is legal); Jung Han-teul plain (two-trophy temp-worker gag); Master Zhao plain (ch150 precedent); Taeyang/GD/Yeongjo/Selena/Sam Smith plain.
- **"？" implementation:** house ships ASCII "?" (fw ？ count 0 in ch155/156/157/158) — convert the raw's ？ to ASCII in EN dialogue.
- **New coinages:** "international public property"; "jealousy with no standing"; "slicing your heart open to go with somebody's drink"; "Before the peach got pickled"; "kind sunbaes will also engineer your manager out of the way"; "Sweet nothing."; "The wind did not, at any point, pick up. The coat did."; "Nothing ends a fan war faster than your own idol strolling in carrying the fire extinguisher."

## §31 — ch159–160 canon: the cat, the coat, the audit, Scooter discipline

- **ch159–160 canon anchors:** the elevator return ("You don't even own a cat." / "So first I need to go buy a cat." — door-close pressed twice, second heavier); Jin-ri's borrowed coat night (Master Zhao raises the cabin two degrees; 25 degrees "not cold"); the pink fine-knit threshold reveal (split warm/cold lighting); IU's mother = "her mother" (NO "U-Mom" in EN prose; raw U妈 converted, 26 tokens); the aunt = "the aunt" (小姨); restaurant <em>Good Days</em>, wall sign "A Delicious Day", Chungjeong-ro; cushion deal: ₩3,000 (NOT the 2,000 she offered) — "Kindness can be priced in as a discount. It can't be priced in as a loss."; first batch day 5, complete day 10; Scooter call: 'Legend' #2 / 'Love Yourself' #22 / 'Uptown Funk' #3, fly on the 20th Seoul time (concert on the 18th, the 19th = "hours of being an ordinary person").
- **Scooter Braun is CARDED** (chr-scooter-braun); bare "Scooter" wrapped in narration (ch102 precedent); pc rows NEVER anchored. Chart talk always: song titles curly-quoted, positions "number two/#22" house-mixed as shipped.
- **Checker-tool discipline (V23 lesson):** an in-zip text audit that strips TAGS but not the full `<a>…</a>` element will report anchor text as "bare" — false positive. Strip `<a …>…</a>` blocks whole. Also: pc/them/me rows carry NO curly quotes by design — never write checker strings that expect them.
- **Sound-effect block reuse:** construction/rhythm sounds ("Clang." ×3, "Ah-choo.") use `<p class="sound-effect">` (ch58 precedent) — standalone paragraphs, period included.
- **Site-rule canon:** live-event field manual rule one — "what you shouldn't have seen, you didn't see" (venue manager, ch159); drivers' canon: "reading the room" beats driving skill (Master Zhao).
- **New coinages:** "Kindness can be priced in as a discount. It can't be priced in as a loss."; "the world's warmest conversational hand grenade, held at chest height, pin attached"; "dismantle romance into physics"; "what you shouldn't have seen, you didn't see"; "From philosophy back to waitstaff, no appeals accepted."; "a feeding operation"; "written for somebody else's road home… walked its own writer to her family's front door"; "Technology also gets off work."

## §32 — wrap-nesting rule, fragment audit, card-id canon, ch161–162 canon, ENGLISH-ONLY process

- **USER RULE (standing):** all process narration, explanations, and checker output shown to the user must be ENGLISH ONLY. Chinese never appears in visible commentary (raws/archives excepted).
- **NESTED-ANCHOR RULE:** never run full-name and short-form wrap patterns as sequential passes over the same segment — the short form nests inside the fresh full-name anchor (`<a>Bae <a>Joo-hyun</a></a>`), which epubcheck may pass silently but is invalid XHTML. Use ONE pass with a combined alternation regex, FULL NAMES listed before their substrings (Bae Joo-hyun before Joo-hyun; Kang Seul-gi before Seul-gi; Son Seung-wan before Seung-wan; Park Soo-young before Soo-young). Standing audit: `grep -c '</a></a>'` bookwide must be 0.
- **FRAGMENT AUDIT (standing, post-wrap):** every `character-intro.xhtml#chr-*` href used in chapters must exist as `id="chr-*"` in character-intro.xhtml. RSC-012 "Fragment identifier is not defined" at epubcheck = this audit missed. Current canon: RV four = chr-irene / chr-seulgi / chr-wendy / chr-joy (NOT chr-bae-joohyun / chr-kang-seulgi / chr-son-seungwan / chr-park-sooyoung). chr-taylor defined, not yet used (accepted).
- **NOT CARDED (memory corrections):** Choi Min-sik is PLAIN (no card, no portrait — "carded" note in old memory was wrong; verify against character-intro.xhtml definitions, never memory). Yeon Sang-ho (연상호, director of 'Train to Busan', ex-animation) PLAIN. Gong Yoo, Lee Soo-man, Jeon Do-yeon, Son Ye-jin, Kim Hye-soo PLAIN.
- **"-sunbaenim" vocatives stay plain** ("Baek Si-on-sunbaenim", "Gong Yoo-sunbaenim" — ch151 shipped precedent with "Sulli-sunbaenim"); the wrap lookahead `(?![\w-])` handles this automatically. Vocative "-ah/-yah" endings likewise stay plain.
- **Scooter speech:** he says **"Baek"** (surname 白), never "Bae" (V24 corrected 2 tokens in ch160).
- **ch161–162 canon:** Blue Dragon 35th — 'Green Bottle Fly' ×4 nominations (Choi Jin-ri's nod = the industry's "signal"); Song Kang-ho = 'The Attorney' rival AND screen father Yeongjo ("Go sing, Crown Prince." / "For today, you are permitted to leave the palace."); Baek Si-on invests in 'Train to Busan' to shield Jin-ri's market risk ("Because she wants to be an actress."); SK Telecom renewal ₩4B/2yrs (Seo Eun-ju redlines); SK duty-free license pulled → Hyundai; the "teacher" shadow → Baek Jeong-hun's new-film concept gaining real soil; Sado wrap Dec 13, five days to the concert; Irene's 7cm heels (tiptoe/group-photo backstory vs Baek Eun-ah), the sack carry → princess carry ("Mom and Dad call me that."), 70% big-screen exposure decision, Asan via the Hyundai Chung family, dorm tribunal ("It's not scene-stealing. It's an entrance." / "We're Red Velvet.").
- **New coinages:** "not one milliliter of shoujo manga"; "If you get a seat at the table, you eat first. Argue later."; "directors keep three-tenths in reserve"; "her fate as a sack"; "the blackmail archive was already shipping in bulk"; "Moving. And also extremely literal."; "seven centimeters of stubbornness"; "It's not scene-stealing. It's an entrance."

## §33 — V25 rules (ch163–164): em-vs-curly split, two-phase short-name wrap, image text-ban, audits closed

**Film-title typography split (RESOLVED via ch161 precedent):** <em> in PROSE narration (plain <p>); curly singles in DISPLAY rows (dl-line/dl-note/sv-*/pc-*/wd-*). Song titles always curly singles everywhere. 'Han Gong-ju' in a presenter dl-line = curly (spoken); in prose it would be <em>. Apply the same check when converting raws: any ‘Title’ surviving in a classless <p> = hole.

**Two-phase wrap (nesting-proof):** phase 1 wrap full names on free text (A.split on anchor regex, skip odd); phase 2 RE-SPLIT and wrap short forms only on anchor-free segments. Substring shorts (Eun-ah ⊂ Baek Eun-ah) are safe only because anchors are excluded between phases. Lookarounds (?<![\w-])…(?![\w-]) keep "Si-on-oppa" (vocative, NEVER anchored — shipped grep: 0 anchored) and possessives behaving. Shorts used V25: Si-on, Eun-ah (both have 1000+/500+ anchored precedent).

**Wardrobe-image generation discipline:** feed character portrait as reference; ALWAYS demand blank banners/signage in stadium/venue prompts (v1 trophy image shipped garbled Korean + a wrong-year "2023" → one regen with "ALL banners, signs and surfaces COMPLETELY BLANK — no text, no letters, no numbers, no year"). Visually verify EVERY output before embedding; check face vs portrait, garment vs wd-block text, and text-free backgrounds.

**Opf-registered image set must equal chapter-referenced set + {cover.jpg(opf properties), cover-art/cover-bg.jpg(CSS), taylor-swift.jpg(chr-taylor card)} — scan artifacts verified, not holes.** New wardrobe images: register in opf AND embed; an unreferenced <item> passes epubcheck silently (V25 first build caught this on the trophy image — added ch163 wb#2 at the Jamsil walk-in).

**Audit battery standing (all ran clean on V25):** fragments used⊆defined bookwide; `Park <a` bookwide = 0 (surname-split collision trap CLOSED — no same-name "Park X" ever split across an anchor); wd-tag/wd-header/wd-photo/wd-sub all present in stylesheet.css (V24 worry resolved); chat-name self → no received rows; fw ？ = 0; </a></a> = 0; straight quotes in text content = 0 (count AFTER stripping tags — markup quotes are not holes); CJK glyph scan = 0.

**V25 canon:** Blue Dragon Dec 17 (Jeong-hun Best Director, Chun Woo-hee upset, Si-on Best Actor accepted by Jin-ri "half of this award is hers", <em>The Attorney</em> Daesang); concert Dec 18 Jamsil 60k free tvN (Min-jun vlogger POV plain, Hye-ja seatmate "You already look the part", 'Legend' door-sync opening, "BAEK SI-ON!!!" chant cliffhang); Jin-ri owns 2 down coats worth of Si-on's Under Armour logistics; "eat at the table" callback ch161→ch163 landed verbatim.

## §34 — V26 rules (ch165–166): hand-typed anchors caught pre-build, cameo-plain rule, dialogue-wrap scope

**HAND-TYPED ANCHORS = BANNED (near-miss logged):** ch165 shipped draft contained hand-typed chr-taeyang/taeyeon/tiffany anchors (undefined ids + nonexistent images — the exact V24 RSC-012 class), caught this time by running the fragment audit BEFORE building. Standing: draft prose with plain names ONLY; wrap exclusively via script; run used⊆defined + image-exists audit immediately after wrap, before opf/nav work.

**Cameo-plain rule:** big-name celebs appearing as audience/cameo shots (Taeyang, Taeyeon, Tiffany, Girl's Day members, Kim Hee-ae, Chun Woo-hee, Song Kang-ho, Bae Suzy, HyunA) stay PLAIN — no card, no anchor — unless they become recurring mains (Yoo In-na precedent: carded because recurring since ch113). Shipped counts prove precedent: Taeyang 13× plain, Taeyeon 1× plain.

**Wrap scope = classless <p> + dialogue-line ONLY.** Everything else (dl-line/dl-note/sv-*/pc-*/wd-*/ls-*/pf-*/beat/lyric/action-beat/comment-*/chat-*/lb-header/lyric-line) stays anchor-free — display-row audit must include ALL these row classes. Lyric text may quote names ("IU" in comments, "Sulli-sunbaenim" on stage) — always plain.

**Suffix-blocking confirmed:** "Baek Si-on-ssi" / "-sunbaenim" / "Si-on-oppa" / "Irene-yah" are NEVER anchored (lookahead (?![\w-]) blocks at the hyphen; 0 anchored instances shipped). Plain by design — do not "fix".

**Deep-scan-before-drafting payoff:** 14 greps locked RV real-name canon (Bae Joo-hyun/Kang Seul-gi/Son Seung-wan/Park Soo-young full + shorts), IU forms (Lee Ji-eun/Ji-eun anchored; bare IU NEVER), 'Friday'-SOTY and Venice "Oh pretty baby" callbacks, lyric-line canon ("Bang bang!"/"until we become legends"), Mom/Auntie/eonni/unnie usage, phone-call pc-head "A → B" format, performance-block children (pf-header/action-beat/beat/lyric), pullquote/sfx/scene-break availability — all consumed directly into the draft.

**V26 canon:** concert setlist order (Legend → Sign of the Times → audience-cam → Human → RV Chu~?+Happiness → Bones → Way Down We Go → King → BTS Danger+2 → Way Back Home → Love Yourself → IU WBH reply + Friday → cherry-blossom duet → Can't Take My Eyes Off You → speeches → bow); KBS fixed-MC offer for Irene pending ("don't answer yet"); thank-you dinner scheduled (IU + Jin-ri seat claims, Irene toast owed); WBH lyrics officially by IU; cushion + light stick keepsakes; Hye-ja's pharmacy-receipt hug; Eun-ah's banned thought.

## §35 — V27 rules (ch167–168): the Park <a audit FIRES for real, BTS split canon, display-row audit scope

**`Park <a` AUDIT PROVEN LIVE:** post-wrap in-zip scan caught the short-form "Ji-eun" wrap splitting "Park Ji-eun" (screenwriter) into "Park <a>Ji-eun</a>" ×2 — repaired by targeted replace, rebuilt. Standing order unchanged: run `Park <a` bookwide AFTER wrap on EVERY build; any hit = same-name collision — resolve by restoring the plain full name for the PLAIN person (never by de-anchoring the carded one globally).

**BTS anchoring canon (5 of 7):** anchor Kim Nam-joon(+Nam-joon), Jeon Jung-kook(+Jung-kook), Park Ji-min(+Ji-min), Kim Tae-hyung(+Tae-hyung), Kim Seok-jin(+Seok-jin) — cards chr-kim-namjoon/jeon-jungkook/park-jimin/kim-taehyung/kim-seokjin. Min Yoon-gi and Jung Ho-seok have NO cards → always PLAIN (shipped: Yoon-gi 12×, Ho-seok 18×, Suga 6×). Never "fix" them into anchors.

**Plain-name canon extended:** Jung Han-teul (IU's manager; glossary-plain ×16+), Park Ji-eun (screenwriter, plain ×20+), <em>Producer</em> (recent form; ch121/122 used <em>The Producers</em>), Cindy plain, Taylor plain (100×), AMAs plain, Kim Min-jun plain, Yeon Sang-ho plain, Peach (nickname, dialogue only — narration uses full anchored name).

**Wet-wipe canon (ch148 + ch168):** he carried wet wipes after the Taylor AMAs right-cheek incident (wiped + photographed it); ch168 "Didn't bring one today." = the deliberate not-wipe. Treat as a running relationship ledger — never contradict.

**Display-row anchor audit scope (full list):** nd-source/nd-headline/sv-*/dl-*/pc-*/chat-*/comment-*/wd-*/pf-header/ls-*/lyric/beat/action-beat/lb-header/nv-row/nv-term — ALL must be anchor-free; hashtags render as plain text inside nv-term (no # glyph needed in English rendering; plain words).

**Chat POV convention:** scene owner = chat-name self (chat-sent only, per standing rule); the other party = plain chat-name + chat-received. ch168: self=Choi Jin-ri, received=Baek Si-on.

**V27 canon:** thank-you dinner at hanwoo grill house ( PRIVATE EVENT sign ); Yeon Sang-ho disaster-film audition pending; BTS table comedy (Ladies first / Kimchi advertisement); RV toast routing (Sulli→broadcast→medical, soft drinks only); "Screenwriter Park Ji-eun" leverage war; IU's fall intercepted — peach/thorns verdict; vlog retitle "Baek Si-on spent the money on our butts" (2M+ views); YG adds hot-drink zone, cushion quote pending; UA/LG/SK brand-shapes sequence; smart-toilet endorsements declined; Sphynx named Blin (Goblin origin); Si-on flies to the US that night; Christmas kiss on the LEFT cheek, unwiped; cat + coat waiting in Chengbei.

## §36 — V28 rules (ch169–170): card-id canon corrections, plain-POV rule, honorific canon

**CARD-ID CANON CORRECTED:** Taylor's card is **chr-taylor** (image taylor-swift.jpg) — NOT chr-taylor-swift. Every historical "chr-taylor unused" audit note refers to this card. ALWAYS grep the exact id from character-intro.xhtml before writing it into a wrap config; NEVER infer from the image filename. (V28 caught 14 mis-pointed anchors pre-ship this way.)

**Plain-POV rule (extended):** chapter POV characters WITHOUT cards stay fully plain regardless of prominence — Kim Min-jun (ch164), Lee Sang-hyeok/Faker (ch170; ch118 name-drop also plain), Jung Han-teul, Park Ji-eun, Ryan Seacrest, Yoo Jae-suk, Rain, PSY, Selena, Yeon Sang-ho. NEVER hand-type an anchor for them in drafts (V28 caught chr-faker — undefined id + missing image). Card creation remains a deliberate, user-visible step (portrait + intro edit), not a wrap-time decision.

**Carded-figure wrap config (current exact ids):** chr-taylor (Taylor), chr-scooter-braun (Scooter Braun + Scooter), chr-adam-levine (Adam Levine + Adam), chr-justin-bieber (Justin Bieber + Justin), chr-hwang-sooah (Hwang Soo-ah, full only), chr-park-jihun (Park Ji-hun), chr-faker DOES NOT EXIST.

**Honorific canon (ENFORCED):** Korean sunbae/sunbaenim ONLY — Japanese "senpai" is banned (grep = 0 standing). Direct address = sunbaenim ("Hello, sunbaenim!", "IU-sunbaenim"); reference = sunbae. Vocatives plain: Oppa, Eonni/Unnie, Mom, Auntie, Cousin, Sulli-sunbaenim, Baek Si-on-ssi/-sunbaenim, "Irene" name-calls in dialogue plain (matches ch165 "stay on Irene").

**Block forms debuted V28:** interview-block (iv-kicker "OUTLET · context" / iv-q question / iv-a answer — Q&A as two rows, no anchors); sfx for UI/UX sounds ("Ding." match-found); sv-block for game-client messages, chat tiles, YouTube tiles, memo lines. MV-description passages stay prose with lb-block only for actual sung lines.

**V28 canon:** LA trip (KIIS FM/Ryan Seacrest "cushions are normal" headline, <em>Time</em> export feature 3 reporters/2 weeks, apple-number history ch147 confirmed eaten, Taylor cat summit + litter-box doctrine, Scooter's Selena→Justin chain and "for you, not for Justin", Eun-ah memo "Reason: Scooter's anxiety", Adam Levine Sugar belt saga + "Seven Wolves = a symbol of patriarchal authority", test show + NA tour seeded); 'Love Yourself' MV live (ceiling-fan transition, kiss scene), Faker −3 LP stream incident ("client lagged" / "face too handsome"), Ji-eun's aggressive-acting reviews → Cindy confidence, Jin-ri's "winning by a little", Irene's low heels + Music Bank + NO PHONE ( comedy engine for V29+), Christmas approaching.

## §37 — Phone-call block rule (user-enforced, bookwide): one call = one .phone-call block

**Rule (absolute):** every genuine two-party phone call renders as ONE `.phone-call` block — never prose `dialogue-line`s. V28's ch169 Adam Levine call shipped as prose → user correction → fixed + bookwide deep-scan; ch156's return call (sugar-division heir) retrofitted in the same pass. **Bookwide now 63 blocks.**

**Structure:** `<div class="phone-call">` wrapping:
- **pc-head** (anchor-free, display row): `Receiver ← Caller · location/context · incoming` or `Sender → Receiver · time · context · outgoing` — matches shipped forms ("Baek Si-on ← Scooter Braun · the hotel, Jeonju · incoming"; "Baek Eun-ah → Bang Si-hyuk · 3:12 p.m. · picked up on ring two").
- **pc-them / pc-me** dialogue rows: **quote-free** (ch149+ house style; 615 legacy curly-quote rows predate the convention — do NOT bulk-convert older chapters). Internal curly singles inside a row are legitimate (ch121/157/160).
- **pc-note** narration rows: verbatim narration; curly doubles + `<em>` allowed inside pc-note (77 and 6 shipped precedents).
- **NO chr- anchors in ANY pc row** (pc-head/them/me/note) — 0 bookwide; names inside rows stay plain.
- Scene frame stays prose outside the block: ring/answer setup ("the nightstand rang", anchored "Caller ID: X."), and post-call meditation after hang-up.

**Scan method that caught ch156:** grep call signals (`phone rang`, `Caller ID`, `picked up`, `receiver`) × per-chapter phone-call counts; then READ each suspect — hybrid scenes where quoted dialogue is NOT call audio (receiver-covered relay: ch152 "Cousin." = in-car relay, caller never speaks) stay prose. Anchor text inside would-be pc rows must use the SHORT speaker form check when splicing (ch169's final beat was `Adam</a>` short-form, not `Adam Levine</a>` — rfind the actual bytes, never assume full name).

## §38 — V29 rules (ch171–172): product cards via album-card, the finance snapshot, split-call with mid-call consultation, the same-date two-morning stamp

**Uncarded products get the album-card grammar.** A physical product a scene hands to the protagonist (Kobe's BodyArmor bottle) is an `.album-card`: `al-header` ("the bottle · handed over with expectations attached"), `al-cover` + generated image, `al-title` = brand name, `al-line` = the spec speech compressed, `al-release` = the hook ("A brand Baek Si-on has never heard of — yet."). Image is text-free per §33 and scene-matched (backyard table, hoop bokeh, palms). One card per product reveal; later mentions stay prose.

**A live two-option decision may take ONE `.finance-block` snapshot** ("the choice, as the manager's blood pressure saw it") — exactly `fb-header` + `fb-row`(`fb-label`+`fb-value`), no `fb-note` (§22). It sits AFTER the prose arithmetic, as the distilled snapshot; never replace the prose reasoning with the block.

**The raw's cute anonymity is kept:** 杭州马 = "the man from Hangzhou" — never "Jack Ma", never "Alibaba's founder" named. 麻辣鸡 = Nicki Minaj (plain cameo). Steph = "Steph" (plain).

**Chapters set in two cities on the same calendar date get the two-morning stamp:** ls-date "December 22 · one Monday, two mornings" — KST morning and PST morning are the same date, 17 hours apart; verify MV-clock arithmetic (drop → +14h Seoul morning → +30h LA morning) against ONE clean reading and smooth the raw's timezone wobble into narration ("the recipient is dead to the world"), never into a false timestamp (§22 smoothing; §23 no re-dating).

**A call interrupted by an in-person consultation splits into chained phone-call blocks around the bridge prose** (§21 pattern): block one ends at the demand, prose carries the mic-cover + schedule math + the manager's verdict, block two resumes "· the same call, continued" with the answer. The hamburger callback ("don't bring three hamburgers into my house") lands in block two with its pc-note beat ("Baek Si-on looked down at the hamburger in his own hand.").

**Kobe-family canon:** Kobe/Kobe Bryant anchored (chr-kobe-bryant, "Kobe" bare form dominant); Vanessa, Natalia, Gi-Gi stay PLAIN (no cards — card creation is a deliberate user-visible step, §36); Gi-Gi's 'Legend' hum is a `lyric-block` ("Bang bang, bang bang—" canon hook, "as hummed courtside"); the steak race, the fist bump, and the farewell stay prose-first (§24) — blocks carry only the lyric, the bottle, and the deal snapshot.

**Headline-flood chapters are block-parades:** counter refresh = `screen-view`; portal #1 = `naver-search` (fill rank terms + one `nv-note` timing gag from canon when the raw gives only "reached #1 in five minutes"); the push-alert list = `news-digest` with six real varied outlets (Naver/Daum/OSEN/Sports Seoul/Ilgan Sports/TV Report) and 《……》 rendered as a closing prose line ("The list went on."); checkout-TV broadcast = `live-stage`; the 99+ notification wall = one `chat-container` (three received bubbles under a single system name row + `chat-meta`); comment before/after = twin `comment-thread`s with the foreign languages DESCRIBED in English, never rendered non-Latin.

**In-verse clock:** ch171–172 = Monday, December 22, 2014 (Seoul morning 7:00–9:00; LA pre-dawn message-viewing → 8 a.m. Escalade → noon Newport Coast, forty minutes). Christmas is three days away (ch170 was Dec 21). 'Love Yourself' MV dropped ≈ Dec 21, 6 p.m. KST; 14h ≈ 17M (Seoul morning), 30h ≈ 30M (LA morning), KBS 8 a.m. = 18M.

## §39 — V30 rules (ch173–174): real-song freeze discipline, the flat-lay wardrobe image, the one-sided ring-off, and prose-first contract drama

**A real-world future song may be "discovered" in-verse — freeze it at discovery.** 'See You Again' enters the book via Wiz's demo (music-player, two lines: "It's been a long day without you, my friend—" / "And I'll tell you all about it when I see you again—"). Those two lines are now frozen canon; any later performance/chapter reuses them verbatim. The raw's narrative translation of a lyric ("老朋友，没有你的日子太漫长") renders as the same English line in narration — never as a second variant.

**Wardrobe images for UNCARDED people are faceless flat-lays.** The §25 rule (generate with the character's portrait as reference) applies only to cast with book portraits. Charlie Puth is PLAIN with no portrait: generate a product/still-life shot instead (three tagged garments + gift bag + peeling wall + rent envelope — the scene's thesis in objects). NEVER fabricate a face for an uncarded person; card-creation remains a deliberate user-visible step (§36). The same image file may serve an `al-cover` and a `wd-photo` role — one manifest entry, referenced twice, is fine.

**A call whose audio never reaches the POV renders ONE one-sided block** (§20: block only when the line actually speaks — to this POV). Scooter's 30-second ring-off at LAX: pc-head "Scooter Braun ← Justin's side · LAX · incoming", pc-me rows only (his half: "Mm." / "…You're kidding." / "Fine. Don't let him near any statements. I'm on my way."), pc-notes carry the face journey (normal → resigned → palm-over-forehead). Do NOT invent the caller's audio; do NOT split into two blocks for drama. Bookwide count after V30: 66.

**Contract/negotiation reveals stay prose when the raw plays them as spoken beats** (§24): the $50,000 → $500,000 gap lands as dialogue with a written "…?" and a "I didn't catch that." — a finance-block would defuse the reveal. Finance-blocks distill a choice the manager is already sweating (§38), not punchlines. The contract-splitting doctrine ("The song: bought. The person: discussed separately.") is the chapter's thesis — prose.

**K-pop-to-Hollywood favor-chain narration:** the belt callback compounds ("a father-in-law's belt will, eventually, lash a Billboard chart-topper into existence?") — log every quid-pro-quo chain in the worklog (Adam MV concept → Adam recommends → Wiz asks → 'See You Again' lands; the BodyArmor bottle rides along as ad duties). Chapter titles from raw irony keep their full clunk ("The Highest-Value Steal in History").

**Transliteration batch canon (V30):** Wiz Khalifa, Charlie Puth, Kendall ("Ken-doll's half-sister — the one the tabloids called Kendall"), Hailey, Selena, Dispatch's Director Lim (林局长), Bodyguard Kang / Bodyguard Han (plain, ch120 precedent), "a goddess of clay had swept an eraser across it" (女娲橡皮擦 — keep the mythic image, never name Nuwa for Western POV). "???" = bare-ASCII dialogue-line (ch128 precedent). ▸ media rows: "▸ Photo — …" / "▸ Sticker — one enormous thumbs-up" (ch148 precedent; NO emoji).

**The Christmas chat scene is a five-container stack** (mom / Jin-ri mega-thread / replies / IU photo / IU reply) under a MID-CHAPTER mini location-stamp — multi-stamp chapters are standard (119 shipped, up to 9). Chat POV: his sends = `chat-name self`; the women's = plain `chat-name` + `chat-received`. Meta lines do the deadpan work ("strategically omitted: hamburgers, sports drinks, and a protein bar eaten in an arena tunnel").

**In-verse clock:** ch173 = Christmas Day (LA morning taping → LAX noon → Chicago afternoon rehearsal → 6:30 p.m. CST opening → immediate return flight). ch174 = same night (West Coast 7:30 p.m. doorbell → ~midnight landing → 12:30 a.m. Four Seasons meeting, twenty minutes budgeted, ten gone at the tears). Seoul-side chat timestamps = Dec 26 afternoon (second Christmas afternoon). Lakers–Bulls Christmas 2014: the raw schedules it, Kobe sits (in-verse body management), United Center hosts.

## §40 — V31 rules (ch175–176): card-parity retrofit, the identifying-feature portrait, cross-ocean call headers, and the other-timeline fact frame

**New recurring cast = page card + modal + ONE in-text card at the TRUE physical debut (§20), then retro-wrap every mention.** When a card is created mid-book, the work is four moves: (1) index card `ci-*` + (2) hover modal `chr-*` appended to character-intro.xhtml, (3) one in-text `.char-intro` at the first PHYSICAL appearance — which may be an EARLIER chapter than the current batch (Kim Jae-wook's card lives in ch171, his newsroom POV scene, not ch176 where the user noticed the gap; Charlie's lives in ch174's "Right man." beat, NOT ch173 where he is only a name and a demo), (4) extend the wrap FORMS (full + short + bare-surname forms: "Charlie Puth"/"Charlie"/"Puth") and re-run the script over ALL affected chapters — retro-anchor counts are expected to be large (ch174 +53). Audit the audit: the wrapper's FORMS list itself must contain every carded person (Lee Joon-ik was caught missing mid-pass).

**Portraits for real people must carry their canonical identifying feature.** Charlie Puth = the broken eyebrow — v1 portrait lacked it and was REGENERATED until the gap was clearly visible; the book text references the feature twice, so a look-alike without it is a defect (§25 "VIEW the output"). Wiz Khalifa: dreads up, shades on forehead, gold chains, courtside.

**Cross-ocean calls:** pc-head may bridge locations with `↔` ("Baek Si-on ← Lee Joon-ik · Los Angeles ↔ Suwon Film Studio · incoming") when the scene cuts between both ends. Party sounds/music/glass-clinks are pc-note texture; the far-end caller keeps pc-them.

**§37 refinement:** curly DOUBLES inside pc-me/pc-them rows are NOT allowed (pc-note only, 77 precedents); internal curly SINGLES are the row-legitimate form ("What does ‘made a song’ mean."). The pre-ship scan now greps pc-me/them rows for doubles specifically.

**Facts from the reincarnator's future stay explicitly framed as other-timeline memory** (§10 extension): Kobe's Jan 26 2020 helicopter (ch175) and Parasite's ≈$10M CJ campaign (ch176) render only inside Si-on's POV reasoning ("He remembered, from the other timeline, exactly what a true campaign cost") — never as narrator-omniscient past events. The 2014 frame never breaks.

**Mass-media chapters are the block-parade stack** (ch176): official-post (the press release, op-body verbatim) → news-digest (four wires) → naver-search (the sweep, nv-note "The board had stopped pretending to be a contest") → comment-thread (the UN-address joke) → prose montage. The Sado-set comedy ("Father may climb out of the rice chest to stop me") stays prose + dialogue-lines; "Humor on a period-drama set runs short by design" is the transition line back into weight.

**In-verse clock:** ch175 = Dec 26 LA (1:00 a.m. Henson → 3:20 done → 3:27 Wiz callback → 3:45 Eun-ah released → 7:04 Scooter → Universal late morning). ch176 = Universal folds same morning; press release 6:04 a.m. KST Dec 27 (= LA Dec 26 midday); Sado set Dec 27 morning KST; Jin-ri 8:07 a.m. KST. UA collar line: Jan 1 global launch (fixed). Furious 7 end-credits slot: locked.

## §41 — V31 correction: "block written ≠ call over" — the audio-after-block check

**Every phone-call block's prose tail must be walked to the next block/scene-break, flagging dialogue-lines.** V31's ch175 shipped the Wiz call's ANSWER ("Not really." / "Then what was it?" / "I was in a hurry." / the silence / "Brother, that reason is even more terrifying.") as prose dialogue-lines after the block closed — the call was still live. User caught it. The fix pattern: fold the beats into the block in order as pc-me/pc-them, converting narration beats to pc-note VERBATIM and STRIPPING any chr- anchor in the fold (no anchors in pc rows); prose resumes at the genuine post-call action ("didn't prolong the call. He sent the file.").

**Exemption:** dialogue-lines in the tail that are IN-PERSON (the caller's party has physically arrived — Scooter in the hotel lobby) are correct prose. Read the tail, don't just count it.

**Lyrics are never dialogue-lines (§5 has no exceptions for playback scenes):** a demo/radio/phone playback heard in a studio gets a `music-player` (mp-artist marks the context: "studio playback · the engineer's first listen"), even when the raw gives only ONE line. The scan that catches this: grep dialogue-line paragraphs for canon lyric phrases + trailing-em-dash line shapes in every NEW chapter.

**Pre-ship battery addition (mechanized):** for each `.phone-call` in the chapter, collect dialogue-lines between `</div>` and the next `<div class="phone-call">`/`<div class="scene-break">`; any hit = either a leak (call audio) or a documented in-person scene. Zero undocumented hits ship.

---

## §42 · V32 Rules (ch177–178)

1. **Never hand-type `chr-` anchors in a draft — even "known" ones.** The ch177 first draft hand-anchored suspect ids and GUESSED image filenames; pre-wrap audit caught `son-namwon.jpg` (true name `son-nam-won.jpg`). Drafts are plain-names-only; the script wraps, the audit verifies ids⊆defined AND imgs-on-disk. (Extends §34.)
2. **Interrogative parity is a diff, not a spot-check.** Count raw ？+? per chapter and EN ? in rendered body; reconcile EVERY delta. ch177's 48→47 gap exposed a paraphrased verbatim re-quote (the pullquote line re-quoted in narration) — restored verbatim → 48/48. EN≥raw is only safe when every raw mark is individually accounted for (ch178: 18 vs 17, all verified).
3. **Remembered phone-calls get real `.phone-call` blocks.** A flashback/retold call (ch178's invitation) is not prose — it's a pc block inside the memory frame, headed with time-stamp + "as it was"; call-audio stays in rows (§41), frame-narration resumes after the div.
4. **Wrapped-anchor FORMS now include:** Goo Hara/Hara, Son Nam-won, Bong Joon-ho/Bong, LeBron James/LeBron (short forms match shipped precedent: bare-Hara 26, bare-Bong 80, bare-LeBron 40 prior uses). Verify forms by grepping shipped anchor text BEFORE extending — house short-form conventions are empirical, not guessable.
5. **POV-local "plain" notes don't generalize.** §36's Yeon Sang-ho-plain rule was ch170-POV config; he is carded (chr-yoon-hyunsang) with ch106 anchor precedent — anchor him everywhere else. Card existence + prior anchor use beats any per-chapter exception list.
6. **billboard-chart stacks:** ONE song per block (bb-kicker/bb-title/bb-artist/bb-rank/bb-note); a top-3 rundown = three stacked blocks (ch86 precedent). Never cram multiple songs into one block's fields.

---

## §43 · V33 Rules (ch179–180)

1. **One raw per chapter file — enforce on save.** A combined two-chapter write was split post-hoc at the 第N章 marker. Archive raws as `chapter-NNN.txt` individually; the split must never be needed again.
2. **Lyric splices = one lyric-block per musical beat.** ch179's medley is FIVE blocks (promised piece → a cappella, no safety net → the promise → the title line → the last word), each lb-header naming its beat. Never merge distinct musical moments into one block.
3. **The author's veils are canon.** "The milk-tea-sipping Heavenly King surnamed Zhou" and Jin-ri's never-quoted Superman diary entry stay veiled in EN exactly as the raw veils them — deep-thinking fills FORM, never reveals withheld content.
4. **Imagined/premonished headlines are screen-views when the sv-header frames them as unprinted** ("tomorrow's edition · as already typeset in Scooter's head"). Mass-media block grammar covers hypotheticals if honestly labeled.
5. **Wrap-audit filename check is load-bearing (2nd catch):** `park-jihun.jpg` (not park-ji-hun), `son-nam-won.jpg` (not son-namwon) — guessed hyphenation WILL drift from disk; the imgs-on-disk audit runs pre-build every time, no exceptions.
6. **Interrogative parity went exact both chapters this cycle (7/7, 14/14)** — the count-diff method from §42 is now standard: count raw ？, count EN ? in rendered body, reconcile every delta to zero before packaging.

---

## §44 · V34 Rules (ch181–182)

1. **Entity-escape ampersands in brand names.** "Van Cleef & Arpels" shipped bare & twice and broke XML well-formedness (caught by minidom at wrap-audit). Any & in prose becomes &amp; — run the entity check after writing any brand/legal name.
2. **Carded-never-anchored characters: anchor FORWARD, don't retro-churn.** chr-irene existed for cycles with zero anchors (16 chapters plain). New chapters touching her anchor "Joo-hyun"/"Irene" via new FORMS entries; shipped chapters stay as shipped unless a user catch demands retrofit. Address forms inside dialogue ("Irene-yah") stay plain — the wrapper's word boundaries already protect them.
3. **Scene registers choose the name.** Red Velvet dorm chapters narrate with Korean real names (Kang Seul-gi / Park Soo-young / Son Seung-wan — ch109/115/118 precedent); stage names never shipped in this book, so the manager's "涩琪…Wendy…Joy" localized to real names. Deep-scan the shipped chapters for the register BEFORE drafting, not after.
4. **Interrogative parity now ends with a per-line verification:** print every raw ？-line, map it to its rendered sentence, THEN trust the count diff (ch181 24/24 mapped; ch182 19/19 mapped; EN margins +2/+1 legal only because every line was individually confirmed).
5. **Fictional institutional documents are screen-views when the header frames them honestly** — the Four Seasons patrol entry that "was never filed" renders as an sv-log with classification note; same license as premonished headlines (§43 rule 4).
6. **New FORMS this cycle:** ("Joo-hyun", chr-irene, irene.jpg), ("Irene", chr-irene, irene.jpg). Uncarded-by-design speakers this cycle: Richard (TIME), Pierre (Churchill), Kang Seul-gi / Park Soo-young / Son Seung-wan (plain by register precedent).

---

## §45 · V35 Rules (ch183–184)

1. **Greppable franchise lines quote the SHIPPED wording.** Wiz's ch184 grievance ("Most romantic thing he ever said to me was 'I'm a finished product.'") is a callback to ch175's shipped line — grep the old chapters BEFORE re-rendering any recurring joke, lyric, or catchphrase. Never re-translate from raw.
2. **Romanized address forms follow shipped capitalization** ("Oppa", "Eonni", "Unnie", "sunbaenim"). Jin-ri's first on-page "Oppa." (V35, the car) is a canon event: render in shipped romanization, never translate ("brother" is banned).
3. **Carded-never-anchored sweep continues:** this cycle chr-ariana-grande, chr-justin-bieber, chr-behati got their FIRST anchors (after chr-irene in V34). Justin Bieber was missing from FORMS entirely while carded — when a "known" name appears in a new raw, check BOTH the card and the FORMS list before drafting.
4. **Competing relayed offers render as a bid-sheet screen-view** (Dubai/Doha identical millions, "identical to the dollar. The second caller knew precisely what the first had offered... showing up was the point.") — the sv block absorbs quote-structure better than dialogue paraphrase.
5. **Video calls are phone-calls** (Hara debrief, 44 rows) — pc-head notes "video"; the visual channel (cotton pad stopping, table slap) lives in pc-note rows.
6. **Self-catch discipline:** the CJK leak in the ch184 stamp line and the missing space were caught by MY OWN pre-wrap audit pass, not by luck — the audit runs on the DRAFT, before wrap, every cycle.

---

## §46 · V36 Rules (ch185–186)

1. **FORMS regress after a rebuild — the residual audit must sweep ALL carded names.** James Corden and Jung Jae-joon were carded (and previously anchored) but vanished from the rebuilt FORMS list; only the plain-"Corden" residual caught it. The per-chapter residual check now enumerates every id in character-intro, not a hand-picked form list.
2. **When a raw references a SHIPPED arc, quote the shipped artifact.** The MAMA repair names Song of the Year + Best Female Singer exactly as ch156 shipped; 'Legend' chorus is "Won't stop till we're legends" per the ch117 lyric sheet — raw phonetics and variant punctuation lose to canon.
3. **Card workflow per new character (V31 doctrine, now routine):** deep-scan canon → generate portrait → VISUALLY verify identifying features → insert ci-card + chr-modal (ids must pair) → FORMS full+short forms → in-text card optional at true debut → wrap → ids-parity check (cards == modals == used). V36 hit the milestone: 76/76/76.
4. **Fullwidth ？ runs inside quoted posts convert mark-for-mark to ASCII** (【？？？？？？？】 → "???????" — 7 marks preserved). The ？=0 battery is absolute; degrading to fewer marks would be an abridgement.
5. **Per-line ？ mapping catches folds, not just losses:** "哪里夸了？" had been absorbed into a summary clause — restored as its own line ("Complimented where, exactly?"). A paraphrase that loses a question is a loss even when the meaning survives.
6. **Uncarded celebrity cameos stay plain by precedent** (Lee Kwang-soo, ch120; Mike Repole; Richard; Pierre). Card only when the raw gives a character sustained presence + a face; a name-drop inside a comparison stays prose.

---

## §47 · V37 Rules (ch187–188 + the Vancouver Box)

1. **Raws archive is the literal FIRST tool call of every new batch.** V37 drafted ch187/188 off the message before saving; the breach surfaced only when a grep hit FileNotFoundError. Recovery worked because drafts could be re-verified line-by-line against post-hoc archives — that luck is not a process. Raw file first, ？-count recorded at archive time, then anything else.
2. **Hand-typed draft anchors are UNVERIFIED claims.** ch187 anchored chr-cha-taehyun/chr-gong-hyojin with images that never existed (no cards, no files, no prior use). Verify every hand-typed id + image against character-intro.xhtml and ../images BEFORE wrap; if no card exists, the V31 plain-POV decision stands and the anchor comes out.
3. **？ audit is two-way:** per-line mapping (raw ？-lines → EN lines) AND mark-total reconciliation (raw ？ count → EN ? count). V37 caught a flattened question ("Paris fashion week?" rendered as a statement) only via the count delta — per-line alone missed it because merges disguise losses.
4. **Re-read the raw after drafting.** A whole sequence (Arabian horse → "Where would I keep a horse?" → Qatar → "diplomatic-incident prevention program") vanished from a draft written in one pass. The archive exists precisely to catch this; a draft without a post-draft raw diff is unfinished.
5. **Style-block rows are anchor-exempt bookwide** (verified: 0 chr-inline anchors inside pc-/chat-/comment-/sv- rows across 193 xhtml). Residual-plain audits must scan prose lines only; sweeping rows produces false positives (ch103 "Vice Chair Lee Mi-kyung" in a pc row is canon-plain forever).
6. **Count nav by links, not `<li>`.** Nested li inflate the count; spine == nav `<a href="text/...">` count == ncx navPoints is the real invariant (V37: 192/192/192).
7. **A user-supplied lyric goes in verbatim, in ONE block, with improv allowed only inside that same block.** The Vancouver box: four user lines byte-verified in the built epub, plus two improvised Si-on lines inside the same lyric-block — never a second block, never a paraphrase.

---

## §48 · V38 Rules (ch189–190)

1. **epubcheck must validate the artifact that actually exists.** The builder's OUT is cwd-relative; V36/V37's "0/0/0/0" runs pointed at repo root while the epub sat in book/ — epubcheck validated nothing and printed zeros, and both versions shipped with 3 RSC-008 errors (undeclared images). Rule: run epubcheck with an absolute path or from the epub's directory, and confirm the output's diagnostics reference the file (line numbers, file names) before recording a clean bill.
2. **Every new image file gets its manifest item in the cycle it is born.** The battery must print BOTH counts — images on disk/zip AND items declared in the opf — and they must match (V38: 116/116 after adding img-lee-mikyung, img-baek-jeonghoon, img-kevin-hart).
3. **Returning-cast anchors are grepped, never assumed.** Kobe and Hara were already carded with images on disk; a hand-typed "new" id would have phantomed again. Grep character-intro.xhtml + ../images for EVERY named returnee before drafting anchors.
4. **Two-way ？reconciliation includes punctuation-level losses.** Per-line mapping looked clean while "干嘛？" shipped as "What." and "怎么？" as "What —" — the words survived, the marks didn't. Mark totals are checked against line totals every cycle (V38: both restored; ch190 54/54 lines, 58 = 57+1 legal).
5. **Lyrics policy, refined:** real song performed on a live stage → real lyrics ('Starboy' chorus at Doha); fictional in-universe song that the raw describes without quoting → original lines invented from the description, ONE block ('Desert Rose').
6. **Shipped-title rule, extended:** a raw short-form title yields to the shipped long title when story time is past release (绿头苍蝇 → 'Green Bottle Fly', per ch163).
7. **Address forms map per PAIR, not globally:** Jin-ri→Hara is "Eonni" (ch183 precedent), whatever the default romanization table says.
8. **In-text debut cards are part of card workflow for NEW characters — and a retrofit obligation when missed.** V36's Mi-kyung/Hart char-intro blocks were skipped and survived two cycles; the bookwide char-intro count (page 76 + in-text total) now belongs in the battery.

---

## §49 · V39 Rules (ch191–192)

1. **？-punctuation-loss is a recurring class, not a one-off.** V39 hit it twice in one chapter ("isn't she." / "Didn't you say…") — per-line mapping called both clean because the words existed; only mark totals flagged them. When totals mismatch, diff question MARKS per line, not just lines (also: "吧？" sentence-final particles ship as "…, isn't …?" — never a period).
2. **Block-plan count belongs in the pre-package scan.** The plan said 3 pullquotes for ch192; the build had 2 and nobody noticed until the battery. Compare planned-vs-shipped block counts per chapter before packaging; promote or add rather than downgrade the plan (V39: the itinerary aphorism promoted to pq, rebuilt, revalidated).
3. **An epithet shipped anywhere is canon everywhere.** "Nation's first love" first appeared inside a ch106 phone-call row — it still governs the ch191 title when the raw title uses 国民初恋. Grep the FULL book (rows included) for epithets, not just prose.
4. **Plain-vs-anchor decisions follow the person's shipped record.** Suzy: prior mentions ch106/166, no card → stays plain at her first on-page appearance. Seo Eun-ju: carded → anchored. Park Ji-hoon: name-drop, no face, no dialogue → plain forever until the raw gives him a scene.
5. **Financial scenes: transcribe, don't audit.** The raw's arithmetic (20% of NA ≠ 11.3M, strictly) is the fiction's arithmetic; the translator's job is fidelity, not reconciliation — flag nothing, fix nothing, round nothing.
6. **A legal editorial ？ (mark added where the raw has none) must be named in the battery entry** (V39: Park Ji-hoon's quoted question) — undocumented +1s are how false confidence starts.

---

## §50 · V40 Rules (ch193–194)

1. **A quoted message lives ONCE.** The In-na exchange was drafted in prose quotes AND replayed in a chat block — +3 phantom ？marks and a rhythm bug. Rule: chat blocks carry the final exchange; abandoned drafts live in prose narration; never render the same text twice.
2. **Planned-vs-shipped block counts are a hard gate.** Both V40 chapters matched their written plans (11/11, 7/7) and the battery now verifies it per chapter before packaging — a plan that can't ship gets amended consciously, not silently downgraded.
3. **Raw-quoted fictional songs use the raw's lines, translated verbatim, ONE block** ('Twenty-Three' take one) — distinct from invented-description songs ('Desert Rose') and live-stage real songs ('Starboy'). Three lyric-block regimes, all settled.
4. **Chat rows stay anchor-free** even when the chat partner is carded (In-na); the anchor goes on her name in prose narration (§47.5 extended to chat-).
5. **Prior-mention greps now include institution names** (BRIT Awards = new canon from the raw; 'SIXTEEN' = new; JYP the company ≠ Park Jin-young the person — grep both before deciding plain-vs-anchor).
6. **Line-surgery edits run with assertions on every index before write** — an off-by-blank-line is a corrupted chapter; the assert costs one second and saved one.

---

## §51 · V41 Rules (ch195–196 + the ls-time Redesign)

1. **The ls-time is a self-growing box, not a capsule.** `border-radius: 999px` sliced multi-line content ("out of the box"); the fix: `display:block; max-width:100%; box-sizing:border-box; border-radius:0.5em; line-height:1.6; overflow-wrap:break-word; box-decoration-break:clone`. Any future stamp child that becomes a framed element must follow the same law: grow vertically, never clip, never spill. Verify the redesign survives in the SHIPPED zip's stylesheet every cycle.
2. **Raw files get a mechanical integrity guard at archive time.** V41's first ch195 archive was corrupted (half-translated mixed lines, missing beats) — caught by re-read, rewritten verbatim. The archive step now ends with a mixed-language leak scan (raw files may contain English only in whitelisted tokens: lyrics, names, titles) + the ？ count. An archive that fails either check is rewritten before any drafting begins.
3. **Title-only stays title-only.** A hummed real-song rhythm ('Shape of You') renders as description + title — no lyric-block — exactly like 'Where Are Ü Now'. Lyric-blocks exist only when the raw quotes words (three regimes, §50.3).
4. **Shipped-record rule has teeth.** Ed Sheeran got a full scene and still ships plain: prior mentions (ch100–110) established him plain; a carding upgrade of an established-plain character is a user decision, not a translator's.
5. **Chat-block splits are a rhythm tool.** One conversation with narration beats between messages = one chat block per beat segment (V41: 5 blocks for the trophy/guitar thread); the only law is §50.1 — a message text appears exactly once.
6. **Indirect speech that carries a raw ？ is a ？-loss.** "The host asked whether the song would blow up" hides the mark; render the question direct first, then audit (V41: restored before wrap; the mapper would have caught it as a −1).

---

## §52 · V42 Rules (ch197–198)

1. **New chapter files are COMPLETE standalone XHTML documents.** V42's drafts began at `<body>` — epubcheck: RSC-005 (namespace), then RSC-016 after a partial prolog clone (ch196's `<title>` residue, missing `</html>`). Recipe: clone prolog+head from the previous chapter, set the correct chapter number in `<title>`, append `</html>`, THEN wrap/audit.
2. **The archived raw file is the ？-ledger; hand counts drift.** V42's plan-phase hand count said 20/35; the file said 24/42. Workflow: save raw → run the guard → print the ？-line list from the FILE → place every mark in the draft → reconcile EN ASCII-? marks AND ？-bearing-line counts to the raw exactly (bookwide convention: EN narration/dialogue uses ASCII `?`; fullwidth ？ must be 0).
3. **Carded-name sweeps take their forms from wrap_v29_anchors.py's FORMS list.** The chi-name regex extraction is broken by the `<a>`-wrapped names (silently matched only 3 cards for many cycles). When a residual sweep over ALL chapters flags surnames, classify before touching: display rows (pc/chat/nd/sv/ls/wd) are plain BY DESIGN; same-surname different-persons (ch03's collector veterans Choi/Park ≠ Jin-ri) must NEVER be blanket-wrapped; only true prose mentions of the carded person are candidates.
4. **Legacy anchor census (V42 finding, closed as cosmetic):** a small population of older chapters carries unanchored carded-name mentions from historical post-wrap patches plus bare-surname protagonist references — missing peek popups only, zero epubcheck impact, shipped record through V41. Any future legacy re-anchor pass requires a per-instance deep scan; it is NOT routine-cycle work.
5. **Raw-echo fidelity:** when a spoken line is echoed later as narration italics, reproduce the raw's punctuation class — the raw's comma-joined wishes (想要什么就说，想留谁就留) carry ZERO question marks in both the dialogue and the echo; inventing marks there breaks parity (V42 caught +3 exactly this way).
6. **Title-only stays title-only, reversed case:** when the raw quotes lyric WORDS but never names the song (ch197's four memorized lines), ship a lyric-block with the lines verbatim and leave the song unnamed — naming it would be an editorial reveal the raw withheld. The raw's translation glosses are apparatus, dropped without content loss.

---

## §53 · V43 Rules (ch199–200 + the Chat-Orientation Law)

1. **Chat orientation = the phone owner's perspective.** `self` + `chat-sent` = the owner of the phone (right side); the other party = `chat-name` (no self) + `chat-bubble chat-received` (left side). The `chat-header` names the room's OTHER party ("KakaoTalk · <other>"). V41's ch195 shipped inverted/all-sent; the user's correction is now law: when a scene follows character X's phone, X is self. A multi-block conversation may re-seat per block ONLY if each block names its own phone; never re-quote a message (§50.1).
2. **Chat-coherence audit every cycle (bookwide):** flag any container where (a) one party appears on two sides, or (b) a container with ≥2 distinct parties is all-sent/all-received. V43's scan proved the ch195 defect was isolated; keep the scan in the battery.
3. **The `-ssi` suffix defeats the anchor wrapper** (`(?![\w-])` guard): "Baek Si-on-ssi" stays unanchored after a normal wrap. Hand-anchor with the suffix OUTSIDE the `</a>`. Expect xi-forms in future raws; sweep for `-ssi` after wrapping.
4. **One-way text notifications render as screen-view rows** (sender + text); a chat-container is for a two-party thread. A conversation whose halves are separated by a scene cut may be split into one container per phone (owner = self in each), as in ch199.
5. **Prophecies stay unnamed:** when narration foresees a future the raw doesn't name (the 2017 summer song), render the foresight without naming the song — same law as §52.6, extended to narration.
6. **Anonymized names stay anonymized:** a raw that writes 金XX/全XX ships as Kim XX / Jun XX with its identifying descriptor (the drama title) intact — do not "restore" real names the source deliberately masked.
7. **Estimate/summary numbers convert exactly:** 亿 = 100 million (160亿 = 16 billion; 24.8亿 = 2.48 billion). Verify every converted figure against the raw before shipping.

---

## §54 · V44 Rules (the Style-Block Completeness Law)

1. **Quoted display material NEVER ships as a plain paragraph.** Any raw 【】-quoted or explicitly-labeled headline, article, disclaimer, platform post, table, or notification MUST land in a display block: single headlines → `news-digest` (nd-source + nd-headline); article bodies/disclaimers → `news-digest` with `<p>` children (ch07 form); public posts → `official-post` (op-band/op-handle/op-body); search terms → `naver-search`; tables/inventories → `screen-view`. The raw's 【】 brackets are the signal. Packaging sweep: grep plain `<p>`s for em-dash-framed lines (`<p>— … —</p>`) and "headline:" intros — zero tolerance.
2. **edit_file on wrapped chapters: re-derive old_text from the CURRENT file first** (the wrapper may have inserted anchors inside the target), and after ANY edit re-parse the XML and check the tail for duplication before building. Fuzzy-match residue can duplicate closing tags past `</html>` (expat: "junk after document element").
3. **Amendments upward are the default repair:** when the user (or a sweep) finds missing blocks, add the blocks — never downgrade the material to prose.

---

## §55 · V45 Rules (ch201–202 + the Reset-Recovery Drill)

1. **Fresh-session pre-flight:** if a build tool or path is suddenly missing (SRC symlink, jdk4py, epubcheck), run `bash book/setup_workspace.sh`, then check `git rev-parse --short HEAD` against origin — environment resets can roll HEAD to the base commit while leaving the worktree intact. Recovery: `git fetch origin arena/01a08c66-ai-storage && git reset -q FETCH_HEAD`, verify `git status` shows only the expected delta, then continue. Never commit from a rolled-back HEAD.
2. **Raw echo fidelity extends to sentence TYPE:** a raw line ending in 。 is a statement — never upgrade it to a question in EN (the ？-ledger catches it as +1 mark with no raw line). V45: the signalman's line ("Am I a manager or a battlefield communications officer.") ships with its period.
3. **Interior monologue question-stacks are ？-LINES, not one paragraph:** the ledger counts lines; compressing 什么火？/谁的火？ into one pc-note breaks line parity. Render one raw line per row/paragraph even inside display blocks.
4. **Phone calls:** one call = one pc block; separate calls = separate blocks (§37). pc-head names parties + scene ("Lee Ji-eun → Baek Si-on's phone · voice · the third ring · answered by Jin-ri"). pc-me = protagonist side; when the protagonist's phone is answered by someone else, that answerer is pc-me for that block.
5. **Nickname registers:** a side character's pet name for another (In-na's "Sulli" for Jin-ri) ships as the stage name — it is dialogue color, not a narration-form change; narration keeps the carded name.
6. **Merch of the ledger:** when a draft merges or splits raw ？ lines, the two-way diff must return to EXACT before build — merges in display rows count the same as in prose.

## §56 · V46 Rules (ch203–204 + the Builder-Clone and Manifest Laws)

**§56.1 Version-bump builder cloning.** `sed 's/v45/v46/g'` does NOT clone the builder safely: the OUT filename is `Seoul_Starting_With_Debt_Collection__Version_45.epub` (contains no "v45") and SRC is an absolute path — an un-renamed clone RUNS THE OLD BUILDER and silently overwrites the validated previous epub with new content under the old name. Clone with explicit replaces: the docstring's "Version 45", and the full OUT filename `Version_45.epub` → `Version_46.epub`. If clobbered: `git checkout -- <old.epub>` (it is committed), fix the clone, rebuild. Never leave two builder generations writing the same OUT.

**§56.2 Manifest ≠ zip-glob.** The builder's os.walk puts EVERY file under epub_src into the ZIP, but the OPF `<manifest>` is hand-maintained: new images (and any new resource) need explicit `<item id="img-…" href="images/….jpg" media-type="image/jpeg"/>` entries. Signature failure: epubcheck `RSC-008 "… is not declared in the OPF manifest"` ×N for exactly the new assets. Battery projections follow the manifest count, not the zip count (V46: zip entries 353, manifest items 350).

**§56.3 New-carded-character pipeline (executed ×2 in V46).** (a) portrait image into OEBPS/images (house photoreal style); (b) `<div class="char-intro" id="ci-…">` card + `<div class="chr-modal" id="chr-…">` modal in character-intro.xhtml (append after last card / last modal); (c) FORMS entry in wrap_v29_anchors.py; (d) re-run wrapper — it is idempotent on already-wrapped files (anchored names live inside `<a>`, never re-matched); (e) debut = the first narration anchor; pc-head/pc-note rows stay plain (§56.5). Already-carded characters (Seo Eun-ju, no FORMS entry since ch88): hand-anchor EVERY instance including dialogue-lines — shipped bookwide carries zero plain instances of carded names in narration/dialogue.

**§56.4 Battery methodology lock.** Reproduce the previous cycle's count patterns EXACTLY; a quick reimplementation invents false deltas: `nd-`/`op-` substrings match hyphenated prose ("trend-merchant", "top-tier", "second-floor", "ground-floor"); `class="chat"` misses the real chat container class; body-only splits hide ch78's CJK. Trust only V45→V46 deltas computed by the SAME code, plus the stable absolutes (？0, framed NONE, unbal 0, epubcheck 0/0/0/0).

**§56.5 Display-row name exemption (re-confirmed against shipped precedent).** pc-head, pc-note, sv-note, mp-artist, chat-name and other display rows routinely carry carded names PLAIN (ch201 "…answered Baek Si-on's phone", ch202 "Baek Si-on wasn't in a hurry", ch195 chat-name cells). The residual-plain sweep scope = classless `<p>` + `dialogue-line` only. Address-only registers ("Representative Chang", "Counselor Seo") stay plain per §55.5; full-name instances of carded characters never do.

**§56.6 Statement lines stay statements.** ch203 客气什么，我们俩谁跟谁。 ends with 。 though it paraphrases a question — EN shipped as "For what — between the two of us." (no ？). The ？-parity diff catches these as +1 mark/+1 line inserts; fix by de-marking the EN, never by marking the raw.

**§56.7 Anchor-point reality check.** Post-wrap patching regexes must anchor on the paragraph's TRUE opening, not a remembered phrase: ch204's freeze-frame passage was one long wrapped `<p>` beginning "The director turned back to the freeze-frame…", not a standalone "Beautiful." paragraph; the music-player insert split mid-paragraph at "put it in. He pressed play." Grep the live file first, then patch with count==1 asserts.

## §57 · V47 Rules (ch205–206 + the Raw-Transcription and Reconciliation Laws)

**§57.1 Raw transcription is a code path.** Hand-copying raws can corrupt them (a line typed as 从合井洞 to 论岘洞). Post-save verification is not optional: run the ？-ledger AND verbatim probes on key lines (messages, punchlines, title lines) immediately after every raw save, before any drafting. Normalize raw artifacts only in EN (Jay—Z → Jay-Z); never edit the raw file.

**§57.2 ？-reconciliation tooling: the ordered walk.** difflib SequenceMatcher degenerates on ？-ledger vectors full of repeated 1-mark lines (嗯？ ×4) — it can emit "everything unmatched" garbage. The reliable reconciler is the ordered greedy walk: walk raw ？-lines and EN ？-lines in parallel, each raw line consuming EN lines until cumulative marks match; report the first true mismatch and every raw line left unconsumed. It isolates exactly the three defect classes: extra EN mark (rhetorical 怎么 with no mark → "What's this? Shy?" must not double-mark), mark lost to "!" (你也太直接了吧？ ≠ "too direct!"), and statement-ized questions (就买了？ → "…and you already bought it?").

**§57.3 Post-wrap conversions: slice the live file.** Generalizing §56.7: any second-pass rewrite of a WRAPPED chapter (upgrading prose to blocks) must cut boundaries by unique marker strings read from the CURRENT file, because the wrapper has already inserted anchor markup inside the target paragraphs. When rebuilding the block, carry the existing `<a class="chr-inline">` anchors into the new sv-lines/sv-notes.

**§57.4 Block-ledger reconciliation (the consolidation trap).** The drafting pass silently consolidates planned blocks into prose/dialogue (ch206 drafted 8 blocks vs 11 planned; ch205's keywords list became dialogue). After drafting, diff the shipped block counts against the ledger BEFORE wrapping and run an upgrade pass — quoted/written/display material (a pen-and-paper list, a domestic wind-down sequence, an argument montage) belongs in display blocks. No compromise means the ledger is a checklist, not a suggestion.

**§57.5 Off-screen pop-star precedent.** Ed Sheeran (6 shipped chapters, message-only presence) stays plain and UNCARDED, same as Meghan Trainor. Cards go to on-page speaking roles with scene presence (Yeri, Park Sang-min), even one-scene ones. Check `character-intro.xhtml` AND shipped-chapter greps for prior plainness before carding anyone.

**§57.6 Carded-but-FORMS-less names.** Seul-gi / Seung-wan / Joy have been carded since their arc yet never had FORMS entries (ch162 was hand-anchored). Systematized in V47: FORMS now carries the full Red Velvet five + Park Sang-min. Before drafting any ensemble chapter, grep FORMS for every expected name — do not assume carded = wrapped.

## §58 · V48 Rules (ch207–208 + the Author-Note and Walker-Blind-Spot Laws)

**§58.1 Author-note sections.** Serialized batches can carry paratext (月末总结兼月初求月票: word-count recaps, update schedules, monthly-ticket requests). Archive it verbatim in the raw file (it was delivered), EXCLUDE it from the EN chapter — it is not narrative, and its absence must be noted in the worklog entry. Never let a translator's completeness instinct pull author commentary into the book. Also: multi-chapter pastes arrive as one blob — split raws at the 第N章 headers before the guard runs.

**§58.2 Walker blind spot: position-absorbed extras.** The ordered mark-walk (§57.2) cannot detect an extra EN ？-line whose marks line up positionally (a 1-mark raw line consuming the extra 1-mark line next to its real translation). When the walk reports no mismatch but totals differ by exactly one line, STOP walking and dump the complete EN ？-line list side-by-side against the raw list — the extra line is a statement carrying an invented mark (rhetorical 怎么/干什么 with raw 。). Two shipped examples: 我怎么站得这么靠边。 and 我取代你干什么，…混音。

**§58.3 POV-owner chat orientation (generalized).** The chat law (§52.7) generalizes: the POV owner of the SCENE is `chat-name self`/`chat-sent` (right), and the other party is left — even when neither is Baek Si-on. V48's Irene↔Baek Eun-ah container: Irene (scene POV) right/self, Eun-ah left. Baek-centered scenes keep Baek right.

**§58.4 Fidelity audit for recurring props.** Recurring display objects have shipped canon that must be re-verified per cycle: 'OOPS' demo filenames (ch202 `OOPS_demo_CP_MT_v1` → v2 drops MT, adds version), Cheongsong Investment (ch139), "Cousin" (Eun-ah, ch6–9), ankle-card wording (ch181), music-show names (Music Bank/Music Core/Inkigayo), S4 World Championship (ch107–114). One grep per prop before drafting; never re-derive from memory.

## §59 · V49 Rules (ch209–210 + the Exclamation and Grading-Sequence Laws)

**§59.1 Raw ！ never becomes ？.** The ？-ledger counts ？ only. Raw exclamations without ？ (为什么！) ship with "!" and zero marks; double-marked single-line dialogue (诶？你们来啦？) must land BOTH marks in ONE EN line. When the walk is EXACT at first pass, do not hunt for extra "balance" — ！-lines and single-line double-marks are legal ledger shapes, not defects.

**§59.2 Callback fidelity for returning gags/props.** When a raw chapter cites an earlier scene (the rice-bag carry, the princess line, the gifted shoes), grep the shipped EN chapters and reuse the exact coined phrases — "a textbook fireman's carry, so textbook it contained not one milliliter of shoujo manga" (ch161), the at-home princess exchange (ch161), "low-top trainers"/collaboration pair (ch180–181), "Princess-nim" (ch199). Never paraphrase a returning prop; the reader's memory is the continuity engine.

**§59.3 Grading sequences → one sv, one line per candidate.** Multi-candidate assessment scenes (tryouts, auditions, interviews, line distributions) convert to a single screen-view with an sv-header like "The tryouts, as graded" and one sv-line per candidate, closing with an sv-note for the tail verdict. Keeps clinical verdict texture display-shaped instead of prose-stacked; the conversion is safe post-wrap if anchors are carried (§57.3) and the passage is ？-free.
