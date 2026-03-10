# synopsis-judge

**Automate ACM synopsis science fair judging** — scoring, evaluation, and ranking for student project submissions.

## What It Does

- Ingest student synopsis submissions (PDF / structured form)
- Score each submission against configurable rubrics
- Rank projects by category and overall
- Generate judge reports and shortlists
- Support multi-judge workflows with score aggregation

## Quick Start

```bash
# Install dependencies
uv sync

# Run the server
uv run uvicorn server.app:app --reload

# Run tests
PYTHONPATH=. uv run pytest tests/ -v
```

## Stack

- **Python 3.13+** · **uv** · **FastAPI** · **Pydantic v2**

## Docs

- [CLAUDE.md](CLAUDE.md) — AI agent guidance
- [AGENTS.md](AGENTS.md) — Multi-agent collaboration
- [CONTRIBUTING.md](CONTRIBUTING.md) — Contribution guidelines
