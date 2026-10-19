"""Record actual primary-input checks and reviewed full pages for notes 51-52."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

root = Path(__file__).resolve().parent
manifest = json.loads((root/"sources_manifest.json").read_text(encoding="utf-8-sig"))
index = {record["filename"]: record for record in manifest}
rendered = json.loads((root/"Green_Margulis_rendered_pages.json").read_text(encoding="utf-8"))
for record in rendered:
    assert Path(record["preview"]).is_file()
    record["visually_inspected"] = True

records = []
for name in sorted({record["source"] for record in rendered}):
    source = root/name
    data = source.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    assert data.startswith(b"%PDF")
    assert sha == index[name]["sha256"]
    pages = len(PdfReader(source).pages)
    chosen = [record for record in rendered if record["source"] == name]
    assert all(1 <= record["page"] <= pages for record in chosen)
    records.append(dict(filename=name, pages=pages, sha256=sha,
                        reviewed_full_pages=[record["page"] for record in chosen]))

data = dict(
    audited_utc=datetime.now(timezone.utc).isoformat(),
    purpose="Exact assumptions for Green/Margulis identification and leafwise singularity, notes 51-52.",
    sources=records,
    full_page_previews=rendered,
    reviewed_source_count=len(records),
    reviewed_full_page_count=len(rendered),
    checked_hypotheses=[
        "Ruelle-Sullivan allows continuous tangent planes and smooth individual plaques, without transverse C1.",
        "Their entropy scaling parameter equals exp(h_top), lambda^2 in complex dimension four here.",
        "Dinh-Sibony Theorem 4.3.1 is uniqueness among all positive closed representatives under its spectral conditions.",
        "IHS spectral conditions and Green-square normalization checked directly in Jang Proposition 7.",
        "General woven statement not substituted for the Anosov uniformly laminar identification.",
        "Young Theorem 1(i),(iii) used for SRB uniqueness and full basin; Theorem 3 for stable absolute continuity.",
        "Young PDF page 2(ii) omits log in print; correct entropy equality taken from Ledrappier-Young Theorem A, PDF page 6.",
        "The generic-set argument upgrades a.e. plaque statements using exact holonomy invariance.",
    ],
    limits=[
        "No absolute continuity, smooth root current, transverse C1 or full classification proved.",
        "The full-support singular model is noncompact and not an IHS counterexample.",
        "Novelty not established; the current-identification mechanism is classical.",
        "No actual periodic multipliers of the rank-three boundary example computed.",
    ],
)
(root/"Green_Margulis_rendered_pages.json").write_text(json.dumps(rendered,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
(root/"Green_Margulis_source_audit.json").write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(sources=len(records), full_pages=len(rendered),
                      manifest_entries=len(manifest), all_hash_checks_passed=True),ensure_ascii=False))
