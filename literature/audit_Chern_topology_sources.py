"""Finalize the manually inspected primary-source audit for notes 31-34."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
pages_path = root / "Chern_topology_rendered_pages.json"
pages = json.loads(pages_path.read_text(encoding="utf-8"))
for page in pages:
    assert Path(page["source"]).is_file() and Path(page["preview"]).is_file()
    page["visually_inspected"] = True
pages_path.write_text(json.dumps(pages, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

source_path = root / "Chern_topology_source_verification.json"
entries = json.loads(source_path.read_text(encoding="utf-8"))
for entry in entries:
    path = root / entry["filename"]
    assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    entry["visually_inspected_pdf_pages"] = sorted({page["page"] for page in pages
        if Path(page["source"]).name == entry["filename"]})
    entry["reading_scope"] = "Only the cited theorem, premise and formula pages; not a whole-paper proof audit."
source_path.write_text(json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
by_name = {entry["filename"]: entry for entry in entries}
manifest = [by_name.get(entry["filename"], entry) for entry in manifest]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"new_source_hashes_verified": len(entries), "inspected_pages": len(pages),
                  "PDF_files": len(list(root.glob("*.pdf"))), "manifest_entries": len(manifest)}))
