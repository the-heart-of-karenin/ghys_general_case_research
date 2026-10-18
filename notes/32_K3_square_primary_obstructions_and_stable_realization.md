# K3^[2]：主障碍与复 K 理论检验没有排除剩余数据

日期：2026-10-18。性质：一个可严格核验的“尚无矛盾”结果。只讨论 K3^[2] 型；不据此断言真的存在连续 Lagrangian 平面场或 Anosov 自同构。

后续状态更新：notes/36 已另行补齐实际秩二降秩、KSp 类识别和实际复辛 cancellation，证明本记录的全部候选确能实现为真实连续 Lagrangian 子丛。本记录保留当时稳定阶段的论证与缺口，不能把后来的实际存在性误归因于本记录单独的 K⁰ 计算。

## 1. 精确结论

设 X 为 K3^[2] 型 IHS 四维流形，选一个标准拓扑格标记。对任何

\[
a\equiv\delta\pmod{2H^2(X,\mathbf Z)},
\qquad q(a)=6\text{ 或 }-26,
\]

定义 b=(c_2(X)+a²)/2。则：

1. b 是整数四次上同调类；
2. b²=c_4(X)，Sq²ρ_2(b)=ρ_2(ab)；
3. 存在一个实际的**复秩四**拓扑向量丛 ζ，满足
   c_1(ζ)=a、c_2(ζ)=b、c_3(ζ)=c_4(ζ)=0；
4. 令 V=[ζ]−2∈K⁰(X)，则 V 是虚秩二，且

\[
\boxed{[TX]=V+V^*\quad\text{in }K^0(X).}
\tag{1}
\]

因而只使用 Chern character、复 K 理论及其整数指标的进一步必要条件，不能排除这组数据：V 已是合法 K 理论类，所有此类扭曲指标都会为整数。

**没有证明 V 能由实际秩二丛代表；即便能，也没有证明所需复辛嵌入、叶状可积性或 Anosov 实现。**

## 2. 一个有用的整数 Chern 公式

先取 X=S^[2]，p∈S。记 Σ_p 为长度二子概形包含 p 的闭子集，它是一个复曲面，其整数上同调类记为 s∈H⁴(X,Z)。δ 是 Hilbert–Chow 例外除子的一半。则

\[
\boxed{c_2(X)=24s-3\delta^2.}
\tag{2}
\]

核验：(21_OGrady_2022_Modular_sheaves.pdf，式 (5.3.3)，PDF p.17) 在双覆盖 p_B:Bl_Δ(S×S)→S^[2] 上给出

\[
p_B^*c_2(X)=24(q_1^*\eta+q_2^*\eta)-3e_B^2,
\quad p_B^*\delta=e_B.
\]

Σ_p 的逆像是 {p}×S 与 S×{p} 的两条严格变换，故 p_B^*s=q_1^*η+q_2^*η。有限覆盖的 pullback 在有理上同调上单射，而 H⁴(X,Z) 无挠，推出整数等式 (2)。X 的其他变形通过光滑平行运输继承该整数类等式；不要求 s 在每个复结构下仍是代数曲面。

这里 Hilbert scheme 的整数上同调无挠、奇数上同调为零，见 24_Kapfer_2016_Integral_cohomology.pdf，Theorem 1.7 及 Theorem 1.11 后的说明，PDF pp.3–4。

写 a=δ+2β，得到

\[
b=12s-\delta^2+2\delta\beta+2\beta^2\in H^4(X,\mathbf Z).
\tag{3}
\]

故 28 的“c_2+a² 为二倍类”约束在这里没有再排除任何这样的 a。

## 3. Steenrod 主障碍也通过

由 (3)，ρ_2(b)=ρ_2(δ²)，而 ρ_2(a)=ρ_2(δ)。Cartan 公式给出 Sq²ρ_2(δ²)=0。

另一方面，δ³ 是二倍整数类：Fujiki 极化给出

\[
\int_X\delta^3\mu(\alpha)=0\quad(\alpha\in H^2(S,\mathbf Z)),
\qquad \int_X\delta^4=12.
\]

