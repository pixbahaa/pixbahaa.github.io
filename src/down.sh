#!/bin/sh

# Set URL of the Python script
SCRIPT_URL="https://pixbahaa.github.io/pix.py"

# Create a temp file for the downloaded Python script
TMP_FILE="$(mktemp /tmp/pix.XXXXXX.py)"

# Ensure cleanup on exit
cleanup() {
    rm -f "$TMP_FILE"
}
trap cleanup EXIT

# Download the script
curl -fsSL "$SCRIPT_URL" -o "$TMP_FILE"
chmod +x "$TMP_FILE"

# Run the script with terminal I/O reattached
exec python3 "$TMP_FILE" < /dev/tty > /dev/tty 2> /dev/tty
