# 77–78：同速归一化流、一形式判据及第一张形式缺口

记录日期：2026-10-19。独立证明在 notes/77–78；本目录仅保存文献与核验记录。本轮没有重跑以前的外代数、模型分类或局部变形脚本。

## 1. 本轮严格完成的独立论证

- 纯连续动力学引理：半单实环面线性映射只有 r、r⁻¹ 两个特征值时，任一由它按时间 r 归一化、并与它共同保持满支撑遍历测度的连续流，必为常平移。证明用位移 cocycle、Birkhoff 的 L¹ 收敛和完全匹配的 r 缩放；不要求测度是 Haar。
- 同速保全纯辛四维环面分支的闭形式维数只有 0 或 4；任一非零形式触发实际紧致复环面作用及完整双全纯线性化。中间维数二由两种垂直辛秩分别排除。
- 同胚 T⁸ 的全纯辛流形的周期定义线性比较复环面，全部实辛铅笔自动 hard Lefschetz。这里只产生比较模型，不识别实际复结构。
- 76 的单值群在实际 Aut(Y,σ) 中闭且离散；给定 Sol 子群内部，任何投影到循环商非零的阿贝尔子群都为循环群。不能由此得到全体自同构群的分类。

以上不是数值猜测；证明逐步写在笔记。没有证明从 76 的原始假设得到 W_Y≠0。

## 2. 来源 64：全纯辛 Lefschetz 与复 Hodge 输入

Andrea Cattaneo–Adriano Tomassini，
*Complex symplectic structures and the ∂bar∂-lemma*，
Annali di Matematica Pura ed Applicata 197 (2018), 139–151。

