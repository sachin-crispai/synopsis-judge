#!/usr/bin/env python3
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
raw_dir = root / "data" / "raw"
docs_path = root / "data" / "manifests" / "documents.json"

docs = json.loads(docs_path.read_text(encoding="utf-8"))
expected = [d["filename"] for d in docs if d["kind"] == "whatsapp_attachment"]

present = {p.name for p in raw_dir.iterdir() if p.is_file()}
missing = [name for name in expected if name not in present]

print("Expected WhatsApp attachment files:", len(expected))
print("Present in data/raw:", len(expected) - len(missing))
print("Missing:", len(missing))

if missing:
    print("\nMissing files:")
    for name in missing:
        print("-", name)
else:
    print("\nAll expected WhatsApp attachment filenames are present.")
