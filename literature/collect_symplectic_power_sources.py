"""Sources for the standard Hodge reduction and a genuine anti-symplectic example."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
jobs = [
    dict(filename="37_Markman_2011_Torelli_monodromy_survey.pdf",
         title="A survey of Torelli and monodromy results for holomorphic-symplectic varieties",
         download_url="https://arxiv.org/pdf/1101.4606",
         landing_url="https://doi.org/10.1007/978-3-642-20300-8_15",
         publication_note="Complex and Differential Geometry, Springer Proceedings in Mathematics 8 (2011), 257-322; arXiv v3, 18 December 2011, 46-page author manuscript"),
    dict(filename="38_Mongardi_2015_Kahler_Mori_cones.pdf",
         title="A note on the Kahler and Mori cones of hyperkahler manifolds",
         download_url="https://arxiv.org/pdf/1307.0393",
         landing_url="https://doi.org/10.4310/AJM.2015.v19.n4.a1",
         publication_note="Asian Journal of Mathematics 19 (2015), 583-592; arXiv v3, 25 March 2014, 9 pages; Proposition 2.12 is the K3^[2] wall criterion"),
    dict(filename="39_Huybrechts_2017_K3_category_cubic_fourfold.pdf",
         title="The K3 category of a cubic fourfold",
         download_url="https://www.math.uni-bonn.de/people/huybrech/CubicPaper.pdf",
         landing_url="https://doi.org/10.1112/S0010437X16008137",
         publication_note="Compositio Mathematica 153 (2017); 40-page author manuscript. Odd-rank Hodge-isometry fact in Proposition 3.11 proof, PDF p.22; journal numbering 3.12."),
]

def collect(entry):
    entry = dict(entry)
    path = root / entry["filename"]
    if path.exists():
        data = path.read_bytes()
    else:
        req = urllib.request.Request(entry["download_url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
            entry["resolved_url"] = response.geturl()
        if not data.startswith(b"%PDF"):
            raise ValueError(entry["filename"])
        path.write_bytes(data)
    pages = [page.extract_text() or "" for page in PdfReader(path).pages]
    (root / "extracted" / (path.stem + ".txt")).write_text(
        "\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}" for i, text in enumerate(pages)), encoding="utf-8")
    entry.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                 pages=len(pages), collected_utc=datetime.now(timezone.utc).isoformat())
    return entry

with ThreadPoolExecutor(max_workers=3) as pool:
    entries = list(pool.map(collect, jobs))
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
names = {entry["filename"] for entry in entries}
manifest = [entry for entry in manifest if entry["filename"] not in names] + entries
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps([{key: entry[key] for key in ("filename", "pages", "bytes", "sha256")} for entry in entries], indent=2))
