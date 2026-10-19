"""Render complete relevant source pages; visual-review flags are set after inspection."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess

root=Path(__file__).resolve().parent
poppler=Path(r'C:\Users\HUAWEI\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin\pdftoppm.exe')
jobs=[
 ('49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf',1,'compact_CD_version'),
 ('49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf',5,'compact_CD_main'),
 ('49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf',6,'compact_CD_exponents_rank_two'),
 ('49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf',12,'compact_CD_Holder_currents'),
 ('49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf',13,'compact_CD_mixing_green'),
 ('49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf',43,'compact_CD_Ruelle_equality'),
 ('49_Cantat_Dupont_2020_Surface_Kummer_rigidity.pdf',44,'compact_CD_Ruelle_proof'),
 ('50_Rey_Bellet_Young_2008_Large_deviations.pdf',3,'pressure_RBY_scope'),
 ('50_Rey_Bellet_Young_2008_Large_deviations.pdf',17,'pressure_RBY_moments'),
 ('50_Rey_Bellet_Young_2008_Large_deviations.pdf',18,'pressure_RBY_translated'),
 ('34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf',3,'compact_AV_symplectic_rank_two'),
 ('34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf',10,'compact_AV_wall_free'),
 ('34_Amerik_Verbitsky_2017_Construction_automorphisms.pdf',11,'compact_AV_corollary'),
 ('21_OGrady_2022_Modular_sheaves.pdf',15,'compact_OG_blowup_quotient'),
 ('21_OGrady_2022_Modular_sheaves.pdf',16,'compact_OG_quotient_continued'),
 ('20_Jang_2024_Kummer_rigidity.pdf',25,'compact_Jang_flatness'),
 ('20_Jang_2024_Kummer_rigidity.pdf',27,'compact_Jang_nonample'),
 ('45_Young_2002_SRB_survey.pdf',6,'pressure_Young_Gibbs'),
 ('45_Young_2002_SRB_survey.pdf',3,'pressure_Young_equilibrium'),
 ('48_Bressaud_Liverani_2002_Anosov_coupling.pdf',7,'pressure_holonomy_product'),
 ('17_Beauville_1983_Decomposition.pdf',8,'compact_Beauville_8'),
 ('17_Beauville_1983_Decomposition.pdf',9,'compact_Beauville_9'),
 ('17_Beauville_1983_Decomposition.pdf',10,'compact_Beauville_10'),
 ('17_Beauville_1983_Decomposition.pdf',12,'compact_Beauville_12'),
 ('17_Beauville_1983_Decomposition.pdf',13,'compact_Beauville_13'),
 ('17_Beauville_1983_Decomposition.pdf',14,'compact_Beauville_14'),
]

def render(job):
 name,page,label=job
 source=root/name
 out=root/'previews'/label
 if not out.with_suffix('.png').exists():
  subprocess.run([str(poppler),'-f',str(page),'-l',str(page),'-r','110','-singlefile','-png',str(source),str(out)],check=True,capture_output=True,creationflags=subprocess.CREATE_NO_WINDOW)
 return dict(source=str(source),page=page,preview=str(out)+'.png',visually_inspected=False)

with ThreadPoolExecutor(max_workers=3) as pool:
 records=list(pool.map(render,jobs))
(root/'pressure_compact_rendered_pages.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'rendered_full_pages':len(records)}))
