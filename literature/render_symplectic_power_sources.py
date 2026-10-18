"""Full pages for notes 43--44, including the reused projectivity criterion."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    ("37_Markman_2011_Torelli_monodromy_survey.pdf", 3, "Markman_period_surjectivity"),
    ("37_Markman_2011_Torelli_monodromy_survey.pdf", 4, "Markman_strong_Torelli"),
    ("37_Markman_2011_Torelli_monodromy_survey.pdf", 32, "Markman_K3_square_monodromy"),
    ("38_Mongardi_2015_Kahler_Mori_cones.pdf", 7, "Mongardi_K3_square_wall_squares"),
    ("38_Mongardi_2015_Kahler_Mori_cones.pdf", 8, "Mongardi_K3_square_wall_proof"),
    ("39_Huybrechts_2017_K3_category_cubic_fourfold.pdf", 22, "Huybrechts_odd_rank_Hodge_isometries"),
    ("18_Huybrechts_2003_Projectivity_erratum.pdf", 3, "Huybrechts_projectivity_rank_two_recheck"),
    ("21_OGrady_2022_Modular_sheaves.pdf", 17, "OGrady_K3_square_Fujiki_Chern"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 4, "Kapfer_odd_cohomology_zero"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 6, "Kapfer_H4_symmetric_square"),
]

def render(job):
    source, page, label = job
    out = root / "previews" / label
    if not out.with_suffix(".png").exists():
        subprocess.run([str(poppler), "-f", str(page), "-l", str(page), "-r", "120", "-singlefile",
                        "-png", str(root / source), str(out)], check=True, capture_output=True,
                       creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=source, page=page, preview=str(out) + ".png", visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(render, jobs))
(root / "symplectic_power_rendered_pages.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"complete_pages_rendered": len(records)}))
