# Contributing

## Workflow

1. Pick an issue from `gh issue list`
2. Create a branch: `git checkout -b feat/<name>` or `fix/<name>`
3. Make changes; commit with conventional style: `feat: add rubric loader`
4. Include `Fixes #N` in commit message
5. Open PR using the template: `gh pr create`
6. Ensure `PYTHONPATH=. uv run pytest tests/ -v` passes

## Commit Style

```
feat: short description

Longer explanation if needed.

Fixes #12
Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`
