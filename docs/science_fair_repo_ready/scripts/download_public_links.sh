#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
OUT_DIR="$ROOT_DIR/downloads"
MANIFEST="$ROOT_DIR/data/manifests/links.csv"

mkdir -p "$OUT_DIR"

echo "[INFO] Download target: $OUT_DIR"
echo "[INFO] Using manifest: $MANIFEST"
echo "[WARN] Google Drive and Google Meet links may not download cleanly via wget without browser auth."
echo "[WARN] WhatsApp attachments are not included because the chat context did not expose attachment URLs."

tail -n +2 "$MANIFEST" | while IFS=, read -r id title category url source access_notes; do
  if [ -z "${url:-}" ]; then
    continue
  fi
  echo "[INFO] Attempting $id -> $url"
  wget --content-disposition --trust-server-names --no-verbose -P "$OUT_DIR" "$url" || true
done

echo "[INFO] Download pass complete."
