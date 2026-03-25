#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
RAW_DIR="$ROOT_DIR/data/raw"

mkdir -p "$RAW_DIR"

echo "[INFO] Raw data directory ready at: $RAW_DIR"
echo "[INFO] Put manually downloaded WhatsApp files here."
echo "[INFO] No automatic rename step is performed yet, by design."
