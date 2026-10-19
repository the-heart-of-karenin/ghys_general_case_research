"""Primary sources for returning to note 30, without merging sources into notes."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
entries = [
    dict(filename="42_Ruelle_Sullivan_1975_Currents.pdf",
         title="Currents, flows and diffeomorphisms",
         author="David Ruelle and Dennis Sullivan",
         download_url="https://www.math.stonybrook.edu/~dennis/publications/PDF/DS-pub-0023.pdf",
         landing_url="https://doi.org/10.1016/0040-9383(75)90016-6",
         publication_note="Topology 14 (1975), 319-327; publisher-formatted PDF on Sullivan's institutional site."),
    dict(filename="43_De_Thelin_Dinh_2012_Dynamics_Kahler.pdf",
         title="Dynamics of automorphisms on compact Kahler manifolds",
         author="Henry de Thelin and Tien-Cuong Dinh",
         download_url="https://arxiv.org/pdf/1009.5796",
         landing_url="https://arxiv.org/abs/1009.5796",
         publication_note="Advances in Mathematics 229 (2012), 2640-2655; arXiv manuscript."),
    dict(filename="44_Dinh_Sibony_2010_Superpotentials_Kahler.pdf",
         title="Super-potentials for currents on compact Kahler manifolds and dynamics of automorphisms",
         author="Tien-Cuong Dinh and Nessim Sibony",
         download_url="https://arxiv.org/pdf/0804.0860",
         landing_url="https://arxiv.org/abs/0804.0860",
         publication_note="Journal of Algebraic Geometry 19 (2010), 473-529; arXiv manuscript."),
    dict(filename="45_Young_2002_SRB_survey.pdf",
         title="What are SRB measures, and which dynamical systems have them?",
         author="Lai-Sang Young",
         download_url="https://math.nyu.edu/~lsy/papers/SRBsurvey.pdf",
         landing_url="https://math.nyu.edu/~lsy/publications-all.html",
         publication_note="Journal of Statistical Physics 108 (2002), 733-754; author-hosted manuscript. Used as an original-author survey for SRB uniqueness, not as a new research theorem."),
    dict(filename="46_Ledrappier_Young_1985_Entropy_I.pdf",
         title="The metric entropy of diffeomorphisms. Part I: Characterization of measures satisfying Pesin's entropy formula",
         author="Francois Ledrappier and Lai-Sang Young",
         download_url="https://math.nyu.edu/~lsy/papers/metric-entropy-part1.pdf",
         landing_url="https://math.nyu.edu/~lsy/publications-all.html",
         publication_note="Annals of Mathematics 122 (1985), 509-539; original paper hosted by coauthor."),
]

def collect(entry):
    path = root / entry["filename"]
    if not path.exists():
        req = urllib.request.Request(entry["download_url"], headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=60) as response:
            data = response.read()
            entry["resolved_url"] = response.geturl()
        if not data.startswith(b"%PDF"):
            raise ValueError((entry["filename"], data[:80]))
        path.write_bytes(data)
    data = path.read_bytes()
    pages = [page.extract_text() or "" for page in PdfReader(path).pages]
    (root/"extracted"/(path.stem+".txt")).write_text(
        "\n\n".join(f"=== PDF PAGE {i+1} ===\n{text}" for i,text in enumerate(pages)), encoding="utf-8")
    entry.update(bytes=len(data), pages=len(pages), sha256=hashlib.sha256(data).hexdigest(),
                 collected_utc=datetime.now(timezone.utc).isoformat())
    return entry

with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(collect, entries))
manifest_path = root / "sources_manifest.json"
manifest = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
names = {item["filename"] for item in records}
manifest = [item for item in manifest if item["filename"] not in names] + records
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
print(json.dumps(records, ensure_ascii=False, indent=2))
