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

## 6. State & next steps (from worklog §105)

**SHIPPED: V56 = chapters 223–224 + bookwide short-name migration (Seulgi ×42 / Wendy ×78) + V55 defect fixes (forescen, ch222 money ×4, OOPS/Oops unify, ch221 email no-op).** epubcheck valid 0 messages; battery ALL GREEN; only the V56 epub on disk.

**V57 (next batch) checklist:**
1. Sandbox pre-flight (§66.4): `ln -s /home/user/AI_Storage/work /home/user/work` + `pip install --break-system-packages epubcheck jdk4py` BEFORE building; if `.git` was rolled back, fetch the branch ref first and `git reset --soft origin/arena/01a08c66-ai-storage` (§55.1) — never commit from a stale base.
2. Save raws FIRST (§57.1); re-verify every write_file; ？-ledger from raw BEFORE prose (line-numbered, incl. 「嗯？」/「这位？」-class marks); 【】 inventory → conversion plan (chat per §66.2, comments per comment-thread, lyrics per canon).
3. Canon greps before drafting: near-name trap (§64.2); RV five = **Seulgi / Wendy / Irene / Joy / Yeri — short forms, never hyphenated (§67.1)**; full names (Kang Seul-gi, Son Seung-wan) untouched; quoted stage names per §66.3; sunbae shapes ("Baek sunbae" two-word; bare "sunbae" direct); OOPS/Oops mirror-the-raw law (§67.2).
4. Real-person check BEFORE any portrait (§65.1); identity-check every search panel; composites get cropped.
5. Drafts: one raw paragraph order; block ledger BEFORE writing; charts = `.naver-search` (§66.1); ckl for cost stacks/slates/skeletons; sv for process/timing/imagery; comment-thread for reader comments (ch215 shape).
6. ？-walker + per-line map on ANY diff (§58.2); close the loop from the BUILT EPUB, not the source (§62.1 head-title included).
7. Wrap (+ FORMS check first — §57.6); post-wrap peek strip in ALL blocks (§63.1/§61.1 exhaustive tuple); in-text debut cards byte-identical to intro page (§64.1).
8. Registration: opf manifest+spine, nav li, ncx np-229/np-230 playOrder 230 next batch; image items for any new portraits.
9. Builder: clone build_epub_v56.py, EXPLICIT replaces, run from repo root.
10. epubcheck 0 messages; battery vs V56 baseline (derive from BOTH artifacts, state the method — §67.3): entries 383+δ, chapters 224+2n, spine/navPoints 228+2n, nav chapter li 224+2n, images 128+n³, cards/modals 88+m³, in-text 82+m³; anchors 12,957+δ; ls520/sv259/pq115/pc99/chat147/ckl26/comment104/mail8/naver-search12/search-bar1; misattr 0; chat-coherence flags triaged (silent-owner pattern §67.4); PEEK 0; Han/fullwidth/【】 0.
11. Pre-package deep scan (§54.1 paragraph-scoped) + typo battery (exclude self-closing p/ §67.5) + chat audit + chart-class audit + OOPS residual grep.
12. Delete previous epub AFTER validation; worklog/SKILL/SETUP updates; commit + push; present_file.
