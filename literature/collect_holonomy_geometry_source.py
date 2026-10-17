"""Collect the primary geometric regularity reference for notes 17-21."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

root = Path(__file__).resolve().parent
filename = "16_Zeghib_2004_Lipschitz_regularity.pdf"
path = root / filename
url = "https://perso.ens-lyon.fr/zeghib/Lipschitz.regularity.pdf"
record = dict(filename=filename, title="Lipschitz Regularity in Some Geometric Problems",
              download_url=url, landing_url=url,
              publication_note="Geometriae Dedicata 107 (2004), 57-83; author-hosted journal PDF",
              collected_utc=datetime.now(timezone.utc).isoformat())
if path.exists():
    data = path.read_bytes()
    record["download_status"] = "existing_verified"
else:
    request = Request(url, headers={"User-Agent": "ResearchLiteratureCollector/1.0"})
    with urlopen(request, timeout=40) as response:
        data = response.read()
        record["resolved_url"] = response.url
    if not data.lstrip().startswith(b"%PDF-"):
        raise ValueError("Response is not a PDF")
    path.write_bytes(data)
    record["download_status"] = "downloaded"
reader = PdfReader(path)
extracted = "\n".join(f"\n===== PDF PAGE {i+1} =====\n{page.extract_text() or ''}"
                       for i, page in enumerate(reader.pages))
(root/"extracted"/(path.stem+".txt")).write_text(extracted, encoding="utf-8")
record.update(bytes=len(data), sha256=sha256(data).hexdigest(), pages=len(reader.pages),
              first_page=reader.pages[0].extract_text()[:750])
manifest_path=root/"sources_manifest.json"
manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
manifest=[entry for entry in manifest if entry["filename"]!=filename]+[record]
manifest.sort(key=lambda entry:entry["filename"])
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding="utf-8")
(root/"holonomy_geometry_source_verification.json").write_text(
    json.dumps(record,ensure_ascii=False,indent=2),encoding="utf-8")
print(record["download_status"], filename, record["pages"], "pages")
print(record["first_page"])
