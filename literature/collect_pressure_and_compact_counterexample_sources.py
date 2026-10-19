"""Primary journal/author PDFs for notes 55 onward; originals stay separate."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import urllib.request
from pypdf import PdfReader

root = Path(__file__).resolve().parent
entries = [
    dict(filename="49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf",
         title="Automorphisms of surfaces: Kummer rigidity and measure of maximal entropy",
         author="Serge Cantat and Christophe Dupont",
         download_url="https://arxiv.org/pdf/1410.1202",
         landing_url="https://doi.org/10.4171/JEMS/946",
         fallback_urls=["https://perso.univ-rennes1.fr/serge.cantat/Articles/smooth-final.pdf", "http://serge_cantat.pages.math.cnrs.fr/Articles/smooth-final.pdf", "https://arxiv.org/pdf/1410.1202"],
         publication_note="JEMS 22 (2020), 1289-1351; locally stored arXiv:1410.1202v1, 5 October 2014, verified from its margin. Corollaries 1.6 and 1.7 here correspond to 1.7 and 1.8 in the later author-final manuscript. Author-final HTTPS certificate and old host failed; the arXiv primary manuscript was used."),
    dict(filename="50_Rey_Bellet_Young_2008_Large_deviations.pdf",
         title="Large deviations in non-uniformly hyperbolic dynamical systems",
         author="Luc Rey-Bellet and Lai-Sang Young",
         download_url="https://luc-umass.github.io/pdf/lsy1.pdf",
         landing_url="https://doi.org/10.1017/S0143385707000478",
         publication_note="ETDS 28 (2008), 587-612; author-hosted journal PDF. Used for standard pressure/logarithmic-moment background, not to claim its tower theorem verbatim gives the independent all-parameter Gibbs calculation.")
]

def collect(entry):
    path = root / entry['filename']
    if not path.exists():
        failures = []
        for url in [entry['download_url']] + entry.get('fallback_urls', []):
            try:
                request = urllib.request.Request(url, headers={'User-Agent':'Mozilla/5.0'})
                with urllib.request.urlopen(request, timeout=20) as response:
                    data = response.read()
                    entry['resolved_url'] = response.geturl()
                if not data.startswith(b'%PDF'):
                    raise ValueError('not a PDF')
                entry['successful_download_url'] = url
                break
            except Exception as error:
                failures.append({'url':url, 'error':str(error)[:220]})
        else:
            raise RuntimeError(failures)
        entry['download_failures'] = failures
        assert data.startswith(b'%PDF'), entry['filename']
        path.write_bytes(data)
    data = path.read_bytes()
    reader = PdfReader(path)
    text = '\n\n'.join(f'=== PDF PAGE {i+1} ===\n{page.extract_text() or ""}' for i,page in enumerate(reader.pages))
    (root / 'extracted' / (path.stem + '.txt')).write_text(text, encoding='utf-8')
    entry.update(bytes=len(data), pages=len(reader.pages), sha256=hashlib.sha256(data).hexdigest(),
                 collected_utc=datetime.now(timezone.utc).isoformat())
    return entry

with ThreadPoolExecutor(max_workers=2) as pool:
    records = list(pool.map(collect, entries))
manifest_path = root / 'sources_manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
new_names = {item['filename'] for item in records}
manifest = [item for item in manifest if item['filename'] not in new_names] + records
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(records, ensure_ascii=False, indent=2))
