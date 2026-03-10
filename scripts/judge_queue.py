#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX_CSV = ROOT / "docs/judging/sachin_n/index/assigned_projects.csv"


def main() -> None:
    rows = list(csv.DictReader(INDEX_CSV.open()))
    print("order\tdate\tcode\tcategory\ttitle")
    for row in rows:
        print(
            f"{row['order']}\t{row['date']}\t{row['project_code']}\t"
            f"{row['category']}\t{row['title']}"
        )


if __name__ == "__main__":
    main()
