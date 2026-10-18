# Kummer 四维型：真实 Lagrangian 子丛与奇数次数 Steenrod 平方

日期：2026-10-18。性质：将 notes/36 的实际降秩方法扩展到广义 Kummer 四维型，补上非零奇数上同调造成的复辛 K 理论障碍。与 36 一起，给出两个标准 IHS 四维变形类型的真实连续复 Lagrangian 子丛存在判据。

## 1. 结论及与 36 的区别

设 X 为 Kummer 四维型 IHS，Ω 为其全纯辛形式。固定标准格标记

\[
H^2(X;\mathbb Z)=U^3\oplus\mathbb Z\delta,\qquad q(\delta)=-6.
\]

则存在连续复秩二 Lagrangian 子丛 E⊂(TX,Ω) 且 c₁(E)=a，当且仅当

\[
\boxed{a\equiv\delta\pmod{2H^2(X;\mathbb Z)},\qquad q(a)=-6.}
\tag{1}
\]

例如 a=δ 确有这样的实际子丛。连续截面可以光滑化。必要性来自 notes/28、31 的纯连续丛论证，不使用动力学。

不能直接照搬 36 的“KSp 无挠”证明：本类型 b₃=b₅=8，KSp AHSS 总次数零线上还出现 H⁵(X;F₂)。下面专门计算消掉它的微分；没有忽略这个项。

## 2. 整数 Chern 数据与实际秩二丛

在 X=K₂(A) 上，记 Y=[Y_p]，其中 Y_p 为长度三子概形包含固定点 p 的曲面类。[29] Proposition 6.23、6.25、6.30 给出

\[
r:=\delta^2/3\in H^4(X;\mathbb Z),\qquad
c:=c_2(X)=24Y-r.
\tag{2}
\]

整数上同调无挠须引用 [30] 的修正证明，而不是 [29] 中原来不适当的参考文献。下述整数等式及上同调运算沿光滑变形运输到全部 Kummer 四维型。

对 a=δ+2β，设 b=(c+a²)/2。由 (2)，

\[
b=12Y+r+2\delta\beta+2\beta^2\in H^4(X;\mathbb Z),
\quad \rho_2b=\rho_2\delta^2.
\tag{3}
\]

Cartan 公式给出 Sq²ρ₂b=0。又 δ³∈2H⁶(X,Z)：它与 U³ 的配对为零，与 δ 的配对为 ∫δ⁴=324；H²、H⁶ 整数对偶完美。因而 ρ₂(ab)=0，满足实际复丛的 Steenrod 条件。

当 q(a)=−6 时，Fujiki–Chern 公式为

\[
\int c^2=756,\quad\int ca^2=-324,\quad
\int a^4=324,\quad\int c_4(X)=108.
\]

于是 b²=c₄(X)。[23] Proposition 3.2 的秩四实现同余为

\[
J=\frac12\int b(b-c-2a^2)
=\frac12(108-216-0)=-54\equiv0\pmod6.
\]

所以确有实际复秩四 ζ，其 Chern 类为 (a,b,0,0)。先由 c₄=0 分裂一个平凡复线；再用 notes/36 引理 A（基流形 spin、单连通而 a mod 2 非零）分裂第二个平凡复线，得到实际复秩二丛 E，c₁(E)=a、c₂(E)=b。

目前只构造了 E。以下两节验证复辛嵌入还需要的信息。

## 3. Sq²:H⁴→H⁶ 满射

[29] Theorem 6.31(i) 给出 Sym²H² 在 H⁴ 中的完整饱和格，特别是全部二次整除信息。同文 §8.3、Proposition 8.10 的证明已经逐系数使用这个饱和格证明

\[
\alpha^2\in2H^4(X;\mathbb Z)
\quad\Longrightarrow\quad
\alpha\in2H^2(X;\mathbb Z).
\tag{4}
\]

