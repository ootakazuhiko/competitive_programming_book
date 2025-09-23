#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: ./watch.sh [start|serve|summary|help]

Commands
  start    Start interactive watcher (default)
  serve    Start watcher and Jekyll server (requires bundle exec jekyll)
  summary  Show latest activity log entries
  help     Show this message

The watcher prints changed files (git status --short), writes timestamped
entries to logs/watch.log, and maintains a machine-readable JSON snapshot in
.logs/watch-latest.json for other agents (e.g., PM agent) to consume.
USAGE
}

LOG_DIR="logs"
LOG_FILE="$LOG_DIR/watch.log"
JSON_STATE=".logs/watch-latest.json"
STATE_CACHE=".tmp/watch.last"

mkdir -p "$LOG_DIR" .logs .tmp

append_log() {
  local message="$1"
  printf '[%(%Y-%m-%d %H:%M:%S %z)T] %s\n' -1 "$message" >> "$LOG_FILE"
}

write_json_state() {
  local porcelain="$1"
  local timestamp
  timestamp=$(date --iso-8601=seconds)
  cat > "$JSON_STATE" <<JSON
{
  "timestamp": "${timestamp}",
  "status": "$(printf '%s' "$porcelain" | sed 's/"/\\"/g')"
}
JSON
}

collect_status() {
  git status --porcelain=2 --branch
}

render_dashboard() {
  clear
  printf '=== Watch Dashboard (%s) ===\n' "$(date '+%Y-%m-%d %H:%M:%S')"
  git status --short
  printf '\nRecent log tail:\n'
  tail -n 10 "$LOG_FILE" 2>/dev/null || true
}

watch_loop() {
  append_log "watcher started"
  local porcelain
  porcelain=$(collect_status)
  printf '%s\n' "$porcelain" > "$STATE_CACHE"
  write_json_state "$porcelain"
  render_dashboard
  trap 'append_log "watcher stopped"; exit 0' INT TERM
  local last_status
  last_status=$(git status --porcelain)
  while true; do
    sleep 2
    local current_status
    current_status=$(git status --porcelain)
    if [[ "$current_status" != "$last_status" ]]; then
      append_log "status change detected"
      git status --short >> "$LOG_FILE"
      porcelain=$(collect_status)
      printf '%s\n' "$porcelain" > "$STATE_CACHE"
      write_json_state "$porcelain"
      render_dashboard
      last_status="$current_status"
    fi
  done
}

serve() {
  append_log "jekyll serve requested"
  (bundle exec jekyll serve --livereload 2>&1 | while read -r line; do append_log "jekyll: $line"; done) &
  SERVE_PID=$!
  trap 'kill $SERVE_PID 2>/dev/null || true' EXIT
  watch_loop
}

summary() {
  echo "Log file: $LOG_FILE"
  tail -n 20 "$LOG_FILE" 2>/dev/null || echo "(no log yet)"
  if [[ -f "$JSON_STATE" ]]; then
    echo
    echo "Latest JSON state ($JSON_STATE):"
    cat "$JSON_STATE"
  fi
}

cmd=${1:-start}
case "$cmd" in
  start)
    watch_loop
    ;;
  serve)
    serve
    ;;
  summary)
    summary
    ;;
  help|-h|--help)
    usage
    ;;
  *)
    usage
    exit 1
    ;;
esac
