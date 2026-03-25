# Repo notes

## Recommended git layout

- Keep manifests under `data/manifests/`
- Put manually downloaded binaries under `data/raw/`
- Keep any parsed derivatives under `data/processed/` if you add them later
- Avoid committing large binaries unless the repo is explicitly meant to archive them

## Naming recommendation

When you manually download files from WhatsApp, preserve original names first.
If you later normalize them, keep a mapping table in source control.

## Suggested next engineering step

Once the actual binaries are downloaded, you can:
- hash them
- deduplicate them
- rename them consistently
- extract PDF text / DOCX text into machine-readable derivatives
