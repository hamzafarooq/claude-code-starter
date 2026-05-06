#!/usr/bin/env bash
# Idempotent setup for the competitor-research workshop.
# Runs on every Claude Code session start; exits fast if everything is in place.
# Wired up via .claude/settings.json (SessionStart hook).

set -e

# Detect Playwright cache directory across platforms
case "$OSTYPE" in
  darwin*)  CACHE_DIR="$HOME/Library/Caches/ms-playwright" ;;
  linux*)   CACHE_DIR="$HOME/.cache/ms-playwright" ;;
  msys*|cygwin*|win32) CACHE_DIR="$LOCALAPPDATA/ms-playwright" ;;
  *)        CACHE_DIR="$HOME/.cache/ms-playwright" ;;
esac

# Fast path: Chromium already installed → exit silently
if compgen -G "$CACHE_DIR/chromium-*" > /dev/null 2>&1; then
  exit 0
fi

# Slow path: first run, install Chromium
echo "──────────────────────────────────────────────────────────────"
echo "  First-time setup: installing Playwright Chromium (~165 MB)"
echo "  This runs once per machine. Subsequent sessions skip this."
echo "──────────────────────────────────────────────────────────────"

if ! command -v npx > /dev/null 2>&1; then
  echo "Error: npx not found. Install Node.js from https://nodejs.org first." >&2
  exit 1
fi

npx playwright install chromium

echo "✓ Playwright setup complete."
