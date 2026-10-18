"""Source identity and full-page reading records for notes 49--50."""
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

root=Path(__file__).resolve().parent
records_path=root/"boundary_normalizer_rendered_pages.json"
records=json.loads(records_path.read_text(encoding="utf-8"))
manifest=json.loads((root/"sources_manifest.json").read_text(encoding="utf-8-sig"))
by_name={item["filename"]:item for item in manifest}
uses={
    "41_Oguiso_2020_Cohomologically_trivial_automorphisms.pdf":"PDF p10 Theorem 5.1, H2 faithfulness for K3^[n]-type. PDF p11 concerns finite-order fixed loci and is inspected background only.",
    "37_Markman_2011_Torelli_monodromy_survey.pdf":"Compactness/finiteness background for the projective transcendental Hodge action, independently proved in note 49.",
    "38_Mongardi_2015_Kahler_Mori_cones.pdf":"Proposition 2.12: exact K3^[2] wall list, for the ample axis.",
    "35_Cantat_2001_Dynamics_K3_surfaces.pdf":"Positive-entropy surface classification, not a statement that a periodic submanifold automatically inherits Anosov.",
    "21_OGrady_2022_Modular_sheaves.pdf":"c2 pairing normalization; quartic Fujiki formula is reused from previously inspected pp5-6.",
    "24_Kapfer_2016_Integral_cohomology.pdf":"Rational H4 symmetric square and Betti dimensions; odd-cohomology vanishing reused from earlier inspected p4.",
}
sources=[]
for name in dict.fromkeys(item["source"] for item in records):
    path=root/name
    data=path.read_bytes()
    digest=hashlib.sha256(data).hexdigest()
    assert digest==by_name[name]["sha256"]
    pages=len(PdfReader(path).pages)
    looked=[item["page"] for item in records if item["source"]==name]
    assert all(1<=p<=pages for p in looked)
    sources.append(dict(filename=name,sha256=digest,pages=pages,complete_pages_visually_inspected=looked,use=uses[name]))
for item in records:
    assert Path(item["preview"]).is_file()
    item["visually_inspected"]=True
records_path.write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
result=dict(date="2026-10-18",all_checks_passed=True,distinct_sources=len(sources),
            complete_pages_inspected=len(records),sources=sources,
            limitation="Hashes and visual-reading records do not certify mathematical correctness or novelty. Proofs are in notes 49--50; exact auxiliary checks have a separate record.")
(root/"boundary_normalizer_source_audit.json").write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(all_checks_passed=True,sources=len(sources),full_pages=len(records))))
