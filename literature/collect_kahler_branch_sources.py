"""Collect primary sources for the first Kahler fourfold exploration."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
sources = [
    ("17_Beauville_1983_Decomposition.pdf",
     "Varietes kahleriennes dont la premiere classe de Chern est nulle",
     "https://math.univ-cotedazur.fr/~beauvill/pubs/jdg.pdf",
     "https://doi.org/10.4310/jdg/1214438181",
     "J. Differential Geom. 18 (1983), 755-782; author-hosted journal PDF"),
    ("18_Huybrechts_2003_Projectivity_erratum.pdf",
     "Erratum: Compact hyperkaehler manifolds: basic results",
     "https://arxiv.org/pdf/math/0106014",
     "https://arxiv.org/abs/math/0106014",
     "arXiv erratum manuscript; published Invent. Math. 152 (2003), 209-212"),
    ("19_Oguiso_2009_Dynamical_degrees.pdf",
     "A remark on dynamical degrees of automorphisms of hyperkahler manifolds",
     "https://arxiv.org/pdf/0901.4827",
     "https://arxiv.org/abs/0901.4827",
     "arXiv manuscript; Manuscripta Math. 130 (2009), 101-111"),
    ("20_Jang_2024_Kummer_rigidity.pdf",
     "Kummer rigidity for hyperkahler automorphisms",
     "https://par.nsf.gov/servlets/purl/10557291",
     "https://www.aimsciences.org/article/doi/10.3934/jmd.2024005",
     "J. Modern Dynamics 20 (2024), 183-213; journal PDF in NSF repository"),
    ("21_OGrady_2022_Modular_sheaves.pdf",
     "Modular sheaves on hyperkahler varieties",
     "https://content.algebraicgeometry.nl/2022-1/2022-1-001.pdf",
     "https://doi.org/10.14231/AG-2022-001",
     "Algebraic Geometry 9 (2022), 1-38; publisher PDF"),
    ("22_OGrady_2024_Kummer_bundles.pdf",
     "Rigid stable rank 4 vector bundles on HK fourfolds of Kummer type",
     "https://epiga.episciences.org/14895/pdf",
     "https://doi.org/10.46298/EPIGA.2024.10857",
     "Epijournal Geom. Algebrique, special volume (2024), article 19; publisher PDF"),
]


def collect(item):
    filename, title, url, landing, note = item
    entry = dict(filename=filename, title=title, download_url=url,
                 landing_url=landing, publication_note=note,
                 collected_utc=datetime.now(timezone.utc).isoformat())
    dest = root / filename
    try:
        if dest.exists():
            data = dest.read_bytes()
            entry["download_status"] = "existing_verified"
        else:
            request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(request, timeout=40) as response:
                data = response.read()
                entry["resolved_url"] = response.geturl()
            if not data.startswith(b"%PDF"):
                raise ValueError("response is not a PDF")
            dest.write_bytes(data)
            entry["download_status"] = "downloaded"
        reader = PdfReader(dest)
        pages = [page.extract_text() or "" for page in reader.pages]
        out = root / "extracted" / (dest.stem + ".txt")
        out.parent.mkdir(exist_ok=True)
        out.write_text("\n\n".join(f"=== PDF PAGE {i+1} ===\n{t}"
                                   for i, t in enumerate(pages)), encoding="utf-8")
        entry.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                     pages=len(pages), extracted_characters=sum(map(len, pages)))
    except Exception as exc:
        entry["download_status"] = "failed"
        entry["error"] = str(exc)
    return entry


with ThreadPoolExecutor(max_workers=3) as pool:
    entries = list(pool.map(collect, sources))

manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
new_names = {e["filename"] for e in entries if e["download_status"] != "failed"}
manifest = [e for e in manifest if e.get("filename") not in new_names]
manifest.extend(e for e in entries if e["download_status"] != "failed")
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
                         encoding="utf-8")
(root / "kahler_source_verification.json").write_text(
    json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(json.dumps(entries, indent=2, ensure_ascii=False))
