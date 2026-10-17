# 条件的非空性、边界与共振检验

日期：2026-10-17。所用 K_{u,p}、K_{s,p} 定义见 04_grassmann_Lp_regularization.md。指数的精确枚举另存 model_weight_checks.json。

## 1. 复四维 (2,2) 的非空严格情形

令

\[
B=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
\lambda=(3+\sqrt5)/2>1,
\]

其特征值为 λ、λ^{-1}。在

\[
T=\mathbb C^4/(\mathbb Z+i\mathbb Z)^4
\]

上取 A=B⊕B。A 为整复线性格自同构，稳定、不稳定复秩均为 2。B 对称，可选平移不变 Hermitian 度量使

\[
S=\lambda^{-1}I_2,\quad U=\lambda I_2,\quad J=1.
\]

于是

\[
K_{u,p}=K_{s,p}=\lambda^{-p}<1.
\]

因此 04 中的充分条件并非空洞条件。

严格不等式有统一余量，Anosov 子丛及块算子在 C1 小扰动下连续变化；选随分裂连续变化的正交度量即可保留不等式。因此它还覆盖该模型附近的一类全纯 Anosov 系统（若允许复结构随系统变化，须同步要求复结构接近原结构）。分类所得复环面结构不必是预先固定的标准模参数。

## 2. 独立核查复六维非全纯模型

来源：J. Zhang, Codimension-one holomorphic Anosov diffeomorphisms, arXiv:2609.37695v2, §5。这里核验原文例子，不声称例子为本工作区新发现。

在 G=C^6 的标准复坐标上定义实 Lie 群乘法

\[
(x,y,z,a,b,c)(x',y',z',a',b',c')
=(x+x',y+y',z+z'+\bar x y',
a+a',b+b',c+c'+\bar a b').
\tag{1}
\]

交叉项为实双线性二步中心项，所以 (1) 满足结合律，是单连通实二步幂零 Lie 群。每个固定左因子的左平移都是全纯映射，标准可积复结构因而左不变；但乘法不对两个变量联合全纯。

令

\[
R=\mathbb Z[i,\sqrt3],\qquad
\sigma(i)=i,\quad \sigma(\sqrt3)=-\sqrt3,
\]

\[
\Gamma=\{(\alpha,\beta,\gamma,
\sigma\alpha,\sigma\beta,\sigma\gamma):
\alpha,\beta,\gamma\in R\}.
\]

σ 与复共轭交换且保持乘法，因此 Γ 对 (1) 乘法及求逆封闭。

映射 α↦(α,σα) 把 R 嵌入为 C² 中的满实格：写 α=A+B√3+i(C+D√3)，对应两个实二维线性变换的行列式均为 −2√3。于是 Γ 离散。依次约化 (x,a)、(y,b)，再用中心坐标约化 (z,c)，得到有界闭基本区域，故 Γ\G 紧致。左作用全纯，商 X 为紧致复流形。

令 λ=2+√3，并取

\[
F(x,y,z,a,b,c)
=(\lambda^2x,\lambda^{-1}y,\lambda z,
\lambda^{-2}a,\lambda b,\lambda^{-1}c).
\tag{2}
\]

交叉项权重分别是 λ²λ^{-1}=λ 和 λ^{-2}λ=λ^{-1}，故 F 为实 Lie 群自同构，同时为标准复结构上的全纯映射。λ 是 R 的单位，σλ=λ^{-1}，因此 F 保持 Γ，并下降为 X 的全纯自同构。

下降到商的左不变 (1,0) 标架为

\[
X_1=\partial_x,\quad Y=\partial_y+\bar x\partial_z,\quad
Z=\partial_z,
\]

\[
A_1=\partial_a,\quad B_1=\partial_b+\bar a\partial_c,\quad
C=\partial_c.
\]

DF 在此标架中的乘子依次为

\[
\lambda^2,\lambda^{-1},\lambda,\lambda^{-2},\lambda,\lambda^{-1}.
\]

