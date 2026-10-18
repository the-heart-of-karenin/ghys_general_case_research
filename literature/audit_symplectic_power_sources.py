"""Record identity and complete-page manual inspections for notes 43--45."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

root = Path(__file__).resolve().parent
rendered_path = root / "symplectic_power_rendered_pages.json"
rendered = json.loads(rendered_path.read_text(encoding="utf-8"))
expected = {
    "18_Huybrechts_2003_Projectivity_erratum.pdf": [3],
    "21_OGrady_2022_Modular_sheaves.pdf": [17],
    "24_Kapfer_2016_Integral_cohomology.pdf": [4, 6],
    "37_Markman_2011_Torelli_monodromy_survey.pdf": [3, 4, 32],
    "38_Mongardi_2015_Kahler_Mori_cones.pdf": [7, 8],
    "39_Huybrechts_2017_K3_category_cubic_fourfold.pdf": [22],
}
assert {(x["source"], x["page"]) for x in rendered} == {
    (name, page) for name, pages in expected.items() for page in pages}
for entry in rendered:
    assert Path(entry["preview"]).is_file()
    entry.update(visually_inspected=True, inspection_date="2026-10-18",
                 method="Complete rendered page visually read by the assistant; this records manual review, not OCR-only validation.")
rendered_path.write_text(json.dumps(rendered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
by_name = {x["filename"]: x for x in manifest}
findings = {
    18: ["Theorem 2: corrected projectivity criterion"],
    21: ["Equation 5.3.4: integral c2^2=828"],
    24: ["Odd cohomology vanishes", "Remark 2.1: b2=23, b4=276, b6=23"],
    37: ["Surjective period map", "Theorem 1.3(2): strong Torelli", "Theorem 9.1 and Lemma 9.2: Mon2=O+ for n=2"],
    38: ["Proposition 2.12: walls of K3^[2] type"],
    39: ["Proposition 3.11 proof in author version: odd-rank simple Hodge isometries are +/-I"],
}
limitations = {
    18: ["Use the corrected criterion, not the flawed original proof."],
    21: ["Nonzero c1 of an actual Lagrangian tangent splitting; not a new stable K obstruction."],
    24: ["Betti numbers alone do not rule out Anosov; the derivative invariance argument is essential."],
    37: ["Torelli gives an actual automorphism only after parallel-transport and Kahler-class hypotheses are verified.",
         "The source uses pushforward in Theorem 1.3; inversion gives the pullback convention of note 44."],
    38: ["Use the K3^[2] case, Proposition 2.12 of the saved nine-page author version; not the higher-dimensional wall tables."],
    39: ["The saved author version has Proposition 3.11; journal numbering is 3.12.",
         "This is a known Hodge fact; note 43 supplies its independent linear-algebra proof."],
}
records = []
for name, pages in expected.items():
    data = (root / name).read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    assert sha == by_name[name]["sha256"]
    number = int(name.split("_", 1)[0])
    by_name[name]["symplectic_power_visual_pages"] = pages
    if number == 38:
        by_name[name]["publication_note"] = "Asian Journal of Mathematics 19 (2015), 583-592; arXiv v3, 25 March 2014, 9 pages; Proposition 2.12 is the K3^[2] wall criterion"
    records.append(dict(path=str(root / name), sha256=sha, page_count=len(PdfReader(root / name).pages),
                        visually_inspected=True, pages=pages, findings=findings[number],
                        limitations=limitations[number]))
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
audit = dict(audited_utc=datetime.now(timezone.utc).isoformat(), sources=records,
             source_count=len(records), complete_pages_visually_checked=len(rendered),
             proof_status={"43": "complete reduction, removes symplectic and extra projectivity hypotheses of 41",
                           "44": "actual anti-symplectic positive-entropy automorphism realized via Torelli",
                           "45": "complete exclusion of all holomorphic Anosov on rank-two X carrying such an automorphism"},
             remaining="General symplectic K3^[2] Anosov branch, transverse C1, and singular-periodic-surface issues are unresolved; publication novelty is not confirmed.")
(root / "symplectic_power_source_audit.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(dict(sources=len(records), complete_pages=len(rendered), hashes_verified=True)))
