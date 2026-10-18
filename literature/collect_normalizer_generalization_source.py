"""One primary source for the sixfold values used to delimit the extension."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
entry = dict(filename="40_Oberdieck_Song_Voisin_2022_Cobordism_HK.pdf",
             title="Hilbert schemes of K3 surfaces, generalized Kummer, and cobordism classes of hyper-Kahler manifolds",
             download_url="https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/cobordismHKsoumis.pdf",
             landing_url="https://doi.org/10.4310/PAMQ.2022.v18.n4.a13",
             publication_note="Pure and Applied Mathematics Quarterly 18 (2022), 1723-1748; 17-page author manuscript; sixfold Chern-number matrix on PDF p.12 is used only for the Euler values and boundary check")
path = root / entry["filename"]
if not path.exists():
    req = urllib.request.Request(entry["download_url"], headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=45) as response:
        data = response.read()
        entry["resolved_url"] = response.geturl()
    assert data.startswith(b"%PDF")
    path.write_bytes(data)
else:
    data = path.read_bytes()
pages = [page.extract_text() or "" for page in PdfReader(path).pages]
(root / "extracted" / (path.stem + ".txt")).write_text(
    "\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}" for i, text in enumerate(pages)), encoding="utf-8")
entry.update(bytes=len(data), pages=len(pages), sha256=hashlib.sha256(data).hexdigest(),
             collected_utc=datetime.now(timezone.utc).isoformat())
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
manifest = [x for x in manifest if x["filename"] != entry["filename"]] + [entry]
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps(entry, ensure_ascii=False, indent=2))
