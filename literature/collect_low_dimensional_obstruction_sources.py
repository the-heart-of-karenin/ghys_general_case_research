"""Primary sources for stable Euler completeness and the KO d2 differential."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
sources = [
    ("27_Klein_Williams_2007_Homotopical_intersection.pdf",
     "Homotopical intersection theory, I",
     "https://msp.org/gt/2007/11-2/gt-v11-n2-p08-p.pdf",
     "https://doi.org/10.2140/gt.2007.11.939",
     "Geometry & Topology 11 (2007), 939-977"),
    ("28_Zibrowius_2011_Witt_groups_cellular_varieties.pdf",
     "Witt groups of complex cellular varieties",
     "https://ems.press/content/serial-article-files/26119?nt=1",
     "https://doi.org/10.4171/DM/339",
     "Documenta Mathematica 16 (2011), 465-511"),
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
(root / "low_dimensional_obstruction_source_verification.json").write_text(
    json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(entries, ensure_ascii=False, indent=2))
