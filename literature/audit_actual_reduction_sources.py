"""Verify source hashes and record complete-page visual inspections for 36-38."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

root = Path(__file__).resolve().parent
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
selected = {
    "23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf": [4, 5, 6],
    "24_Kapfer_2016_Integral_cohomology.pdf": [2, 3, 4],
    "27_Klein_Williams_2007_Homotopical_intersection.pdf": [8, 10, 14],
    "28_Zibrowius_2011_Witt_groups_cellular_varieties.pdf": [24, 27],
    "29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf": [16, 17, 21, 23, 25, 34],
    "30_Kapfer_Menet_2020_Kummer_corrigendum.pdf": [1],
    "31_Meachan_2015_Derived_autoequivalences_Kummer.pdf": [5, 6],
}
verified = []
for entry in manifest:
    if entry.get("filename") not in selected:
        continue
    path = root / entry["filename"]
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    assert digest == entry["sha256"], path.name
    assert len(PdfReader(path).pages) == entry["pages"]
    if path.name.startswith("28_"):
        entry["landing_url"] = "https://doi.org/10.4171/DM/339"
    entry["actual_reduction_visual_pages"] = selected[path.name]
    verified.append(dict(filename=path.name, sha256=digest,
                         verified_complete_visual_pages=selected[path.name]))
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
verification_path = root / "low_dimensional_obstruction_source_verification.json"
if verification_path.exists():
    verification = json.loads(verification_path.read_text(encoding="utf-8"))
    for item in verification:
        if item.get("filename", "").startswith("28_"):
            item["landing_url"] = "https://doi.org/10.4171/DM/339"
    verification_path.write_text(json.dumps(verification, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

render_path = root / "actual_reduction_rendered_pages.json"
rendered = json.loads(render_path.read_text(encoding="utf-8"))
for item in rendered:
    name = item["source"]
    item["visually_inspected"] = item["page"] in selected.get(name, [])
    if name.startswith("25_") and item["page"] == 8:
        item["visually_inspected"] = True
        item["purpose"] = "Background scope only; not a sufficient criterion used in 36-37"
    if name.startswith("27_") and item["page"] == 13:
        item["visually_inspected"] = True
        item["purpose"] = "Inspected background; actual duality theorem is on PDF p.14"
render_path.write_text(json.dumps(rendered, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")

result = dict(audited_utc=datetime.now(timezone.utc).isoformat(),
              source_count=len(verified), visual_pages=sum(len(v) for v in selected.values()),
              sources=verified,
              scope="Source identities and cited theorem pages verified. This audit does not automate the mathematical proofs.")
(root / "actual_reduction_source_audit.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps({k: v for k, v in result.items() if k != "sources"}, ensure_ascii=False, indent=2))
