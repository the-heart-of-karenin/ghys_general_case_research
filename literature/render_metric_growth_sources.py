"""Relevant full pages for the double-sided metric and derivative-tail route."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root=Path(__file__).resolve().parent
historical=root.parent.parent/"2"/"historical_literature"
poppler=Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs=[
    (root/"20_Jang_2024_Kummer_rigidity.pdf",7,"metric_growth_BBF_signature"),
    (root/"20_Jang_2024_Kummer_rigidity.pdf",8,"metric_growth_eigenclasses"),
    (root/"20_Jang_2024_Kummer_rigidity.pdf",9,"metric_growth_null_locus"),
    (root/"20_Jang_2024_Kummer_rigidity.pdf",11,"metric_growth_simple_eigenvalue"),
    (root/"36_Lesieutre_Satriano_2021_Canonical_heights.pdf",16,"metric_growth_periodic_subvarieties"),
    (root/"36_Lesieutre_Satriano_2021_Canonical_heights.pdf",17,"metric_growth_odd_dimension_comparison"),
    (historical/"02_Cantat_2004_Diffeomorphismes_holomorphes_Anosov.pdf",7,"metric_growth_Cantat_comparison"),
    (historical/"02_Cantat_2004_Diffeomorphismes_holomorphes_Anosov.pdf",8,"metric_growth_Cantat_positive_forms"),
    (historical/"02_Cantat_2004_Diffeomorphismes_holomorphes_Anosov.pdf",9,"metric_growth_Cantat_regularization"),
    (root/"47_De_Thelin_2008_Lyapunov_exponents.pdf",1,"metric_growth_Thelin_integrability"),
    (root/"47_De_Thelin_2008_Lyapunov_exponents.pdf",2,"metric_growth_Thelin_corollary3"),
    (root/"46_Ledrappier_Young_1985_Entropy_I.pdf",6,"metric_growth_LY_equality"),
    (root/"48_Bressaud_Liverani_2002_Anosov_coupling.pdf",6,"metric_growth_holonomy_definitions"),
    (root/"48_Bressaud_Liverani_2002_Anosov_coupling.pdf",7,"metric_growth_holonomy_Jacobian_bounds"),
]

def render(job):
    source,page,label=job
    out=root/"previews"/label
    if not out.with_suffix(".png").exists():
        subprocess.run([str(poppler),"-f",str(page),"-l",str(page),"-r","110","-singlefile","-png",str(source),str(out)],
                       check=True,capture_output=True,creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=str(source),page=page,preview=str(out)+".png",visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
    records=list(pool.map(render,jobs))
(root/"metric_growth_rendered_pages.json").write_text(json.dumps(records,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(dict(full_pages_rendered=len(records))))
