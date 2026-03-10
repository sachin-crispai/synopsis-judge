# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

**synopsis-judge** — Automates ACM science fair synopsis judging: ingestion, rubric scoring, ranking, and report generation.

## Commands

```bash
uv sync                                   # Install / sync dependencies
uv add <package>                          # Add a dependency
uv run uvicorn server.app:app --reload   # Start dev server (localhost:8000)
PYTHONPATH=. uv run pytest tests/ -v     # Run all tests
PYTHONPATH=. uv run pytest tests/test_scoring.py::test_name -v  # Single test
uv run python -m scripts.<script>        # Run a utility script
```

## Architecture

```
synopsis-judge/
├── server/
│   ├── app.py               # FastAPI app (REST endpoints)
│   └── environment.py       # Core judging logic
├── src/
│   ├── models.py            # Pydantic dataclasses (Submission, Score, Rubric, Report)
│   ├── scorer.py            # Scoring engine (rubric evaluation)
│   ├── ingester.py          # Submission ingestion (PDF / JSON)
│   └── ranker.py            # Ranking and aggregation
├── scripts/                 # One-off CLI utilities
├── tests/                   # pytest suite (asyncio_mode = auto)
├── docs/                    # Product docs, rubric specs
├── openenv.yaml             # Environment manifest
└── pyproject.toml
```

**Data flow:** Submission → Ingest → Score (per rubric criterion) → Aggregate → Rank → Report

## Key Conventions

- **Package manager:** `uv` only — never pip directly
- **Type hints:** Full annotations everywhere; `str | None` union syntax
- **Models:** `@dataclass` or Pydantic `BaseModel` for all structured data
- **Async:** All server handlers and I/O are `async def`
- **Commits:** Conventional commits (`feat:`, `fix:`, `docs:`) + `Fixes #N`
- **Branches:** `feat/<name>`, `fix/<name>` off `main`

## New Contributor Sequence

1. Read `AGENTS.md` → `CLAUDE.md` → `README.md`
2. `gh issue list` to find open work; `gh pr list` for active PRs
3. `git log --oneline -20` for recent context
4. `PYTHONPATH=. uv run pytest tests/ -v` — all tests must pass before PR
