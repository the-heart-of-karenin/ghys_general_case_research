"""Render complete relevant pages for the model-classification source audit."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess

root = Path(__file__).resolve().parent
poppler = Path(r'C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
jobs = [
    ('51_Lauret_Will_2004_Anosov_up_to_dimension_8.pdf', 1, 'nil_LW_2004_version'),
    ('53_Lauret_Will_Nilmanifolds_dimension_8_journal_author.pdf', 1, 'nil_LW_2007_cover'),
    ('53_Lauret_Will_Nilmanifolds_dimension_8_journal_author.pdf', 3, 'nil_LW_lattice_rational_structure'),
    ('53_Lauret_Will_Nilmanifolds_dimension_8_journal_author.pdf', 5, 'nil_LW_units_definition'),
    ('53_Lauret_Will_Nilmanifolds_dimension_8_journal_author.pdf', 8, 'nil_LW_brackets'),
    ('53_Lauret_Will_Nilmanifolds_dimension_8_journal_author.pdf', 14, 'nil_LW_real_classification'),
    ('53_Lauret_Will_Nilmanifolds_dimension_8_journal_author.pdf', 18, 'nil_LW_table3'),
    ('53_Lauret_Will_Nilmanifolds_dimension_8_journal_author.pdf', 19, 'nil_LW_rational_scope'),
    ('54_Latorre_Ugarte_Villacampa_Ascending_central_series.pdf', 3, 'nil_LUV_definitions'),
    ('54_Latorre_Ugarte_Villacampa_Ascending_central_series.pdf', 9, 'nil_LUV_center_bound'),
    ('54_Latorre_Ugarte_Villacampa_Ascending_central_series.pdf', 13, 'nil_LUV_eight_dimensional_corollary'),
    ('52_Bazzoni_Freibert_Latorre_Meinke_Complex_symplectic_Lie_algebras.pdf', 1, 'nil_BFLM_version'),
    ('52_Bazzoni_Freibert_Latorre_Meinke_Complex_symplectic_Lie_algebras.pdf', 17, 'nil_BFLM_center_background'),
    ('52_Bazzoni_Freibert_Latorre_Meinke_Complex_symplectic_Lie_algebras.pdf', 20, 'nil_BFLM_oxidation_scope'),
    ('02_Zhang_2026_Invariant_complex_structures.pdf', 3, 'nil_Zhang_known_invariant_structures'),
    ('02_Zhang_2026_Invariant_complex_structures.pdf', 4, 'nil_Zhang_known_bilipschitz_interface'),
]

previous_path = root / 'nil_model_rendered_pages.json'
previous = json.loads(previous_path.read_text(encoding='utf-8')) if previous_path.exists() else []
reviewed = {(entry['source'], entry['page']): entry['visually_inspected'] for entry in previous}


def render(job):
    name, page, label = job
    output = root / 'previews' / label
    if not output.with_suffix('.png').exists():
        subprocess.run([str(poppler), '-f', str(page), '-l', str(page), '-r', '110',
                        '-singlefile', '-png', str(root / name), str(output)], check=True,
                       capture_output=True, creationflags=subprocess.CREATE_NO_WINDOW)
    return dict(source=str(root / name), page=page, preview=str(output) + '.png',
                visually_inspected=reviewed.get((str(root / name), page), False))


with ThreadPoolExecutor(max_workers=3) as pool:
    records = list(pool.map(render, jobs))
(root / 'nil_model_rendered_pages.json').write_text(
    json.dumps(records, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(rendered_full_pages=len(records))))
