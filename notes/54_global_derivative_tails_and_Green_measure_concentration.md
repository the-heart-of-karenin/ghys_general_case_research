# 全局导数质量界、指数小体积异常集与 Green 测度的集中

日期：2026-10-18。接续 51–53。范围：假想的 Kähler、保全纯辛、IHS 复四维 Anosov。下面先给出完整的全局估计，再说明它为什么还不能给出逐叶绝对连续性。

记 λ=d₁(f)>1、L=log λ、h_top(f)=2L；m 为归一化光滑辛体积，θ 为归一化 Green/最大熵测度。沿用 51 的 νᵘ=(S⁺|Wu)²=Margulis 叶测度。

## 1. 导数的全局平方可积界

固定任意光滑 Kähler 形式 ω，所有算子范数均用其 Hermitian 度量。存在 C>0，使所有 n≥0 满足

\[
\boxed{
\int_X\|Df^{\pm n}\|^2\,dm\le C\lambda^n,
\qquad
\int_X\|\Lambda^2_{\mathbb C}Df^{\pm n}\|^2\,dm
\le C\lambda^{2n}.
}
\tag{1}
\]

这里可以取算子范数；证明先控制更大的 Hilbert–Schmidt 范数。

**证明。** ω⁴ 与 m 一致可比。设 Dfⁿ 的四个复奇异值为 s₁,…,s₄，则

\[
\operatorname{tr}_{\omega}(f^n)^*\omega=\sum_i s_i^2,
\]

而外平方的 Hilbert–Schmidt 范数平方是 Σ_{i<j}sᵢ²sⱼ²。线性代数的楔积公式因此给

\[
\int_X\|\Lambda^p Df^n\|_{HS}^2\,\omega^4
=\binom4p\int_X(f^n)^*\omega^p\wedge\omega^{4-p},
\quad p=1,2.
\tag{2}
\]

右侧只依赖上同调。IHS 的 H¹,¹ 作用由 λ、λ⁻¹ 及负定部分上的有界等距组成，故 p=1 的右侧为 O(λⁿ)。H²,² 的最大谱模 λ² 是唯一且简单的最大特征值，其余谱模严格更小，故其迭代算子为 O(λ²ⁿ)，给 p=2。对 f⁻¹ 同理，证明 (1)。

p=2 的简单性输入已经在 20 Proposition 7 的证明以及 51 中核验，未将一般带 Jordan 块的情形无条件写成 O(d_pⁿ)。

## 2. 指数小体积的高导数集合

对任意 ε>0，令

\[
E_n^{(1)}(\varepsilon)=
\{x:\max(\|Df^n_x\|,\|Df^{-n}_x\|)
>\lambda^{n/2}e^{\varepsilon n}\}.
\]

Markov 不等式与 (1) 给

\[
\boxed{m(E_n^{(1)}(\varepsilon))\le C e^{-2\varepsilon n}.}
\tag{3}
\]

由 Borel–Cantelli（不需要独立性），m-几乎处处的所有 Lyapunov 指数都在区间

\[
[-L/2,L/2]
\tag{4}
\]

内。对每个正有理 ε 取交即可。这一上界先由可积估计推出，没有先假定 m 遍历。

对第 53 节的统一 Anosov 速率 κ，还必有

\[
\boxed{2\kappa\le L.}
\tag{5}
\]

否则 53(1) 在 m 上积分的指数下界会超过 (1) 的上界。这里的 κ 是适用于整个 X 的统一速率，不是任意一个周期点的最大扩张指数。

## 3. 体积与最大熵测度的指数位于临界值的两侧

de Thélin [47, Corollaire 3] 对唯一最大动力学次数 d₂=λ² 给 θ 的复 Lyapunov 指数下界：

\[
\chi_1(\theta)\ge\chi_2(\theta)\ge L/2>0,
\qquad
\chi_3(\theta),\chi_4(\theta)\le-L/2.
\tag{6}
\]

此处不需要 θ 对体积绝对连续。原文的临界/不定点距离可积条件在全纯自同构情形无障碍，因为该集合为空。θ 遍历来自 Green 测度的 mixing。

在 Anosov 分支，52 已证明 m 是唯一 SRB，而 θ≠m。记 m 的两个正复指数为 χ₁(m)≥χ₂(m)>0。由 (4) 及严格熵缺口，

