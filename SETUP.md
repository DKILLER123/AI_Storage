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

## 6. State & next steps (from worklog §108)

**SHIPPED: V59 = chapters 229–230 (the Red Bebe set-visit day / the loophole ruling) + the user-flagged ch227 pq-wrapper bug FIXED + Kim Eun-sook / Baek Ji-young / 'Like Being Hit by a Bullet' / 'Lovers in Paris' / 'Secret Garden' / 'A Gentleman's Dignity' / "sasaeng" canonized.** epubcheck valid 0 messages; battery = exact 6-file sha1 delta vs V58; only the V59 epub on disk (22,894,421 B, 389 entries).

**V60 (next batch) checklist:**
1. Sandbox pre-flight (§66.4): symlink + pip epubcheck jdk4py + `ln -sf $(python3 -c 'import jdk4py;print(jdk4py.JAVA)') /usr/local/bin/java`; rolled-back `.git` → fetch + `git reset --soft origin/arena/01a08c66-ai-storage` (§55.1).
2. Save raws FIRST (ch231+); ？-ledger with THREE numbers (marks / lines / double-mark positions — §69.1); 【】 inventory before prose.
3. Canon greps before drafting: 'The Three Evils' / 'Like Being Hit by a Bullet' / "Red-eh Beh-beh" now canonical; RV five short forms; Wendy = Son Seung-wan in narration + "Wendy." soft call; Kim Eun-sook OST thread continues (Seung-wan audition arc); Yook Sung-jae card pipeline if he recurs (§61.5).
4. Drafts: block ledger BEFORE writing; wrap pass with EXPLICIT argv (§70.2 — the script defaults to ch171/172); pq trios inside div.pullquote, battery 0 bare (§70.1); display rows anchor-exempt (§70.3); pc blocks quote only the raw's quoted side (§69.3); repair regexes from the actual bytes (§70.4).
5. Post-wrap: minidom re-parse BOTH files immediately (§69.4 hard gate), then registration (ncx np-235/np-236 playOrder 236 next batch).
6. Builder: clone build_epub_v59.py, EXPLICIT replaces, run from repo root.
7. epubcheck 0 messages; battery: prefer the artifact-to-artifact sha1 diff (§70.5) — exact delta = opf/ncx/nav + 2 new chapters (+ any owed repairs), everything else byte-identical. Anchors 13,691+δ; ls 535 / sv 274 / pq 119 / pc 100 / chat 150 / ckl 43 / mail 10 / naver-search 12 / search-bar 1; images 128; cards/modals 88/88; Han/fullwidth/【】 0 in chapters; front-matter Hangul 241 identical; ？ targets = the new raws' ledgers (marks AND lines AND doubles).
8. Pre-package deep scan: spot checks 20/20, misattr sweep, doubled-word scan, OOPS residual, peek parity, framed sweep, chat-coherence (silent-owner §67.4).
9. Delete previous epub AFTER validation; worklog/SKILL/SETUP updates; commit + push; present_file.
