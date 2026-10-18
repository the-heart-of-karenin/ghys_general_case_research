"""Complete-page previews for the K3-square surface and difficulty notes."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    ("33_Mongardi_2012_Symplectic_involutions_K3_square.pdf", 1, "Mongardi_involution_version"),
    ("33_Mongardi_2012_Symplectic_involutions_K3_square.pdf", 8, "Mongardi_transcendental_Hodge_argument"),
    ("33_Mongardi_2012_Symplectic_involutions_K3_square.pdf", 10, "Mongardi_fixed_K3"),
    ("33_Mongardi_2012_Symplectic_involutions_K3_square.pdf", 13, "Mongardi_coinvariant_E8"),
    ("34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf", 3, "Amerik_Verbitsky_rank_two_existence"),
    ("34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf", 10, "Amerik_Verbitsky_hyperbolic_construction"),
    ("34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf", 11, "Amerik_Verbitsky_quadratic_units"),
    ("35_Cantat_2001_Dynamics_K3_surfaces.pdf", 2, "Cantat_surface_classification_start"),
    ("35_Cantat_2001_Dynamics_K3_surfaces.pdf", 3, "Cantat_surface_classification"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 6, "Kapfer_H4_symmetric_square"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 4, "Kapfer_odd_cohomology_zero"),
    ("21_OGrady_2022_Modular_sheaves.pdf", 17, "OGrady_K3_square_Fujiki_Chern"),
    ("21_OGrady_2022_Modular_sheaves.pdf", 5, "OGrady_Fujiki_normalization_recheck"),
    ("21_OGrady_2022_Modular_sheaves.pdf", 6, "OGrady_Fujiki_constants"),
    ("36_Lesieutre_Satriano_2021_Canonical_heights.pdf", 15, "Lesieutre_Satriano_periodic_criterion"),
    ("36_Lesieutre_Satriano_2021_Canonical_heights.pdf", 16, "Lesieutre_Satriano_rank_two_ample"),
    ("36_Lesieutre_Satriano_2021_Canonical_heights.pdf", 17, "Lesieutre_Satriano_even_periodic_examples"),
]

def render(job):
    name, page, label = job
    dest = root / "previews" / label
    if not dest.with_suffix(".png").exists():
        subprocess.run([str(poppler), "-f", str(page), "-l", str(page), "-r", "115",
                        "-singlefile", "-png", str(root / name), str(dest)],
                       check=True, capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=name, page=page, preview=str(dest) + ".png", visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(render, jobs))
(root / "K3_square_surface_rendered_pages.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"complete_pages_rendered": len(records)}))
