# 74–76 的外部输入、有限检索与范围

日期：2026-10-19。新增原始 PDF 仅 63；没有重做 71–73 的文献审计或旧数学测试。独立论证在 notes/74–76，来源原文与预览在 literature/。

## 本轮新增的准确输入

- **63，Giménez Conejero–Lê–Nuño-Ballesteros，Thom condition and monodromy**，RACSAM 117 (2023), article 18，期刊在线日期 2022-11-13。下载自 [机构仓储的期刊 PDF](https://real.mtak.hu/191928/1/s13398-022-01353-y.pdf)，[期刊页](https://doi.org/10.1007/s13398-022-01353-y)。完整 PDF 26 页，第 1–2 页已提取并逐页渲染目视核验。
- 第 2 页 Theorem 0.1：f∈m² 时局部单值的 Lefschetz 数为零。**没有孤立临界点假设**；引言还明确解释去掉孤立性后的 Milnor tube。Theorem 0.2 在同文证明无固定点的几何单值，是所需结论的加强。这里有可核查的原始证明来源；未取得 A'Campo 1973 原篇全文，不伪称读过该原篇。
- 74 从该输入加映射芽的 nearby-cycle 拓扑不变性推出“拓扑投影的全纯映射无临界点”。没有仅从全局纤维同调判别局部奇点。

## 已知输入的复用与边界

- **09，Rodriguez Hertz–Wang，§2.2，PDF 第 6 页**：标记 Franks–Manning bi-Hölder 共轭同伦于恒等。本轮只检查这一整页并渲染目视核验；不重做该文其他页。本研究只调用经典单映射定理，不使用此文高秩刚性定理来替代我们的证明。
- **Anosov–Hopf 遍历定理**：光滑保体积 Anosov 在紧致连通底上对该体积遍历；75 给出所需 Hopf 机制及全部假设。原始发表条目为 [Anosov–Sinai 1967](https://www.mathnet.ru/eng/rm5792)。本轮未下载这篇 65 页原文，未伪称逐页审计；现代原始研究论文 [Flexibility of Lyapunov exponents](https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/flexibility-of-lyapunov-exponents/C17B9DA4A5ACE2AD95F83765E62ABB78) 的正文也明确重述保守 C² Anosov 的该结论。绝不假设 Franks 共轭将实际辛体积送到 Haar 测度。
- **Bochner–Montgomery**：紧致复流形的自同构群为 Lie 群，紧致 Lie 子群的连续双全纯作用光滑。只将它用于已经构造出的实际紧致自由 T⁴ 作用，不据抽象中心直接断言有全纯作用。闭包元素的全纯性及保 Ω 性在 75 用一致收敛和 Cauchy 估计单独证明。
- **紧复曲面分类**：K 平凡且 b₁=4 的紧复曲面为复二维环面。只在已经得到的复二维纤维上使用，不将它推广到四维同伦环面。
- **Fischer–Grauert**：proper holomorphic submersion 全部纤维同构时，得到全纯局部平凡性。75 先由周期纤维的实际 g 作用证明标记复结构常值，再调用该定理。
- **62，Catanese–Frediani Theorem 3.6**：主全纯环面丛的 complete Appell–Humbert 描述；复用上轮的整页核验，见 Albanese_source_audit.json。本轮只用零 Chern 类 ⇒总空间为复环面的特殊情况，正文也说明常数加性格 cocycle；适用 m=2,d=2，**没有使用维数受限的 Theorem 4.11**。
- 71 的一阶上界、68/70 的全局固定闭二形式基、66 的唯一代表及 Nomizu 已作为仓库已证明输入复用，没有重做所有旧检查。
- 74–76 本身不使用 2026 来源 58、59、60。只有将 dim W=4 再升级为 73 的固定 F 全局光滑共轭时，仍明确采用来源 59 的全局仿射性；其预印本状态保持不变。

## 有限新颖性检索

检索包括下列主题及其精确短语：

- holomorphic Anosov / closed holomorphic one-forms / zeros / Albanese submersion；
- holomorphic symplectic / nilmanifold / Albanese / compact homotopy torus；
- holomorphic map / topological submersion / A'Campo / non-isolated critical point；
- Anosov / zero flux / normalized flows / nilmanifold；
- compact complex automorphism groups / Bochner–Montgomery；
- K-trivial homotopy torus / Catanese–Oguiso–Peternell。

未发现与 74–76 全部特定结论相同的可直接套用定理，但这是有限定位，**不证明新颖性**。精确缩放、Birkhoff 位移、闭包紧致群与 torus family 的周期方法都与既有动力学和复几何机制相通；不得据“没有命中”称其为首创。

检索所得 Catanese–Oguiso–Peternell 的同伦环面文章明确以复三维及附加纤维化条件陈述其主定理；本轮没有把这些结论用于剩余的复四维 Y。∂∂-complex symplectic Albanese submersion 文献有额外 ∂∂ 假设，也没有用来证明我们的非 Kähler nil 情形。

## 实际证明、计算与尚缺步骤

**正文证明：** 74 的发展映射和无临界点；75 的 slow flux 零、精确位移消去、真实中心复环面及商环面；76 的非最大 W 维数列表、快谱平坦辛悬挂和 W_Y=0。

**精确计算：** check_slow_form_reduction.py 仅检查新支持恒等式、格单值矩阵和非紧半次流。25344 个支持零项为全符号系数的组合穷尽，不是随机拟合；它们仍不代替全局分析证明。没有运行旧套件。

**未证明：** 任意原始系统都有一张闭全纯一形式；仅快谱时能否产生慢谱；W_Y=0 的四维辛 Anosov 同伦环面能否与显式正规化 unipotent 群共存。非紧半次流只是迭代障碍检验，不是原猜想反例。
