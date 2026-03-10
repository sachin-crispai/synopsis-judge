# AGENTS.md — Multi-Agent Collaboration Guide

## Quick Start Sequence

1. Read `AGENTS.md` (this file)
2. Read `CLAUDE.md` for architecture + commands
3. Read `README.md` for project overview
4. `gh issue list` — pick unassigned work
5. `gh pr list` — check what's in flight to avoid conflicts
6. `git log --oneline -20` — recent commit context
7. `PYTHONPATH=. uv run pytest tests/ -v` — confirm green baseline

## Architecture Highlights

- **Single environment, deterministic scoring** — rubric weights and criteria are versioned in `docs/rubric.yaml`
- **Stateless scoring** — each submission scored independently; no shared mutable state
- **Multi-judge aggregation** — scores from multiple judges merged via configurable strategy (mean, median, trimmed mean)

## Collaboration Standards

- One issue per logical change; reference with `Fixes #N` in commit and PR
- PR requires: summary, files changed with reasoning, test output
- Do not modify rubric weights without a docs PR updating `docs/rubric.yaml`
- Never commit `.env` or any file containing API keys

## Build & Test

```bash
uv sync
PYTHONPATH=. uv run pytest tests/ -v
uv run uvicorn server.app:app --reload
```
