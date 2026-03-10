# Copilot Instructions

- Package manager is `uv` — never suggest `pip install`
- Python 3.13+; use `str | None` union syntax (not `Optional[str]`)
- All models use `@dataclass` or Pydantic `BaseModel`
- All server handlers and I/O must be `async def`
- Tests live in `tests/`; run with `PYTHONPATH=. uv run pytest tests/ -v`
- Conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`
- Reference issues in commits: `Fixes #N`
