"""One primary source for faithfulness on K3^[n]-type deformations."""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
entry = dict(filename="41_Oguiso_2020_Cohomologically_trivial_automorphisms.pdf",
             title="No cohomologically trivial nontrivial automorphism of generalized Kummer manifolds",
             author="Keiji Oguiso",
             download_url="https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0027763018000296",
             landing_url="https://doi.org/10.1017/nmj.2018.29",
             publication_note="Nagoya Mathematical Journal 239 (2020), 110-122; first published online 2018. Theorem 5.1 concerns faithfulness on H2 for K3^[n]-type deformations.")
path = root / entry["filename"]
if not path.exists():
    req = urllib.request.Request(entry["download_url"], headers={"User-Agent":"Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=40) as response:
        data = response.read()
        entry["resolved_url"] = response.geturl()
    assert data.startswith(b"%PDF"), data[:50]
    path.write_bytes(data)
else:
    data = path.read_bytes()
pages = [page.extract_text() or "" for page in PdfReader(path).pages]
(root / "extracted" / (path.stem + ".txt")).write_text(
    "\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}" for i,text in enumerate(pages)),encoding="utf-8")
entry.update(bytes=len(data),pages=len(pages),sha256=hashlib.sha256(data).hexdigest(),
             collected_utc=datetime.now(timezone.utc).isoformat())
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
manifest = [item for item in manifest if item["filename"] != entry["filename"]]+[entry]
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(entry,ensure_ascii=False,indent=2))
for i,page in enumerate(pages):
    if "Theorem 5.1" in page or "Theorem5.1" in page:
        print(f"Theorem 5.1 located on PDF page {i+1}")
