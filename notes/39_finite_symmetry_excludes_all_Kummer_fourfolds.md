# 有限对称群的固定曲面：排除整个 Kummer 四维变形类型

日期：2026-10-18。性质：完整的非存在性推论，使用已核验的已发表变形定理、固定点集定理和 Ghys 曲面分类。本轮给出这些输入之间的完整动力学论证；没有声称文献首创。它不依赖 36–37 的拓扑存在性证明，也不经过 38 的周期影随估计。

## 1. 结论与范围

**定理。** 任意广义 Kummer 四维型 IHS 流形 X 都不承认全纯 Anosov 微分同胚。

这里的“广义 Kummer 四维型”指所有与 K₂(A) 变形等价的 IHS 四维流形，**不限于具体的 K₂(A)，也不限于自然诱导自同构**。不需要额外假设原映射保持全纯辛形式、射影、pinching、分布 C¹、稠密轨道或体积为最大熵测度。

这把 29 中仅排除自然自同构的结论，升级为排除整个变形类型。K3^[2] 型及可能的其他 IHS 四维类型仍未被这个定理排除。

## 2. 动力学引理：等变投影允许限制 Anosov 分裂

**引理 A。** 设 F 是紧光滑流形 M 上的 Anosov 微分同胚，Y⊂M 是紧、F-不变的光滑子流形。若存在连续的丛自同态

\[
P:TM|_Y\longrightarrow TM|_Y,
\qquad P^2=P,\quad\operatorname{im}P=TY,
\]

且

\[
DF_yP_y=P_{Fy}DF_y,
\tag{1}
\]

则 F|Y 是 Anosov，且

\[
TY=(TY\cap E^s)\oplus(TY\cap E^u).
\tag{2}
\]

**证明。** P 在紧 Y 上一致有界。若 v∈E^s_y，则

\[
\|DF_y^nP_yv\|
=\|P_{F^ny}DF_y^nv\|
\le \|P\|_\infty C\rho^n\|v\|.
\]

只有 E^s 中的向量具有这种正向收缩，故 P(E^s)⊂E^s。反迭代同理得 P(E^u)⊂E^u。因此 P 在 E^s、E^u 上都是连续幂等元；其像是连续子丛，秩在每个连通分支上为常数。又

\[
P(E^\sigma)=TY\cap E^\sigma\quad(\sigma=s,u),
\]

从而得到 (2)，收缩/膨胀估计直接继承。对正维紧连通 Y，两侧不可能有一侧为零：否则 F|Y 或其逆的充分大次迭代在整个 Y 上严格收缩，却又满射，和 Y 的正直径矛盾。证毕。

这里没有使用“一般不变子流形自动继承 Anosov”这种未经论证的说法。真正补上缺失步骤的是有界的等变投影。

**固定点集推论。** 若有限阶光滑微分同胚 ι 与 F 交换，则 Fix(ι) 的每个正维连通分支在被 F 的某个幂保持之后，都继承该幂的 Anosov 动力学。

有限群作用的固定点集是光滑子流形。在其上，若 ι 的阶为 r，则

\[
P_y=\frac1r\sum_{j=0}^{r-1}D(\iota^j)_y
\tag{3}
\]

是到 T_yFix(ι) 的投影。由 Fι=ιF 的链式法则，(3) 满足 (1)。固定点集紧且只有有限多个连通分支，取幂即可保持指定分支。全纯情形中固定分支为复子流形，限制仍是全纯映射。

对合时，公式只是 P=(I+Dι)/2。无需先取得 E^s、E^u 的 C¹ 正则性。

## 3. 三项已发表的输入

令

\[
\Gamma_X=\ker\!\left(\operatorname{Aut}(X)
\longrightarrow\operatorname{Aut}H^2(X,\mathbb Z)\right).
\]

**输入 1：核群及其作用沿整个变形类型保留。** Hassett–Tschinkel [32] Theorem 2.1、Proposition 3.1：作用在 H² 上平凡的全纯自同构组成一个沿变形的群局部系统，实际作用也延拓到每个变形。作者稿 PDF pp.3–6；原文明确区分 Kähler manifold 和 projective variety，其定理不只适用于射影纤维。

在 X=K₂(A) 上，[29] Corollary 7.1 给出

\[
\Gamma_{K_2(A)}=A[3]\rtimes\langle-1_A\rangle.
\tag{4}
\]

因此对任意 Kummer 四维型 X，Γ_X 有限，且含非平凡对合。该对合在 H² 上平凡，因而保持全纯辛形式。

**输入 2：固定 K3 曲面。** Kapfer–Menet [29] Theorem 7.5(iii)：Kummer 四维型 X 上任意辛对合的固定点集，是一张 K3 曲面和 36 个孤立点的并。PDF pp.28–30，定理末项在 p.29，证明在 p.30。这里尤其存在一张光滑、紧、唯一的二维固定分支 S。

