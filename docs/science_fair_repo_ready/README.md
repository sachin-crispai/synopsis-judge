# Science Fair 2026 ACM Judges — repo-ready extract

This bundle is structured for direct drop-in use inside a repository.

## Directory layout

```text
science_fair_repo_ready/
├── README.md
├── docs/
│   ├── captured_links.md
│   ├── documents_manifest.md
│   └── repo_notes.md
├── data/
│   ├── manifests/
│   │   ├── links.csv
│   │   ├── links.json
│   │   ├── documents.csv
│   │   ├── documents.json
│   │   └── summary.json
│   └── raw/
├── downloads/
└── scripts/
    ├── download_public_links.sh
    ├── normalize_tree.sh
    └── verify_manifest.py
```

## What this is

A cleaned manifest of links and document references captured from the visible WhatsApp chat context for the
**Science Fair 2026 ACM Judges** group.

## What this is not

This is **not** a full export of WhatsApp attachments.
The WhatsApp page context exposed filenames for inline files, but not the file download URLs or binaries.

## Practical workflow

1. Put this folder in your repository.
2. Run `scripts/download_public_links.sh` to fetch whatever public links are directly retrievable.
3. Manually download the WhatsApp attachments that are listed in `docs/documents_manifest.md`.
4. Place the manually downloaded files into `data/raw/`.
5. Run `python3 scripts/verify_manifest.py` to check what is still missing.

## Summary

- Total captured links: 8
- Total document entries: 13
- WhatsApp attachments lacking direct download URLs: 9

## Constraint

The blocker is structural, not accidental: the supplied WhatsApp page text simply did not contain the underlying
attachment download URLs, so those files could not be auto-fetched into this bundle.
