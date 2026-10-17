"""Collect primary sources for the unpinched symplectic branch."""
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
from urllib.request import Request, urlopen
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parent
SOURCES = [
    ("10_Feres_1995_Invariant_connection.pdf",
     "The invariant connection of a 1/2-pinched Anosov diffeomorphism and rigidity",
     "https://msp.org/pjm/1995/171-1/pjm-v171-n1-p05-s.pdf",
     "https://doi.org/10.2140/pjm.1995.171.139",
     "Pacific Journal of Mathematics 171 (1995), 139-155"),
    ("11_Kalinin_Sadovskaya_Strong_weak_foliations.pdf",
     "Rigidity of strong and weak foliations",
     "https://arxiv.org/pdf/2509.13986v2",
     "https://arxiv.org/abs/2509.13986v2",
     "ArXiv v2 served 2026-10-17; journal DOI 10.3934/jmd.2026009"),
    ("12_Gogolev_Rodriguez_Hertz_2026_Symplecto_rigidity.pdf",
     "Symplecto-rigidity and bootstrap for Anosov symplectomorphisms and contact Anosov flows",
     "https://arxiv.org/pdf/2609.10769v1",
     "https://arxiv.org/abs/2609.10769v1",
     "ArXiv v1, 2026-09-09"),
]

records = []
for filename, title, url, landing, publication in SOURCES:
    target = ROOT / filename
    record = dict(filename=filename, title=title, download_url=url,
                  landing_url=landing, publication_note=publication,
                  collected_utc=datetime.now(timezone.utc).isoformat())
    try:
        if target.exists():
            data = target.read_bytes()
            record["download_status"] = "existing_verified"
        else:
            request = Request(url, headers={"User-Agent": "ResearchLiteratureCollector/1.0"})
            with urlopen(request, timeout=40) as response:
                data = response.read()
                record["resolved_url"] = response.url
            if not data.lstrip().startswith(b"%PDF-"):
                raise ValueError("Response is not a PDF")
            target.write_bytes(data)
            record["download_status"] = "downloaded"
        reader = PdfReader(target)
        text = "\n".join(f"\n===== PDF PAGE {i+1} =====\n{p.extract_text() or ''}"
                         for i, p in enumerate(reader.pages))
        extracted = ROOT / "extracted" / (target.stem + ".txt")
        extracted.write_text(text, encoding="utf-8")
        record.update(bytes=len(data), sha256=sha256(data).hexdigest(),
                      pages=len(reader.pages), first_page=reader.pages[0].extract_text()[:600])
    except Exception as exc:
        record.update(download_status="failed", error=str(exc))
    records.append(record)
    print(record["download_status"], filename, record.get("pages"), flush=True)

manifest = ROOT / "sources_manifest.json"
existing = json.loads(manifest.read_text(encoding="utf-8"))
incoming = {r["filename"] for r in records}
existing = [r for r in existing if r["filename"] not in incoming] + records
existing.sort(key=lambda r: r["filename"])
manifest.write_text(json.dumps(existing, ensure_ascii=False, indent=2), encoding="utf-8")
(ROOT / "symplectic_source_verification.json").write_text(
    json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