所以它是 Anosov，且

\[
E^s=\langle Y,A_1,C\rangle_{\mathbb C},
\qquad E^u=\langle X_1,Z,B_1\rangle_{\mathbb C}.
\]

取此标架正交归一的光滑 Hermitian 度量。因为

\[
\bar\partial Y=d\bar x\otimes Z,\qquad
\bar\partial B_1=d\bar a\otimes C,
\]

两侧都不全纯。每条叶本身仍为复子流形，且在本例中可显式参数化为 C³；不能将叶的复结构和分布的全纯性混同。

## 3. 已知反例恰落在收缩边界

本例中

\[
\|S\|=\lambda^{-1},\quad m(S)=\lambda^{-2},
\quad\|U\|=\lambda^2,\quad m(U)=\lambda,
\quad J=1.
\]

因此

\[
\frac{\|S\|}{m(U)m(S)}=1,\qquad
\frac{\|S\|\|U\|}{m(U)}=1,
\]

\[
\boxed{K_{u,p}=K_{s,p}=1\quad\text{对所有 }1\le p<\infty.}
\]

所有正迭代也如此。故 04 的严格条件与此例相容，而且不能统一将严格不等式替换为 ≤1。

这个障碍不能通过仅仅把 L² 改成另一个 Lp 消除。

## 4. 非零缺陷的确切共振

对稳定分布，非零反全纯缺陷 Y→Z 的反全纯自变量为 \bar X_1。其乘子满足

\[
\lambda_Z=\lambda_Y\,\overline{\lambda_{X_1}}
=\lambda^{-1}\lambda^2=\lambda.
\]

对不稳定分布，非零缺陷 B_1→C 的反全纯自变量为 \bar A_1：

\[
\lambda_C=\lambda_{B_1}\,\overline{\lambda_{A_1}}
=\lambda\lambda^{-2}=\lambda^{-1}.
\]

所以这两个缺陷都是相应不变张量表示的权重 1 分量。它们也正对应

\[
[\bar X_1,Y]=Z,\qquad [\bar A_1,B_1]=C
\]

这两个二步幂零括号。

这是一般路线应保留并识别的结构，不能继续要求所有反全纯缺陷为零。但这个例子本身不证明任意系统的缺陷都是有限维、光滑或常系数；那些仍是待证步骤。

## 5. 严格条件不是必要条件

在标准复四维环面上改取 A=B³⊕B，块权重为

\[
S:\lambda^{-1},\lambda^{-3},\qquad
U:\lambda,\lambda^3.
\]

J=1，K_{u,2}=K_{s,2}=λ²>1，但两侧在标准复环面上当然全纯。这个例子也没有上述混合二阶共振。

因此需要区分：

- 收缩条件失效；
- 真正存在非零共振缺陷；
- 分布是否光滑；
- 全局分类能否成立。

不能将第一个问题直接当作后面三个问题的反例。

## 6. 非全纯模型本身还有不变全纯辛形式

这里另做一个与下一阶段有关的核验。上述六维例子上有

\[
\omega=dx\wedge da+dz\wedge dy+dc\wedge db.
\]

左平移中 dz 只多出常数倍 dy，dc 只多出常数倍 db，所以 ω 对 Γ 不变并下降到商。它是闭的、处处非退化的全纯 (2,0) 形式。

各配对的 F 权重为 λ²λ^{-2}、λλ^{-1}、λ^{-1}λ，均为 1，因此 F*ω=ω。于是 Re ω 是 F 不变的实辛形式。

这说明：即使额外假设存在不变全纯辛形式，也不能普遍证明两侧全纯，更不能普遍把结论加强成环面有限覆盖。保辛而去掉 pinching 后，非交换 nil 模型仍然必须保留。

但此例两侧确实光滑，因此它与“保辛全纯 Anosov 的两侧应为 C∞，再接 Benoist–Labourie”的研究目标相容。
