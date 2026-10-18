"""Collect primary sources for actual, rather than stable, reductions."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
sources = [
    ("25_Sadovek_Schutte_2026_Complex_line_fields.pdf",
     "Complex line fields on almost-complex manifolds",
     "https://link.springer.com/content/pdf/10.1007/s00208-026-03440-6.pdf",
     "https://doi.org/10.1007/s00208-026-03440-6",
     "Mathematische Annalen 395, article 46 (2026); published 30 April 2026"),
    ("26_Cadek_Crabb_Vanzura_2010_Quaternionic_structures.pdf",
     "Quaternionic structures",
     "https://www.math.muni.cz/~cadek/papers/qst_rev.pdf",
     "https://doi.org/10.1016/j.topol.2010.09.005",
     "Author manuscript dated 17 September 2010; Topology and its Applications 157 (2010)"),
]

def collect(item):
    name, title, url, landing, version = item
    path = root / name
    entry = dict(filename=name, title=title, download_url=url, landing_url=landing,
                 publication_note=version, collected_utc=datetime.now(timezone.utc).isoformat())
    if not path.exists():
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as response:
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
(root / "actual_reduction_source_verification.json").write_text(
    json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(entries, ensure_ascii=False, indent=2))
