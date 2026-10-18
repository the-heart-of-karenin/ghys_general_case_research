"""Complete-page previews for the completed results on the rank-three example."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parent
poppler=Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs=[
    ("41_Oguiso_2020_Cohomologically_trivial_automorphisms.pdf",10,"boundary_H2_faithfulness"),
    ("41_Oguiso_2020_Cohomologically_trivial_automorphisms.pdf",11,"boundary_finite_symmetry_background"),
    ("37_Markman_2011_Torelli_monodromy_survey.pdf",21,"boundary_transcendental_finite_action"),
    ("38_Mongardi_2015_Kahler_Mori_cones.pdf",7,"boundary_exact_walls"),
    ("38_Mongardi_2015_Kahler_Mori_cones.pdf",8,"boundary_exact_walls_proof"),
    ("35_Cantat_2001_Dynamics_K3_surfaces.pdf",2,"boundary_surface_entropy_classification"),
    ("35_Cantat_2001_Dynamics_K3_surfaces.pdf",3,"boundary_surface_entropy_classification_continued"),
    ("21_OGrady_2022_Modular_sheaves.pdf",17,"boundary_Chern_pairings"),
    ("24_Kapfer_2016_Integral_cohomology.pdf",6,"boundary_H4_Sym2"),
]

def render(job):
    name,page,label=job
    out=root/"previews"/label
    if not out.with_suffix(".png").exists():
        subprocess.run([str(poppler),"-f",str(page),"-l",str(page),"-r","120","-singlefile","-png",str(root/name),str(out)],
                       check=True,capture_output=True,creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=name,page=page,preview=str(out)+".png",visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
    records=list(pool.map(render,jobs))
(root/"boundary_normalizer_rendered_pages.json").write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(full_pages_rendered=len(records))))
