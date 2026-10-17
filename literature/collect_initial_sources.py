"""Download the initial research corpus; preserve URLs and SHA-256 hashes."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from hashlib import sha256
from pathlib import Path
from urllib.request import Request, urlopen
import json

ROOT = Path(__file__).resolve().parent
SOURCES = [
    ("01_Zhang_2026_Codimension_one_v2.pdf",
     "Codimension-one holomorphic Anosov diffeomorphisms",
     "https://arxiv.org/pdf/2609.37695v2",
     "https://arxiv.org/abs/2609.37695",
     "2026 preprint, v2, 2026-10-05"),
    ("02_Zhang_2026_Invariant_complex_structures.pdf",
     "Invariant complex structures for affine automorphisms: a cocycle viewpoint",
     "https://arxiv.org/pdf/2606.17794v1",
     "https://arxiv.org/abs/2606.17794",
     "2026 preprint, v1"),
    ("03_Kalinin_Sadovskaya_Normal_forms_narrow_band.pdf",
     "Normal forms on contracting foliations: smoothness and homogeneous structure",
     "https://vsadovskaya.github.io/Papers/narrow_band.pdf",
     "https://arxiv.org/abs/1612.03454",
     "Author-hosted manuscript; arXiv first submitted 2016"),
    ("04_Kalinin_2020_Contracting_extensions.pdf",
     "Non-stationary normal forms for contracting extensions",
     "https://arxiv.org/pdf/2006.12662",
     "https://arxiv.org/abs/2006.12662",
     "ArXiv manuscript; version served on collection date"),
    ("05_Berteloot_Dupont_Molino_2008_Holomorphic_contractions.pdf",
     "Normalization of bundle holomorphic contractions and applications to dynamics",
     "https://arxiv.org/pdf/0705.2649",
     "https://aif.centre-mersenne.org/articles/10.5802/aif.2409/",
     "ArXiv manuscript of Annales de l'Institut Fourier 58 (2008), 2137-2168"),
    ("06_Melnick_Nonstationary_geometric_structures.pdf",
     "Nonstationary smooth geometric structures for contracting measurable cocycles",
     "https://arxiv.org/pdf/1604.04423",
     "https://arxiv.org/abs/1604.04423",
     "ArXiv manuscript; publication DOI 10.1017/etds.2017.38"),
    ("07_Bera_Verma_Uniform_non_autonomous_basins.pdf",
     "Uniform non-autonomous basins of attraction",
     "https://arxiv.org/pdf/2211.15169",
     "https://arxiv.org/abs/2211.15169",
     "ArXiv manuscript; journal publication Invent. Math. 238 (2024), 995-1040"),
    ("08_Kalinin_Sadovskaya_2003_Quasiconformal_rigidity.pdf",
     "On local and global rigidity of quasiconformal Anosov diffeomorphisms",
     "https://vsadovskaya.github.io/Papers/qcdiff.pdf",
     "https://doi.org/10.1017/S1474748003000161",
     "Author-hosted manuscript; J. Inst. Math. Jussieu 2 (2003), 567-582"),
    ("09_Rodriguez_Hertz_Wang_Higher_rank_rigidity.pdf",
     "Global rigidity of higher rank Anosov algebraic actions",
     "https://arxiv.org/pdf/1304.1234",
     "https://arxiv.org/abs/1304.1234",
     "ArXiv manuscript; Invent. Math. 198 (2014), 165-209"),
]

def collect(spec):
    filename, title, url, landing, status = spec
    record = dict(filename=filename, title=title, download_url=url,
                  landing_url=landing, publication_note=status,
                  collected_utc=datetime.now(timezone.utc).isoformat())
    try:
        target = ROOT / filename
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
        record.update(bytes=len(data), sha256=sha256(data).hexdigest())
    except Exception as exc:
        record.update(download_status="failed", error=str(exc))
    return record

def main():
    records = []
    with ThreadPoolExecutor(max_workers=3) as executor:
        jobs = [executor.submit(collect, spec) for spec in SOURCES]
        for job in as_completed(jobs):
            item = job.result()
            records.append(item)
            print(item["download_status"], item["filename"], flush=True)
    records.sort(key=lambda item: item["filename"])
    (ROOT / "sources_manifest.json").write_text(
        json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Manifest saved:", len(records), "records", flush=True)

if __name__ == "__main__":
    main()
