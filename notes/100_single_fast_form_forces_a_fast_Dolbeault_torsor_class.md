# 一维快谱分支强迫非零快 Dolbeault 类：第二张形式的准确障碍

日期：2026-10-19。性质：98–99 的全局约化所给的严格障碍定理及失败路线。本轮尚未排除 dim_C W_X=1，也没有得到原始 Ghys 分类。没有把等周期、拓扑平凡或 Hodge 数恒定当作全纯平凡。

## 1. 从原始一维分支推出的定理

沿用 98 的取逆约定 f*α=r⁻¹α、r=λ²。99 构造

\[
\pi:\widehat X\longrightarrow Q\quad\text{主全纯 }\mathbb C\text{ 丛},
\qquad q:Q\longrightarrow\mathbb C,
\]

以及紧致四维 Y=Y₀、保辛 Anosov g。令这个加法群 torsor 的类为

\[
\kappa\in H^1(Q,\mathcal O_Q),\qquad
\kappa_0=\kappa|_Y\in H^1(Y,\mathcal O_Y).
\tag{1.1}
\]

**定理。**

1. 若 κ₀=0，则原 X 至少有两张独立闭全纯一形式；结合 75、97 的已有分支排除，实际 dim_C W_X=4。
2. 因此，若 dim_C W_X=1，则约化 Y 必满足

\[
\boxed{\kappa_0\ne0,\quad g^*\kappa_0=\lambda^2\kappa_0,
\quad W_Y=0.}
\tag{1.2}
\]

3. 这个类不在自然映射 H¹(Y,C)→H¹(Y,O_Y) 的像中；该映射在本分支为单射但非满射，且

\[
\boxed{h^{0,1}(Y)\ge9.}
\tag{1.3}
\]

这里 H¹(Y,C) 的复维数为八、谱仅 λ、λ⁻¹；(1.2) 是一个真正新增的快 Dolbeault 共振，不是把原有一阶特征值重新命名。它是**从一维原始分支强迫得到的结构**，不是另加一个任意强正则性条件。

## 2. 全纯 torsor 类的准确正规化

主加法群 C 丛的局部全纯截面 s_i 之差为全纯函数 t_ij，形成 O_Q 的一阶 Čech cocycle；κ=0 当且仅当存在全局全纯截面。这是加法 torsor 的定义性分类。

deck γ_{r₀} 与 C 流交换，所以 γ_{r₀}^*κ=κ。另一方面，f̂ 在纤维参数上乘 r。若 s_j=s_i+t_ij，则 f̂s_j=f̂s_i+r t_ij，作为 G^*π 的局部截面给出

\[
G^*\kappa=r\kappa.
\tag{2.1}
\]

限制到 G 固定的 Y₀，得到

\[
g^*\kappa_0=r\kappa_0.
\tag{2.2}
\]

这是拉回特征值 r，不是 r⁻¹；取逆约定及 torsor 纤维伸缩已在上面的局部截面计算中固定。

## 3. 为什么 κ₀=0 已经使整个主 C 丛全纯平凡

99 已从稠密 deck 平移和 Grauert 上半连续性证明所有 h^{p,k}(Y_ζ) 恒定。因此

\[
E=R^1q_*\mathcal O_Q
\]

为全纯向量丛，准确 base-change 到每个 H¹(Y_ζ,O)。κ 的纤维限制组成 E 的全纯截面 k(ζ)。

若 k(0)=0，deck 等变性使 k(ℓ(r₀))=0 对全部 r₀∈R 成立。ℓ(R) 稠密，连续性给 k≡0。

q 的纤维紧致连通，q_*O_Q=O_C。C 为 Stein；Leray 谱序列的低阶项和 Cartan B 给

\[
H^1(Q,\mathcal O_Q)\simeq
H^0(\mathbb C,R^1q_*\mathcal O_Q),
\tag{3.1}
\]

因为 H¹(C,O)=H²(C,O)=0。因此 k≡0 使 κ=0，π 有全局全纯截面。

这里稠密平移解决了“只在单张纤维上消失”到“整个非紧族上消失”的接口；Hodge 数恒定先保证 base-change，不能把这些环节直接省略。

## 4. 全纯截面给出实际保辛乘积分解

取全局全纯截面 s:Q→X̂，令

\[
\eta=s^*\Omega.
\tag{4.1}
\]

