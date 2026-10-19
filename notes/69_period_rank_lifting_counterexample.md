# 周期不能恢复逐点秩：紧致六维模型上的显式反例

日期：2026-10-18。性质：完成上一轮所建议的有边界检验，结果是否定的。本文证明 66 的逐点条件不能用相应杯积条件代替；反例就在 05 的同一紧致模型上，并可任意接近原模型。不是 Ghys 猜想的反例，也没有构造非模型的保全纯辛全纯 Anosov 系统。全文是外代数、Lie 代数和显式微分计算，不使用新的外部预印本主定理；首创性未确认。

## 1. 要检验的命题与反例定理

沿用 05 的 M=Γ\G，复维数六、实维数十二，以及保格双曲自同构 F。令 λ=2+√3。原不变 coframe 满足

\[
d\gamma=\beta\wedge\bar\alpha,\qquad
d\zeta=\epsilon\wedge\bar\delta,
\qquad d\alpha=d\beta=d\delta=d\epsilon=0,
\tag{1.1}
\]

及共轭方程；F* 在 α,β,γ,δ,ε,ζ 上的权重依次为 λ²,λ⁻¹,λ,λ⁻²,λ,λ⁻¹。原全纯辛形式为

\[
\Omega_0=\alpha\wedge\delta+
\gamma\wedge\beta+\zeta\wedge\epsilon.
\]

66 已证明每个 F 固定二阶上同调类 c 有唯一的闭、左不变且 F 固定代表 S_Fc。原拟检验：

\[
c^4=0,\quad\langle c^3\bar c^3,[M]\rangle\ne0
\quad\Longrightarrow\quad (S_Fc)^4=0\ ?
\tag{1.2}
\]

**反例定理。** 令

\[
\boxed{\omega_t=\Omega_0+t\,\bar\beta\wedge\bar\epsilon,
\qquad c_t=[\omega_t],\qquad t\in\mathbb C.}
\tag{1.3}
\]

则 dω_t=0，F*ω_t=ω_t，故 S_Fc_t=ω_t。对每个 t≠0，

\[
c_t^4=0,\qquad
\omega_t^3\wedge\bar\omega_t^3
=\Omega_0^3\wedge\bar\Omega_0^3\ne0,
\qquad\omega_t^4\ne0.
\tag{1.4}
\]

ω_t 的复秩为八，不能是任何复结构上的全纯辛形式；六复维的全纯辛形式在实切丛复化上应有复秩六。特别地，(1.2) 在原模型周期的每个邻域均失败。

更强地，c_t 本身可以由同一紧致流形上的真实闭全纯辛形式实现，只是相应复结构不被 F 保持。见第 3 节。

## 2. 完整的 exact 原函数与非退化检验

记 H=α∧δ、U=γ∧β、V=ζ∧ε、B=barβ∧barε。四者各自平方为零，其支撑的八个一形式互异，故

\[
\omega_t^4=24t\,H\wedge U\wedge V\wedge B\ne0
\quad(t\ne0),\qquad\omega_t^5=0.
\tag{2.1}
\]

定义全局左不变七形式

\[
\eta=\bar\gamma\wedge\delta\wedge\gamma\wedge\beta
\wedge\zeta\wedge\epsilon\wedge\bar\epsilon.
\]

因为 dbarγ=−α∧barβ，而 d(γ∧β)=d(ζ∧ε)=0，直接逐项计算得

\[
d\eta=H\wedge U\wedge V\wedge B.
\qquad\boxed{\omega_t^4=24t\,d\eta.}
\tag{2.2}
\]

所以四次幂在 de Rham 上同调中为零，却逐点非零。这里 η 也 F 固定：它的总权重为零。因此即使只在 F 固定的不变复形中工作，该 exact 误差也真实存在。

顶形式 ω_t³∧barω_t³ 必须同时含 α,δ,barα,barδ，所以各取 H 与 barH；同时必须含 γ,ζ,barγ,barζ，只能各取 U,V,barU,barV。任何使用 B 或 barB 的项均缺少某个中心一形式。因此