为明确这里的整数输入，取基 y₁,…,y₆ 为 U³ 的标准基。二局部饱和格除原有乘积外，由

\[
\frac{y_i^2-\delta y_i/3}{2}\quad(i=1,\ldots,6),
\qquad
\frac{y_1y_2+y_3y_4+y_5y_6}{2}
\]

生成；三次分母在二局部是单位。若 α=Σtᵢyᵢ+kδ 的平方可除二，比较这些半积类的 δyᵢ 系数，逐一迫使 tᵢ 偶；再比较 δ² 系数，迫使 k 偶。这正是 [29] 式 (8.2)、(8.3) 后的论证。

H³、H⁴ 整数上同调无挠，故 H²(F₂) 的所有类可以整数提升。(4) 意味着平方 H²(F₂)→H⁴(F₂) 单射。由 spin Wu 公式，Sq²:H⁴(F₂)→H⁶(F₂) 是它的转置，因此满射。记为

\[
\mathrm{Sq}^2:H^4(X;\mathbb F_2)\twoheadrightarrow H^6(X;\mathbb F_2).
\tag{5}
\]

## 4. 奇数次数的关键计算

**引理。** 对 Kummer 四维型，有

\[
\mathrm{Sq}^2:H^3(X;\mathbb F_2)
\xrightarrow{\ \simeq\ } H^5(X;\mathbb F_2).
\tag{6}
\]

以下给出证明，包括通用族的分歧项，不能只引用 b₃=b₅ 就断言同构。

### 4.1 文献中的整数对偶基

在 K₂(A) 上，令 aᵢ∈H¹(A,Z) 为基，aᵢ*∈H³(A,Z) 为其整数对偶。记 θ:K₂(A)→A^[3]。按 [29] Proposition 6.2，H³(X,Z) 有基

\[
p_i=\frac12\theta^*\bigl(q_1(a_i^*)q_1(1)^2|0\rangle\bigr),
\qquad
q_i=\frac12\theta^*\bigl(q_2(a_i)q_1(1)|0\rangle\bigr).
\]

H⁵ 中有对偶基 uᵢ、vᵢ，其中

\[
v_i=\theta^*\bigl(q_2(a_i^*)q_1(1)|0\rangle\bigr),
\quad
\langle p_i,u_j\rangle=\delta_{ij},\quad
\langle q_i,v_j\rangle=\pm\delta_{ij},\quad
\langle p_i,v_j\rangle=\langle q_i,u_j\rangle=0.
\tag{7}
\]

模二以后符号无关。先证明

\[
\mathrm{Sq}^2\rho_2(p_i)=\rho_2(v_i).
\tag{8}
\]

### 4.2 光滑关联空间及分歧除子

取光滑 nested Hilbert scheme A^[2,3]，忘掉长度二子概形的映射为 g:A^[2,3]→A^[3]，剩余点映射为 p:A^[2,3]→A。此空间光滑，g 通过通用族分解为其 birational resolution 后接三重有限映射，见 [31] §2、Proposition 2.1（追溯 Ellingsrud–Strømme）。

令

\[
Y=(\Sigma\circ g)^{-1}(0),\qquad \pi=g|_Y:Y\longrightarrow X.
\]

Y 是光滑紧致复四维流形：平移 A 的作用使 Σ∘g 的微分在平移方向等于乘 3，处处满射。π 是泛型次数三的全纯映射。通用族对应给出

\[
p_i=\pi_*p^*(a_i^*).
\tag{9}
\]

这里的光滑性也可只在所需的小长度情形核验：[31] Proposition 2.1(ii) 把 A^[2,3] 写成 A×A^[2] 沿通用族 Z₂ 的吹起，而 Z₂≅Bl_Δ(A×A) 光滑。该文 PDF p.6 还直接给出 K_(A^[2,3])≅O(E_inc)，E_inc 为“剩余点包含在长度二子概形中”的例外除子。对光滑纤维 Y 作 adjunction，K_Y=O(E_inc|Y)，独立核对了下面分歧类的来源。

