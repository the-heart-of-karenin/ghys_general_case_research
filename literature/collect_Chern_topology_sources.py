"""Download primary sources for the Chern-class continuation, 2026-10-18."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
sources = [
    ("23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf",
     "Obstruction theory on 8-manifolds",
     "https://www.math.muni.cz/~cadek/papers/8_manifolds.pdf",
     "https://doi.org/10.1007/s00229-008-0203-x",
     "Author manuscript corrected 8 July 2008; Manuscripta Math. 127 (2008), 167-186"),
    ("24_Kapfer_2016_Integral_cohomology.pdf",
     "Computing cup products in integral cohomology of Hilbert schemes of points on K3 surfaces",
     "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/DAF03A697F193564320B645D5634EA92/S1461157016000012a.pdf/computing_cup_products_in_integral_cohomology_of_hilbert_schemes_of_points_on_k3_surfaces.pdf",
     "https://doi.org/10.1112/S1461157016000012",
     "Publisher PDF; LMS J. Comput. Math. 19 (2016), 78-97"),
]


def collect(item):
    filename, title, url, landing, version = item
    path = root / filename
    entry = dict(filename=filename, title=title, download_url=url,
                 landing_url=landing, publication_note=version,
                 collected_utc=datetime.now(timezone.utc).isoformat())
    if not path.exists():
        request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(request, timeout=45) as response:
            data = response.read()
            entry["resolved_url"] = response.geturl()
        if not data.startswith(b"%PDF"):
            raise ValueError("Response is not PDF: " + filename)
        path.write_bytes(data)
        entry["download_status"] = "downloaded"
    else:
        data = path.read_bytes()
        entry["download_status"] = "existing_verified"
    pages = [page.extract_text() or "" for page in PdfReader(path).pages]
    text_path = root / "extracted" / (path.stem + ".txt")
    text_path.write_text("\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}"
                                    for i, text in enumerate(pages)), encoding="utf-8")
    entry.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                 pages=len(pages), extracted_characters=sum(map(len, pages)))
    return entry


with ThreadPoolExecutor(max_workers=2) as pool:
    entries = list(pool.map(collect, sources))
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
names = {entry["filename"] for entry in entries}
manifest = [entry for entry in manifest if entry.get("filename") not in names] + entries
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
(root / "Chern_topology_source_verification.json").write_text(
    json.dumps(entries, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(entries, ensure_ascii=False, indent=2))
