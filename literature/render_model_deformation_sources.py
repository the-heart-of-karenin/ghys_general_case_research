"""Complete-page previews for the source audit of notes 61-63."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r'C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
jobs = [
    ('01_Zhang_2026_Codimension_one_v2.pdf', 17, 'deform_Zhang_model'),
    ('02_Zhang_2026_Invariant_complex_structures.pdf', 3, 'nil_Zhang_known_invariant_structures'),
    ('02_Zhang_2026_Invariant_complex_structures.pdf', 4, 'nil_Zhang_known_bilipschitz_interface'),
    ('55_Console_Fino_2001_Dolbeault_nilmanifolds.pdf', 1, 'deform_CF_version'),
    ('55_Console_Fino_2001_Dolbeault_nilmanifolds.pdf', 2, 'deform_CF_rational_theorem'),
    ('56_Rollenske_2009_Dolbeault_small_deformations_nilmanifolds.pdf', 1, 'deform_Rollenske_version'),
    ('56_Rollenske_2009_Dolbeault_small_deformations_nilmanifolds.pdf', 14, 'deform_Rollenske_graphs'),
    ('56_Rollenske_2009_Dolbeault_small_deformations_nilmanifolds.pdf', 16, 'deform_Rollenske_tangent_cohomology'),
    ('56_Rollenske_2009_Dolbeault_small_deformations_nilmanifolds.pdf', 17, 'deform_Rollenske_invariant_Kuranishi'),
    ('57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf', 1, 'deform_CFP_version'),
    ('57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf', 2, 'deform_CFP_scope'),
    ('57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf', 5, 'deform_CFP_vector_Dolbeault'),
    ('57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf', 8, 'deform_CFP_global_cohomology'),
    ('57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf', 11, 'deform_CFP_harmonic_comparison'),
    ('57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf', 12, 'deform_CFP_Kuranishi_graphs'),
    ('57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf', 13, 'deform_CFP_invariant_not_necessarily_abelian'),
]
record_path = root / 'model_deformation_rendered_pages.json'
previous = json.loads(record_path.read_text(encoding='utf-8')) if record_path.exists() else []
viewed = {(entry['source'], entry['page']): entry['visually_inspected'] for entry in previous}


def render(job):
    name, page, label = job
    output = root / 'previews' / label
    if not output.with_suffix('.png').exists():
        subprocess.run([str(poppler), '-f', str(page), '-l', str(page), '-r', '110',
                        '-singlefile', '-png', str(root / name), str(output)], check=True,
                       capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=str(root / name), page=page, preview=str(output) + '.png',
                visually_inspected=viewed.get((str(root / name), page), False))


with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(render, jobs))
record_path.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(rendered_full_pages=len(records))))
