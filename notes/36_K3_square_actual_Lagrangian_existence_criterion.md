# K3^[2] 型：真实连续复 Lagrangian 子丛的存在判据

日期：2026-10-18。性质：完成 notes/32、34 在 K3^[2] 型上的真实降秩及复辛同构步骤。结论只涉及拓扑子丛，不包含可积性、f-不变性或 Anosov 实现。文献新颖性只完成有范围的检索，未确认首创。

## 1. 结论

设 X 为 K3^[2] 型 IHS 四维流形，Ω 为其全纯辛形式。固定标准格标记

\[
H^2(X,\mathbb Z)=L_0\oplus\mathbb Z\delta,
\quad L_0=U^3\oplus E_8(-1)^2,\quad q(\delta)=-2.
\]

则对 a∈H²(X,Z)，下列条件等价：

1. (TX,Ω) 有一个连续的复秩二 Lagrangian 子丛 E，且 c₁(E)=a；
2. a≡δ mod 2H²(X,Z)，且 q(a)=6 或 −26。

连续截面可光滑逼近为 Lagrangian Grassmann 丛的光滑截面，所以也可要求 E 为光滑拓扑子丛。这里“光滑”不等于全纯或可积。

特别地，两组候选都确实存在，例如

\[
a=2e+2f+\delta,\qquad a=2e-6f+\delta
\]

在一个双曲平面 U=Ze⊕Zf 中分别有平方 6、−26。因此，忘掉动力学以后，K3^[2] 的真实 Lagrangian 平面场并不存在进一步的普遍不存在障碍。

必要性已经由 notes/28、31 证明，而且那些证明只用了连续 Lagrangian 分裂。以下完整补上充分性，不能跳过其中任一环节。

## 2. 降秩引理：非特征行列式消掉最后的二维障碍

**引理 A。** 设 M 是闭、单连通、有向八维光滑流形，F 是有向实秩六丛。若

\[
w_2(F)\ne w_2(TM),
\]

则 F 有处处非零截面，当且仅当 e(F)=0。

**证明。** 必要性为 Euler 类的基本性质。证明充分性时，先用稳定同伦 Euler 类 γ(F)。球丛的纤维 S⁵ 是四连通的，M 的维数 8≤9，因此稳定 Euler 类的消失是实际截面存在的充分必要条件。准确的稳定范围见 Klein–Williams [27]，Corollary 3.5（PDF p.10）；其 §4 的 Poincaré 对偶把 Euler 类识别到

\[
\gamma(F)\in\pi_0\bigl(M^{F-TM}\bigr)
       =\pi_2\bigl(M^{\xi}\bigr),
\quad \xi=F-TM+\mathbb R^2.
\tag{1}
\]

ξ 是有向虚秩零丛；其 Thom **谱**可以有零维及以上的胞腔。球谱到 connective ko 的单位映射在 π₀、π₁、π₂ 上为同构（分别为 Z、Z/2、Z/2），在 π₃ 上满射。因而它在 (1) 的 π₂ 上仍给出同构。注意此处用 connective ko，不能让周期 KO 的负次数系数进入低维计算。

计算 ko₂(M^ξ) 的同调 AHSS。按 Thom 同构，总次数二只有

\[
E^2_{2,0}=H_2(M;\mathbb Z),\quad
E^2_{1,1}=H_1(M;\mathbb F_2)=0,\quad
E^2_{0,2}=H_0(M;\mathbb F_2)=\mathbb F_2.
\]

最后一项是可能保留的 Arf 型模二障碍。微分

\[
d_2:E^2_{2,1}=H_2(M;\mathbb F_2)
       \longrightarrow E^2_{0,2}=\mathbb F_2
\tag{2}
\]

由 Thom 空间上的 Sq² 对偶给出。若 U 是虚秩零 Thom 类，则

\[
\mathrm{Sq}^2 U=w_2(\xi)U,
\quad w_2(\xi)=w_2(F)+w_2(TM).
\]

因此 d₂(z)=〈w₂(ξ),z〉。这是通常的 KO/ko d₂ 与 Thom 公式；参见 Zibrowius [28] §3、Lemma 3.5（PDF pp.24、27）。也可先在 q=0 行计算 d₂，再乘系数 η∈ko₁，利用 η²生成 ko₂；单连通性保证 H₂(M;Z)→H₂(M;F₂) 满射。

由 w₂(ξ)≠0，(2) 满射，故 E^∞_{0,2}=0。中间项也为零，于是 AHSS 的边缘同态

\[
ko_2(M^\xi)\longrightarrow H_2(M;\mathbb Z)
\]

单射；其像可能只是 H₂ 的一个子群，**不需要声称它满射**。γ(F) 的边缘像是 e(F) 的 Poincaré 对偶。若 e(F)=0，γ(F)=0，稳定 Euler 完备性便给出真实截面。证毕。

