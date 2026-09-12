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

## 6. State & next steps (from worklog §109)

**SHIPPED: V60 = chapters 231–232 (corny pickup lines accepted / the invisible ex invades the marriage) + USER LAW: zero character anchors inside ANY style block (book-wide purge of 70; battery = 0; wrap script block-guarded) + ls spacing fix (explicit margins, flex-gap retired as sole rhythm).** epubcheck valid 0 messages; battery = exact 22-entry sha1 delta vs V59; only the V60 epub on disk (22,917,611 B, 391 entries).

**V61 (next batch) checklist:**
1. Sandbox pre-flight (§66.4): symlink + pip epubcheck jdk4py + `ln -sf $(python3 -c 'import jdk4py;print(jdk4py.JAVA)') /usr/local/bin/java`; rolled-back `.git` → fetch + `git reset --soft origin/arena/01a08c66-ai-storage` (§55.1).
2. Save raws FIRST (ch233+); ？-ledger THREE numbers (§69.1); 【】 inventory (nds/captions/comments/mail/slogans all route to blocks per §71.5); narration ？ counts too (§71.6).
3. Canon: 'We Got Married' arc live (Yook Sung-jae PLAIN); 'Jumpshot' (Feat. IRENE) secret out to the dorm; Holy Mother church arc opening (Kim Hye-soo plain); Jung Jae-joon / Hwang Soo-ah anchored in prose ONLY (§71.1).
4. Drafts: block ledger BEFORE writing; pc-them for two-sided calls (§71.4); NO anchors in any block (§71.1); repair regexes from actual bytes (§70.4); MORE blocks — fill thin context from deep thinking.
5. Wrap with EXPLICIT argv (block-guarded script §71.2); minidom re-parse gate (§69.4); anchors-in-blocks battery = 0 before packaging.
6. Builder: clone build_epub_v60.py, EXPLICIT replaces, run from repo root.
7. epubcheck 0 messages; battery via sha1 diff (§70.5) — assert delta = opf/ncx/nav + stylesheet (only if owed) + new chapters (+ owed repairs). Baselines: anchors 13,790; peek 13,632; ls 542 / sv 277 / pq 122 / ckl 48 / pc 102 / mail 11; images 128; cards/modals 88/88; Han/fw/【】 0; front-matter Hangul 241.
8. Pre-package deep scan: ？ marks+lines+doubles from artifact; 20+ spot probes; doubled-word scan; OOPS residual; peek parity; misattr sweep.
9. Delete previous epub AFTER validation; worklog/SKILL/SETUP updates; commit + push; present_file.
