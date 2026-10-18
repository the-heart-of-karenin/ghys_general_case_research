"""Primary source for the smooth nested Hilbert correspondence."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
name = "31_Meachan_2015_Derived_autoequivalences_Kummer.pdf"
url = "https://archive.intlpress.com/site/pub/files/_fulltext/journals/mrl/2015/0022/0004/MRL-2015-0022-0004-a012.pdf"
path = root / name
entry = dict(filename=name, title="Derived autoequivalences of generalised Kummer varieties",
             download_url=url, landing_url="https://doi.org/10.4310/MRL.2015.v22.n4.a12",
             publication_note="Mathematical Research Letters 22 (2015), 1193-1221; Ciaran Meachan",
             collected_utc=datetime.now(timezone.utc).isoformat())
if not path.exists():
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=45) as response:
        data = response.read()
        entry["resolved_url"] = response.geturl()
    if not data.startswith(b"%PDF"):
        raise ValueError("Not a PDF")
    path.write_bytes(data)
else:
    data = path.read_bytes()
pages = [page.extract_text() or "" for page in PdfReader(path).pages]
(root / "extracted" / (path.stem + ".txt")).write_text(
    "\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}" for i, text in enumerate(pages)), encoding="utf-8")
entry.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(), pages=len(pages))
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
manifest = [e for e in manifest if e.get("filename") != name] + [entry]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(entry, ensure_ascii=False, indent=2))
