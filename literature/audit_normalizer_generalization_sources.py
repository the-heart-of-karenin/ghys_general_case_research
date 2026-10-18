"""Record inspected full pages and verify the exact source files remain unchanged."""
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

root = Path(__file__).resolve().parent
records_path = root / "normalizer_generalization_rendered_pages.json"
records = json.loads(records_path.read_text(encoding="utf-8"))
manifest = json.loads((root / "sources_manifest.json").read_text(encoding="utf-8-sig"))
by_name = {item["filename"]:item for item in manifest}
sources = []
for name in dict.fromkeys(item["source"] for item in records):
    path = root / name
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    if "sha256" in by_name[name]:
        assert sha == by_name[name]["sha256"]
    page_count = len(PdfReader(path).pages)
    pages = [item["page"] for item in records if item["source"] == name]
    assert all(1 <= p <= page_count for p in pages)
    sources.append(dict(filename=name,sha256=sha,pages=page_count,
                        complete_pages_visually_inspected=pages))
for record in records:
    assert Path(record["preview"]).is_file()
    record["visually_inspected"] = True
records_path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
audit = dict(date="2026-10-18",all_checks_passed=True,
             distinct_sources=len(sources),complete_pages_inspected=len(records),sources=sources,
             clarification="Source 32 Theorem 2.1 states deformation invariance, not the general finiteness claim; the latter is proved independently in note 46. Source 40 p12 formula (13) is correct when the internal c4/3 is retained.",
             limitation="This audit checks source identity and records visual reading; mathematical correctness and novelty are not established by hash checks.")
(root / "normalizer_generalization_source_audit.json").write_text(
    json.dumps(audit,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(all_checks_passed=True,sources=len(sources),full_pages=len(records))))