**复丛推论。** M 若是 spin，β 是复秩三丛，c₁(β) mod 2 非零且 c₃(β)=0，则 β 分裂掉一条平凡复线。真实实截面也是复向量丛的非零截面；取 Hermitian 正交补即得到复秩二丛。

这里不是套用 [23] Corollary 8.4。后者要求行列式类模二等于 w₂(M)，而本引理处理的恰是两者不相等的情形。

## 3. 把 notes/32 的虚秩二类实现成真实秩二丛

对满足条件 2 的 a，令

\[
c=c_2(X),\quad d=c_4(X),\quad b=(c+a^2)/2.
\]

notes/32 已严格证明：b 是整数类，b²=d，Sq²ρ₂b=ρ₂(ab)，且存在实际复秩四丛 ζ，满足

\[
c_1(\zeta)=a,\quad c_2(\zeta)=b,\quad
c_3(\zeta)=c_4(\zeta)=0.
\tag{3}
\]

这里使用 [23] Proposition 3.2，而非秩二判据。其最终同余 J 在两种平方值下分别为 −234、−474，均为 6 的倍数。

因为 c₄(ζ)=0，八维底空间上秩八实丛 ζ_R 的唯一截面障碍消失，先得到 ζ≅C⊕β，β 为复秩三，c₁(β)=a、c₃(β)=0。X 单连通、spin，a mod 2=δ mod 2≠0。由引理 A，再得

\[
\zeta\simeq\mathbb C^2\oplus E,
\qquad \operatorname{rank}_{\mathbb C}E=2,
\quad c_1(E)=a,\quad c_2(E)=b.
\tag{4}
\]

这一步首次把 notes/32 的 V=[ζ]−2 实现为实际 E，但还没有给出复辛嵌入。下一步专门处理后者。

## 4. K3 Hilbert 平方的 Steenrod 平方满射

**引理 B。** 对 K3^[2] 型 X，有

\[
\mathrm{Sq}^2:H^4(X;\mathbb F_2)\longrightarrow
H^6(X;\mathbb F_2)\quad\text{满射。}
\tag{5}
\]

**证明。** 可在 S^[2] 上计算，再沿光滑变形运输。记 μ:H²(S,Z)→H²(X,Z)，s=[Σ_p]，Σ_p 是包含固定 p∈S 的长度二子概形曲面。除 s 为整数类外，还需要以下真正的整数类：

\[
D_\theta:=\frac{\mu(\theta)^2-\delta\mu(\theta)}2
\in H^4(X;\mathbb Z),\qquad\theta\in H^2(S;\mathbb Z).
\tag{6}
\]

核对 (6)：在 Nakajima 记号中，q₁(θ)q₁(θ)|0〉与 q₂(θ)|0〉之差的一半是 monomial symmetric function m_(1,1),θ，对整数基 θ 为 [24] Theorem 1.7 的整数类；任意 θ 的情形通过展开整数线性组合得到。另一方面，双覆盖 Bl_Δ(S×S)→S^[2] 的 pullback 给出

\[
\mu(\theta)^2=q_1(\theta)q_1(\theta)|0\rangle
                 +q_S(\theta)s,\qquad
\delta\mu(\theta)=q_2(\theta)|0\rangle.
\]

q_S(θ) 偶，故 (6) 成立。若采用相反的 δ/Nakajima 符号，(6) 的加减号互换；两类相差一个整数类，不影响下面的模二论证。

先证明平方映射 H²(X;F₂)→H⁴(X;F₂) 单射。写整数提升 α=μ(γ)+kδ；所有二次模二类均有整数提升。曲面 Σ_p≅Bl_p S 上，μ(γ) 限制为 γ 的 pullback，δ 限制为例外曲线，故

\[
\int_Xs\alpha^2=q_S(\gamma)-k^2\equiv k\pmod2.
\]

若 α² mod 2=0，先得 k 偶。再与 (6) 配对，Fujiki 极化给出

\[
\int_X\mu(\gamma)^2D_\theta
=\frac{q_S(\gamma)q_S(\theta)}2+B_S(\gamma,\theta)^2
\equiv B_S(\gamma,\theta)\pmod2.
\]

因为 K3 格偶且幺模，所有配对为偶迫使 γ∈2H²(S,Z)。故 α 偶，证明了平方映射单射。

最后，对 x∈H²(X;F₂)、y∈H⁴(X;F₂)，spin Wu 公式及 Sq¹=0 给出

\[
\int_Xx\,\mathrm{Sq}^2y=\int_Xx^2y.
\]

所以 (5) 的转置正是刚证明单射的平方映射。Poincaré 对偶推出 (5) 满射。证毕。

本证明使用整数 H⁴ 中的半积类，而不是只在 Sym²H² 的有理子空间内检验交数；这是它能够识别实际二阶挠元的原因。