η 为闭全纯二形式，限制每个 Y_ζ 为 σ_ζ。Q 复维数五，η 在四维垂直空间非退化，故其秩处处四，核为横截 q 纤维的全纯线。存在唯一全纯向量场 W，使

\[
\iota_W\eta=0,\qquad d\zeta(W)=1.
\tag{4.2}
\]

q proper，所以 W 沿每条有限长度底路径的提升留在一个紧致逆像内，不会有限时爆破；全纯 ODE 遂给完备的 C 流。Cartan 公式给 L_Wη=0。因此水平流提供

\[
Q\simeq\mathbb C_\zeta\times Y,
\qquad\eta=\operatorname{pr}_Y^*\sigma.
\tag{4.3}
\]

主 C 丛的全纯截面给全局纤维坐标 a，V=∂_a。Ω 对 C 不变且 ι_VΩ=dζ，使

\[
\boxed{\widehat X\simeq\mathbb C_a\times\mathbb C_\zeta\times Y,
\quad\Omega=da\wedge d\zeta+\sigma.}
\tag{4.4}
\]

这是真实的全纯保辛乘积；99 §5 只有光滑截面时不能作出同样推论。

## 5. 下降得到紧致复曲面底，确实产生第二张形式

在 (4.4) 中，deck γ_{r₀} 与 a 平移交换，ζ 改变常数 ℓ(r₀)，故形如

\[
(a,\zeta,y)\longmapsto
(a+A_{r_0}(\zeta,y),\zeta+\ell(r_0),\rho_{r_0,\zeta}(y)).
\tag{5.1}
\]

Y 紧致连通，A_r₀ 是全局全纯函数，故在 y 上常值，只依赖 ζ。再由 Ω 的保持，(5.1) 的 dζ∧dy 混合项须为零；σ 非退化使 ∂_ζρ_{r₀,ζ}=0。因此

\[
\gamma_{r_0}(a,\zeta,y)
=(a+A_{r_0}(\zeta),\zeta+\ell(r_0),\rho_{r_0}(y)).
\tag{5.2}
\]

所以 R 在 C²_{a,ζ} 上确有独立的全纯作用。它自由，因为 ℓ 无核；它 proper，因为若无限多个格元素把一个紧集 K⊂C² 送回 K，则它们也把 K×Y 送回 K×Y，违背 X̂→X 的 proper deck 作用。于是

\[
S=\mathbb C^2/R
\tag{5.3}
\]

是复曲面，X→S 为满射全纯 submersion。X 紧致使 S 紧致。S 的万有覆盖 C² 可缩、π₁S=Z⁴，故它是 T⁴ 的同伦型，整数上同调环为 H¹ 的外代数。

97 §2 的曲面证明只使用 b₁=4 及这个上同调环，故对同伦四环面同样成立：Buchdahl 使 S Kähler，Albanese 的度为一，H² 满射与 Kähler 正性排除例外曲线。S 因而为复二维环面。

其两张独立闭全纯一形式经 X→S 拉回，证明 dim W_X≥2。75 与 97 进一步使 dim W_X=4。这完成定理第 1 项；没有假定 f 在底上的表达已经线性，也没有把非离散周期群直接取商。

## 6. 一维分支必须有异常的 Dolbeault 谱

若 dim W_X=1，§3–5 的逆否命题给 κ₀≠0，(2.2) 给快特征值 r=λ²。

若 W_Y≠0，77 的同速环面判据使 Y 为复四维环面。此时 H¹(Y,O) 是 H¹(Y,C) 的 Hodge 商，g* 的特征值只能是 λ、λ⁻¹，没有 r。因此 (2.2) 迫使 κ₀=0，矛盾。故 W_Y=0。

局部全纯 Poincaré 引理给层正合列

\[
0\longrightarrow\mathbb C\longrightarrow\mathcal O_Y
\overset d\longrightarrow d\mathcal O_Y\longrightarrow0.
\tag{6.1}
\]

其长正合列说明 H¹(Y,C)→H¹(Y,O) 的核正是 W_Y。现在 W_Y=0，所以该映射单射，像为八复维、g* 只含 λ、λ⁻¹。κ₀ 的特征值 λ² 不在这些谱中，不能位于该像，故 h^{0,1}(Y)≥9，证明第 2–3 项。

这同时严格排除任何满足一阶 Hodge 满射 H¹(Y,C)→H¹(Y,O) 的约化。没有证明这个满射性由当前非 Kähler 原始假设自动成立。

