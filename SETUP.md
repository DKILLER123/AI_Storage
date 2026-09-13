# Workspace Setup — State of Restore (2026-09-10)

The full previous workspace was archived to GitHub (`DKILLER123/AI_Storage`) and is
restored here. This file records the restored layout, verification results, and the
one structural change (repo now lives at `/home/user/AI_Storage` instead of
`/home/user` directly). `SKILL.md` remains the operating manual; `worklog.md` the
per-pass history. All legacy `/home/user/...` paths keep working via symlinks.

## 1. Layout (restored + extracted)

| Item | Canonical location (repo) | Legacy path (symlink, still valid) |
|---|---|---|
| Repo / workspace root | `/home/user/AI_Storage/` | `/home/user/` |
| Operating manual | `SKILL.md` | — |
| Per-pass worklog (§1–§75) | `worklog.md` | — |
| **EPUB source root (extracted from V28)** | `work/epub_src/OEBPS/` | `/home/user/work/epub_src/OEBPS/` |
| Raw chapter texts (Chinese) | `raw/chapter-NNN.txt` | `/home/user/raw/chapter-NNN.txt` |
| Build & fix scripts | `book/` (build_epub_v4 … v28, fix_v4_*, apply_name_previews.py, setup_workspace.sh) | `/home/user/book/` |
| Card payload + helpers | `work/payload40.json`, `work/cardlib.py`, `work/pc_convert.py` | `/home/user/work/…` |
| Pre-fix chapter references | `work/pristine/OEBPS/text/chapter-{57,58,127}.xhtml` | — |
| **Latest deliverable** | `Seoul_Starting_With_Debt_Collection__Version_28.epub` (19,477,108 B · 309 entries · ch1–170) | — |

**Symlink farm (recreated by `book/setup_workspace.sh`, not persisted by git):**
`/home/user/{work,raw,book}` → `/home/user/AI_Storage/{work,raw,book}`.
Every hard-coded path in existing scripts therefore resolves unchanged — do not
rewrite the scripts' paths.

## 2. Extraction (done)

`Seoul_Starting_With_Debt_Collection__Version_28.epub` → `work/epub_src/`:
309 files = 309 zip entries. Contents: `mimetype`, `META-INF/container.xml`,
`OEBPS/{content.opf, nav.xhtml, toc.ncx}`, `OEBPS/text/` (170 chapters +
character-intro + characters + cover + glossary = 174 xhtml), `OEBPS/images/`
(108 jpg), `OEBPS/fonts/` (20 woff), `OEBPS/styles/` (fonts.css + stylesheet.css).

**Reproducibility proof:** `python3 book/build_epub_v28.py` run against the
extracted tree produces a byte-identical EPUB (19,477,108 B; all 309 CRCs equal).

## 3. Deep-scan verification (all green, matches worklog §75)

| Check | Result |
|---|---|
| XML well-formedness (174 xhtml) | 174/174 parse OK |
| character-intro cards | 70 `chr-*` ids (Taylor = `chr-taylor`, image `taylor-swift.jpg`; no `chr-faker`) |
| Anchor audit (9,334 `chr-`/`char-` hrefs bookwide) | 0 missing targets |
| Images | 108 on disk / 105 referenced in text / 3 outside text (`cover-art.jpg`, `cover-bg.jpg` in stylesheet.css; `cover.jpg` in OPF only) → 0 true-unref |
| `.phone-call` blocks bookwide | 63 (matches §75) |
| CSS coverage | 455 distinct classes used, 0 unknown |
| epubcheck 5.x on V28 | **0 fatals / 0 errors / 0 warnings / 0 infos** |
| CJK/fullwidth in chapters | 0 (house regex) — 10 legacy `「」` corner brackets in ch78 only, documented, left as shipped |
| Straight apostrophes | 2,643 legacy (ch21–24/76–80 era), documented ~2,661 — **do not bulk-fix** |

## 4. Raw coverage

`raw/` holds ch121–130, 135–186 (60 files) + the ch117–120 placeholder note.
V36 update: ch185–186 raws archived verbatim before translation (standing rule).
**Not on disk:** ch1–116, ch117–120 bodies, ch131–134 — chapters shipped from
in-session raws before the archive; per `raw/chapters-117-120.txt` the project
rule is *raws first, then translate*, so ask for re-paste if re-verification of
those chapters is ever needed.

## 5. Toolchain (reinstall each session)

`epubcheck` + JRE live in pip packages (`jdk4py` = OpenJDK 25 runtime,
`epubcheck` = 5.x jar), because `/tmp` and apt are not reliably available.
Bootstrap everything with:

```bash
bash /home/user/AI_Storage/book/setup_workspace.sh --validate
```

Run-from-source QA battery lives in the worklog §69/§75 method notes (fragment
audit, Park `<a` check, chat-name self audit, typography, image accounting).

## 6. State & next steps (from worklog §114)

**SHIPPED: V65 = chapters 241–242 (the Norwegian bedroom producer / three gazes at the premiere).** epubcheck valid 0; battery = exact 3-file sha1 delta + 2 new chapters; only the V65 epub on disk (23,024,958 B, 401 entries).

**SHIPPED: V66 = chapters 243–244 (one screen, three rules of love / the recording studio doesn’t believe in pink) + the Alan Walker card.** epubcheck 0; only the V66 epub on disk (23,182,233 B, 404 entries).

