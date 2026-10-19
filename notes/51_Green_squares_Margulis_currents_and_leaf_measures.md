# 回到 30：Green 平方、Margulis 流与每片叶上的非零测度

日期：2026-10-18。研究范围：Kähler、保全纯辛、复四维的剩余射影 IHS 分支。本文给出原始 Anosov 假设下的一个完整接口，不假设 pinching、横向 C¹、Green 流光滑或体积为最大熵测度。

这是 Ruelle–Sullivan 和 Dinh–Sibony 等已知定理的组合及逐叶连续性论证；未确认该组合表述的新颖性，不能据此宣称新的分类定理。

## 1. 设置与准确结论

设 X 是射影 IHS 四维，f 为保持全纯辛形式的全纯 Anosov，λ=d₁(f)>1，h=h_top(f)=2 log λ。稳定、不稳定复秩都为 2。取有 Hölder 局部势的正闭 Green (1,1) 流 S⁺、S⁻：

\[
f^*S^+=\lambda S^+,
\qquad f^*S^-=\lambda^{-1}S^-.
\]

调整正常数，使

\[
\int_X(S^+)^2\wedge(S^-)^2=1.
\tag{1}
\]

本文使用 θ=(S⁺)²∧(S⁻)² 表示最大熵概率测度，m 表示光滑辛体积；两者不预设相等。此归一化与 20 中相差一个二项式系数，无数学差异。

**命题。** 可以选择规范相容的 Margulis 叶测度 mᵘ、mˢ，使：

1. (S⁺)² 是由稳定叶组成的 Ruelle–Sullivan 流，(S⁻)² 是由不稳定叶组成的 Ruelle–Sullivan 流。它们在 Anosov 盒内是由互不相交、统一大小的全纯叶片组成的 uniformly laminar 流，而不只是 woven 流。
2. 对**每一片**不稳定叶和稳定叶，Bedford–Taylor 限制满足

\[
\boxed{\ (S^+|_{W^u})^2=m^u,
\qquad (S^-|_{W^s})^2=m^s.\ }
\tag{2}
\]

3. (2) 在每片叶上都有满支撑；稳定 holonomy 精确保不稳定侧的测度，不稳定 holonomy 精确保稳定侧的测度。
4. 在统一小叶球上，有与中心无关的正常数 c,C 和指数 0<a≤b，使

\[
c r^b\le m^u(B^u_r(x))\le C r^a
\qquad(0<r<r_0),
\tag{3}
\]

稳定侧同理。这里的“非退化”只指测度的满支撑及质量界，**不指** S⁺ 的叶向系数为正定矩阵，也不指绝对连续性。

## 2. 为什么可用全局 Margulis 流

f 保持满支撑的有限光滑体积，故不存在 wandering 开集：否则其正迭代两两不交且体积相同。于是非游荡集为 X。

Anosov 闭轨道引理及谱分解把 X 分成有限个两两不交的闭 basic sets。X 连通，故只有一个；因此 f 拓扑传递。无需把稠密轨道当作额外假设。

全纯性使两侧叶片为复子流形，且复定向由 f 保持。Ruelle–Sullivan [42, Theorems 1–2] 因而给出正闭 (2,2) 流 Cˢ、Cᵘ，其局部表示为

\[
C^s=\int[P^s_z]\,dm^u(z),
\qquad
C^u=\int[P^u_y]\,dm^s(y).
\tag{4}
\]

该文的横向要求是叶片光滑、切平面连续；没有要求整个叶状结构 C¹ 或全纯。流的闭性可直接由光滑环境分割统一和叶内 Stokes 得到。

记 Λ=eʰ=λ²。注意推前与拉回的方向：

\[
f_*C^s=\Lambda^{-1}C^s,
\qquad f_*C^u=\Lambda C^u,
\]

因而

\[
f^*C^s=\Lambda C^s,
\qquad f^*C^u=\Lambda^{-1}C^u.
\tag{5}
\]

两流的几何交是 Bowen 最大熵测度。其叶测度满足

\[
m^u(fB)=\Lambda m^u(B),
\qquad m^s(fB)=\Lambda^{-1}m^s(B),
\tag{6}
\]

并具有局部横向 holonomy 不变性和局部乘积结构。

Bowen 测度在 X 上有满支撑，例如由 Markov 编码中正的 Perron 特征向量和柱集测度即得。因此 (4) 的两个叶测度也在各自叶片上有满支撑：否则乘积盒中存在一个非空开子盒，Bowen 测度为零。

## 3. 用唯一性识别整个 (2,2) 流

两个流的上同调类均非零，因为对 Kähler 形式 ω 有

\[
\langle C^{s/u},\omega^2\rangle>0.
\]