等价地，在 Frölicher 谱序列的快特征部分，κ₀ 必须被下列某一步杀掉：

\[
d_1\kappa_0\ne0\ \text{于 }H^1(Y,\Omega_Y^1),
\quad\text{或}\quad
d_1\kappa_0=0,\ d_2[\kappa_0]\ne0\ \text{于 }E_2^{2,0}.
\tag{6.2}
\]

理由是 (0,1) 位置没有入射微分，可能的出射只有 d₁、d₂；若两者都为零，该快特征向量会存活到总次数一的 de Rham 上同调，与其只有 λ、λ⁻¹ 的谱矛盾。因此下一接口可更窄地表述为排除这个**特定快特征部分**的 d₁/d₂ 障碍，无须先证明一般 Kähler 性或整个谱序列退化。

## 7. 反检验：等周期、proper 约化和拓扑平凡仍不强迫全纯截面

为避免把 κ=0 当作免费结论，构造一个明确比较模型。取

\[
Y_*=(\mathbb C/(\mathbb Z+i\mathbb Z))^4,
\quad\sigma_*=dy_1\wedge dy_2+dy_3\wedge dy_4.
\]

取格同态 c:Λ→C，令 c(e₁)=0、c(ie₁)=1，其余标准格生成元像为零。它不是复线性泛函在格上的限制。定义

\[
P_*=(\mathbb C_a\times\mathbb C_\zeta\times\mathbb C_y^4)/\Lambda,
\quad\gamma(a,\zeta,y)=(a+c(\gamma),\zeta,y+\gamma).
\tag{7.1}
\]

Ω_*=da∧dζ+σ_* 下降为闭全纯辛形式；a 平移给自由 proper 主 C 丛

\[
P_*\longrightarrow\mathbb C_\zeta\times Y_*.
\]

其约化族为同一个紧致复环面，周期和全部 Hodge 数恒定，且主 C 丛光滑平凡；它却没有全局全纯截面。否则截面在覆盖上由全纯函数 a=s(y) 给出，ds 为格周期一形式，系数在紧致环面上为常数，故 s(y)=L(y)+b，迫使 c=L|Λ，与 c 的选取矛盾。

这不是当前分支的反例：P_* 非紧，也没有给定原始 X 的快格紧致化和归一化 Anosov。更具体地，对同速 toral g，H¹(Y_*,O) 只有 λ、λ⁻¹，非零 torsor 类不可能满足 g*κ=rκ。它只证明“等周期＋拓扑平凡＋proper 全纯约化”本身不足；真正待排除的是 (1.2) 的快 Dolbeault 类。

05 的完整紧致代数模型则有 κ₀=0，能够恢复第二快形式，并最终有 W_X=4，与本篇结论一致。

## 8. 本轮成败及下一步判断

**已证明：** 非退化快 flux、准确快位移、覆盖上的 proper C 约化、紧致四维保辛 Anosov 族、恒定辛周期和 Hodge 数，以及一维分支强迫非零 λ²-Dolbeault torsor 类、W_Y=0、h^{0,1}≥9。

**尚未证明：** κ₀ 消失、第二张闭全纯形式存在或一维分支不可能。普通 H¹ 的谱计算不能替代 Dolbeault H¹(O) 的谱计算；没有 Kähler/一阶 Hodge 满射时，这正是缺口。

**失败或被绕过的尝试：** 快流紧致闭包不自动存在；完整中央椭圆项在同侧阿贝尔流里缺失；临界平方根项未被消去，但 proper 约化不需要消去它；等周期也没有自动给全纯截面。

与最初判断相比，一维分支确有零维分支没有的切入结构，本轮因此能推出真实约化。可是它并没有立即落入 76 已解决的固定纤维单值系统，而是留下一个非 Kähler、同速环面型 Anosov 上的快 Dolbeault 共振。继续一轮最值得核验的是：能否用真实 g 及主 C 丛的特殊几何排除这个特定 κ₀，而不是再次假设一般局部 Torelli 或重算 Chern 数。若没有新的 Dolbeault/动力学连接，不能仅沿“周期恒定”反复推进。

文献、五整页核验、勘误影响及有限新颖性检索见 literature/Single_fast_form_scope_and_novelty_log.md 与 Single_fast_form_source_audit.json。使用旧长证明链，没有重跑旧套件；本轮结构定理与具体应用的新颖性未确认。
