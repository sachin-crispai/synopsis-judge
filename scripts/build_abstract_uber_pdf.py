#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from pathlib import Path

import fitz


ROOT = Path(__file__).resolve().parents[1]
INDEX_CSV = ROOT / "docs/judging/sachin_n/index/assigned_projects.csv"
OUT_DIR = ROOT / "docs/judging/sachin_n/exports"
OUT_FILE = OUT_DIR / "sachin_n_abstracts_uber.pdf"
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


def _shorten(text: str, max_len: int = 82) -> str:
    if len(text) <= max_len:
        return text
    return text[: max_len - 1].rstrip() + "…"


NAME_RE = re.compile(r"^[A-Z][A-Za-z'\-]+(?: [A-Z][A-Za-z'.\-]+){1,2}$")
STOP_PHRASES = (
    "project number",
    "full name of every team member",
    "purpose of",
    "procedure",
    "observations",
    "conclusions",
    "abstract",
    "synopsys",
    "championship",
    "title",
)


def _extract_first_member_name(doc: fitz.Document, title: str) -> str:
    title_low = title.lower()
    for pno in range(min(2, doc.page_count)):
        text = doc[pno].get_text("text")
        for raw in text.splitlines():
            line = raw.replace("•", "").replace("●", "").strip()
            if not line or len(line) > 48:
                continue
            if any(ch.isdigit() for ch in line) or "," in line:
                continue
            low = line.lower()
            if any(phrase in low for phrase in STOP_PHRASES):
                continue
            if low in title_low:
                continue
            if NAME_RE.match(line):
                return line
    return "TBD"


def build() -> Path:
    rows = list(csv.DictReader(INDEX_CSV.open()))
    merged = fitz.open()
    toc_entries: list[tuple[str, str, str, int]] = []

    for row in rows:
        order = row["order"].strip()
        code = row["project_code"].strip().upper()
        abstract_path = ROOT / row["local_abstract_pdf"]
        if not abstract_path.exists():
            print(f"Skipping {code}: missing {abstract_path}")
            continue

        source = fitz.open(str(abstract_path))
        first_member = _extract_first_member_name(source, row["title"].strip())
        start_page = merged.page_count
        merged.insert_pdf(source)
        source.close()
        toc_entries.append(
            (
                order,
                code,
                _shorten(ONE_LINE_DESCRIPTIONS.get(code, row["title"].strip())),
                start_page,
            )
        )

        for page_num in range(start_page, merged.page_count):
            page = merged[page_num]
            rect = page.rect
            summary = ONE_LINE_DESCRIPTIONS.get(code, row["title"].strip())
            footer_line1 = f"{code} | {first_member}"
            footer_line2 = _shorten(summary, 120)
            footer = f"{footer_line1}\n{footer_line2}"
            footer_rect = fitz.Rect(24, rect.height - 44, rect.width - 24, rect.height - 8)
            page.draw_rect(footer_rect, color=None, fill=(1, 1, 1), overlay=True)
            page.insert_textbox(
                footer_rect,
                footer,
                fontsize=7,
                fontname="helv",
                color=(0.29, 0.33, 0.38),
                align=fitz.TEXT_ALIGN_LEFT,
                lineheight=1.05,
            )

    # Insert table-of-contents as page 1 after abstracts are merged.
    toc_page = merged.new_page(pno=0)
    toc_page.insert_text(
        fitz.Point(36, 40),
        "Sachin N. Redbook - Abstracts",
        fontsize=15,
        fontname="helv",
        color=(0.08, 0.08, 0.08),
    )
    toc_page.insert_text(
        fitz.Point(36, 58),
        "Table of Contents (lexical tags; click to open abstract)",
        fontsize=10,
        fontname="helv",
        color=(0.22, 0.22, 0.22),
    )

    y = 84
    line_height = 18
    for order, code, desc, target_page_before_toc in toc_entries:
        line = f"{order}  {code}  {desc}"
        rect = fitz.Rect(36, y - 11, 560, y + 4)
        toc_page.insert_text(
            fitz.Point(36, y),
            line,
            fontsize=10,
            fontname="helv",
            color=(0.0, 0.24, 0.55),
        )
        toc_page.insert_link(
            {
                "kind": fitz.LINK_GOTO,
                "from": rect,
                "page": target_page_before_toc + 1,  # +1 because TOC is inserted at page 0
                "to": fitz.Point(0, 0),
            }
        )
        y += line_height

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    merged.save(str(OUT_FILE), deflate=True)
    merged.close()
    return OUT_FILE


if __name__ == "__main__":
    output = build()
    print(output)
