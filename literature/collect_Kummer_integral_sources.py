"""The full integral cohomology source and its essential torsion corrigendum."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
sources = [
    ("29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf",
     "Integral cohomology of the generalized Kummer fourfold",
     "https://content.algebraicgeometry.nl/2018-5/2018-5-014.pdf",
     "https://doi.org/10.14231/AG-2018-014",
     "Algebraic Geometry 5 (2018), 523-567; use with 2020 corrigendum"),
    ("30_Kapfer_Menet_2020_Kummer_corrigendum.pdf",
     "Corrigendum: Integral cohomology of the generalized Kummer fourfold",
     "https://arxiv.org/pdf/1907.07031",
     "https://doi.org/10.14231/AG-2020-014",
     "Algebraic Geometry 7 (2020), 482-485; author preprint"),
]

def collect(item):
    name, title, url, landing, version = item
    path = root / name
    entry = dict(filename=name, title=title, download_url=url, landing_url=landing,
                 publication_note=version, collected_utc=datetime.now(timezone.utc).isoformat())
    if not path.exists():
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=45) as response:
            data = response.read()
            entry["resolved_url"] = response.geturl()
        if not data.startswith(b"%PDF"):
            raise ValueError("Not a PDF: " + name)
        path.write_bytes(data)
    else:
        data = path.read_bytes()
    pages = [page.extract_text() or "" for page in PdfReader(path).pages]
    (root / "extracted" / (path.stem + ".txt")).write_text(
        "\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}" for i, text in enumerate(pages)), encoding="utf-8")
    entry.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pages=len(pages))
    return entry

with ThreadPoolExecutor(max_workers=2) as pool:
    entries = list(pool.map(collect, sources))
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
names = {e["filename"] for e in entries}
manifest = [e for e in manifest if e.get("filename") not in names] + entries
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(root / "Kummer_integral_source_verification.json").write_text(
    json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(entries, ensure_ascii=False, indent=2))
