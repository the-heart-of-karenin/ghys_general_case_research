"""Primary sources for the K3-square periodic-surface audit."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
jobs = [
    dict(filename="33_Mongardi_2012_Symplectic_involutions_K3_square.pdf",
         title="Symplectic involutions on deformations of K3^[2]",
         download_url="https://arxiv.org/pdf/1107.2854",
         landing_url="https://doi.org/10.2478/s11533-012-0073-z",
         publication_note="Central European Journal of Mathematics 10 (2012), 1472-1485; arXiv v3 margin dated 9 May 2012, downloaded manuscript title date 8 March 2021; 17 pages, not the journal pagination"),
    dict(filename="34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf",
         title="Construction of automorphisms of hyperkahler manifolds",
         download_url="https://www.imo.universite-paris-saclay.fr/~amerik/articles/sublattices.pdf",
         landing_url="https://doi.org/10.1112/S0010437X17007138",
         publication_note="Compositio Mathematica 153 (2017), 1610-1621; author manuscript dated April 2016"),
    dict(filename="35_Cantat_2001_Dynamics_K3_surfaces.pdf",
         title="Dynamique des automorphismes des surfaces K3",
         download_url="https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6611-11511_2006_Article_BF02392831.pdf",
         landing_url="https://doi.org/10.1007/BF02392831",
         publication_note="Acta Mathematica 187 (2001), 1-57; original journal PDF"),
    dict(filename="36_Lesieutre_Satriano_2021_Canonical_heights.pdf",
         title="Canonical Heights on Hyper-Kahler Varieties and the Kawaguchi-Silverman Conjecture",
         download_url="https://www.math.uwaterloo.ca/~msatrian/papers/Canonical-heights-hyperkahler.pdf",
         landing_url="https://doi.org/10.1093/imrn/rnz067",
         publication_note="International Mathematics Research Notices 2021, no. 10; advance journal PDF published online in 2019, 38 pages; used for comparison with periodic-subvariety results, not as a proof input for note 41"),
]

def collect(item):
    item = dict(item)
    path = root / item["filename"]
    if path.exists():
        data = path.read_bytes()
    else:
        req = urllib.request.Request(item["download_url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=45) as response:
            data = response.read()
            item["resolved_url"] = response.geturl()
        if not data.startswith(b"%PDF"):
            raise ValueError(f"Not a PDF: {item['filename']}")
        path.write_bytes(data)
    pages = [page.extract_text() or "" for page in PdfReader(path).pages]
    (root / "extracted" / (path.stem + ".txt")).write_text(
        "\n\n".join(f"=== PDF PAGE {i + 1} ===\n{text}" for i, text in enumerate(pages)), encoding="utf-8")
    item.update(bytes=len(data), sha256=hashlib.sha256(data).hexdigest(),
                pages=len(pages), collected_utc=datetime.now(timezone.utc).isoformat())
    return item

with ThreadPoolExecutor(max_workers=3) as pool:
    entries = list(pool.map(collect, jobs))
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
names = {entry["filename"] for entry in entries}
manifest = [entry for entry in manifest if entry.get("filename") not in names] + entries
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps([{k: item[k] for k in ("filename", "pages", "bytes", "sha256")} for item in entries], indent=2))
