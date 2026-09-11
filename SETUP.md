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

## 6. State & next steps (from worklog §101)

**SHIPPED: V53 = chapters 217–218 + REAL celebrity photos (Yeri fansite crop, Emma Cannes crop — AI stand-ins retired) + `.search-bar` block (ch215 retrofit) + Ayesha Curry card (85²).** epubcheck 0/0/0/0; V52 baseline beaten on every battery metric; only the V53 epub on disk.

**RESOLVED this cycle:** the Yeri/Emma image directive — image_search-sourced, visually verified, ImageMagick-cropped real photos installed under canonical filenames (§62.4). The user's gist-upload route (§62.3) stays open ONLY if they re-assert their own files.

**V54 (next batch) checklist:**
1. Save raws FIRST (split pastes at 第N章 headers) + ？-ledger + guard + verbatim probes (§57.1); author-note paratext excluded from EN (§58.1).
2. §55.1 pre-flight; canon greps BEFORE drafting; one grep per recurring prop (§58.4); callback fidelity on returning gags (§59.2).
3. Full standalone XHTML drafts; block ledger; reconcile counts before wrapping (§57.4); grading sequences → one sv per candidate line (§59.3).
4. ？-ledger ordered walk (§57.2); one-line-total diffs → dump full EN ？-list (§58.2); ！ stays ！ (§59.1); statements stay statements (§56.6).
5. wrap + audit: XML, undef NONE, imgs, CSS, CJK, bare &, unbal, framed sweep, residual-plain (§56.5); post-wrap patches slice the LIVE file (§57.3); STRIP chr-peek from ALL block rows post-wrap (§63.1 — wrapper's skip-list lags the block inventory).
6. Cards: grep intro page + shipped chapters first (§57.5); FORMS completeness (§57.6); chat POV owner = self/right (§58.3).
7. Registration: opf items + spine after last chapter; explicit image items for new portraits (§56.2); nav li ×2 word-form; ncx np-223/np-224 for the next batch.
8. `.search-bar` block mandatory for ANY internet/app search scene (§63); hover previews stay banned in every block (§63.1).
9. Builder: clone build_epub_v53.py with EXPLICIT replaces (OUT filename), run FROM REPO ROOT — SRC is the /home/user/work symlink into the repo; NO sync step exists or is needed (§56.1).
10. epubcheck → 0/0/0/0; in-zip battery vs V53 baseline (§56.4 same-code deltas): entries 374+delta, chapters 218+2n, spine/navPoints 222+2n, nav chapter-li 218+2n, images 125+n³, cards/modals 85+m³, in-text 79+m³; ls504/sv228/pq117/lb31/mp35/pc94/chat134/ct103+590/nv11/wb35+wd91/sb187/search-bar1; anchors 12,333+delta; ？-parity EXACT; PEEK-IN-BLOCKS 0; CJK 0 (ch78 「 ×10 sanctioned); 【】 0; ls-time box + search-bar CSS in shipped stylesheet.
11. Pre-package in-zip deep scan: ？-parity + 【】/framed sweep + raw-vs-EN block coverage (§54.1).
12. Delete previous epub AFTER validation; worklog / SKILL (new rules) / SETUP §6 rewrite; commit + push; present_file.
