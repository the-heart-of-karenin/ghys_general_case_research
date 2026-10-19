# 模型小变形：文献分工、实际完备性及新颖性范围

日期：2026-10-18。对应 notes/61–63。原始 PDF 与本文独立推导继续分开保存。

## 1. 这一阶段得到什么

61：对 05 的紧致复六维二步模型，固定其 Anosov 格自同构 F，精确穷尽所有小不变复结构（六复参数）及承认不变闭复辛形式的分支（四个复结构参数，加四个指定形式参数）。

62：证明一个独立的小映射引理。在二步格商上，如果基点 J₀ 的全部全局全纯向量场都左不变，那么附近左不变复结构之间、足够接近恒等的双全纯映射只能为右平移。证明使用精确二步 Maurer–Cartan 公式、去平均值、过定椭圆估计与小非线性误差吸收。

将该引理与已知收敛的 Kuranishi 左不变变形族结合，再用 F−I 的有限维可逆性，实际把变化的 f 也共轭回 F。因此得到全部一般小变形的局部正规形，并由 expansivity 得到小共轭和参数的唯一性。这一步是实际小映射论证，不是从形式级数完备性猜测收敛。

同一证明覆盖任何二步、基点 J₀ 为 abelian 的双曲格自同构。两个全局输入在该类别由旧定理自动满足；八参数公式则专属于当前六维模型。

63：用全局自然 Dolbeault 同构独立计算 h¹=24，F 固定 H¹ 六维，一般保辛三元组的一阶商八维。只做计算核验，不用这一阶计数替代 62 的实际完备性证明。

## 2. 下载、版本与准确使用范围

### 55：Console–Fino

- 下载：https://arxiv.org/pdf/math/9803135
- 实存 arXiv:math/9803135v2，边注 2001-01-23，15 页。
- 期刊：Transformation Groups 6 (2001), 111–124，DOI 10.1007/BF01597131。
- PDF pp.1–2 已查看完整图像。Theorem B 是 rational 结构的标量 Dolbeault 同构；同页也说明 abelian 情形。
- 角色：原始背景与适用范围核对。本文切丛系数同构直接用 57，不把 55 的标量命题无解释地换为切丛命题，也不必另证本例 J₀ 对格有理。

### 56：Rollenske

- 下载：https://arxiv.org/pdf/0709.0467v2
- 实存 v2，2009-01-20，19 页。
- 期刊：Journal of the London Mathematical Society 79(2) (2009), 346–362，DOI 10.1112/jlms/jdn076。
- PDF pp.1、14、16–17 的完整图像已核验。
- p.14：不变复结构的图参数及实际族。
- p.16：Corollary 2.5 是自然切丛上同调同构；Theorem 2.6 在所列假设下给出全部小变形仍左不变。
- p.17：Kuranishi Green 迭代在不变张量内进行，并使用既有 Kuranishi 理论的收敛与局部完备性。
- 不超用：该定理没有说同步变化的 f 已经仿射。62 的小映射引理另行完成这个步骤。

### 57：Console–Fino–Poon

- 下载：https://arxiv.org/pdf/math/0506314v1
- 实存 17 页，边注为 arXiv v1、2005-06-15；标题页另印 November 9, 2018。两种日期原样记录，不猜测 PDF 生成历史或据此断言某个新版本的定理。
- 期刊：International Journal of Mathematics 17(4) (2006), 401–416，DOI 10.1142/S0129167X06003576。
- PDF pp.1–2、5、8、11–13 全部完整查看。
- p.5：切丛 Dolbeault 不变复形的准确约定。
- p.8 Theorem 1：abelian 复结构的全局切丛上同调由不变复形计算，包含映射自然，故与 F 等变。
- p.11 Theorem 2：调和代表及全局伴随在不变子复形上的相容性。
- pp.12–13 Theorem 3：局部完备 Kuranishi 族全部不变。
- p.13 后半明确另行研究“何时仍 abelian”。本文不假设全部变形保持 abelian；ξ、η 方向的反检验正说明其必要。

### 复用 01、02

01 PDF p.17：六维群、格、F 与两侧非全纯分布的原例。该页未陈述本文的具体 Ω₀ 或八参数分类；这些在 notes/05 §6、61 直接核验。

02 PDF pp.3–4：不变复结构及 bi-Lipschitz bootstrap 的已知边界。后者先要求 bi-Lipschitz 共轭；本文的局部证明没有将这个假设默认为由结构稳定性得到。