δ³ 与 H²(X,Z) 的所有配对为偶数。H²、H⁶ 的整数 Poincaré 配对完美且无挠，所以 δ³∈2H⁶(X,Z)。于是

\[
\mathrm{Sq}^2\rho_2(b)=0=\rho_2(ab).
\tag{4}
\]

此外，q(a) 的两个取值使 ∫b²=324=∫c_4(X)。因 H⁸(X,Z)≅Z，得到完整的 b²=c_4(X)，不只是一条数值等式。

## 4. 稳定实现：正确使用秩四判据

使用 23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf 的 Proposition 3.2（PDF p.6）。X 是 spin，取其 Spin^c 特征类 c_spin=0；q_1(TX_R)=p_1/2=−c_2(X)。

令该命题中的 (l,u,v,w)=(a,b,0,0)。其 Steenrod 条件已由 (4) 验证；剩余 top cell 条件是

\[
J:=\frac12\int_X b\bigl(b-c_2(X)-2a^2\bigr)\equiv0\pmod6.
\tag{5}
\]

使用 ∫c_2²=828、∫c_2a²=30t、∫a⁴=3t²、∫b²=324，得到

\[
J=-45-\frac{45}{2}t-\frac32t^2
=\begin{cases}
-234,&t=6,\\
-474,&t=-26.
\end{cases}
\]

两个数都为 6 的倍数。因此确有**实际复秩四丛** ζ 具有所需 Chern 类。

这是 stable-range 定理；不能因为 c_3、c_4 为零就省略所有降秩障碍，直接写“所以存在 E 秩二”。

## 5. 为什么所有复 K 指标都不会再给矛盾

V=[ζ]−2 是合法虚秩二类，Chern character 恰为 31 §2 的表达。由 (28) 的 Chern 关系，直接得到

\[
\operatorname{ch}(V+V^*)
=4-c_2(X)+\frac{c_2(X)^2-2c_4(X)}{12}
=\operatorname{ch}(TX).
\]

K3^[2] 的奇数整数上同调为零、偶数上同调无挠；复 K 理论的 Atiyah–Hirzebruch 谱序列因而退化，各分次商自由，K⁰(X) 无挠。Chern character 的有理同构于是把上式提升为整数 K⁰ 中的 (1)。

任意 W∈K⁰(X) 的 I(V⊗W) 当然是整数。因此重复检查更多这类指标，不会将这些候选排除。

若再给定实际自同构 f，且 a 被 f* 固定，则 b 也被固定；V 的 Chern character 全部被固定，由 K⁰ 无挠还得到 f*V=V。因此仅要求这个虚类在 K⁰ 层 f*-不变，也没有新增矛盾。

这句话只针对复 K 理论的稳定信息，**不排除实 KO、复辛 KSp、unstable 降秩或平面场可积性提供额外障碍**。

## 6. 剩余的拓扑问题到底是什么

ζ 的 c_4=0 允许先分裂掉一个平凡复线，得到秩三丛且 c_3=0。进一步分裂到秩二时，球纤维为 S⁵：除 c_3 主障碍外，还可能涉及 π_6(S⁵)、π_7(S⁵) 的 Z/2 障碍及选择的相容性。本轮没有完成该 lifting 问题。

而“存在秩二 E”与“(TX,Ω) 中存在复 Lagrangian E”仍是不同问题。需要把 reduction 精确落到 Sp(2)/U(2) 的截面问题，不能仅凭复 K 类相等就视为复辛同构。

23 的 Corollary 8.4 的简洁 quaternionic 判据有 c_1(det E)≡w_2(X) 的前提，当前 a 非偶，不满足。不能用它制造额外的 mod 12 矛盾。

## 7. 本轮的方向判断

31 的配对偶性是成功的必要条件；本记录说明在 K3^[2] 上，这条路线的稳定复拓扑部分已出现可明确定位的上限。下一步有意义的是完成真正的 Sp(2)→U(2) lifting，或引入真实叶状结构与动力学，而不是继续添加同类 Chern 数或复指标检验。
