"""Complete-page previews for the precise inputs used by notes 46--48."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    ("32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf", 3, "normalizer_kernel_finiteness"),
    ("19_Oguiso_2009_Dynamical_degrees.pdf", 1, "normalizer_entropy_H2"),
    ("21_OGrady_2022_Modular_sheaves.pdf", 17, "normalizer_K3_square_intersections"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 6, "normalizer_sixfold_H6_extra"),
    ("37_Markman_2011_Torelli_monodromy_survey.pdf", 3, "normalizer_period_surjectivity"),
    ("37_Markman_2011_Torelli_monodromy_survey.pdf", 4, "normalizer_Torelli_chambers"),
    ("37_Markman_2011_Torelli_monodromy_survey.pdf", 5, "normalizer_birational_Kahler_density"),
    ("37_Markman_2011_Torelli_monodromy_survey.pdf", 32, "normalizer_K3_square_monodromy"),
    ("38_Mongardi_2015_Kahler_Mori_cones.pdf", 7, "normalizer_wall_classes"),
    ("38_Mongardi_2015_Kahler_Mori_cones.pdf", 8, "normalizer_wall_proof"),
    ("40_Oberdieck_Song_Voisin_2022_Cobordism_HK.pdf", 12, "normalizer_sixfold_Euler_values"),
]

def render(job):
    source, page, label = job
    out = root / "previews" / label
    if not out.with_suffix(".png").exists():
        subprocess.run([str(poppler), "-f", str(page), "-l", str(page), "-r", "120",
                        "-singlefile", "-png", str(root / source), str(out)],
                       check=True, capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=source, page=page, preview=str(out) + ".png", visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(render, jobs))
(root / "normalizer_generalization_rendered_pages.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(dict(complete_pages_rendered=len(records))))
