#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 <PROJECT_CODE>" >&2
  exit 1
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
CODE="$(echo "$1" | tr '[:lower:]' '[:upper:]')"
BASE="$ROOT_DIR/docs/judging/sachin_n/projects"

project_dir="$(find "$BASE" -maxdepth 1 -type d -name "*_${CODE}" | head -n 1 || true)"
if [[ -z "${project_dir}" ]]; then
  echo "No project folder found for code ${CODE}" >&2
  exit 1
fi

pick_pdf() {
  local dir="$1"
  find "$dir" -type f \( -iname "*.pdf" \) | sort | head -n 1 || true
}

pdf_path="$(pick_pdf "$project_dir/abstract")"
if [[ -z "${pdf_path}" ]]; then
  pdf_path="$(pick_pdf "$project_dir/pdfs")"
fi
if [[ -z "${pdf_path}" ]]; then
  pdf_path="$(pick_pdf "$project_dir")"
fi

if [[ -z "${pdf_path}" ]]; then
  echo "No PDF found for ${CODE}. Download files first with scripts/download_sachin_projects.py" >&2
  exit 1
fi

open -a Skim "$pdf_path"
echo "Opened in Skim: $pdf_path"
