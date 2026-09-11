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

## 6. State & next steps (from worklog §84)

- **Shipped:** Version 36 — 186 chapters, epubcheck 0/0/0/0, all audits green
  (phone-call 77, music-player 28, lyric-blocks 19, spine 190, navPoints 190,
  manifest 327, 333 entries, cards 76 = modals 76 = anchored 76 — FULL PARITY,
  images 116/116, ？0, CJK 0 except ch78 「」 exception, interrogative parity
  ch185 16/16 exact + ch186 44/44 lines mapped).
  V36 = ch185 "Chaebols Can't Picket, but Movies Can Fire" (LAX farewell, the
  First Light Tour brand sheet, locusts vs 36 shows, Corden's refund moment,
  the CJ joint venture 60/20/20, the MAMA debt repaid, the hit-list pitch —
  No. 1 is a certain teacher — and the plastic-bottle toast) + ch186
  "Forbidden From Increasing America's GDP With Your Life" (Kevin Hart's
  booster seat, Charlie's twenty-thousand-person stage + Dubai brief,
  Jung Jae-joon's Doha commission, Silicon Valley retention fandom,
  Vancouver's Korean chorus, Ariana at Madison-level NYC, three fansite
  masters grounded and deported by their own idol, and the forum post that
  made the hot list before Korea woke up).
- **Next build:** V37 = ch187+ — raws not yet provided (archive to
  `raw/chapter-187.txt` … first, then translate).
- **Open threads:** The HIT-LIST FILM is in motion (uncle Baek Jeong-hoon
  directing; CJ financing; the "teacher" unnamed on-page — Blue House
  powder keg); Mi-kyung exile backstory (protection-foundation non-payer);
  tour continues (36 shows; Chicago → 'See You Again' LIVE PREMIERE planned
  w/ Universal's blessing); Charlie's Dubai song (2-week deadline, 30%
  publishing, sand-touching trip, ECONOMY); Jung Jae-joon's Doha song;
  Arabian horse contingency ("Where would I keep a horse?"); Warm Light's
  viral deportation post (Korean forums heating up); "I'll answer." promise
  to Jin-ri (long-distance test); Kevin Hart's booster-seat grudge; Jason/
  Bieber album-pressure watch; MAMA-repair secret held by CJ+Si-on; Blin in
  Hara custody; Furious 7 end-credits + Wiz Chicago dates; Seoul premiere +
  solo performance; Sado wrap + Oscar campaign (Showbox/Orion, Director Lee
  meal); Charlie's $500k; Train to Busan SIGNED (Jin-hee); Irene — Music
  Bank MC, ANCHORED now; UA collab live; Dispatch Director Lim gift
  (reason unstated on-page).
