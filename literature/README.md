# 文献目录

收集日期：2026-10-17。共十六篇 PDF 已下载并核验 PDF 文件头；URL、下载时间、版本说明、大小及 SHA-256 见 sources_manifest.json。arXiv 手稿与期刊最终版的区别保存在版本说明中。

| 编号 | 文献 | 首先阅读的内容 | 在规划中的作用 |
|---|---|---|---|
| 01 | Zhang 2026, Codimension-one holomorphic Anosov diffeomorphisms, v2 | §1.2、Theorem 1.2、§5 | 一般化障碍；环面拓扑分支的已知出口；两侧非全纯模型 |
| 02 | Zhang 2026, Invariant complex structures for affine automorphisms, v1 | Corollary D、§2.2、Corollary E | 双 Lipschitz 到双全纯的接口；一般模型定义 |
| 03 | Kalinin–Sadovskaya, Normal forms on contracting foliations | 引言、主定理、谱条件 | 相干逐叶正规形及有限维转移群 |
| 04 | Kalinin 2020, Non-stationary normal forms for contracting extensions | 主定理及正规形唯一性 | 精确追踪共振与中心化子 |
| 05 | Berteloot–Dupont–Molino 2008, Normalization of bundle holomorphic contractions | 全纯正规形定理与其假设 | 优先使用全纯丛版本，避免直接把实结果称为全纯结果 |
| 06 | Melnick, Nonstationary smooth geometric structures | 引言、几何结构解释 | 正规形的有限阶几何表达 |
| 07 | Bera–Verma, Uniform non-autonomous basins of attraction | 主定理及稳定流形应用 | 单叶统一化，避免重复攻克已有结果 |
| 08 | Kalinin–Sadovskaya 2003, Quasiconformal rigidity | Theorem 1.1 | 附加拟共形假设下的已知刚性校验场 |
| 09 | Rodriguez Hertz–Wang, Higher rank rigidity | 主定理及无秩一因子条件 | 附加高秩作用分支的已知终点 |
| 10 | Feres 1995, The invariant connection of a 1/2-pinched Anosov diffeomorphism and rigidity | Theorems 2、4、6，p.141 | 审查有限正则性分类是否确实撤去了非共振；答案是否定的 |
| 11 | Kalinin–Sadovskaya, Rigidity of strong and weak foliations | Theorem 1.6；holonomy 与正规形接口 | 保辛扰动的已知刚性条件；不能自动套用于任意 X |
| 12 | Gogolev–Rodriguez Hertz 2026, Symplecto-rigidity and bootstrap | Theorem 1.6、Corollary 1.7、Conjecture 1.1 | 区分已有 C1 共轭的升级、pinching，以及尚未证明的 symplecto-rigidity |
| 13 | Alekseevsky–Cortés–Devchand, Special complex manifolds | 定义、联络族等价性、外在全纯浸入 | 审查实 Bott 坐标的多重调和性；不将 d∇J=0 误作 ∇J=0 |
| 14 | Loustau–Sanders, Bi-Lagrangian structures and Teichmüller theory | §1.3 实与复 Bott；Theorems 1.10–1.12 | 实 Bott 仿射背景；不把复范畴适配坐标用于仅各叶全纯的实叶状结构 |
| 15 | Journé 1988, A Regularity Lemma for Functions of Several Variables | p.187 主定理 | 将两侧一致逐叶 C∞ 升级为整体 C∞；原始扫描页已渲染核验 |
| 16 | Zeghib 2004, Lipschitz Regularity in Some Geometric Problems | §2、§8–9；期刊 pp.63、77 | 审查由不相交性取得横向 Lipschitz 的适用范围；高余维中不能直接移植标量正锥论证 |

主要原始入口：

- https://arxiv.org/abs/2609.37695
- https://arxiv.org/abs/2606.17794
- https://arxiv.org/abs/1612.03454
- https://arxiv.org/abs/2006.12662
- https://aif.centre-mersenne.org/articles/10.5802/aif.2409/
- https://arxiv.org/abs/1604.04423
- https://link.springer.com/article/10.1007/s00222-024-01295-9
- https://doi.org/10.1017/S1474748003000161
- https://arxiv.org/abs/1304.1234
- https://msp.org/pjm/1995/171-1/pjm-v171-n1-p05-s.pdf
- https://arxiv.org/abs/2509.13986v2
- https://arxiv.org/abs/2609.10769v1
- https://arxiv.org/abs/math/9910091
- https://brice.loustau.eu/ressources/BiLagrangian.pdf
- https://doi.org/10.4171/RMI/69
- https://perso.ens-lyon.fr/zeghib/Lipschitz.regularity.pdf

已有 Ghys 1995、Cantat 2004、Benoist–Labourie 1993 的原始 PDF 仍保留在 ../../2/historical_literature/，未重复下载或修改。

extracted/ 和 previews/ 为阅读辅助，不是独立研究结论。下载程序只下载公开 PDF，不执行论文中的任何内容。

第二批三篇的页数、首屏提取及散列另存 symplectic_source_verification.json；Feres p.141、Kalinin–Sadovskaya PDF p.5、Gogolev–Rodriguez Hertz PDF p.2 已按渲染图像核对。

13–14 的元数据在 leaf_geometry_source_verification.json；special complex 等价性、实 Bott 页及复 Bott 页已渲染核对。15 的元数据在 journe_source_verification.json；PDF 为扫描图像，pypdf 首屏提取为空，主定理通过 previews/Journe_theorem.png 直接核验，不能把空文本当作未含定理。

16 的元数据在 holonomy_geometry_source_verification.json；PDF 第 7、21 页（期刊 pp.63、77）已按渲染图像核对。该文作为适用范围与障碍背景，未提供本研究目标所缺的无夹逼 C1 定理。
