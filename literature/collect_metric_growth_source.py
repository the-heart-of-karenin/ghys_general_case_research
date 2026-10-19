"""Two primary sources for the metric-growth and leafwise-tail estimates."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root=Path(__file__).resolve().parent
entries=[dict(filename="47_De_Thelin_2008_Lyapunov_exponents.pdf",
           title="Sur les exposants de Lyapounov des applications meromorphes",
           author="Henry de Thelin",
           download_url="https://arxiv.org/pdf/math/0609628",
           landing_url="https://doi.org/10.1007/s00222-007-0095-5",
           publication_note="Inventiones Mathematicae 172 (2008), 89-116; arXiv author manuscript, first submitted 2006. Text extraction has broken font encoding; theorem verified on rendered PDF page 2."),
         dict(filename="48_Bressaud_Liverani_2002_Anosov_coupling.pdf",
              title="Anosov diffeomorphisms and coupling",
              author="Xavier Bressaud and Carlangelo Liverani",
              download_url="https://www.math.univ-toulouse.fr/~bressaud/Papiers/ForwarCouplingDec2000.pdf",
              landing_url="https://doi.org/10.1017/S0143385702000056",
              publication_note="Ergodic Theory and Dynamical Systems 22 (2002), 129-152; author-hosted manuscript dated December 20, 2000. Proposition 4.1 used only for its two-sided Jacobian bound.")]

def collect(entry):
    path=root/entry["filename"]
    if not path.exists():
        req=urllib.request.Request(entry["download_url"],headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req,timeout=60) as response:
            data=response.read()
            entry["resolved_url"]=response.geturl()
        assert data.startswith(b"%PDF")
        path.write_bytes(data)
    data=path.read_bytes()
    pages=[page.extract_text() or "" for page in PdfReader(path).pages]
    (root/"extracted"/(path.stem+".txt")).write_text(
        "\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}" for i,text in enumerate(pages)),encoding="utf-8")
    entry.update(bytes=len(data),pages=len(pages),sha256=hashlib.sha256(data).hexdigest(),
                 collected_utc=datetime.now(timezone.utc).isoformat())
    return entry

with ThreadPoolExecutor(max_workers=2) as pool:
    records=list(pool.map(collect,entries))
manifest_path=root/"sources_manifest.json"
manifest=json.loads(manifest_path.read_text(encoding="utf-8-sig"))
names={entry["filename"] for entry in records}
manifest=[record for record in manifest if record["filename"] not in names]+records
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
print(json.dumps(records,ensure_ascii=False,indent=2))
