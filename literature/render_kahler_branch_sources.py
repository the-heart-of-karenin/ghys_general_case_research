"""Render the exact source pages used in the Kahler exploration."""
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import subprocess
from pypdf import PdfReader

root = Path(__file__).resolve().parent
poppler = Path(r"C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe")
jobs = [
    (root / "17_Beauville_1983_Decomposition.pdf", 2, "Beauville_1983_theorem"),
    (root / "17_Beauville_1983_Decomposition.pdf", 3, "Beauville_1983_p3"),
    (root / "17_Beauville_1983_Decomposition.pdf", 4, "Beauville_1983_p4"),
    (root / "17_Beauville_1983_Decomposition.pdf", 5, "Beauville_1983_p5"),
    (root / "18_Huybrechts_2003_Projectivity_erratum.pdf", 3, "Huybrechts_projectivity"),
    (root / "19_Oguiso_2009_Dynamical_degrees.pdf", 1, "Oguiso_degrees"),
    (root / "20_Jang_2024_Kummer_rigidity.pdf", 2, "Jang_hypotheses"),
    (root / "20_Jang_2024_Kummer_rigidity.pdf", 10, "Jang_Green_currents"),
    (root / "20_Jang_2024_Kummer_rigidity.pdf", 21, "Jang_exact_dilation"),
    (root / "20_Jang_2024_Kummer_rigidity.pdf", 22, "Jang_smooth_distributions"),
    (root / "20_Jang_2024_Kummer_rigidity.pdf", 24, "Jang_holomorphic_proof"),
    (root / "20_Jang_2024_Kummer_rigidity.pdf", 25, "Jang_holomorphic_conclusion"),
    (root / "21_OGrady_2022_Modular_sheaves.pdf", 5, "OGrady_Fujiki_convention"),
    (root / "21_OGrady_2022_Modular_sheaves.pdf", 6, "OGrady_Fujiki_constants"),
    (Path(r"D:\Users\Desktop\work\2\historical_literature\01_Ghys_1995_Holomorphic_Anosov_systems.pdf"), 2, "Ghys_surface_theorem"),
    (Path(r"D:\Users\Desktop\work\2\historical_literature\01_Ghys_1995_Holomorphic_Anosov_systems.pdf"), 1, "Ghys_surface_p1"),
]
extra = [
    ("20_Jang_2024_Kummer_rigidity.pdf", "PROPOSITION 19", "Jang_holomorphic_distributions"),
    ("21_OGrady_2022_Modular_sheaves.pdf", "828", "OGrady_K3_constants"),
    ("22_OGrady_2024_Kummer_bundles.pdf", "756", "OGrady_Kummer_constants"),
]
for filename, needle, name in extra:
    pdf = root / filename
    pages = [(i + 1, p.extract_text() or "") for i, p in enumerate(PdfReader(pdf).pages)]
    found = [(i, text) for i, text in pages if needle in text]
    if not found:
        raise ValueError(f"Not found: {needle!r} in {filename}")
    page, text = found[0]
    jobs.append((pdf, page, name))
    print(json.dumps({"file": filename, "page": page, "needle": needle}, ensure_ascii=False))


def render(job):
    pdf, page, name = job
    dest = root / "previews" / name
    dest.parent.mkdir(exist_ok=True)
    if not dest.with_suffix(".png").exists():
        subprocess.run([str(poppler), "-f", str(page), "-l", str(page), "-r", "110",
                        "-singlefile", "-png", str(pdf), str(dest)], check=True,
                       capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return {"source": str(pdf), "page": page, "preview": str(dest) + ".png"}


with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(render, jobs))
(root / "kahler_rendered_pages.json").write_text(
    json.dumps(results, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(results, indent=2, ensure_ascii=False))
