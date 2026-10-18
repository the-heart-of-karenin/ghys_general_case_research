"""Render only the source pages actually used in notes 31-34."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    ("23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf", 4, "Cadek_Chern_Steenrod"),
    ("23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf", 5, "Cadek_topological_index"),
    ("23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf", 6, "Cadek_rank_four_extension"),
    ("23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf", 10, "Cadek_quaternionic_hypothesis"),
    ("23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf", 13, "Cadek_rank_two_hypothesis"),
    ("23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf", 17, "Cadek_rank_five_representation"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 3, "Kapfer_integral_basis"),
    ("24_Kapfer_2016_Integral_cohomology.pdf", 4, "Kapfer_torsion_free_even"),
]


def render(job):
    filename, page, prefix = job
    dest = root / "previews" / prefix
    if not dest.with_suffix(".png").exists():
        subprocess.run([str(poppler), "-f", str(page), "-l", str(page), "-r", "120",
                        "-singlefile", "-png", str(root / filename), str(dest)],
                       check=True, capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=str(root / filename), page=page, preview=str(dest) + ".png")


with ThreadPoolExecutor(max_workers=3) as pool:
    result = list(pool.map(render, jobs))
(root / "Chern_topology_rendered_pages.json").write_text(
    json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"pages_rendered": len(result)}, indent=2))