可以先删去 X 中 81 个非 curvilinear 三重点，再进行以下计算。其余地方通用族光滑，nested resolution 为同构，π 是光滑流形之间的有限分歧映射。删去有限点不改变 H³、H⁵ 或 H⁶，因此足以确定 (8)。

π 的虚法丛 ν_π=π*TX−TY 有

\[
w_2(\nu_\pi)=\rho_2(c_1(\nu_\pi))=\rho_2[R],
\tag{10}
\]

其中 R 是 det Dπ 的零除子。确实，det Dπ 是 K_Y⊗π*K_X^{-1} 的截面；K_X 平凡，所以 c₁(ν_π)=c₁(K_Y)=[R]。

泛型分歧点对应“一个二重点 x 加一个不同的单点 y，所标记的剩余点为 x”。局部 π 在碰撞方向就是 (z,…)↦(z²,…)；因此 R 的重数为 1。π 将这一除子以次数 1 映到 Hilbert–Chow 边界，并保留二重点 x 的标签。故，作为带 H*(A) 插入的对应，

\[
\pi_*\bigl([R]p^*\alpha\bigr)
=\theta^*\bigl(q_2(\alpha)q_1(1)|0\rangle\bigr),
\qquad \alpha\in H^*(A).
\tag{11}
\]

这里没有额外系数 2：q₂(1)q₁(1)|0〉本来就是完整边界除子，即 2δ，而不是 δ。三重点的边界低一复维，不会增加新的除子分量；在删点开集上的上述对应由泛型带标签的边界唯一确定。

### 4.3 Thom–Gysin 公式与对偶性

对两个有向光滑流形之间的 proper 映射，Thom 公式给出

\[
\mathrm{Sq}^2\pi_*z
=\pi_*\bigl(\mathrm{Sq}^2z+w_2(\nu_\pi)z\bigr).
\tag{12}
\]

可把 π 与一个嵌入组成图嵌入，再对其 Thom 类应用 Sq(U)=w(ν)U 推出；因丛和流形有向，Sq¹ 的交叉项为零。这也适用于上述删点开集上的 proper 映射。

A 是四维实环面，正次数 Steenrod 运算在其上全部为零：H*(A,F₂) 由平方为零的一次类生成，直接用 Cartan 公式即可。将 (9)、(10)、(11) 代入 (12)，便得 (8)。

为核对这个分歧项的系数，同一个公式用于 α∈H²(A,Z) 时给出

\[
\mu(\alpha)^2\equiv q_2(\alpha)q_1(1)|0\rangle
\equiv\delta\mu(\alpha)/3\pmod2,
\]

与 [29] Proposition 6.30(iii) 的独立整数半积关系一致；此处 α² 在 A 上为偶数，相关推前项模二为零。这个检验不代替 (12) 的证明，但排除了常见的边界 2 倍因子混淆。

最后，X spin，且所有模二类整数提升，所以 Sq¹=0。对 x,y∈H³(X,F₂)，

\[
\langle\mathrm{Sq}^2x,y\rangle
=\langle x,\mathrm{Sq}^2y\rangle.
\tag{13}
\]

若 x=Σrᵢpᵢ+Σsᵢqᵢ 满足 Sq²x=0，用 (8)、(13) 与 pⱼ 配对，得

\[
0=\langle x,v_j\rangle=s_j.
\]

于是 Sq²x=Σrᵢvᵢ，由 (7) 得所有 rᵢ=0。故 (6) 单射；两侧维数都为 8，所以为同构。证明完毕。

注意无需计算 Sq²qᵢ 的全部系数。按两组对偶基，Sq² 的矩阵形如

\[
\begin{pmatrix}0&I\\ I&C\end{pmatrix},
\]

C 的具体值不影响可逆性。

## 5. KSp 没有留下不可见的二阶挠元

