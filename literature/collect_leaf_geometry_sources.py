"""Primary references for leafwise affine and special complex geometry."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

root = Path(__file__).resolve().parent
specifications = [
    ("13_Alekseevsky_Cortes_Devchand_Special_complex_manifolds.pdf",
     "Special complex manifolds",
     "https://arxiv.org/pdf/math/9910091v3",
     "https://arxiv.org/abs/math/9910091",
     "ArXiv v3, 2001-11-05; J. Geom. Phys. 42 (2002), 85-105"),
    ("14_Loustau_Sanders_Bi_Lagrangian_structures.pdf",
     "Bi-Lagrangian structures and Teichmuller theory",
     "https://brice.loustau.eu/ressources/BiLagrangian.pdf",
     "https://arxiv.org/abs/1708.09145",
     "Author-hosted manuscript, version served 2026-10-17"),
]
records = []
for filename, title, url, landing, publication in specifications:
    record = dict(filename=filename, title=title, download_url=url,
                  landing_url=landing, publication_note=publication,
                  collected_utc=datetime.now(timezone.utc).isoformat())
    try:
        path = root / filename
        if path.exists():
            data = path.read_bytes()
            record["download_status"] = "existing_verified"
        else:
            with urlopen(Request(url, headers={"User-Agent": "ResearchLiteratureCollector/1.0"}), timeout=40) as response:
                data = response.read()
                record["resolved_url"] = response.url
            if not data.lstrip().startswith(b"%PDF-"):
                raise ValueError("Response is not a PDF")
            path.write_bytes(data)
            record["download_status"] = "downloaded"
        reader = PdfReader(path)
        text = "\n".join(f"\n===== PDF PAGE {i+1} =====\n{p.extract_text() or ''}"
                         for i, p in enumerate(reader.pages))
        (root / "extracted" / (path.stem + ".txt")).write_text(text, encoding="utf-8")
        record.update(bytes=len(data), sha256=sha256(data).hexdigest(),
                      pages=len(reader.pages), first_page=reader.pages[0].extract_text()[:700])
    except Exception as error:
        record.update(download_status="failed", error=str(error))
    records.append(record)
    print(record["download_status"], filename, record.get("pages"), flush=True)

manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
names = {r["filename"] for r in records}
manifest = [r for r in manifest if r["filename"] not in names] + records
manifest.sort(key=lambda r: r["filename"])
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
(root / "leaf_geometry_source_verification.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