**SHIPPED: V67 = chapters 245–246 (Producer Lee advances step by step / ‘Sado’ opens to a smash) + the user-provided Ariana Grande & Alan Walker portraits installed over the in-book images.** epubcheck 0; only the V67 epub on disk (23,039,761 B, 406 entries).

**SHIPPED: V68 = chapters 247–248 (the pretty noona buying dinner / the same four-leaf clover, different hearts) + the ch78 KakaoTalk chat-block repair.** epubcheck exit 0, no errors; only the V68 epub on disk (23,070,930 B, 408 entries). ？-ledger 61/48 preserved; anchors-in-blocks 0; CJK-ideograph 0; chat-container 157→158.

**SHIPPED: V69 = chapters 249–250 (welcome to La La Land / the bottom line of art is the insurance company).** epubcheck (EPUB 3.3) 0 fatals / 0 errors / 0 warnings / 0 infos; only the V69 epub on disk (23,097,105 B, 410 entries). ？-ledger 42/8 preserved; chr-inline anchors 15,745; anchors-in-blocks 0; CJK-ideograph 0; invented classes 0. Latent V68 nav gap (ch243–248 missing from nav.xhtml) closed — nav now complete 1–250. Builder SRC repointed to the real path (the `/home/user/work` symlink was absent at session start). Tooling reinstalled after a sandbox reset (jdk4py 25.0.2 + epubcheck 5.3.0).

**SHIPPED: V70 = fix pass (no new chapters): book-wide list-block line-separation redesign (21 CSS rules), ch249 video call → facetime block, ch250 Hyundai call → phone-call block, ch78 「」 → curly quotes.** epubcheck (EPUB 3.3) 0/0/0/0; only the V70 epub on disk (23,097,231 B, 410 entries). CJK/fullwidth now 0 across all 250 chapters; fullwidth ？ 0; anchors-in-blocks 0. Damien Chazelle portrait installed (user's `uploads/Damien.jpg`, delivered via GitHub upload f521910, over `images/damien-chazelle.jpg`).

**V67 (next batch) checklist:**
1. Sandbox pre-flight (§66.4): `ln -sfn /home/user/AI_Storage/work /home/user/work`; `pip install --break-system-packages epubcheck jdk4py`; java symlink; rolled-back `.git` → fetch + reset --soft (§55.1).
2. Save raws FIRST; VERIFY THE RAWS (token sweep + probes) before anything else (§76.1); ？-ledger THREE numbers BOTH widths, one raw paragraph = one EPUB paragraph (§76.2).
3. Canon states (post-ch244): ‘Sado’ premiere + Q&A DONE (Aug 3, Megabox COEX); Alan asked the onstage comprehension question and OWES Baek Si-on the European-viewer report; Alan still in the studio at night (had planned PC-bang LOL). ‘Everytime’ (= Descendants of the Sun OST, Baek Si-on × Lee Ji-eun) first-round trial vocal = Wendy, Lee Ji-eun producing hard, Irene “accompanying,” Jin-ri + Jeong Han-teuk (overtime) + Jung Jae-joon present. Three love rules read from the harem scenes: Jin-ri = true favor includes not consuming; Ji-eun = plant your name in his songs; Irene = catch the chances, don’t mistake favor for power. Baek Si-on: stage greetings upcoming, flies to America in a week. Alan Walker NOW CARDED (chr-alan-walker) — anchor every mention.
4. Drafts: block ledger BEFORE writing; card pre-flight AT DRAFT TIME (§72.3); sv for emails/screens/lists, ckl for briefs/eras/plans, tv for broadcast replays; NO hand-anchors in blocks.
5. Wrap EXPLICIT argv; minidom gate; anchors-in-blocks = 0; invented-class = 0.
6. Builder: clone build_epub_v68.py via python replaces (no CJK sed), run from repo root.
7. epubcheck 0 (JRE may need `/usr/local/lib/python3.11/dist-packages/jdk4py/java-runtime/bin` on PATH); battery sha1: opf/ncx/nav + new chapters (+ owed repairs); CJK-ideograph sweep ALL content files. Baselines: anchors 15,457; ls 575 / sv 325 / pq 158 / ckl 73 / pc 110 / mail 13 / comment-item 646 / tv-screen 15 / lyric-block 36 / music-player 40 / live-stage 37 / interview-block 6 / news-digest 83 / chat-container 158 / comment-thread 114; images 129; cards/modals 89/89; ？ total 5,961.
8. Pre-package deep scan: ？ from artifact; 20+ spot probes; doubled-word scan; OOPS residual; misattr sweep (Kim Ye-rim ban active).
9. Delete previous epub AFTER validation; worklog/SKILL/SETUP updates; commit + push; present_file.

**SHIPPED: V71 = fix pass (no new chapters): `.ckl-step` restyled to mirror `sv-line`'s bar-row implementation in the checklist's own cyan palette (not sv-line's gold/cream), and three `slate-block` film blocks added to ch250's La La Land shoots (freeway ensemble dance / Mia & Sebastian first meeting / A Lovely Night).** epubcheck (EPUB 3.3) 0/0/0/0; only the V71 epub on disk (22,989,415 B, 410 entries).
