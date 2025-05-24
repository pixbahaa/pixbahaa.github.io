#!/usr/bin/env bash
set -euo pipefail

# 1) where the remote TUI lives:
SCRIPT_URL="https://pixbahaa.github.io/pix.py"

# 2) grab it into a temp file
TMP="$(mktemp /tmp/stripttui.XXXX.py)"
trap 'rm -f "$TMP"' EXIT
curl -fsSL "$SCRIPT_URL" -o "$TMP"
chmod +x "$TMP"

# 3) exec into it, redirecting std{in,out,err} to your tty
exec python3 "$TMP" < /dev/tty > /dev/tty 2> /dev/tty
