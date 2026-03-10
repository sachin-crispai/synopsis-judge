#!/usr/bin/env python3
from __future__ import annotations

import csv
import shutil
from pathlib import Path

import gdown


ROOT = Path(__file__).resolve().parents[1]
INDEX_CSV = ROOT / "docs/judging/sachin_n/index/assigned_projects.csv"
PROJECTS_DIR = ROOT / "docs/judging/sachin_n/projects"


def detect_subfolder_name(file_name: str) -> str:
    name = file_name.lower()
    if "abstract" in name or "synopsis" in name:
        return "abstract"
    return "pdfs"


def main() -> None:
    rows = list(csv.DictReader(INDEX_CSV.open()))
    for row in rows:
        order = int(row["order"])
        code = row["project_code"]
        url = row["drive_folder_url"]
        project_dir = PROJECTS_DIR / f"{order:02d}_{code}"
        temp_dir = project_dir / "_download_tmp"
        temp_dir.mkdir(parents=True, exist_ok=True)

        print(f"Downloading {code} from {url}")
        gdown.download_folder(url=url, output=str(temp_dir), quiet=False, use_cookies=False, remaining_ok=True)

        for item in sorted(temp_dir.rglob("*")):
            if not item.is_file():
                continue
            dest_subfolder = detect_subfolder_name(item.name)
            dest_dir = project_dir / dest_subfolder
            dest_dir.mkdir(parents=True, exist_ok=True)
            dest_path = dest_dir / item.name
            shutil.move(str(item), str(dest_path))
        shutil.rmtree(temp_dir, ignore_errors=True)
        print(f"Completed {code}")


if __name__ == "__main__":
    main()