\[
0<\chi_2(m)\le\chi_1(m)\le L/2,
\qquad \chi_2(m)<L/2.
\tag{7}
\]

θ 不为 SRB，Ledrappier–Young 的熵等号刻画给

\[
2(\chi_1(\theta)+\chi_2(\theta))>2L,
\quad\text{从而 }\chi_1(\theta)>L/2.
\tag{8}
\]

因此存在某个 ε>0，使

\[
\theta(E_n^{(1)}(\varepsilon))\longrightarrow1,
\qquad m(E_n^{(1)}(\varepsilon))\le Ce^{-2\varepsilon n}.
\tag{9}
\]

证明：选择 0<ε<χ₁(θ)−L/2，用 θ 的 Oseledec 极限。故同一族连续导数所定义的异常集合，光滑体积指数趋零，却渐近承载全部 Green 测度。

没有从“θ 满支撑”将 (4) 推广到 θ 或所有周期点。满支撑不提供在一列变化集合上的定量比较。

## 4. 行列式版本：每片不稳定叶上的指数集中

令

\[
J_n^u(x)=|\det_{\mathbb R}(Df^n_x:E^u_x\to E^u_{f^nx})|,
\quad
\Phi(x)=\log J_1^u(x).
\]

Eᵘ 只需要连续；该 Jacobian 已定义且 Φ 为 Hölder。复二维叶的实行列式满足

\[
J_n^u(x)\le\|\Lambda^2_{\mathbb C}Df^n_x\|^2.
\]

所以对于

\[
E_n^{(2)}(\varepsilon)=
\{x:J_n^u(x)>\lambda^{2n}e^{\varepsilon n}\},
\]

有

\[
\boxed{m(E_n^{(2)}(\varepsilon))\le Ce^{-\varepsilon n}.}
\tag{10}
\]

还可以将这一界升级为统一小不稳定叶片上的叶体积界。

**叶体积引理。** 对统一大小的小不稳定叶片 P，有与叶片无关的 C_P≤C，使

\[
\operatorname{vol}_{P}(P\cap E_n^{(2)}(\varepsilon))
\le Ce^{-\varepsilon n}.
\tag{11}
\]

**证明。** 由 51，Cᵘ=(S⁻)² 是不稳定叶的积分流，f_*Cᵘ=λ²Cᵘ。因此

\[
\int_X C^u\wedge(f^n)^*\omega^2
=\lambda^{2n}\int_XC^u\wedge\omega^2.
\tag{12}
\]

在小乘积盒中，左侧限制为对参数 Margulis 测度 mˢ 的

\[
\int_y\left(\int_{P_y}J_n^u\,d\operatorname{vol}_{P_y}\right)dm^s(y)
\]

的固定正常数倍。对由稳定 holonomy H 对应的两片叶，

\[
\log\frac{J_n^u(Hx)}{J_n^u(x)}
=\sum_{j=0}^{n-1}\bigl(\Phi(f^jHx)-\Phi(f^jx)\bigr)
\]

一致有界，因为 Φ Hölder、同稳定叶的正迭代距离指数下降。C² Anosov 的稳定 holonomy 在这些光滑不稳定横截面间绝对连续，Jacobian 及其倒数一致有界；这也是同一收敛乘积公式的标准绝对连续性结论，不要求 holonomy C¹。原始作者稿 [48, Proposition 4.1, PDF p.7] 给出所需的双边 Jacobian 界；其定义中两横截面取不稳定叶时 γ_U=γ_V=0。

因此各匹配叶片上的 ∫J_nᵘ dvol 一致可比，常数与 n 无关。mˢ 在固定参数小盒上有正且有限的质量，(12) 遂给每片匹配叶片的 ∫J_nᵘ dvol≤Cλ²ⁿ。有限盒覆盖、稍缩小叶片得到统一常数。最后用叶内 Markov 不等式即得 (11)。

注意这一步只比较**行列式**，而不是两片叶上的导数矩阵或最大奇异值。不能未经额外证明把 (11) 的论证用于 E_n^(1)。

取

\[
0<\varepsilon<\int_X\Phi\,d\theta-2L,
\]

右端由 52 的严格不等式为正。θ-generic 集 Bθ 稳定饱和，51 的局部乘积和精确 holonomy 不变性又使每片不稳定叶的 νᵘ-几乎每一点都属于 Bθ。因此对每片 P，

