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

## 6. State & next steps (from worklog §95)

**SHIPPED: V47 = chapters 205–206.** epubcheck 0/0/0/0 first pass; epub 21,806,759 B; commit pushed; V46 epub deleted (in git history). Only `Seoul_Starting_With_Debt_Collection__Version_47.epub` on disk.

**Toolchain (reinstall each session):** `bash book/setup_workspace.sh`; then
`git fetch origin arena/01a08c66-ai-storage && git reset -q FETCH_HEAD`; verify `git rev-parse --short HEAD` matches the last pushed commit (§55.1 pre-flight). epubcheck:
`/usr/local/lib/python3.11/dist-packages/jdk4py/java-runtime/bin/java -jar /usr/local/lib/python3.11/dist-packages/epubcheck/epubcheck.jar <ABSOLUTE epub>` — require the literal line "EPUBCheck completed".

**V48 (chapters 207–208) checklist:**
1. Save raws FIRST → `raw/chapter-207.txt`, `raw/chapter-208.txt` + ？-ledger + guard + VERBATIM PROBES on key lines (§57.1).
2. §55.1 pre-flight (HEAD check); canon deep-greps BEFORE drafting; grep FORMS for every expected ensemble name (§57.6).
3. Full standalone XHTML drafts; block ledger from raw display material; RECONCILE drafted block counts against the ledger before wrapping (§57.4).
4. ？-ledger ordered walk (§57.2) → EXACT marks AND lines vs raw (§56.6: statements stay statements).
5. wrap_v29_anchors.py + audit: XML/minidom, undef NONE, imgs-on-disk, CSS classes, CJK, bare &, unbal, framed-plain sweep, residual-plain (scope: classless + dialogue-line, §56.5). Post-wrap patches slice the LIVE file (§57.3).
6. New carded characters: card+modal+portrait+FORMS+re-wrap (§56.3); grep intro page + shipped chapters FIRST (Ed Sheeran/Meghan precedent: off-screen presences stay plain, §57.5).
7. Registration: opf manifest items + spine itemrefs after last chapter + EXPLICIT image `<item>` entries for new portraits (§56.2); nav li ×2 word-form; ncx navPoints np-211/np-212 if next batch.
8. Builder: clone build_epub_v47.py with EXPLICIT replaces (docstring "Version 47" + full OUT filename), run FROM REPO ROOT (§56.1).
9. epubcheck (absolute paths) → 0/0/0/0; in-zip battery vs V47 baseline, same-code deltas (§56.4): entries 357+delta, manifest 354+delta, spine/navPoints 210+2n, nav li 206+2n, images 120+n³, cards/modals 80+m³; ls475/sv186/pc89/pq88/mp32/lb29/chat128/ct111/nv201/hn12; ？0; CJK 20 ch78; ？-parity EXACT for new chapters; ch195 chat-name 8; ls-time box in CSS.
10. Pre-package in-zip deep scan: ？-parity + 【】/framed sweep + raw-vs-EN block coverage (§54.1).
11. Delete previous epub AFTER validation; worklog §96 / SKILL (new rules) / SETUP §6 rewrite; commit + push; present_file.
