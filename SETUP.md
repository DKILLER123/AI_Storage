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

## 6. State & next steps (from worklog §111)

**SHIPPED: V62 = chapters 235–236 (the launch that emptied to its tester sticks / chocolate for the overtime roundup) + the 'Legends Never Die' correction applied book-wide (raw-verbatim law).** epubcheck valid 0 messages; battery = exact 4-file sha1 delta + 2 new chapters; only the V62 epub on disk (22,958,352 B, 395 entries).

**V63 (next batch) checklist:**
1. Sandbox pre-flight (§66.4): symlink + pip epubcheck jdk4py + `ln -sf $(python3 -c 'import jdk4py;print(jdk4py.JAVA)') /usr/local/bin/java`; rolled-back `.git` → fetch + `git reset --soft origin/arena/01a08c66-ai-storage` (§55.1).
2. Save raws FIRST (ch237+); ？-ledger THREE numbers, line-by-line (§72.4); 【】 inventory → block routing (§71.5/§72.5).
3. Canon: 'Legends Never Die' canonical (demo session with IU beginning); 'Sado' campaign live (press conference within days); LAVUE sold out ×2 with factory-vlog next; Kim Ji-min PLAIN (never bare "Ji-min"); Yoon Hye-ja = the professor, carded; 'Uchiage Hanabi' register.
4. Drafts: block ledger BEFORE writing; NO hand-anchors inside any block — the battery strips them anyway (§71.1); tv-screen for broadcast/video playback; anchor pre-flight (§72.3).
5. Wrap with EXPLICIT argv; minidom gate; anchors-in-blocks = 0; invented-class audit = 0.
6. Builder: clone build_epub_v62.py, EXPLICIT replaces, run from repo root.
7. epubcheck 0 messages; battery via sha1 diff — assert delta = opf/ncx/nav + new chapters (+ owed repairs). Baselines: anchors 13,973 / peek 13,815; ls 552 / sv 290 / pq 132 / ckl 56 / pc 107 / mail 13 / comment-item 626 / tv-screen 8; images 128; cards/modals 88/88; Han/fw/【】 0; front-matter Hangul 241.
8. Pre-package deep scan: ？ marks+lines+doubles from artifact; 20+ spot probes; doubled-word scan; OOPS residual; peek parity; misattr sweep.
9. Delete previous epub AFTER validation; worklog/SKILL/SETUP updates; commit + push; present_file.
