# 任意复秩的 Grassmann 丛正则化：完整证明

日期：2026-10-17。性质：本工作区独立推导的条件性结果；没有据有限检索声称其文献新颖性。它完成规划 A1，并在相同收缩条件下撤去了“一侧已全纯”的假设。

## 1. 设置

设 f 是紧致复流形 X 的全纯 Anosov 微分同胚，稳定、不稳定复秩分别为 k,r，均大于零。不预设任一分布全纯。

取连续 Hermitian 度量 g 使 E^s、E^u 正交。取迭代 F=f^m，使

\[
\|S_x\|<1<m(U_x),\qquad
S_x=DF_x|_{E^s_x},\quad U_x=DF_x|_{E^u_x},
\]

其中 m(B)=\|B^{-1}\|^{-1} 为余范数。由紧致性，两个不等式都有统一严格界。

用此度量的连续正体积 dV 换元。实 Jacobian 为

\[
J(x)=|\det_{\mathbb C}S_x|^2|\det_{\mathbb C}U_x|^2.
\]

对 1≤p<∞ 定义

\[
K_{u,p}(F)=
\sup_{x\in X}J(x)
\left(\frac{\|S_x\|}{m(U_x)m(S_x)}\right)^p,
\tag{1}
\]

\[
K_{s,p}(F)=
\sup_{x\in X}J(x)^{-1}
\left(\frac{\|S_x\|\|U_x\|}{m(U_x)}\right)^p.
\tag{2}
\]

这里各块的行列式模均指所选 Hermitian 体积之间的行列式模；不需要全局标架。

## 2. 定理

若 K_{u,p}(F)<1，则 E^u 为全纯子丛。

若 K_{s,p}(F)<1，则 E^s 为全纯子丛。

两项可使用不同的 p、不同的迭代及不同的连续正交度量。两项分别成立时，两侧都全纯。

## 3. 对一般全纯纤维丛的内蕴反全纯导数

令 π:Z→X 为全纯纤维丛，σ 为光滑截面。定义

\[
\mathcal D\sigma
=(d\sigma|_{T^{0,1}X})^{1,0}.
\]

因为 π 全纯且 πσ=id，右侧取值于垂直全纯切空间 V^{1,0}Z=ker(dπ|T^{1,0}Z)。在局部全纯纤维坐标 (z,w) 中，σ(z)=(z,w(z))，此张量就是 \bar\partial w。

若 \widehat F:Z→Z 是覆盖 F 的全纯丛映射，截面推送记为

\[
(\mathcal P\sigma)(Fx)=\widehat F(\sigma(x)),
\]

则全纯链式法则给出

\[
(\mathcal D\mathcal P\sigma)_{Fx}
=D^v\widehat F_{\sigma(x)}
(\mathcal D\sigma)_x\,\overline{DF_x}^{-1}.
\tag{3}
\]

这是内蕴张量等式，不需要预先选择光滑水平分布。局部写 \widehat F(z,w)=(F(z),G(z,w)) 时，G 对所有复变量全纯，故 \bar\partial 链式法则中只有纤维导数 D_wG 这一项。

## 4. 用连续不变分裂选择垂直范数

取全纯 Grassmann 丛

\[
Z=\operatorname{Gr}_r(T^{1,0}X).
\]

全纯 DF 诱导全纯丛自同构 \widehat F。E^u 是连续不变截面 σ_u。

每个与 E^s_x 横截的 r 平面唯一写为

\[
\Psi_x(B)=\operatorname{graph}(B),
\qquad B:E^u_x\longrightarrow E^s_x.
\]

映射 Ψ_x 对 B 全纯，并随 x 连续。不对它关于 x 求导。由于实际分裂不变，

\[
\Psi_{Fx}^{-1}\widehat F\Psi_x(B)
=S_xBU_x^{-1}. \tag{4}
\]

这在纤维上是精确线性式，而不只是零截面附近的一阶近似。

在垂直切空间上，用 D_BΨ_x 将 Hilbert–Schmidt 范数从 Hom(E^u_x,E^s_x) 搬过来。所得度量关于 x 连续、关于 B 光滑。在任意有界图坐标管状邻域中，它与标准光滑垂直度量统一等价。

由 (4)，

\[
\|D^v\widehat F\|
\le \frac{\|S_x\|}{m(U_x)}. \tag{5}
\]

**关键区别：** Ψ_x 只用于定义垂直范数及计算垂直导数。没有将 \mathcal Dσ 写成 \bar\partial B(x)，也没有对未知正则性的 E^s、E^u 求导。

## 5. 光滑逼近与整体估计

取光滑 Grassmann 截面 σ_0，一致接近 σ_u，使其与 E^s 处处横截。其存在性可由光滑截面逼近定理取得；也可将连续 Hermitian 正交投影先光滑逼近，再用分离的谱簇作光滑谱投影。