IHS 四维的相关已知事实为：d₂(f)=λ²>d₁(f)，λ² 在 H²,² 上的扩张特征空间为一维；对 f⁻¹ 亦然。这正是 [20, Proposition 7 证明，PDF pp.10–11] 核验的情形。

于是由 (5)，[Cˢ] 为 [(S⁺)²] 的正倍数，[Cᵘ] 为 [(S⁻)²] 的正倍数。

Dinh–Sibony [44, Theorem 4.3.1, PDF p.38] 的条件是 d_q>d_{q−1}，且所取不变子空间上的谱模严格大于 d_{q−1}；结论是该子空间中每个类至多有一个正闭 (q,q) 流。这里对 q=2、V=R[(S⁺)²] 应用于 f，对负侧应用于 f⁻¹。故

\[
C^s=A(S^+)^2,
\qquad C^u=B(S^-)^2,
\quad A,B>0.
\tag{7}
\]

Ruelle–Sullivan 的几何交有总质量 1，而上同调交数和 (1) 给出 AB=1。将 mᵘ 乘以 A⁻¹、mˢ 乘以 A，保持它们的乘积不变，可使

\[
\boxed{C^s=(S^+)^2,\qquad C^u=(S^-)^2.}
\tag{8}
\]

这一步用的是**整个流在其类中的唯一性**，没有从逐叶消失直接猜测环境流的切核。

## 4. Bedford–Taylor 楔积与叶片积分相容

在一个足够小的乘积盒中，S⁺=ddᶜψ，ψ 为 Hölder 连续 psh 势，且由 (8)

\[
(S^-)^2=\int[P^u_y]\,dm^s(y).
\]

先乘连续函数 ψ，再取 ddᶜ，可以在此积分下进行；对紧支测试形式由 Fubini 及统一叶片质量界证明。连续局部势的 Bedford–Taylor 定义于是逐次给出

\[
(S^+)^2\wedge(S^-)^2
=\int_{y}(dd^c(\psi|_{P^u_y}))^2\,dm^s(y).
\tag{9}
\]

第二次乘 ψ 同样合法，因为第一次楔积为正流，局部质量一致有界。故没有将两个任意弱收敛流直接相乘。

另一方面 Ruelle–Sullivan Theorem 1(d) 的局部乘积表示是

\[
\theta|_{\rm box}=\int_y m^u|_{P^u_y}\,dm^s(y).
\tag{10}
\]

这里 θ 确为同一测度：Green 楔积是唯一最大熵测度 [20, Proposition 7; 43, Theorem 1.2]，Bowen 测度也具有该性质。

由 (9)–(10) 的测度分解唯一性，先得到

\[
(S^+|_{P^u_y})^2=m^u|_{P^u_y}
\quad\text{对 }m^s\text{-几乎处处的 }y.
\tag{11}
\]

接下来需要认真处理“每片叶”，不能停在条件测度的几乎处处版本。

## 5. 逐叶弱连续性：将 (11) 延拓至每片叶

将一簇不稳定叶片写成共同复平面上的全纯图

\[
F_y:D\subset\mathbb C^2\longrightarrow X.
\]

它们连续依赖于 y，缩小 D 后，Cauchy 估计保证所有固定阶叶内导数连续。令 u_y=ψ∘F_y、ν_y=(ddᶜu_y)²。若

\[
\delta=\sup_D d(F_y,F_z),
\]

则 ∥u_y−u_z∥∞≤Cδ^γ，其中 γ 是 ψ 的一个 Hölder 指数。对固定 K⊂⊂D、φ∈C²_c(K)，Bedford–Taylor 分部积分和一致局部质量界给出

\[
\begin{aligned}
|\langle\nu_y-\nu_z,\varphi\rangle|
&=\left|\int_D(u_y-u_z)
\,dd^c\varphi\wedge(dd^cu_y+dd^cu_z)\right|\\
&\le C_K\,\delta^\gamma\,\|\varphi\|_{C^2}.
\end{aligned}
\tag{12}
\]

所以 ν_y 弱连续。这里只比较两个**全纯图的参数化**，没有沿非全纯 holonomy 拉回 (1,1) 流。

Margulis 叶测度也弱连续：在一个较小公共乘积盒内，它们是某片固定叶测度在连续变化的稳定 holonomy 下的推前。测试连续函数、再用紧支性即可。

mˢ 在参数空间满支撑，故 (11) 成立的参数集合稠密。两边弱连续，(11) 延拓至每个参数。稳定侧对 f⁻¹ 同证，完成 (2)。

## 6. 从固定半径质量到幂次上下界

先固定足够小的 r₀。由逐叶弱连续性、每片叶满支撑及 X 紧致性，存在 c₀,C₀>0，使