## 5. 忘掉复辛结构的映射在这里单射

**引理 C。** K3^[2] 型 X 的 KSp⁰(X)=KO⁻⁴(X) 无挠，且忘却映射

\[
F:KSp^0(X)\longrightarrow K^0(X)
\tag{7}
\]

单射。

**证明。** H^odd(X,Z)=0，H^even(X,Z) 自由。在 KSp AHSS 的总次数零线上，唯一可能的挠分次项是

\[
E_2^{6,-6}=H^6(X;\mathbb Z/2).
\]

进入它的微分为

\[
d_2:E_2^{4,-5}=H^4(X;\mathbb Z/2)
       \longrightarrow E_2^{6,-6},\qquad d_2=\mathrm{Sq}^2.
\]

这是 KO 的 q≡−1→−2 行平移四度后的微分，见 [28] §3；由引理 B，它满射。因此该挠项在 E₃ 页消失。其余可能非零分次项是 p=0、4、8 的自由整数项。高阶微分有理化后为零；进入自由群的挠像为零，故它们的最终子商仍自由。于是 KSp⁰(X) 无挠。

忘却映射有理化后单射：四元数 Chern character 在 0、4、8 次上均非零。因此 (7) 的核是挠群，已证无挠，故核为零。证毕。

这里未假设 AHSS 在所有总次数上退化，也未把复 K⁰ 无挠误写成 KSp⁰ 无挠。

## 6. 从真实 E 到 TX 内的真实 Lagrangian 子丛

给 E⊕E* 赋典范复辛形式

\[
\omega_H((v,\phi),(w,\psi))=\psi(v)-\phi(w).
\]

记该 quaternionic/复辛丛为 H(E)。由 (4) 和 notes/32，

\[
F([H(E)])=[E]+[E^*]=[TX]\quad\text{in }K^0(X).
\]

TX 的给定 Ω 与 H(E) 都定义 KSp⁰ 中的类。由引理 C，

\[
[H(E)]=[(TX,\Omega)]\quad\text{in }KSp^0(X).
\tag{8}
\]

最后必须进行实际 cancellation：Sp(2)→Sp(∞) 的首个商球面是 S¹¹，因此 BSp(2)→BSp(∞) 在八维底空间上处于唯一稳定实现范围。两侧都是实际四元数秩二丛，(8) 推出实际 Sp(2) 丛同构，亦即实际复辛同构

\[
(TX,\Omega)\simeq (E\oplus E^*,\omega_H).
\tag{9}
\]

(9) 将第一个 E 作为真实连续复 Lagrangian 子丛送入 TX。这才完成充分性。

证明链中的三个不同步骤是：实际秩二实现 (4)、复辛稳定类识别 (8)、实际复辛 cancellation (9)。没有将稳定复 K 数据直接视为真实子丛。

## 7. 对研究方向的含义与准确限制

K3^[2] 型上，notes/31 的全部剩余行列式候选确实能够实现为真实连续复 Lagrangian 子丛。因而不能再期待用“根本不存在任何连续 Lagrangian 平面场”来排除此类型。

本定理不声称这些平面场可积、保持全纯叶片、被某个自同构保持或可作为统一收缩丛。即使 f* 固定 a，也不能由此构造一个 Df-不变截面。后续应利用真实切导数、Anosov 叶状结构或全局全纯动力学。

## 8. 文献核验及新颖性状态

- [21] O'Grady, Modular sheaves on hyperkähler varieties，式 (5.3.3)、(5.3.4)：c₂ 与 Fujiki 输入；相关页沿用 notes/32 的核验。
- [23] Čadek–Crabb–Vanžura, Obstruction theory on 8-manifolds，Proposition 3.2：实际秩四 ζ 的实现；未误用 Corollary 8.4。
- [24] Kapfer, Computing cup products in integral cohomology of Hilbert schemes of points on K3 surfaces，Definition 1.2、Theorem 1.7：整数半积类；同文确认整数上同调自由且奇数为零。
- [27] Klein–Williams, Homotopical intersection theory I，Corollary 3.5、Theorem 4.1：稳定 Euler 障碍的完备范围及对偶。
- [28] Zibrowius, Witt groups of complex cellular varieties，§3、Lemma 3.5：通用 KO d₂ 与 Thom 公式。这里只用该通用公式，不假设 K3^[2] 是 cellular variety。

引理 A、B、C 是本记录中展开证明的特化/组合步骤，不把标准稳定同伦工具宣称为新方法。针对“continuous Lagrangian subbundle / topological polarization / K3 Hilbert square / tangent splitting”及两组平方值的检索，没有发现陈述本判据的原始论文；这仅是未检出同一结论，不能证明首创。详见 literature/actual_reduction_novelty_search_log.md。
