"""Only the newly used primary pages for notes 65-68; old audits are reused."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r'C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
sources = [
    ('58_Hasegawa_Sillari_Tomassini_2026_Invariant_forms_Dolbeault.pdf', [1, 2, 15, 16], 'progress_HST'),
    ('59_Wehler_2026_Teichmuller_moduli_complex_nilmanifolds.pdf', [3, 12, 13, 14, 15, 16], 'progress_Wehler'),
    ('60_Hasegawa_Rollenske_Sillari_Tomassini_Wehler_2026_Biholomorphism_type.pdf', [1], 'progress_cover'),
]
jobs = [(name, page, f'{label}_{page}') for name, pages, label in sources for page in pages]
output_path = root / 'nil_progression_rendered_pages.json'
previous = json.loads(output_path.read_text(encoding='utf-8')) if output_path.exists() else []
seen = {(entry['source'], entry['page']): entry['visually_inspected'] for entry in previous}


def render(job):
    name, page, label = job
    target = root / 'previews' / label
    if not target.with_suffix('.png').exists():
        subprocess.run([str(poppler), '-f', str(page), '-l', str(page), '-r', '110',
                        '-singlefile', '-png', str(root/name), str(target)], check=True,
                       capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=str(root/name), page=page, preview=str(target)+'.png',
                visually_inspected=seen.get((str(root/name), page), False))


with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(render, jobs))
output_path.write_text(json.dumps(records, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps(dict(full_pages=len(records))))