\[
\omega_t^3\wedge\bar\omega_t^3
=36H\wedge U\wedge V\wedge\bar H\wedge\bar U\wedge\bar V
=\Omega_0^3\wedge\bar\Omega_0^3.
\tag{2.3}
\]

此为处处非零的不变顶形式，积分非零。由 (2.1) 的四次幂非零、五次幂为零，ω_t 复秩恰为八。证明完毕。

这不与 66 的二阶代表唯一性矛盾。唯一性只排除非零 F 固定 exact **二形式**；这里出现的是非零 F 固定 exact **八形式**。S_F 是二阶线性截面，未被证明、也不能被视为保楔积的截面。

## 3. 这些周期甚至来自真实的全纯辛结构

对任意 s,u∈C，令

\[
\begin{split}
\theta_1&=\alpha-u\bar\epsilon,&\theta_2&=\beta,&\theta_3&=\gamma,\\
\theta_4&=\delta+s\bar\beta,&\theta_5&=\epsilon,&\theta_6&=\zeta,\\
\widetilde\Omega_{s,u}
&=\theta_1\wedge\theta_4+
\theta_3\wedge\theta_2+\theta_6\wedge\theta_5.
\end{split}
\tag{3.1}
\]

θ₁,…,θ₆ 与其共轭始终构成十二维复 coframe：其相对于旧 coframe 的变换是行列式一的三角变换。这些形式定义全局几乎复结构 J_{s,u}。

θ₁、θ₄、θ₂、θ₅ 闭；而

\[
d\theta_3=\theta_2\wedge(\bar\theta_1+\bar u\theta_5),
\qquad
d\theta_6=\theta_5\wedge(\bar\theta_4-\bar s\theta_2).
\]

右侧没有 (0,2) 项，所以 J_{s,u} 可积。由 (3.1)，tildeΩ_{s,u} 在该复结构上非退化且闭，因而全纯辛。等价地，也可使用闭复二形式核的 Cartan 可积性论证。

展开得

\[
\widetilde\Omega_{s,u}
=\omega_{su}+s\alpha\wedge\bar\beta
+u\delta\wedge\bar\epsilon
=\omega_{su}-d(s\bar\gamma+u\bar\zeta).
\tag{3.2}
\]

因此 [tildeΩ_{s,u}]=c_{su}，且其全纯辛体积与 Ω₀ 完全相同。令 s=u=r→0，就得到真实全纯辛结构趋于原模型，而其周期 c_{r²} 的唯一 F 固定不变代表秩为八。

同时

\[
F^*\widetilde\Omega_{s,u}
=\widetilde\Omega_{\lambda s,\lambda^{-1}u},
\qquad F^*J_{s,u}=J_{\lambda s,\lambda^{-1}u}.
\tag{3.3}
\]

这些复结构的 coframe 图参数唯一，故 F 对 J_{s,u} 全纯当且仅当 s=u=0。对任何固定 t=su，周期不变，但 F 在实际结构参数上按相反方向伸缩。

**边界必须保留：** (M,J_{s,u},tildeΩ_{s,u}) 是真实紧致全纯辛流形，F 是底层的真实 Anosov，但二者在 (s,u)≠(0,0) 时不相容。本文没有把它们合并成保全纯辛全纯 Anosov 三元组。它证明的是“实际全纯辛周期＋F 在上同调上固定”仍不够。

## 4. 实部、虚部构成完整辛形式铅笔仍不足

令 a_t=Re ω_t、b_t=Im ω_t。任意 r,s∈R 有逐点恒等式

\[
\boxed{(r a_t+s b_t)^6
=(r^2+s^2)^3(\operatorname{Re}\Omega_0)^6.}
\tag{4.1}
\]

证明：在 (Aω_t+Bbarω_t)⁶ 中，顶项只可能是 20A³B³ω_t³barω_t³；令 A=(r−is)/2、B=(r+is)/2 并使用 (2.3)。所以每个非零实线性组合均为闭实辛形式，且全由同一紧致 Anosov F 保持。

连这个比单一混合顶交数更强的逐点性质，也不能使 ω_t 具有全纯辛型。

还可以精确指出缺陷的 Jordan 性质。以下只取 t=τ∈R。按四个 Heisenberg 因子的 coframe 次序

