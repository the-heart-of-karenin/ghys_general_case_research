# 直接攻击 76：原始输入、独立结论与失败范围

日期：2026-10-19。对应独立记录 79–82；原始 PDF 与研究笔记分目录保存。本轮没有重跑旧数学计算套件，没有以数值抽样代替证明。

## 1. 本轮得到的严格结论

- **79：实际导数与位移。** 从 R⋊_B Z 在 Sol 型实 Lie 群中的对数群字长度，取得实际单值的多项式 C^j 增长、零拓扑熵、统一零切指数。利用原始 X 的 F-不变 π₁ 截面选取准确提升，再由共同保测度和谱不匹配证明零条件旋转。对数 distortion 的基本机制是经典的，不称为新的普遍理论。
- **80：真实切方向。** 只调用 Hurtado–Xue 的高维 Theorem 1.11，结合复辛四维的代数相交引理，得到逐点有限、对整个给定可解群等变的非零各向同性方向族。以全纯稳定叶的完备性、解析延拓和稠密性排除局部全平面保持，再用 Baire 得到某个开集上的恰一维连续公共复线。未得到全局恒秩或横向正则性。
- **82：完整中央方程的新增估计。** 参数 1、i 的中央剪切配对 N₁=I、N_i=−J、J²=−I，使单位谱附近有椭圆型下界。该下界直接给出慢商 cocycle 的 L² transfer function 及谱无关的范数界；Anosov 正规化继而使慢商位移处处为零。因此实际单值逐纤维保持指定拓扑中心纤维化，原快流的慢商位移也为零。该证明不调用来源 67、68 的刚性定理，也不需要真实分布 C¹。

**未完成：** 中心误差 w_r 的消去、指定拓扑纤维的复解析性、第一张闭全纯一形式，以及 76 的 W_Y=0 排除。不能将 80 的实际公共线直接等同于 82 拓扑纤维的切方向。

## 2. 来源 67：distortion 文献只是比较

John Franks–Michael Handel，
*Distortion Elements in Group actions on surfaces*，
Duke Mathematical Journal 131 (2006), 441–468。

- [期刊 DOI](https://doi.org/10.1215/S0012-7094-06-13132-0)。
- [arXiv v2 PDF](https://arxiv.org/pdf/math/0404532v2)，边注版本日期为 2005-03-03。
- 标题页另印 2018-11-10；保留这个版本日期与生成日期差异，不把它算作 2018 新结果。
- 已完整视觉核验 PDF 第 1、2 页。

其核心表面动力学结论针对曲面及相应 Diff₀ 条件，不能应用于本问题实八维 Y 上、H₁ 作用非平凡的单值。79 的导数界由正文中自足的群字长度和链式法则证明；未引用该文表面固定点定理。

## 3. 来源 68：只使用真正适用的高维判据

Sebastian Hurtado–Jinxin Xue，
*Global rigidity of some Abelian-by-cyclic group actions on T²*，
Geometry & Topology 25 (2021), 3133–3178。

- [期刊 DOI](https://doi.org/10.2140/gt.2021.25.3133)。
- [arXiv v2 PDF](https://arxiv.org/pdf/1909.10112v2)，2020-12-05，36 页。
- 已完整视觉核验 PDF 第 5、8、9、10 页。

**实际调用：** 第 5 页 Theorem 1.11：传递 Anosov 的稳定、不稳定维数相等时，一点上的四重横截使某些共轭迭代生成自由群。76 的稳定、不稳定实秩均四，且整个给定群可解，满足使用该定理的全部前提。第 8–9 页核对其 ping-pong 证明。

**明确不调用：** Theorem 1.10 的实二维叶保持二择一，以及第 10 页 Proposition 3.2 的二维特殊步骤。Theorem 1.12 只产生自由半群；Sol 型可解群可以有自由半群，故不能据此造矛盾。

78 与上一日志未套用该文实二维全局分类的判断仍正确；本轮新增的是对其高维部分的实际使用。

## 4. 反检验与一个被完整方程推翻的停点

81 的平方根区间 cocycle 准确满足投影后的交换酉 cocycle 及归一化，并无共同不变分量。它检验“一般相关衰减或次线性已够”的推断为假。

但 **82 已证明它不能扩张到原始单值的完整中央方程**。否则它是 L² coboundary，沿整数倍有界，与精确 √n 范数矛盾。因而不能再用它为实际慢商保留一个尚未解决的平方根障碍。79、81、76 的相关表述均已更新。

05 的实际紧致代数模型满足全部新结论。11 的粗糙局部模型即使有一条全纯公共线，整个稳定平面仍可不为 Lipschitz；它没有本轮完整格群、紧致 Anosov 或稠密完备叶输入。另一个精确线性代数族检验了逐点 Zariski 共同交可能跳秩；没有把这些局部/代数模型称为原始系统反例。

## 5. 有限新颖性检索和状态

本轮实际检索过以下方向：

- distortion、Abelian-by-cyclic、Anosov、holomorphic symplectic、zero entropy；
- 可解 Anosov 群与 invariant Lagrangian / finite invariant directions；
- stable leaf completeness、局部全纯叶保持与全局延拓；
- unitary cocycle、unipotent twist、elliptic coboundary、complex Heisenberg 型中央相容。

判断实际数学输入时只用原始论文、作者稿或主来源；不采用检索聚合页和二手自动摘要作为定理。未找到与 80、82 完全同述的已知结果，不等于不存在。

新定位但未作全文核验、也未调用的比较线索包括：

- [Maruhashi，Parameter rigid actions of simply connected nilpotent Lie groups，2011](https://arxiv.org/abs/1101.4161)；
- [Wang，Cocycle rigidity of abelian partially hyperbolic actions，2017](https://arxiv.org/abs/1703.05879)；
- [Ramirez，Cocycles over higher-rank abelian actions on quotients of semisimple Lie groups，2009](https://arxiv.org/abs/0911.5369)。

这些线索的已知框架与本问题并不自动相符；本轮未借其摘要宣称有一个可覆盖 76 的现成定理。

**首创性未确认。** 82 的椭圆型谱估计和此处应用目前仅作为已写出完整证明的独立结果记录。两份新增 PDF 均为早于 2026-06-01 的已发表研究旧稿；本轮新证明不依赖 2026 新预印本。

来源身份、散列、完整页核验见 Residual_monodromy_source_audit.json；这些文件检查不代替正文数学证明。