写 σ_0(x)=Ψ_x(B_0(x))。B_0 连续且有界。令

\[
\sigma_j=\mathcal P^j\sigma_0.
\]

这些截面全都光滑。(4) 和统一界 \|S\|/m(U)<1 给出图坐标指数收缩，故

\[
\sigma_j\longrightarrow\sigma_u
\quad\text{一致收敛}. \tag{6}
\]

令 β_j=\mathcal Dσ_j。在基底反全纯余切因子上，

\[
\|\overline{DF_x}^{-1}\|
=\frac1{m(S_x)},
\]

因为两分布正交、稳定块全部收缩、不稳定块全部扩张。由 (3)、(5)，

\[
\|\beta_{j+1}(Fx)\|
\le\frac{\|S_x\|}{m(U_x)m(S_x)}
\|\beta_j(x)\|. \tag{7}
\]

Hilbert–Schmidt 范数满足 \|ABC\|_{HS}≤\|A\|\|B\|_{HS}\|C\|，所以这里没有额外维数常数。

积分换元得

\[
\|\beta_{j+1}\|_{L^p(dV)}^p
\le K_{u,p}(F)\|\beta_j\|_{L^p(dV)}^p.
\tag{8}
\]

当 K_{u,p}(F)<1 时，β_j 在 L^p 中趋零，因而在 L^1_loc 和分布意义下趋零。

## 6. 极限全纯

在任一点附近，先取一个底空间全纯坐标邻域和 Grassmann 全纯纤维坐标，使连续 σ_u 的像落在该纤维坐标图的相对紧部分。(6) 保证 j 充分大时 σ_j 也落在同一图内。

其纤维坐标 w_j 一致收敛于 w_u；由垂直范数的统一等价性，\bar\partial w_j→0 于 L^p。于是

\[
\bar\partial w_u=0
\]

在分布意义下成立。分布 Cauchy–Riemann 定理给出 w_u 全纯。σ_u 因而是全纯截面，它所定义的 E^u 是全纯子丛。第一项结论证毕。

## 7. 稳定方向的公式

把同一结论用于 F^{-1}。在 y=Fx 处，其稳定和不稳定块分别为 U_x^{-1}、S_x^{-1}，Jacobian 为 J(x)^{-1}，而

\[
\frac{\|U_x^{-1}\|}
 {m(S_x^{-1})m(U_x^{-1})}
=\frac{\|S_x\|\|U_x\|}{m(U_x)}.
\]

因此得到的充分条件正是 (2)。定理证毕。

## 8. 换度量与迭代

可使用渐近版本：若

\[
\limsup_{\ell\to\infty}\frac1\ell
\log\sup_x J_{f^\ell}(x)
\left(\frac{\|S_{\ell,x}\|}
 {m(U_{\ell,x})m(S_{\ell,x})}\right)^p<0,
\tag{9}
\]

则某个大迭代满足 (1)。稳定方向类似。

两个等价连续 Hermitian 度量之间，所有块范数、余范数以及体积密度的比较只产生与 ℓ 无关的有界乘法因子。因此 (9) 的严格负性不依赖具体度量。

这些量关于时间满足次乘性；某一迭代严格收缩即可在其整数倍上指数收缩。不能因为某个不合适的小迭代不收缩就断言方法不适用。

## 9. 与已知复秩一结果的一致性

若 r=1，取 p=2，稳定复奇异值 s_1≥…≥s_k，唯一不稳定奇异值 u，则

\[
J\left(\frac{s_1}{u s_k}\right)^2
=s_1^2\prod_{i<k}s_i^2<1
\]

在足够大迭代上一致成立。因此此 Grassmann 证明直接给出复秩一的不稳定子丛全纯，不需要先引用另一侧全纯。

稳定复秩一时用逆映射得到对应结论。一般秩下 (1)、(2) 不自动成立，已知非全纯例子恰落在边界；见 05_model_checks.md。

## 10. 有环面拓扑时的分类推论

若再假定 X 同胚于实 2n 维环面，且 (1)、(2) 各自对某个 p、迭代成立，则两侧全纯。接 Zhang 2026, Codimension-one holomorphic Anosov diffeomorphisms, Theorem 1.2，即得

\[
X\simeq\mathbb C^n/\Lambda,\qquad
hfh^{-1}=A,\qquad A\Lambda=\Lambda,\quad
\operatorname{Spec}(A)\cap S^1=\varnothing.
\]

这里使用的外部分类输入：
https://arxiv.org/html/2609.37695v2

本推论不假设 Kähler、保体积、传递性或任一侧已全纯；但是仍保留环面拓扑及明确谱条件。它不是一般猜想的证明。