共五份来源、16 个完整页的散列及视觉记录在 model_deformation_source_audit.json；独立推导在 notes/61–63。三份新文件共一次瞬时 TLS EOF 后通过正常重试取得；没有关闭 TLS 验证，也没有将未完成请求登记为有效 PDF。

## 3. 有限检索实际覆盖什么

检索组合包括：

- nilmanifold left invariant complex structures biholomorphism close identity affine deformations automorphisms
- nilmanifold local rigidity holomorphic Anosov abelian complex structure deformation affine
- "nilmanifolds" "biholomorphisms" "affine" "deformations"
- "Anosov" "Kuranishi" nilmanifold
- "holomorphic" "Anosov" "local rigidity" nilmanifolds
- "left-invariant" "biholomorphism" "identity" nilmanifold
- "nilmanifold" "holomorphic vector fields" "affine"
- "nilmanifold" "biholomorphisms" "right translations"
- "left-invariant complex structures" "affine" "small"
- "holomorphic Anosov" "deformations" nilmanifold

原始来源核对：55–57 以及 01、02。其他搜索页面只用于寻找线索；未将 ResearchGate、搜索摘要或其他转录当作定理证明输入。

检索还命中：

- McLaughlin–Pedersen–Poon–Salamon, Deformation of 2-step Nilmanifolds with Abelian Complex Structures，2004 原始预印本：https://arxiv.org/abs/math/0402069 。其二步不变小变形结果是 57 的前序工作；本轮未另下载全文，不据此确认某条关于变化的 automorphism 的结论。
- Jonathan DeWitt, Local Lyapunov spectrum rigidity of nilmanifold automorphisms，JMD 17 (2021), 65–109，出版社：https://www.aimsciences.org/article/doi/10.3934/jmd.2021003 。只核对出版社摘要的体积/谱与额外条件，未将它作为本证明的输入。
- Rollenske 2009 关于 deformations in the large 的原始来源：https://arxiv.org/abs/0901.3120 。未用其全局结论，不把小邻域稳定性推广为所有大变形。
- Bazzoni–Freibert–Latorre–Tardini 2025, Complex symplectic structures: deformations and cohomology：https://arxiv.org/abs/2507.03940 。仅登记为后续比较线索，未用其全文或把一般复辛变形稳定性当作现成结论。
- 2026 年较新的一般 nil Dolbeault/统一化题目的搜索线索。未使用非原始转录，也未以它们代替已经足够的旧 abelian 变形理论。

有限检索没有确认本文小双全纯映射引理、二步 abelian 模型局部共轭推论或具体八参数族的最早出处。**不能据此宣称首创。** 不变 Kuranishi 小变形理论本身明确是旧结果。

## 4. 失败路线与被实际绕开的障碍

- 任意光滑向量场上的 F*−I 不能直接求逆；周期条件及正则性会妨碍这种做法。63 的一阶证明只在 H⁰ 上求逆，62 的实际证明只对有限维平移求逆。
- 仅有 J 的左不变化不推出 f 的仿射化。62 §3 给出遗漏步骤的完整估计。
- 仅由所有一阶方向可积或形式正规形，不能宣称实际共轭收敛。62 的证明使用已有收敛 Kuranishi 族加实际小映射刚性，避开该未证明推断。
- 不变闭复辛形式不会随任意 F 不变 J 自动延拓。p、t 的精确反检验已经排除这种猜测；不将它夸大为不存在任何非 F 不变全纯辛形式。
- 模型有真实四/八个复参数，不能称原始固定三元组“无模局部刚性”。准确结论是局部模型稳定和完整正规形。

## 5. 尚未处理的范围

- 任意未知紧致全纯 Anosov 流形的 nil 几何入口。
- 离开该邻域后的全局模型化、全局模空间或大变形。
- 更高步 BCH 的估计；当前小映射引理完整证明仅写在二步。
- 一般非 abelian 基点的全部小变形是否仍可在同群同格上实现。
- IHS 四维 K3^[2] 分支的全局排除或无 pinching 横向正则性。

这些未解决项不影响 61–62 在既定邻域内的证明，但也不能由本轮局部定理自动取得。

## 后续定位修正（2026-10-18）

65–68 新取得的来源 59（arXiv:2609.31516v1）Theorem 2.1 已有一般 complex nilmanifold 间全纯映射的全局仿射性，覆盖这里的小映射结论。因此上文的有限检索状态只保留为当时记录，当前结论状态为“已有更强文献覆盖”。本工作继续保留独立椭圆证明，但新的研究重点转为 66 的保辛动力学周期闭性及 67 的模型分支结果。来源 58 还提供全部 nil 结构的小变形输入，准确外部依赖见 nil_progression_scope_and_novelty_log.md。