\[
c_0\le m^u(B^u_{r_0}(x))\le C_0
\quad\text{对所有 }x.
\tag{13}
\]

下界可以使用支撑在稍小叶球中的连续截断函数证明，避免假定球面不带测度；上界由统一局部势界与叶片几何界得到。

选择 K≥κ>0、L≥1，使对所有 n≥0，

\[
\|Df^n|_{E^u}\|\le Le^{Kn},
\qquad
\|Df^{-n}|_{E^u}\|\le Le^{-\kappa n}.
\]

叶内长度估计给出

\[
B^u_{L^{-1}e^{-Kn}r_0}(x)
\subset f^{-n}B^u_{r_0}(f^nx)
\subset B^u_{Le^{-\kappa n}r_0}(x).
\tag{14}
\]

结合 (6)、(13)，得到

\[
c r^{h/\kappa}\le m^u(B^u_r(x))
\le C r^{h/K}.
\tag{15}
\]

取 a=h/K、b=h/κ 即为 (3)。可适当减小 κ、增大 K 吸收统一常数。此估计不含任何两侧谱宽夹逼。

## 7. 已经闭合与尚未闭合

**已证明：** Green 平方的 uniformly laminar 表示；每片互补叶上二次测度的满支撑、精确 holonomy 不变性；弱连续性估计 (12) 和统一幂次质量界 (15)。这些来自紧致 Anosov 全局结构及 IHS 的 Green 类唯一性，不能由 30 的局部消失引理单独得到。

**未证明：** S⁺|Wu 是 Hermitian 度量；νᵘ 对叶体积绝对连续；holonomy 全纯或 C¹；θ=m。满支撑允许测度完全奇异。52 将证明，在假想 IHS Anosov 中，叶测度反而必须每片叶都完全奇异，并给出局部模型说明这不构成形式矛盾。

**模型检验：** 05 的复四维线性环面满足该机制，叶测度为常系数叶体积，但它不是 IHS；05 的复六维非阿贝尔紧致模型不满足本命题的 Kähler/IHS 输入；30 从 11 局部模型取出的秩一特征流在复二维互补叶上平方为零，无法满足 (2)，正好显示新增全局输入排除了那种退化选择。没有用此排除否定局部粗糙模型本身。

## 8. 原始来源

- 42_Ruelle_Sullivan_1975_Currents.pdf：PDF p.1 的连续切平面要求，p.2 的闭流构造，p.6 Theorem 1 的叶测度和乘积，p.7 Theorem 2 的闭性、几何交和特征关系。
- 44_Dinh_Sibony_2010_Superpotentials_Kahler.pdf：PDF p.38 Theorem 4.3.1，同调类中正闭流的唯一性。
- 43_De_Thelin_Dinh_2012_Dynamics_Kahler.pdf：PDF pp.2–3，主 Green 流与唯一最大熵测度。本文不将一般 woven 结论误写为 uniformly laminar；后者由 Anosov 与 (8) 得到。
- 20_Jang_2024_Kummer_rigidity.pdf：PDF pp.10–11，IHS Green 平方、简单特征值及最大熵测度的准确输入。

原始 PDF 与下载、核验记录保存在 literature/；本文件为独立论证。


## 2026-10-18 后续：53–54 的推进与边界

53 已从原始 Anosov 切导数推出双向拉回 Kähler 形式的逐点指数下界，并证明 IHS 的整个 Green 正轴是 Kähler 类；null locus 为空，奇数复维周期解析子簇不存在。54 给出全局及逐不稳定叶的高导数/行列式异常集尾界，但这些指数小体积集合仍可能承载 Green 质量。**没有由 Kähler 类推出 Green 根流光滑，也没有证明绝对连续性、横向 C¹ 或完整刚性；48 的实际例子尚未排除。** 完整证明和未闭合处分别见 53、54；原始输入的核验及有限新颖性范围在 literature/metric_growth_source_audit.json 和 literature/metric_growth_scope_and_novelty_log.md。


## 2026-10-18 后续：55–57 的临界分离与紧致反检验

55 将行列式版本加强到临界阈值 λ²ⁿ，取得全局及每片不稳定叶上的双向指数分离，同时指出它是一般 Gibbs 机制。56 在真实紧致保辛 IHS 四维的非 Kummer K3 Hilbert 平方上实现高导数小体积、大 Green 质量和非小容量，并算出三个互相奇异、熵严格居中的规范测度；该例有不变例外除子，明确不是 Anosov。57 记录为什么应暂停纯标量尾界优化，以及哪些全局输入尚未耦合。没有得到绝对连续性、横向 C¹ 或 IHS Anosov 排除；原始边界例子仍未判定。严格证明、模型缺失条件及文献范围分别见 55、56、57 和 literature/pressure_compact_scope_and_novelty_log.md。
