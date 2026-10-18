"""Render complete pages used in the finite-symmetry obstruction."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    ("32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf", 3, "Hassett_Tschinkel_deformation_theorem"),
    ("32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf", 4, "Hassett_Tschinkel_deformation_proof"),
    ("32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf", 5, "Hassett_Tschinkel_finite_group_definition"),
    ("32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf", 6, "Hassett_Tschinkel_group_extension"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 27, "Kapfer_Menet_kernel_and_involutions"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 28, "Kapfer_Menet_involution_theorem_start"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 29, "Kapfer_Menet_involution_theorem"),
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf", 30, "Kapfer_Menet_fixed_K3_proof"),
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
    result = list(pool.map(render, jobs))
(root / "fixed_locus_rendered_pages.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"pages_rendered": len(result)}))
