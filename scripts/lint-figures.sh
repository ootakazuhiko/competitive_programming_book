#!/usr/bin/env bash
set -euo pipefail

# Lint to prevent panels/figures being wrapped inside code fences.
# Checks only changed Markdown files in PRs (diff against BASE_SHA if provided).

BASE_REF=${BASE_SHA:-}

if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  :
else
  echo "error: not inside a git repo" >&2
  exit 2
fi

if [[ -n "${BASE_REF}" ]]; then
  CHANGED=$(git diff --name-only "${BASE_REF}...HEAD" -- 'src/**/*.md' || true)
else
  # Fallback: compare with origin/main if available
  git fetch origin main >/dev/null 2>&1 || true
  CHANGED=$(git diff --name-only origin/main...HEAD -- 'src/**/*.md' || true)
fi

if [[ -z "${CHANGED}" ]]; then
  echo "lint-figures: no changed markdown files; skipping"
  exit 0
fi

echo "lint-figures: checking files:" $CHANGED | tr '\n' ' ' | sed 's/  */ /g'

FAILED=0

check_file() {
  local f="$1"
  # 1) Standalone ``` directly before/after figure/panel include or label
  #    This often disables Liquid includes and wraps content in <pre>.
  #    We search for lines that are exactly ``` where the next non-empty line
  #    starts with one of the suspicious markers.
  local bad1
  bad1=$(awk '
    function ltrim(s){ sub(/^\s+/, "", s); return s }
    function print_line(){ printf("%s:%d:%s\n", FILENAME, NR, $0) }
    {
      line=$0
      if (line ~ /^```\s*$/) {
        # peek ahead for next non-empty
        for(i=1;i<=5;i++){
          if (getline nextl <= 0) break
          if (nextl ~ /[^[:space:]]/) { break }
        }
        nextl=ltrim(nextl)
        if (nextl ~ /^(【図|\{%\s*include|<figure|!\[図)/) {
          print_line()
        }
        # push back not supported; accept limited lookahead
      }
    }
  ' "$f" || true)

  # 2) Unbalanced code fences (odd count of lines starting with ```)
  local fence_count
  fence_count=$(grep -E "^```" -c "$f" || true)
  local bad2=""
  if [[ $(( fence_count % 2 )) -ne 0 ]]; then
    bad2="$f:0:unbalanced code fences (count=$fence_count)"
  fi

  if [[ -n "$bad1" || -n "$bad2" ]]; then
    echo "lint-figures: violations in $f" >&2
    [[ -n "$bad1" ]] && echo "$bad1" >&2
    [[ -n "$bad2" ]] && echo "$bad2" >&2
    FAILED=1
  fi
}

for f in $CHANGED; do
  [[ -f "$f" ]] || continue
  check_file "$f"
done

if [[ $FAILED -ne 0 ]]; then
  echo "lint-figures: found violations. Please remove stray ``` around figures/panels or balance fences." >&2
  exit 1
fi

echo "lint-figures: OK"
exit 0