**输入 3：Ghys 曲面定理。** Ghys 1995 Theorem A：承认全纯 Anosov 微分同胚的紧复曲面必须双全纯同构于复二维环面。已核验 PDF p.1，Inventiones p.585。故 K3 曲面不承认这样的映射。

这些均为文献输入；本笔记不把它们称为本轮独立证明的定理。

## 4. 主定理的证明

反设 f∈Aut(X) 为 Anosov。Γ_X 是表示的核，故 f 通过共轭置换这个有限群。于是存在 N≥1，使

\[
f^N\gamma f^{-N}=\gamma\qquad(\gamma\in\Gamma_X).
\tag{5}
\]

选 Γ_X 中一个非平凡对合 ι，令 F=f^N。由输入 2，Fix(ι) 含唯一的 K3 曲面分支 S。由 (5)，F 保持 Fix(ι)，因此保持 S。

公式 P=(I+Dι)/2 是 TX|_S 到 TS 的连续、实际为光滑的等变投影。由引理 A，F|S 是全纯 Anosov 微分同胚。输入 3 迫使 S 为复二维环面，与 S 为 K3 矛盾。证毕。

注意：f 本身是否保辛没有进入证明。需要保辛的是取自 Γ_X 的辅助对合；这是其 H²-平凡性自动保证的。

## 5. 为什么它确实超出了纯拓扑和抽象 cocycle

决定性公式 (1) 来自两个实际映射的链式法则。一个任意给定的双曲 cocycle 即使在 TX 上，也不会自动与 Dι 交换，更不会自动保持固定曲面的真实切丛。

36–37 的连续复 Lagrangian 子丛存在性依然成立；但在 Kummer 型中，它们无法成为某个全纯自同构的 Anosov 稳定丛。不存在性所用的是实际自同构群、固定子流形和真实切导数，而不是追加 Chern 数或稳定 K 指标。

05 的非 Kähler 幂零模型、11/18/25 的非紧局部粗糙模型，都没有上述“整个 IHS 变形类型保留的有限核群 + 固定 K3 曲面”输入，不构成反例。35 的任意丛 cocycle 同样不具有这里所需的切映射相容性。

## 6. 文献核验与精确边界

核验时遇到两处不能照抄的材料：

- [29] PDF p.27 的说明性段落把平移群写成 (Z/3)³，但同页正式 Corollary 7.1 给出 A[3]；复二维环面的 A[3] 为 (Z/3)⁴。本证明只用正式推论与变形定理，不依赖该说明段落中的指数。
- [32] 作者稿 Theorem 4.4(1) 的孤立固定点数不完整；本证明没有使用该项。固定曲面的准确分类采用较晚的 [29] Theorem 7.5，正文还在 Remark 7.7(2) 明确解释额外的 35 个孤立点。

本轮定向检索了 Anosov / generalized or generalised Kummer / fixed K3 / finite involution / uniform hyperbolicity 的组合，没有找到直接陈述主定理的原始文章。不过，这个论证是几个已知定理的短推论，完全可能早已被知晓；**不能声称已确认首创**。准确状态为：证明闭合、来源已核验、同一结论的文献优先权未确认。

下一步应集中在 K3^[2] 型。上述有限核群机制不自动推广到那里；尤其不能从“存在辛对合”跳到“某个 f 的幂与它交换”。必须另证有限共轭轨道，或找到另一种周期子流形。

**后续范围更新（41–42）：** 辛对合具有有限 f-共轭轨道的 K3^[2] 子情形已由同一投影法闭合，但不能证明一般具有该条件。41 又证明 ρ=2 的射影保辛正熵分支没有任何光滑周期曲面，所以一般正熵几何不能普遍提供所需 K3。完整 K3^[2] Ghys 问题仍未解决。

## 7. 来源位置

- [32] [Hassett–Tschinkel 原文](D:/Users/Desktop/work/ghys_general_case_research/literature/32_Hassett_Tschinkel_2013_Hodge_Kummer_planes.pdf)；Moscow Math. J. 13 (2013), 33–56；作者稿日期 2012-06-11。出版 DOI：https://doi.org/10.17323/1609-4514-2013-13-1-33-56。
- [29] [Kapfer–Menet 原文](D:/Users/Desktop/work/ghys_general_case_research/literature/29_Kapfer_Menet_2018_Kummer_integral_cohomology.pdf)；Algebraic Geometry 5 (2018), 523–567。出版 DOI：https://doi.org/10.14231/AG-2018-014。
- [Ghys 原文](D:/Users/Desktop/work/2/historical_literature/01_Ghys_1995_Holomorphic_Anosov_systems.pdf)；Invent. Math. 119 (1995), 585–614。

原始 PDF、提取文本及整页预览保存在 literature/；本证明保存在 notes/，二者分开。