\[
(\bar\alpha,\beta,\gamma;
\alpha,\bar\beta,\bar\gamma;
\bar\delta,\epsilon,\zeta;
\delta,\bar\epsilon,\bar\zeta)
\tag{4.2}
\]

取其对偶复向量基。令 R₀=−iJ₀，对角元为

\[
(-1,1,1; 1,-1,-1; -1,1,1; 1,-1,-1).
\]

定义 K 的非零作用为

\[
K B=2Z,\quad K Y=-2C,\quad
K\bar B=-2\bar Z,\quad K\bar Y=2\bar C.
\tag{4.3}
\]

它满足 K²=0、rank_C K=4、[K,R₀]=[K,A]=0，且复共轭把 K 变为 −K。直接比较二形式矩阵，递推算子 N_τ=a_τ⁻¹b_τ 为

\[
N_\tau=-i(R_0+\tau K),\qquad
N_\tau^2+I=-2\tau R_0K.
\tag{4.4}
\]

N_τ 是实算子。τ≠0 时，其缺陷非零、秩四、平方为零；特征多项式却仍为 (z²+1)⁶。缺陷只连接 A 的相同特征值空间：B 与 Z 都有 λ 权重，Y 与 C 都有 λ⁻¹ 权重。双曲性没有排除这个共振。

甚至 N_τ 的 Nijenhuis 张量也为零。理由是 K 的像位于中心，K 消去交换子代数，R₀ 保持该代数。代入

\[
\mathcal N_R(U,V)=[RU,RV]-R([RU,V]+[U,RV])+R^2[U,V]
\]

得 mathcal N_{R₀+τK}=mathcal N_{R₀}=0，后者来自 J₀ 可积。故“递推算子 Nijenhuis 为零”也不能代替 N²=−I。这里沿用的是标准递推算子语言，不宣称这个一般机制新颖。

## 5. 反例延伸到所有偶复维数至少六

与任意复维数 2k 的标准全纯辛环面 (T,Θ) 作乘积，并在每个 E² 因子上选整数 SL₂ 双曲矩阵，例如 [[2,1],[1,1]]，得到保 Θ 的全纯 Anosov B。

令 m=3+k、F'=F×B、ω'_t=ω_t+Θ、c'_t=[ω'_t]。由 (2.2) 及 Θ^{k+1}=0，

\[
(c'_t)^{m+1}=0,
\quad (\omega'_t)^m(\bar\omega'_t)^m\ne0,
\quad (\omega'_t)^{m+1}\ne0\quad(t\ne0).
\]

最后一个非零项是非零常数乘 ω_t⁴∧Θ^k。这些乘积仍是实际紧致模型，且同样可由 tildeΩ_{s,u}+Θ 实现坏周期类。

## 6. 对原研究路线的结论

**已否定：** 仅由周期固定、c^{m+1}=0、非零混合顶交数恢复唯一不变代表的全纯辛型。即使补上真实全纯辛周期可实现性，或者唯一代表的完整实辛铅笔及 Nijenhuis 零条件，仍不能进行这个推断。

**未否定：** 真实保全纯辛全纯 Anosov 系统可能对其周期施加额外约束，排除本文的坏类。原假设中“同一个 f 同时全纯、保 Ω 且 Anosov”的相容性，正是反例没有满足、也没有被纯周期论证使用的全局输入。

66 的闭性证明完全不受影响：其中模型序列本来就满足 ω_j^{m+1}=0，逐点恒等式通过有限维极限传递，而不是由杯积关系重新推断。

环面模型的代数情况不同：不变复形的微分为零，杯积关系就是常系数形式的楔积关系，因此这一步确实成立；后续实际共轭仍另需证明。本反例是复六维的非 Kähler 模型，不能作为 Kähler 四维分支的反检验。

不应继续用同一杯积推断撤去 66 的“可由模型逼近”前提。70 精确给出原周期附近多出来的两个分支，解释障碍并非一次偶然的退化。

计算核验：check_period_rank_lifting.py、period_rank_lifting_checks.json。原函数、积分非零、可积性及范围的证明均在本文；计算只检查新符号与恒等式。有限文献定位见 literature/period_rank_lifting_scope_and_search_log.md。
