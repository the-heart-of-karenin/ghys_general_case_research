"""Record source identity and completed manual page checks for notes 41--42."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

root = Path(__file__).resolve().parent
now = datetime.now(timezone.utc).isoformat()
rendered_path = root / "K3_square_surface_rendered_pages.json"
rendered = json.loads(rendered_path.read_text(encoding="utf-8"))
expected_pages = {
    "33_Mongardi_2012_Symplectic_involutions_K3_square.pdf": [1, 8, 10, 13],
    "34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf": [3, 10, 11],
    "35_Cantat_2001_Dynamics_K3_surfaces.pdf": [2, 3],
    "24_Kapfer_2016_Integral_cohomology.pdf": [4, 6],
    "21_OGrady_2022_Modular_sheaves.pdf": [5, 6, 17],
    "36_Lesieutre_Satriano_2021_Canonical_heights.pdf": [15, 16, 17],
}
manual_checked = {(name, page) for name, pages in expected_pages.items() for page in pages}
assert {(entry["source"], entry["page"]) for entry in rendered} == manual_checked
for entry in rendered:
    assert Path(entry["preview"]).is_file()
    entry.update(visually_inspected=True, inspection_date="2026-10-18",
                 method="Complete rendered page visually read by the assistant; marking records that manual review, not an OCR check.")
rendered_path.write_text(json.dumps(rendered, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
by_name = {entry["filename"]: entry for entry in manifest}
results = {
    33: ["Theorem 4.1", "Theorem 5.2", "Lemma 3.4 proof", "Remark 4.3"],
    34: ["Theorem 1.1", "Corollary 3.7", "rank-two quadratic-unit construction"],
    35: ["Introduction: classification of positive-entropy compact complex surface automorphisms"],
    24: ["Odd cohomology vanishes", "Remark 2.1", "Proposition 2.2"],
    21: ["Convention 1.5.1", "Section 2.2: normalized Fujiki constant", "Equation 5.3.4"],
    36: ["Theorem 2.21", "Remark 2.22", "Corollary 2.23", "Example 2.24"],
}
limitations = {
    33: ["Downloaded PDF margin says arXiv v3 9 May 2012, while its title date is 8 March 2021; do not identify its pagination with the 2012 journal version.",
         "The minimal-Hodge argument for infinite-order symplectic f is proved directly in note 41; a finite-group lemma is not applied beyond its hypotheses."],
    34: ["Hyperbolic here concerns cohomology/positive entropy; these examples are not claimed to be Anosov."],
    35: ["Only the surface-classification consequence chi(O)<=2 is used, not a maximal-entropy or Anosov conclusion."],
    24: ["Use rational Sym^2 H^2 = H^4, not an integral isomorphism."],
    21: ["Fujiki and Chern identities alone do not exclude continuous Lagrangian subbundles; here they apply to the class of an actual invariant smooth surface."],
    36: ["Comparison source only; its arithmetic hypotheses over Qbar are not applied to arbitrary complex X.",
         "The checked periodic-subvariety results do not themselves exclude every smooth even-dimensional periodic surface.",
         "No first-publication priority is inferred from the finite search."],
}
records = []
for name, pages in expected_pages.items():
    path = root / name
    data = path.read_bytes()
    sha = hashlib.sha256(data).hexdigest()
    assert sha == by_name[name]["sha256"]
    number = int(name.split("_", 1)[0])
    by_name[name]["K3_square_surface_visual_pages"] = pages
    records.append(dict(path=str(path), sha256=sha, page_count=len(PdfReader(path).pages),
                        visually_inspected=True, pages=pages, results=results[number],
                        role="novelty comparison" if number == 36 else "proof input",
                        limitations=limitations[number]))
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
audit = dict(audited_utc=now, sources=records, source_count=len(records),
             complete_pages_visually_checked=len(rendered),
             reused_surface_Anosov_input="Ghys 1995 Theorem A, previously audited in fixed_locus_and_submanifold_source_audit.json",
             statements=["Notes 41--42 give complete proofs of their stated weak results.",
                         "The K3^[2] Ghys problem and transverse C1 remain open in this research.",
                         "Publication novelty is not confirmed."])
(root / "K3_square_surface_source_audit.json").write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(dict(sources=len(records), complete_pages=len(rendered), hashes_verified=True)))