\[
\boxed{\quad
\nu^u\bigl(P\setminus\liminf_{n\to\infty}E_n^{(2)}(\varepsilon)\bigr)=0,
\qquad
\operatorname{vol}_{P}\bigl(P\cap\limsup_{n\to\infty}E_n^{(2)}(\varepsilon)\bigr)=0.
\quad}
\tag{13}
\]

第二式由 (11) 和 Borel–Cantelli 得到。这是 52 逐叶完全奇异性的一个具体、带指数叶体积估计的动力学实现。

## 5. 为什么这些估计仍未闭合刚性

我们确实得到了全局和逐叶的定量控制，但被控制的是**光滑体积**。要排除假想系统，需说明这种指数小叶体积集合不能渐近承载全部 Green 叶测度。51 的满支撑、弱连续性、幂次小球界均不提供这种集合比较。

Hölder 势或 Green 测度的 pluripotential 正则性也不能被直接理解为对体积的幂次绝对连续估计。零体积集合仍可能具有正的 Bedford–Taylor 容量；52 的稠密直线模型正给出满支撑、Lipschitz 势而完全奇异的 Monge–Ampère 测度。

若尝试把高导数集合写成统一受控的 quasi-psh 超水平集，还需控制 log∥Dfⁿ∥ 的曲率误差。它是 Hom(TX,(fⁿ)*TX) 的全纯截面的对数范数，靶丛曲率含 (fⁿ)*Rm 项；不能预设其相对于固定 ω 的负曲率界与 n 无关。53 只使 Ricci-flat 度量处处光滑，没有消除这个实际拉回曲率项。

这指出一个具体的下一步：寻找**真正利用切导数及 IHS 几何**的容量/Green 质量估计，控制 (9) 或 (13) 的特殊高导数集合。不能对任意小体积集合要求这种比较，因为 52 已说明它为假。

## 6. 对旧模型与已有结果的检验

- 05 的复四维环面 A=B⊕B：若其不稳定模为 a>1，则 d₁=a²、h_top=4 log a，m=θ；所有正复指数等于 L/2，(1)–(7) 的非严格界精确，(8) 不适用，因为它使用 IHS 分支 θ≠m。
- 52 的非紧奇异模型：不稳定模 a，但其人为特征流缩放为 a，而非 a²。若冒充紧 IHS 的 d₁，便违反统一速率约束 (5)。所以该模型检验局部测度推理，不能检验本轮新增的紧 Kähler 上同调增长界；它也不是原命题反例。
- 48 的实际边界例子：53 的 Kähler 轴条件已通过。本轮没有计算其导数积分或周期乘子，不能把 (9)/(13) 的必要集中结构说成已在该例中证明存在，或已证明不可能。
- (1) 的质量计算是标准 Kähler 恒等式和有限维谱估计，(3)/(10) 是 Markov 界；不得称其为新的 Lyapunov 理论。逐叶组合及其适用性已单独论证，新颖性未确认。

## 7. 本轮停止点

53 去掉了 null locus；本记录把绝对连续性缺口具体化成“特殊高导数集合的 Green 质量控制”。没有推出该控制。没有证明横向 C¹、体积最大熵或 IHS Anosov 不存在。

原始输入：20 的 IHS 谱和 Green 测度；47 PDF p.2 Corollaire 3 的 θ 指数下界；46 PDF p.6 Theorem A 的等号刻画；45 的标准 Anosov/SRB 理论，以及 48 PDF pp.6–7 的 holonomy Jacobian 双边界。原始文献与本文件独立证明分开存储。


## 2026-10-18 后续：55–57 的临界分离与紧致反检验

55 将行列式版本加强到临界阈值 λ²ⁿ，取得全局及每片不稳定叶上的双向指数分离，同时指出它是一般 Gibbs 机制。56 在真实紧致保辛 IHS 四维的非 Kummer K3 Hilbert 平方上实现高导数小体积、大 Green 质量和非小容量，并算出三个互相奇异、熵严格居中的规范测度；该例有不变例外除子，明确不是 Anosov。57 记录为什么应暂停纯标量尾界优化，以及哪些全局输入尚未耦合。没有得到绝对连续性、横向 C¹ 或 IHS Anosov 排除；原始边界例子仍未判定。严格证明、模型缺失条件及文献范围分别见 55、56、57 和 literature/pressure_compact_scope_and_novelty_log.md。
