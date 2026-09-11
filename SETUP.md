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

`raw/` holds ch121–130, 135–180 (55 files) + the ch117–120 placeholder note.
V33 update: ch179–180 raws archived verbatim before translation (standing rule).
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

## 6. State & next steps (from worklog §81)

- **Shipped:** Version 33 — 180 chapters, epubcheck 0/0/0/0, all audits green
  (phone-call 73, music-player 28, lyric-blocks 17, spine 184, navPoints 184,
  manifest 321, 324 entries, chr 73/73, images 113/113, ？0, CJK 0 except ch78
  「」 exception, interrogative parity ch179 7/7 + ch180 14/14, both exact).
  V33 = ch179 "I'll Be There to Save the Day" (Temple Theatre NYE: TIME's
  Next-Generation-Leader headline, the setlist screen-view, the Furious 7
  cover condition, the five-lyric-block splice into One Call Away, the a
  cappella drop, Jin-ri's Superman beat, the countdown to 2015, dumplings for
  ticket stubs, Scooter's premonished poisoning headline) + ch180 "The
  Four-Leaf Clover Gets the Final Say" (Koreatown army stew, the aurora
  physics lecture, two tickets to Canada, "Does eating count?", the Under
  Armour Melrose drop, and the Beverly Hills lawn that produces the fourth
  leaf).
- **Next build:** V34 = ch181+ — raws not yet provided (archive to
  `raw/chapter-181.txt` … first, then translate).
- **Open threads:** Jan 2 — aurora trip for Si-on + Jin-ri (Eun-ah keeps
  Hye-ja company; Scooter collapses); TIME "Next Generation Leader" piece +
  Billboard update + TIME interview (Jan 1–2); 'One Call Away' now
  half-public (3,000 sworn ears vs "does not end up on the internet"); CJ
  dumpling New Year events; UA collab launch NOW LIVE (reservation page
  crashed once, queue around the block); NYE test-show aftermath;
  one-album-two-crowns chase vs 'Uptown Funk'; Grammy "next year =
  credibility disaster" framing; Producers fallout + Park Ji-eun pressure
  arc; Blin in Hara custody; Furious 7 end-credits drop + Wiz's bottle cameo;
  Seoul premiere + solo performance; Sado wrap + Oscar campaign
  (Showbox/Orion pending, the meal with Director Lee); Charlie's $500k +
  separate signing negotiation; Yeon Sang-ho arc — Train to Busan SIGNED
  (role: high schooler Jin-hee); Irene — Music Bank MC + no phone; Adam's
  dinner debt; Wiz's "brother for life"; Dispatch Director Lim gift (reason
  still unstated on-page).
