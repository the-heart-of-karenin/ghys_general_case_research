"""Download and verify the primary regularity lemma used in note 14."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

root = Path(__file__).resolve().parent
filename = "15_Journe_1988_Regularity_lemma.pdf"
url = "https://ems.press/content/serial-article-files/37769"
path = root / filename
record = dict(
    filename=filename,
    title="A Regularity Lemma for Functions of Several Variables",
    download_url=url,
    landing_url="https://doi.org/10.4171/RMI/69",
    publication_note="Rev. Mat. Iberoam. 4 (1988), no. 2; original publisher PDF",
    collected_utc=datetime.now(timezone.utc).isoformat(),
)
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
extracted = "\n".join(
    f"\n===== PDF PAGE {i+1} =====\n{page.extract_text() or ''}"
    for i, page in enumerate(reader.pages)
)
(root / "extracted" / (path.stem + ".txt")).write_text(extracted, encoding="utf-8")
record.update(bytes=len(data), sha256=sha256(data).hexdigest(),
              pages=len(reader.pages), first_page=reader.pages[0].extract_text()[:900])
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
manifest = [item for item in manifest if item["filename"] != filename] + [record]
manifest.sort(key=lambda item: item["filename"])
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
(root / "journe_source_verification.json").write_text(
    json.dumps(record, ensure_ascii=False, indent=2), encoding="utf-8")
print(record["download_status"], filename, "pages", record["pages"])
print(record["first_page"])
