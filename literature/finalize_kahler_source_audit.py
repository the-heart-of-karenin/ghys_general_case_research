"""Record inspected source pages and verify their on-disk hashes."""
import hashlib
import json
from pathlib import Path

root = Path(__file__).resolve().parent
pages_path = root / "kahler_rendered_pages.json"
pages = json.loads(pages_path.read_text(encoding="utf-8"))
for item in pages:
    assert Path(item["source"]).is_file()
    assert Path(item["preview"]).is_file()
    item["visually_inspected"] = True
    if Path(item["source"]).name.startswith("17_") and item["page"] == 2:
        item["scope_note"] = "Overview page; decomposition Theorem 1 is PDF page 5."
    if Path(item["source"]).name.startswith("01_Ghys") and item["page"] == 2:
        item["scope_note"] = "Subsequent theorem page; surface Theorem A is PDF page 1."
pages_path.write_text(json.dumps(pages, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

new_sources_path = root / "kahler_source_verification.json"
sources = json.loads(new_sources_path.read_text(encoding="utf-8"))
for entry in sources:
    path = root / entry["filename"]
    assert path.read_bytes().startswith(b"%PDF")
    assert hashlib.sha256(path.read_bytes()).hexdigest() == entry["sha256"]
    entry["visually_inspected_pdf_pages"] = sorted({
        page["page"] for page in pages if Path(page["source"]).name == entry["filename"]})
    entry["reading_scope"] = "Selected theorem, hypothesis, or formula pages; not full-paper proof audit."
new_sources_path.write_text(json.dumps(sources, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
by_name = {entry["filename"]: entry for entry in sources}
for index, entry in enumerate(manifest):
    if entry["filename"] in by_name:
        manifest[index] = by_name[entry["filename"]]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"new_PDF_hashes_verified": len(sources),
                  "inspected_source_pages_recorded": len(pages),
                  "total_PDFs": len(list(root.glob("*.pdf")))}, indent=2))
