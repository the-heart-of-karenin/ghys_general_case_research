"""Collect the original deformation-invariance input for the fixed-locus argument."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
name = "32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf"
url = "https://www.math.brown.edu/bhassett/papers/hodge/hodge13.pdf"
path = root / name
entry = dict(
    filename=name,
    title="Hodge theory and Lagrangian planes on generalized Kummer fourfolds",
    download_url=url,
    landing_url="https://doi.org/10.17323/1609-4514-2013-13-1-33-56",
    publication_note="Moscow Mathematical Journal 13 (2013), no. 1, 33-56; author manuscript dated 11 June 2012",
    collected_utc=datetime.now(timezone.utc).isoformat(),
)
if not path.exists():
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=45) as response:
        data = response.read()
        entry["resolved_url"] = response.geturl()
    if not data.startswith(b"%PDF"):
        raise ValueError("Response is not a PDF")
    path.write_bytes(data)
else:
    data = path.read_bytes()
pages = [page.extract_text() or "" for page in PdfReader(path).pages]
(root / "extracted" / (path.stem + ".txt")).write_text(
    "\n\n".join(f"=== PDF PAGE {i + 1} ===\n{text}" for i, text in enumerate(pages)), encoding="utf-8"
)
entry.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pages=len(pages))
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
manifest = [item for item in manifest if item.get("filename") != name] + [entry]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(entry, ensure_ascii=False, indent=2))
