#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path

from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
INDEX_CSV = ROOT / "docs/judging/sachin_n/index/assigned_projects.csv"
PROJECTS_DIR = ROOT / "docs/judging/sachin_n/projects"
REDBOOK = ROOT / "docs/judging/sachin_n/REDBOOK.md"
ONE_LINE_DESCRIPTIONS = {
    "H35": "Speeds up discrete solver decisions using combinatorial game and graph techniques.",
    "E13": "Improves deep optimization stability with a convex directional spline and Huber-regularized loss.",
    "P99": "Studies online learning methods for smooth functions under capped constraints.",
    "R16": "Analyzes Reed-Muller code distance distributions for coding and cryptography applications.",
    "A59": "Uses context-aware ant-colony metaheuristics for dynamic route optimization.",
    "A31": "Builds vision-plus-floor-plan indoor navigation assistance for blind users.",
    "O82": "Develops an AI assistant that turns NBA statistics into interactive analytics answers.",
    "A49": "Proposes a multistep neural pipeline for better cloud-operation anomaly detection.",
    "L92": "Optimizes multi-party barter trading network matching and exchange efficiency.",
    "A73": "Implements real-time UAV-based disaster search and rescue using segmentation and object recognition.",
    "Q38": "Classifies cognitive patterns from speech, drawing, and game-based multimodal signals.",
    "A74": "Applies coverage-guided fuzzing to detect vulnerabilities in zero-knowledge proof systems.",
}


def extract_abstract_excerpt(pdf_path: Path) -> str:
    try:
        text = "\n".join((page.extract_text() or "") for page in PdfReader(str(pdf_path)).pages[:3])
    except Exception:
        return ""
    normalized = re.sub(r"\s+", " ", text).strip()
    if not normalized:
        return ""
    marker = re.search(r"\babstract\b[:\s-]*", normalized, flags=re.IGNORECASE)
    if marker:
        snippet = normalized[marker.end() : marker.end() + 700]
    else:
        snippet = normalized[:700]
    return snippet.strip()


def first_pdf(dir_path: Path) -> Path | None:
    files = sorted(dir_path.glob("*.pdf"))
    return files[0] if files else None


def build() -> None:
    rows = list(csv.DictReader(INDEX_CSV.open()))
    lines: list[str] = []
    lines.append("# Sachin N. Redbook - Synopsys Championship 2026")
    lines.append("")
    lines.append("Lexical tag-ordered judging list keyed by project code.")
    lines.append("")
    lines.append("## Quick Open")
    lines.append("")
    lines.append("```bash")
    lines.append("./scripts/skim.sh A31")
    lines.append("./scripts/judge_open.sh A31")
    lines.append("```")
    lines.append("")
    lines.append("## Table of Contents")
    lines.append("")
    lines.append("| # | Code | Date | One-line Description |")
    lines.append("|---|---|---|---|")
    for row in rows:
        order = int(row["order"])
        code = row["project_code"]
        desc = ONE_LINE_DESCRIPTIONS.get(code, row["title"])
        lines.append(f"| {order:02d} | {code} | {row['date']} | {desc} |")
    lines.append("")
    lines.append("## Projects")
    lines.append("")

    for row in rows:
        order = int(row["order"])
        code = row["project_code"]
        folder = PROJECTS_DIR / f"{order:02d}_{code}"
        abstract_pdf = first_pdf(folder / "abstract")
        project_pdf = first_pdf(folder / "pdfs")
        candidate = abstract_pdf or project_pdf
        excerpt = extract_abstract_excerpt(candidate) if candidate else ""

        lines.append(f"### {order:02d}. {code} - {row['title']}")
        lines.append("")
        lines.append(f"- Date: {row['date']}")
        lines.append(f"- Division: {row['division']}")
        lines.append(f"- Category: {row['category']}")
        lines.append(f"- Drive Folder: {row['drive_folder_url']}")
        lines.append(f"- Notes: `docs/judging/sachin_n/projects/{order:02d}_{code}/notes.md`")
        lines.append(f"- Poster Photos: `docs/judging/sachin_n/projects/{order:02d}_{code}/poster_photos/`")
        lines.append(f"- Abstract Folder: `docs/judging/sachin_n/projects/{order:02d}_{code}/abstract/`")
        lines.append(f"- PDFs Folder: `docs/judging/sachin_n/projects/{order:02d}_{code}/pdfs/`")
        if excerpt:
            lines.append("")
            lines.append("Abstract excerpt:")
            lines.append(f"> {excerpt}")
        lines.append("")

    REDBOOK.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
