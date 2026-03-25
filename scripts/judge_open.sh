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

"$ROOT_DIR/scripts/skim_abstract.sh" "$CODE"
open "$project_dir/notes.md"
echo "Opened judge workspace: $project_dir"
