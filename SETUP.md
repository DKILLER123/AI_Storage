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

## 6. State & next steps (from worklog §92)

**SHIPPED: Version 44** — `Seoul_Starting_With_Debt_Collection__Version_44.epub` (repo root), epubcheck 0/0/0/0 (absolute path, §48.1). Book: 200 chapters; spine 204; navPoints 204; manifest 344; entries 347; images 116=116=116; cards 76=76=76; pc 81 / lb 27 / sv 151 / pq 66 / chat 125 / ct 99 / nd 69 / op 32 / nv 10 / mp 29 / ls 465; ？ fullwidth 0; ？-parity ch197 24/23, ch198 42/42, ch199 24/24, ch200 25/24 — exact; ch195 chats at the user's orientation (§53.1); ls-time box in shipped CSS. ch200 hotfix: quoted headline/disclaimer/post now in news-digest ×2 + official-post ×1 (§54.1).

**Builder:** `book/build_epub_v44.py` — OUT is cwd-RELATIVE: run from repo root; epubcheck with the absolute path. epubcheck: `/usr/local/lib/python3.11/dist-packages/jdk4py/java-runtime/bin/java -jar /usr/local/lib/python3.11/dist-packages/epubcheck/epubcheck.jar`.

**Raws:** 76 files in `raw/` (ch121–130, 135–200).

**Next (V45, awaiting raws ch201+):**
1. FIRST TOOL CALL: archive every new raw + ？ counts + mixed-language leak scan (§51.2); print the ？-ledger from the FILES (§52.2).
2. Deep scan + deep thinking; chats per §53.1; quoted display material into display blocks per §54.1 (【】 = signal); unnamed prophecies (§53.5); anonymized names stay anonymized (§53.6); sweep for `-ssi` after wrap (§53.3).
3. NEW chapter files are FULL standalone XHTML before wrap/audit (§52.1); after ANY edit_file on wrapped chapters re-derive old_text from the CURRENT file + re-parse XML + check the tail (§54.2).
4. WRITTEN block plan → draft → wrap → audit → two-way ？ reconciliation → post-draft raw re-read.
5. Register navPoints; sed-clone builder v45; build FROM REPO ROOT; epubcheck absolute; battery incl. chat-coherence (§53.2) + framed-residue sweep (§54.1) + planned-vs-shipped + ls-time-in-CSS; pre-package deep scan (missing blocks AND ？); rm old epub; worklog §93 / SKILL §55 / this section; commit + push; present_file.
