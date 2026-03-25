# Sachin N. Judging Workspace

Use project code as the canonical tag (for example `H35`).

## Quick Commands

```bash
# Show lexical tag queue
python3 scripts/judge_queue.py

# Open abstract in Skim
./scripts/skim.sh A31

# Open abstract in Skim + notes file
./scripts/judge_open.sh A31

# Re-download all assigned project files from Drive folders
uv run --with gdown python scripts/download_sachin_projects.py

# Rebuild redbook with abstract excerpts
uv run --with pypdf python scripts/build_sachin_redbook.py
```

## Key Files

- `docs/judging/sachin_n/index/assigned_projects.csv`:
  Lexical tag-ordered source of truth for all assigned projects and local file paths.
- `docs/judging/sachin_n/REDBOOK.md`:
  Combined lexical tag-ordered judge redbook.
- `docs/judging/sachin_n/projects/<NN_CODE>/poster_photos/`:
  Put poster/interview photos here.
- `docs/judging/sachin_n/projects/<NN_CODE>/notes.md`:
  Free-form notes for rubric/interview/final comments.
- `docs/judging/sachin_n/projects/<NN_CODE>/rubric_scores.yaml`:
  Structured scoring placeholders.
