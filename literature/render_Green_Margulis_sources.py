"""Full-page previews of the actual external inputs for notes 51-52."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    ("42_Ruelle_Sullivan_1975_Currents.pdf", 1, "Green_RS_continuous_tangents"),
    ("42_Ruelle_Sullivan_1975_Currents.pdf", 2, "Green_RS_closed_current"),
    ("42_Ruelle_Sullivan_1975_Currents.pdf", 6, "Green_RS_Margulis_product"),
    ("42_Ruelle_Sullivan_1975_Currents.pdf", 7, "Green_RS_eigencurrents"),
    ("44_Dinh_Sibony_2010_Superpotentials_Kahler.pdf", 38, "Green_DS_class_uniqueness"),
    ("43_De_Thelin_Dinh_2012_Dynamics_Kahler.pdf", 2, "Green_DT_cohomology_hypotheses"),
    ("43_De_Thelin_Dinh_2012_Dynamics_Kahler.pdf", 3, "Green_DT_unique_MME"),
    ("20_Jang_2024_Kummer_rigidity.pdf", 2, "Green_Jang_rigidity_statement"),
    ("20_Jang_2024_Kummer_rigidity.pdf", 6, "Green_Jang_metric_gap"),
    ("20_Jang_2024_Kummer_rigidity.pdf", 10, "Green_Jang_Green_squares"),
    ("20_Jang_2024_Kummer_rigidity.pdf", 11, "Green_Jang_simple_eigenvalue"),
    ("45_Young_2002_SRB_survey.pdf", 2, "Green_Young_unique_SRB"),
    ("45_Young_2002_SRB_survey.pdf", 3, "Green_Young_log_Jacobian"),
    ("46_Ledrappier_Young_1985_Entropy_I.pdf", 2, "Green_LY_entropy_characterization"),
    ("46_Ledrappier_Young_1985_Entropy_I.pdf", 3, "Green_LY_absolute_continuity"),
    ("46_Ledrappier_Young_1985_Entropy_I.pdf", 6, "Green_LY_Theorem_A"),
    ("45_Young_2002_SRB_survey.pdf", 6, "Green_Young_stable_absolute_continuity"),
]

def render(job):
    name, page, label = job
    out = root/"previews"/label
    if not out.with_suffix(".png").exists():
        subprocess.run([str(poppler), "-f", str(page), "-l", str(page), "-r", "100",
                        "-singlefile", "-png", str(root/name), str(out)],
                       check=True, capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=name, page=page, preview=str(out)+".png", visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(render, jobs))
(root/"Green_Margulis_rendered_pages.json").write_text(json.dumps(records, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(dict(full_pages_rendered=len(records))))
