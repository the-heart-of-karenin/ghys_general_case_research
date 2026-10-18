"""Record source identity and complete-page visual checks for notes 39-40.

This is a provenance check, not an automated verification of the mathematical proofs.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

root = Path(__file__).resolve().parent
records = json.loads((root / "fixed_locus_rendered_pages.json").read_text(encoding="utf-8"))
for record in records:
    if not Path(record["preview"]).is_file():
        raise FileNotFoundError(record["preview"])
    # Each of these complete pages has been viewed through the image tool.
    record["visually_inspected"] = True
(root / "fixed_locus_rendered_pages.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

manifest = {item["filename"]: item for item in json.loads((root / "sources_manifest.json").read_text(encoding="utf-8"))}
source_inputs = [
    dict(path=root / "32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf",
         pages=[3, 4, 5, 6], results=["Theorem 2.1", "Proposition 3.1"],
         limitations=["Do not use the isolated fixed point count in author manuscript Theorem 4.4(1)."]),
    dict(path=root / "29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf",
         pages=[27, 28, 29, 30], results=["Corollary 7.1", "Theorem 7.5(iii)", "Remark 7.7(2)"],
         limitations=["Page 27 explanatory sentence prints exponent 3; use the formal A[3] statement, with A[3]=(Z/3)^4."]),
    dict(path=Path(r"D:\Users\Desktop\work\2\historical_literature\01_Ghys_1995_Holomorphic_Anosov_systems.pdf"),
         pages=[1], results=["Theorem A"], limitations=[]),
]
sources = []
for item in source_inputs:
    path = item.pop("path")
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    old = manifest.get(path.name)
    if old and digest != old["sha256"]:
        raise ValueError(f"Hash mismatch: {path.name}")
    sources.append(dict(path=str(path), sha256=digest,
                        page_count=len(PdfReader(path).pages),
                        visually_inspected=True, **item))
ghys_preview = root / "previews" / "Ghys_surface_p1.png"
if not ghys_preview.is_file():
    raise FileNotFoundError(ghys_preview)
audit = dict(
    audited_utc=datetime.now(timezone.utc).isoformat(),
    sources=sources, source_count=len(sources),
    complete_pages_visually_checked=sum(len(source["pages"]) for source in sources),
    notes=["39 proof uses actual tangent projections and finite conjugation orbits.",
           "40 supplies a direct invariant-subbundle proof; it does not rely on a quasi-Anosov classification theorem.",
           "No automated proof or first-publication priority is claimed."],
)
(root / "fixed_locus_and_submanifold_source_audit.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({key: audit[key] for key in ["source_count", "complete_pages_visually_checked"]}))
