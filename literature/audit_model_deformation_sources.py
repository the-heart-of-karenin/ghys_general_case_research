"""Recheck the original files and record explicitly reviewed full pages."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
from pypdf import PdfReader

root = Path(__file__).resolve().parent
manifest_path = root / 'sources_manifest.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8-sig'))
by_name = {entry['filename']: entry for entry in manifest}
updates = {
    '55_Console_Fino_2001_Dolbeault_nilmanifolds.pdf':
        'Transformation Groups 6 (2001), 111-124; stored arXiv:math/9803135v2, 23 January 2001, 15 pages. Scalar Dolbeault background; tangent-coefficient input is verified directly in file 57.',
    '57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf':
        'International Journal of Mathematics 17(4) (2006), 401-416; download is arXiv:math/0506314v1, margin 15 June 2005, but title page reads November 9, 2018. Both dates recorded without inferring file-generation history. Theorems 1-3 directly checked.',
}
for name, note in updates.items():
    by_name[name]['publication_note'] = note
manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

rendered_path = root / 'model_deformation_rendered_pages.json'
rendered = json.loads(rendered_path.read_text(encoding='utf-8'))
# Every pair below was actually displayed in full via view_image in this turn.
reviewed = {
    '01_Zhang_2026_Codimension_one_v2.pdf': [17],
    '02_Zhang_2026_Invariant_complex_structures.pdf': [3, 4],
    '55_Console_Fino_2001_Dolbeault_nilmanifolds.pdf': [1, 2],
    '56_Rollenske_2009_Dolbeault_small_deformations_nilmanifolds.pdf': [1, 14, 16, 17],
    '57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf': [1, 2, 5, 8, 11, 12, 13],
}
for item in rendered:
    name = Path(item['source']).name
    assert item['page'] in reviewed[name]
    assert Path(item['preview']).is_file()
    item['visually_inspected'] = True
rendered_path.write_text(json.dumps(rendered, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

roles = {
    '01_Zhang_2026_Codimension_one_v2.pdf':
        'Existing six-dimensional non-holomorphic-splitting nil model; no attribution of the new symplectic normal-form calculation to this page.',
    '02_Zhang_2026_Invariant_complex_structures.pdf':
        'Scope comparison only: invariant structures and the already-bi-Lipschitz bootstrap.',
    '55_Console_Fino_2001_Dolbeault_nilmanifolds.pdf':
        'Scalar rational/abelian Dolbeault background, not a substitute for tangent-coefficient cohomology.',
    '56_Rollenske_2009_Dolbeault_small_deformations_nilmanifolds.pdf':
        'Actual graph families, natural tangent cohomology, convergent complete left-invariant Kuranishi family under the applicable hypotheses.',
    '57_Console_Fino_Poon_Stability_abelian_complex_structures.pdf':
        'Primary input: abelian-base global tangent cohomology (Theorem 1), invariant harmonic theory (Theorem 2), actual complete invariant Kuranishi family (Theorem 3). Does not itself normalize the varying automorphism.',
}
sources = []
for name, pages in reviewed.items():
    data = (root / name).read_bytes()
    assert data.startswith(b'%PDF-'), name
    digest = hashlib.sha256(data).hexdigest()
    assert digest == by_name[name]['sha256'], name
    count = len(PdfReader(root / name).pages)
    assert max(pages) <= count
    sources.append(dict(filename=name, absolute_path=str(root / name),
                        bytes=len(data), pages=count, sha256=digest,
                        reviewed_full_pages=pages,
                        all_reviewed_pages_visually_inspected=True,
                        role=roles[name], publication_note=by_name[name].get('publication_note')))

audit = dict(
    audited_utc=datetime.now(timezone.utc).isoformat(),
    purpose='Notes 61-63: exact fixed-F model moduli, actual local normalization of varying holomorphic automorphisms, independent global first-order verification.',
    manifest_count=len(manifest), new_pdf_files=[by_name[name] for name in list(reviewed)[2:]],
    source_count=len(sources), sources=sources,
    rendered_full_pages=len(rendered), all_pages_visually_inspected=True,
    actual_completeness_input='Known convergent marked Kuranishi slice plus independently proved nonlinear elliptic near-identity mapping lemma; not merely a formal deformation comparison.',
    independent_results='Two-step small-biholomorphism lemma; actual local conjugacy to the fixed F; six/four/eight complex parameter classification for the specified model.',
    novelty='Not confirmed; old invariant Kuranishi theorems explicitly attributed.',
    mathematical_limit='Local model theorem only; no arbitrary global Ghys classification, no IHS exclusion, no general transverse-regularity theorem.'
)
(root / 'model_deformation_source_audit.json').write_text(
    json.dumps(audit, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(dict(manifest_count=len(manifest), sources=len(sources),
                      full_pages=len(rendered), hash_checks='passed',
                      visually_inspected='all recorded full pages')))
