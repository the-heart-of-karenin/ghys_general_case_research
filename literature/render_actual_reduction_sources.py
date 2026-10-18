"""Render complete primary-source pages needed for the actual reduction audit."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    ("27_Klein_Williams_2007_Homotopical_intersection.pdf", 8, "Klein_Williams_section_obstruction"),
    ("27_Klein_Williams_2007_Homotopical_intersection.pdf", 10, "Klein_Williams_stable_Euler_complete"),
    ("27_Klein_Williams_2007_Homotopical_intersection.pdf", 13, "Klein_Williams_duality"),
    ("28_Zibrowius_2011_Witt_groups_cellular_varieties.pdf", 24, "Zibrowius_KO_d2"),
    ("28_Zibrowius_2011_Witt_groups_cellular_varieties.pdf", 27, "Zibrowius_Thom_twist"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 2, "Kapfer_symmetric_functions"),
    ("25_Sadovek_Schutte_2026_Complex_line_fields.pdf", 8, "Sadovek_Schutte_spin_scope"),
    ("27_Klein_Williams_2007_Homotopical_intersection.pdf", 14, "Klein_Williams_actual_duality"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 16, "Kapfer_Menet_odd_basis"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 17, "Kapfer_Menet_odd_dual_basis"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 21, "Kapfer_Menet_c2_integral"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 23, "Kapfer_Menet_halved_products"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 25, "Kapfer_Menet_saturation"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 34, "Kapfer_Menet_square_injective"),
    ("30_Kapfer_Menet_2020_Kummer_corrigendum.pdf", 1, "Kapfer_Menet_torsion_correction"),
    ("31_Meachan_2015_Derived_autoequivalences_Kummer.pdf", 5, "Meachan_nested_correspondence"),
    ("31_Meachan_2015_Derived_autoequivalences_Kummer.pdf", 6, "Meachan_blowup"),
]

def render(job):
    name, page, prefix = job
    dest = root / "previews" / prefix
    if not dest.with_suffix(".png").exists():
        subprocess.run([str(poppler), "-f", str(page), "-l", str(page), "-r", "120",
                        "-singlefile", "-png", str(root / name), str(dest)],
                       check=True, capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=name, page=page, preview=str(dest) + ".png", visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
    result = list(pool.map(render, jobs))
(root / "actual_reduction_rendered_pages.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"pages_rendered": len(result)}))