- [期刊 DOI](https://doi.org/10.1007/s10231-017-0672-1)
- [明确版本 arXiv:1612.08183v2](https://arxiv.org/abs/1612.08183v2)，2017-09-15；本地 PDF 11 页。
- PDF 第 4 页完整视觉核验：Lemma 2.3 / Corollary 2.4 的全纯辛向量丛与 Dolbeault 同构；Lemma 2.5 明确额外假定 ∂bar∂。
- PDF 第 8 页完整视觉核验：Example 4.1 的 underlying Iwasawa×椭圆曲线结构。
- 文本还检查了 Remark 2.6 的范围警示。

**实际用法：** 核对 Hodge 尝试不能直接调用何种结论。没有借此声称已否定“环面上同调 + 全纯辛 + 实 HLC 推出弱一阶 Hodge”。例 4.1 不满足本问题的环面拓扑。

**没有用于 77 的主要证明。** 77 采用流与紧致群作用，而非假定本论文的 ∂bar∂ 前提。

## 3. 来源 65：紧致全纯群作用的联合光滑性

M. S. Baouendi–L. P. Rothschild–J. Winkelmann–D. Zaitsev，
*Lie group structures on groups of diffeomorphisms and applications to CR manifolds*，
Annales de l'Institut Fourier 54 (2004), 1279–1303。

- [作者稿 PDF](https://www.maths.tcd.ie/~zaitsev/papers/brwz.pdf)，本地 18 页。
- 完整视觉核验 PDF 第 9 页 Theorem 3.5。
- 该处准确转述 Bochner–Montgomery：局部紧群连续作用，各元光滑，且没有非平凡元素在非空开集上逐点恒等，则群为 Lie 群且作用联合光滑。

**77 的假设对照：** 群 K 是经 H 拉回的紧致平移子环面；作用自由，特别满足开集有效性。全纯映射及逆映射的 C⁰ 极限仍双全纯，Cauchy 估计使其保持 σ。故定理确实适用，不要求 H 可微。

**版本边界：** 本轮核验的是 2004 论文中的准确转述，没有下载或声称逐页核验 Bochner–Montgomery 1946 原文。全纯自同构群的经典复 Lie 结构、曲面 Riemann–Roch、Serre 对偶及层长正合序列作为标准输入明确使用，不称为本轮新定理。

## 4. 来源 66：ABC 群刚性为什么尚不能套用

Amie Wilkinson–Jinxin Xue，
*Rigidity of some Abelian-by-cyclic solvable group actions on T^N*，
Communications in Mathematical Physics 376 (2020), 1223–1259。

- [期刊 DOI](https://doi.org/10.1007/s00220-019-03658-3)
- [作者稿 PDF](https://www.math.uchicago.edu/~wilkinso/papers/rigidity_solvable.pdf)，2017-05-22，40 页。
- PDF 第 3、8 页完整视觉核验，阅读其仿射平移型阿贝尔子群及全局刚性入口。

**范围结论：** 此处所比较的阿贝尔生成元为平移型、在 H₁ 上为恒等。76 的 L_r 为非平凡剪切，任何拓扑共轭也不能将它变成在 H₁ 上为恒等的平移。因此不能仅凭群关系都为 Abelian-by-cyclic，就用该文完成 76 的八维实际单值群分类。

本文的方法可能提供后续工具，但本轮没有声称其某条高维全局定理已经覆盖本问题。

## 5. 已核验的主来源 HTML，未新增 PDF

Li-Sheng Tseng–Shing-Tung Yau，
*Cohomology and Hodge Theory on Symplectic Manifolds: I*，
J. Differential Geometry 91 (2012), 383–416；
[arXiv HTML 正文](https://arxiv.org/html/0909.5418#S3.SS2.SSS2)。

已核验 §3.2.2 的 Definition 3.12 及 Proposition 3.13：紧致实辛情形，HLC 与 d d^Λ 引理等价。78 使用的只是这个实辛结论。它不自动给出 (3.1) 所需的函数型原函数。

最初一个期刊 PDF 镜像在浏览工具中获取超时，随后改读作者预印本的主来源 HTML；没有将失败请求记为已核验 PDF，也没有为这项浏览另增本地 PDF 编号。

## 6. 有限新颖性检索

以下方向已实际检索，均以数学论文、作者稿或主来源为判断依据：

- “holomorphic Anosov” + “Albanese / one-forms / symplectic / two eigenvalues”；
- “Anosov” + “unipotent / Abelian-by-cyclic / solvable group / global rigidity”；
- “holomorphic symplectic” + “homotopy torus / diffeomorphic to a torus”；
- “complex symplectic” + “hard Lefschetz / weak Hodge / closed holomorphic one-forms”。

另外定位到 Hurtado–Xue 的 [arXiv:1909.10112](https://arxiv.org/abs/1909.10112)，其题目和摘要的全局分类在实二维环面；没有据此处理本问题的 T⁸。也定位到若干局部 KAM/抛物群作用结果，未验证到能够撤去其局部性而覆盖 76 的结论。

**新颖性状态：未确认。** 未找到完全同述的结果不等于不存在。77 的连续流引理可能属于已有的平均旋转/归一化流刚性机制；本轮只宣称独立完成了这里需要的证明。

## 7. 本轮的失败与停点

- 从全部实辛 HLC 获得闭全纯一形式：卡在 dδ 原函数的受限选择，见 78 §3；既未证明也未反驳目标蕴含。
- 从单值群取紧致闭包获得连续全纯辛作用：原群闭离散，直接做法不可行，见 78 §4。
- 从给定群直接制造高秩交换 Anosov 作用：其内部含双曲元素的阿贝尔子群只能循环，不能套来源 09 的高秩阿贝尔刚性。

76 的零形式纤维仍是明确的未决对象。下一步若再继续，应当处理真实单值导数或真实叶方向，而不是再增加同调必要条件。若这一步没有新入口，应如实报告，不能将 77 的充分判据写成原分支已经被排除。

文件散列、完整页核验与来源版本见 Single_rate_toral_source_audit.json；独立数学证明不由这些文件一致性检查代替。

## 8. 后续范围更新：Hurtado–Xue 的高维部分

2026-10-19 的 79–82 轮已下载其旧稿为来源 68，并完整核验 Theorem 1.11 及证明相关页。其**实二维全局分类**仍不能处理 T⁸；但同篇另有一般维数的全横截 ping-pong 定理，80 已用它排除可解群动作的四重全横截。先前“没有套用全局分类”的判断不应误读为整篇没有任何适用工具。具体输入范围、版本及新增独立 cocycle 引理见 Residual_monodromy_scope_and_novelty_log.md。
