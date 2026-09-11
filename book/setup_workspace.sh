#!/usr/bin/env bash
# setup_workspace.sh — idempotent session bootstrap for the Seoul EPUB project.
# Run once at the start of any fresh sandbox/session. Safe to re-run.
#
# What it does:
#   1. Verifies the repo checkout (AI_Storage) is present and on the arena branch.
#   2. Recreates the legacy-path symlink farm at /home/user so every path hard-coded
#      in the build/fix scripts (e.g. /home/user/work/epub_src, /home/user/raw,
#      /home/user/work/payload40.json) resolves into the repo.
#   3. Reinstalls the epubcheck toolchain (jdk4py JRE + epubcheck jar via pip),
#      since neither /tmp nor pip site-packages persist between sandboxes.
#   4. Smoke-tests: epub_src integrity + epubcheck on the latest .epub if asked.
set -euo pipefail

REPO="/home/user/AI_Storage"

echo "== 1. repo check =="
cd "$REPO"
git rev-parse --is-inside-work-tree >/dev/null && echo "   repo OK: $(git rev-parse --short HEAD) on $(git rev-parse --abbrev-ref HEAD)"

echo "== 2. legacy-path symlinks =="
for d in work raw book; do
  ln -sfn "$REPO/$d" "/home/user/$d"
  echo "   /home/user/$d -> $REPO/$d"
done

echo "== 3. epub_src present? =="
if [ -f "$REPO/work/epub_src/mimetype" ]; then
  echo "   work/epub_src: $(find "$REPO/work/epub_src" -type f | wc -l) files — OK"
else
  echo "   MISSING — re-extract: cd /tmp && unzip -o -q '$REPO'/*.epub -d x && mv x '$REPO/work/epub_src'"
fi

echo "== 4. epubcheck toolchain (pip: jdk4py + epubcheck) =="
if python3 -c "import jdk4py, epubcheck" 2>/dev/null; then
  echo "   already installed"
else
  pip3 install --break-system-packages --quiet jdk4py epubcheck
  echo "   installed"
fi
JDK_JAVA=$(python3 -c "import jdk4py; print(jdk4py.JAVA)")
JDK_JAR=$(python3 -c "import epubcheck, os; print(os.path.join(os.path.dirname(epubcheck.__file__), 'epubcheck.jar'))")
echo "   java : $JDK_JAVA"
echo "   jar  : $JDK_JAR"

if [ "${1:-}" = "--validate" ]; then
  echo "== 5. epubcheck on latest epub =="
  EPUB=$(ls -t "$REPO"/Seoul_Starting_With_Debt_Collection__Version_*.epub | head -1)
  "$JDK_JAVA" -jar "$JDK_JAR" "$EPUB" | tail -3
fi

echo "== done =="