KSp⁰=KO⁻⁴ 的 AHSS 总次数零线上的全部可能项为

\[
H^0(X;\mathbb Z),\ H^4(X;\mathbb Z),\
H^5(X;\mathbb F_2),\ H^6(X;\mathbb F_2),\ H^8(X;\mathbb Z).
\]

其中

\[
d_2:H^3(X;\mathbb Z)\to H^5(X;\mathbb F_2)
\quad\text{是 }\mathrm{Sq}^2\rho_2,
\]

由 (6) 及 H⁴ 无二挠而满射；另一个

\[
d_2:H^4(X;\mathbb F_2)\to H^6(X;\mathbb F_2)
\quad\text{是 }\mathrm{Sq}^2,
\]

由 (5) 满射。两个潜在挠项在 E₃ 页全部消失。其余分次项自由，高阶微分不能产生挠像于自由目标。因此 KSp⁰(X) 无挠，忘却 KSp⁰→K⁰ 单射，理由与 notes/36 引理 C 相同。

另一方面，[30] 保证全部整数上同调自由。复 K 理论 AHSS 的各项也自由，其微分有理化后为零，逐页得到所有微分为零，故 K⁰(X) 无挠。因此实际 E 满足

\[
[E]+[E^*]=[TX]\quad\text{in }K^0(X).
\]

忘却映射单射将等式提升到 KSp⁰；再用实际四元数秩二的稳定 cancellation，得到

\[
(TX,\Omega)\simeq H(E).
\]

其第一因子 E 是所需的实际连续复 Lagrangian 子丛，证明 (1) 的充分性。

## 6. 已闭合与仍未闭合

**已闭合：** 两个标准类型的全部剩余行列式候选都能由真实连续、乃至光滑复 Lagrangian 子丛实现。Kummer 的奇数上同调项没有被略去，而由 (6) 消掉。36 与本记录均经过实际降秩、复辛类识别及实际 cancellation。

**没有闭合：** 这些分布的可积性、f-不变性、由真实切导数一致收缩，以及全局 Anosov 实现。没有推出两侧分布全纯，也没有证明 Ghys 刚性，更没有构造 Anosov 反例。

既然纯拓扑真实存在问题在这两个类型上得到肯定判据，下一步主动转向动力学；不继续重复同类 Chern 数或复指标计算来尝试否定已实现的候选。一个直接但非平凡的真实切导数约束见 notes/38。

## 7. 文献及新颖性核验范围

- [29] Kapfer–Menet, Integral cohomology of the generalized Kummer fourfold，Proposition 6.2（PDF pp.16–17）、6.23（p.21）、6.30（p.23）、Theorem 6.31（pp.25–26）、§8.3（p.34）。
- [30] 同作者 Corrigendum，Theorem 1：整数上同调无挠的正确证明。
- [31] Meachan, Derived autoequivalences of generalised Kummer varieties，§2、Proposition 2.1：光滑 nested Hilbert 对应、通用族及其分解。
- [23] Proposition 3.2、[27] 稳定 Euler 完备性、[28] KO d₂ 及 Thom 公式，使用范围同 notes/36。

上述论文提供输入；本记录中的 (8) 由通用族分歧与 Thom–Gysin 公式直接推导，再由对偶性证明 (6)。针对 Kummer、Steenrod、continuous Lagrangian subbundle、topological polarization 等检索未发现陈述 (1) 或 (6) 的原始论文，但尚不能据此认定新颖性。标准工具及已发表的整数基不作为本研究的原创结果。检索范围另见 literature/actual_reduction_novelty_search_log.md。

2026-10-18 动力学更新：39 已独立于本笔记的拓扑计算，排除整个 Kummer 四维变形类型上的全纯 Anosov。这里的真实 Lagrangian 子丛仍然存在；它们不能实现为这种实际自同构的稳定丛。不能把“拓扑存在性已解决”误解成“动力学候选依旧未被排除”。
