# 紧致 IHS 四维中的真实高导数集中，以及三个互相奇异的规范测度

日期：2026-10-18。接续 51–55。这里构造真实、紧致、射影、保全纯辛的 IHS 四维自同构，证明 54 的高导数集中可以发生，并精确指出它缺少的 Anosov 条件。它不是 Ghys 猜想反例。

主要文献输入是 Cantat–Dupont 的曲面 Kummer 刚性与 Lyapunov 等号刻画；其高维推导、接近对角线时的导数核验及混合测度计算在下文完整写出。没有确认这些组合结论的独立新颖性。

## 1. 一个完整的紧致反检验定理

**定理 A。** 存在射影 IHS 四维 X、保持全纯辛形式的全纯自同构 f、λ=d₁(f)>1、光滑辛概率体积 m 及 Green 最大熵概率测度 θ，满足：

1. Green 根流具有 Hölder 局部势，θ⊥m。
2. 对任意固定光滑 Kähler 度量，存在 ε>0，使

\[
E_n(\varepsilon)=
\{x:\|Df_x^n\|>\lambda^{n/2}e^{\varepsilon n}\}
\]

满足

\[
\boxed{m(E_n(\varepsilon))\le Ce^{-2\varepsilon n},
\qquad\theta(E_n(\varepsilon))\longrightarrow1.}
\tag{1}
\]

3. 存在 ε₂>0，使真实复外平方导数定义的

\[
F_n(\varepsilon_2)=
\{x:\|\Lambda^2_{\mathbb C}Df_x^n\|
>\lambda^ne^{\varepsilon_2n}\}
\]

也满足 m(F_n)≤Ce^{-2ε₂n}、θ(F_n)→1。

4. 对任意固定 Kähler 背景的全局 Bedford–Taylor 容量，Cap_ω(E_n) 不趋零，事实上具有统一正下界（n 足够大）。

因此，不能只由“紧致 IHS 四维、保全纯辛、真实全纯切导数、Hölder Green 势、正确的动力学次数质量界”推出这些高导数集合具有小 Green 质量或小容量。这里明确没有包含全局 Anosov 或空 null locus 假设。

## 2. 曲面输入及版本

取射影 K3 曲面 S，ρ(S)=2，NS 不表示 0 或 −2，并取正熵保全纯辛自同构 g。这样的 (S,g) 存在：例如 [34] Amerik–Verbitsky 的无 MBM、Picard 数二的构造，应用于 K3 变形类型。该构造取得双曲作用，并给出保辛自同构；二元双曲格若表示 0，其整等距群不能有这里的双曲无限阶作用。

设

\[
\lambda=d_1(g)>1,\quad L=\log\lambda,
\quad \mu=T^+\wedge T^-,\quad
\int_S T^+\wedge T^-=1,
\quad m_S=\Omega_S\wedge\overline{\Omega_S},
\quad\int_Sm_S=1.
\]

Cantat–Dupont [49] 给出：

- µ 是 mixing 的唯一最大熵概率测度，h_µ(g)=L；
- µ⊥m_S；
- µ 的两个复 Lyapunov 指数为 χ、−χ，且

\[
\boxed{\chi>L/2.}
\tag{2}
\]

精确编号：本地 PDF 为 arXiv:1410.1202v1（2014-10-05），使用 **Corollaries 1.6、1.7，PDF p.6**。较后作者最终稿中对应编号为 1.7、1.8；不能混用。Corollary 1.6 将临界指数等号与绝对连续、Kummer 等价；保体积使两指数相反，再结合 Ruelle 不等式及非 Kummer 性得到 (2)。它是已知曲面定理，不是本轮新证。

## 3. Hilbert 平方与测度的准确识别

令

\[
X=S^{[2]},\qquad f=g^{[2]}.
\]

X 为射影 IHS 四维，f 保持其全纯辛形式。[17] Beauville 的 Propositions 5–6 及其后关于射影 S 的说明（PDF pp.12–14）给出所需全纯辛结构、单连通性与射影/Kähler 性；不将 Theorem 3 对一般非射影曲面的历史表述误用于本例。记 Δ⊂S² 为对角线，D⊂X 为 Hilbert–Chow 例外除子，

\[
q:S^2\setminus\Delta\longrightarrow X\setminus D,
\quad (x,y)\longmapsto\{x,y\}.
\]

这是二重 étale 覆盖，并 intertwine g×g 与 f。等价的全局图示为

\[
B=\operatorname{Bl}_{\Delta}(S^2)
\xrightarrow{\ p\ }X,
\qquad b:B\to S^2,
\]

p 为交换两点的提升对合的商；原始出处可核对 [21, §5.2]。

由于 µ 无原子，(µ×µ)(Δ)=0。有限对一因子不损失测度熵，故 q_*(µ×µ) 的熵为 2L。Oguiso 的动力学次数公式给 h_top(f)=2L、d₁(f)=λ。由最大熵测度唯一性，

\[
\boxed{\theta=q_*(\mu\otimes\mu).}
\tag{3}
\]

此处把 q 在 Δ 上任意作可测延拓即可：所有使用的概率测度均不给 Δ 质量，推前不依赖该延拓。

另一方面，

\[
q^*\Omega_X=\Omega_1+\Omega_2,
\quad \Omega_X^2\text{ 拉回为 }2\Omega_1\wedge\Omega_2.
\]

利用覆盖次数及概率归一化，

\[
\boxed{m=q_*(m_S\otimes m_S).}
\tag{4}
\]

例外除子对 m 的质量为零。取 µ(B₀)=1、m_S(B₀)=0 的 Borel 集 B₀，B₀² 是交换两点不变的零体积满 µ² 集，故 (3)–(4) 已证明 θ⊥m。

## 4. 不能省略的检验：靠近对角线时导数是否 tempered

仅凭 X\D 与无序 S²\Δ 双全纯，不能直接断言它们的 Lyapunov 指数相同：坐标导数靠近 Δ 可能发散。下面补齐该步骤。

由 T± 的统一 Hölder 局部势及缩放后的 Chern–Levine–Nirenberg 估计，存在 a>0，使

\[
\mu(B_r(x))\le Cr^a
\quad\text{对所有足够小 }r\text{ 及所有 }x\in S.
\tag{5}
\]

具体地，若两局部势有共同 Hölder 指数 γ，可在 B_{2r} 上减去中心常数，再除以 r^γ，使缩放后的势一致有界；二次混合 CLN 估计给 (5) 的 a=2γ，适当减小指数也可。

于是

\[
(\mu\otimes\mu)\{d(x,y)<r\}
=\int\mu(B_r(x))\,d\mu(x)\le Cr^a.
\]

µ² 对 g×g 不变，因此对每个 η>0，Borel–Cantelli 给

\[
d(g^nx,g^ny)\ge e^{-\eta n}
\quad\text{对 µ²-几乎处处的 }(x,y)
\text{ 及全部充分大的 }n.
\tag{6}
\]

不需要独立性，反迭代亦然。

局部写 z=(x+y)/2、v=(x−y)/2。在 |v₁|≥|v₂| 的 blow-up chart 中，无序点的 Hilbert 坐标可写为

\[
(z_1,z_2,\ s=v_1^2,\ t=v_2/v_1).
\]

另一张图交换两个分量。对固定光滑背景度量，有限张图给某个 N、C：

\[
\|Dq\|+\|(Dq)^{-1}\|
\le C\bigl(1+d(x,y)^{-N}\bigr).
\tag{7}
\]

式 (6)–(7) 证明沿 µ²-典型轨道，这些坐标变换及逆变换的导数范数的对数都是 o(n)。这里“逆”是覆盖的局部逆的切映射，不要求全局选择有序点。

对

\[
Df^n_{q(x,y)}=
Dq_{(g^nx,g^ny)}\,
D(g\times g)^n_{(x,y)}\,
(Dq_{(x,y)})^{-1}
\]

及其逆等式作奇异值比较，tempered 因子不改变 Lyapunov 指数。故 θ 下 f 的四个复指数是

\[
\boxed{\chi,\chi,-\chi,-\chi.}
\tag{8}
\]

这一步实际使用了 Hölder Green 势与真实 Hilbert 局部几何，不是形式地忽略一个零测解析集。

## 5. 真实高导数集中及容量不消失

54 的全局上同调质量界不依赖 Anosov，任意正熵 IHS 四维自同构都满足

\[
\int_X\|Df^n\|^2dm\le C\lambda^n,
\qquad
\int_X\|\Lambda^2_{\mathbb C}Df^n\|^2dm
\le C\lambda^{2n}.
\tag{9}
\]

其证明是 Kähler 楔积恒等式与 IHS 相关上同调谱估计，已在 54 写出。Markov 不等式给 (1) 的体积界。取 0<ε<χ−L/2，由 (8) 得 θ(E_n)→1。取 0<ε₂<2χ−L，同理得到外平方版本。至此证明定理 A 的前三项。

容量结论也可直接证明。令 S=S_X^++S_X^-，其全局连续势表示为 S=η+ddᶜu，η 为光滑闭实 (1,1) 形式，u 有界。两根流的三次幂都为零：它们正闭而同调类为零，故其 Kähler 质量为零。于是

\[
S^4=c_0\theta\quad(c_0>0).
\]

选 K 足够大，使 Kω−η≥0、osc(u)≤K。则

\[
v=(u-\sup u)/K\in\operatorname{PSH}(X,\omega),
\quad -1\le v\le0,
\quad \omega+dd^cv\ge K^{-1}S.
\]

Bedford–Taylor 正楔积的单调展开给

\[
\theta(A)\le K^4c_0^{-1}
\int_A(\omega+dd^cv)^4
\le K^4c_0^{-1}\operatorname{Cap}_{\omega}(A)
\tag{10}
\]

对所有 Borel 集 A 成立。θ(E_n)→1，故 Cap_ω(E_n)≥c>0，尽管其光滑体积指数趋零。

**被严格否定的猜测。** 对这种真实高导数集，即使 f 是紧致射影 IHS 四维上的保全纯辛自同构，也不一定存在与 n 无关的 C,a>0，使 θ(E_n)≤C m(E_n)^a；更一般的 θ(E_n)≤ω₀(m(E_n))、ω₀(s)→0 也不成立。它们在本例中直接与 (1) 矛盾。把高导数集的指数小体积直接升级为容量趋零，同样不成立。

这没有否定**再额外使用全局 Anosov 和空 null locus**后可能取得的估计。

## 6. 一条自然的混合测度桥梁，以及一个完整反例

在任意 IHS 四维正熵保辛自同构上，还可以定义

\[
\nu_\Omega=
\frac{S^+\wedge S^-\wedge\Omega\wedge\bar\Omega}
{\int_X S^+\wedge S^-\wedge\Omega\wedge\bar\Omega}.
\tag{11}
\]

它是正的有限不变概率测度。局部用光滑正 (1,1) 形式近似两根流；楔积的密度是适当全纯楔积的模平方之和，故非负。连续势保证极限存在；Fujiki 配对 q(α₊,α₋)q(Ω,Ω̄)>0 保证分母严格正。f*Ω=Ω 及两根流的互逆特征缩放给不变性。

看似可能用 ν_Ω 连接光滑辛体积与 θ。但在上述紧致 Hilbert 平方中，可以算出三者反而**两两互相奇异**。

先选择 X 上 Green 根流的尺度，使在 B 上

\[
p^*S_X^\pm=b^*(T_1^\pm+T_2^\pm).
\tag{12}
\]

其类的识别来自 blow-up 的 H² 分解和交换两点不变性；例外类的特征值为 1，不能出现在 λ^{±1} 特征类中。整个流的识别也可不用唯一性定理而直接证明：两边有相同类及连续势，差为 ddᶜa，且均被提升自同构按 λ^{±1} 缩放。于是 a∘F−λ^{±1}a 为全局常数；加上适当常数后得到齐次等式。a 有界而 λ^{±1}≠1，正、负迭代迫使 a=0。

在 S 上 (T±)²=0，故在有序无对角线的开集上，

\[
q^*\bigl((S_X^+)^2(S_X^-)^2\bigr)
=4\,\mu\otimes\mu.
\tag{13}
\]

另一方面，次数原因使所有混合跨因子的 Ω 项消失，留下

\[
q^*\bigl(S_X^+S_X^-\Omega_X\bar\Omega_X\bigr)
=\mu\otimes m_S+m_S\otimes\mu.
\tag{14}
\]

Green 流连续局部势的混合楔积不赋予例外解析除子质量：局部可用加入光滑正形式后的有界 psh Monge–Ampère 测度控制，而后者不充解析多极集。故没有遗漏边界质量。在本节选择的尺度下，(S_X⁺)²(S_X⁻)² 的总质量为 2，Ω_X²Ω̄_X² 的总质量也是 2，而 S_X⁺S_X⁻Ω_XΩ̄_X 的总质量为 1。利用二重覆盖的概率归一化，得到全局等式

\[
\boxed{
\begin{aligned}
m&=q_*(m_S\otimes m_S),\\
\nu_\Omega&=q_*\!\left(\frac{\mu\otimes m_S+m_S\otimes\mu}{2}\right),\\
\theta&=q_*(\mu\otimes\mu).
\end{aligned}}
\tag{15}
\]

对选定的 B₀，三者分别承载于“一对点中恰有 0、1、2 个属于 B₀”的集合；这些集合交换不变且两两不交。因此三者两两奇异。

进一步，设 e=h_{m_S}(g)。由 µ 唯一最大熵及 µ≠m_S，e<L。有限因子保持熵、乘积熵可加、熵对不变概率的混合仿射，给

\[
\boxed{
h_m(f)=2e
\;<\;
h_{\nu_\Omega}(f)=e+L
\;<\;
h_\theta(f)=2L.}
\tag{16}
\]

不要求 m_S 遍历。由此，规范性、不变性以及同时含 Green 流与 Ω 的构造都不迫使混合测度等于 θ 或 m；本例给出一个具有严格中间熵的规范测度。

这没有排除在**全局 Anosov**下 ν_Ω 获得其他性质的可能性，也没有证明其在该假想分支与 θ 或 m 相等。

## 7. 本例为何不是 Anosov：明确缺失的条件

D 是 f-不变的复三维例外除子。Green 双曲轴类来自 Hilbert–Chow 底空间，与例外 P¹ 纤维交数为零，因此该轴 big and nef，但不是 Kähler。

53 已证明任意 IHS 全纯 Anosov 的轴必须 Kähler，且没有奇数复维周期解析子簇。上述 f 两项都不满足，故不是 Anosov。

因此，本例能够否定的是**未使用全局 Anosov 结构或空 null locus 的容量/体积转移猜测**。它不能否定把这些条件与真实切导数微分相容性共同使用的新结构引理。也没有在此证明 θ 的支撑为整个 X，或构造 51 的全局一致叶片。

## 8. 本轮结论的价值和边界

相比 52 的非紧人造特征流模型，本例同时具有正确的 λ=d₁、真实紧致切导数、有限 Green 概率测度、IHS 上同调增长和全纯辛结构，故补上了一大部分模型缺口；定理 A 是完整的反检验。

但“整体均匀双曲叶状结构 + Kähler 双曲轴”仍没有进入反例。55 说明单纯概率大偏差在均匀 Anosov 下也正常成立；这里说明紧致全纯 IHS 几何本身也允许这种集中。要证明 Ghys 刚性，必须取得二者之间的**新耦合约束**，不能把分别成立的正性和指数界再作形式拼接。

独立的有限外代数核验确认了 (13) 的系数 4、(14) 的两个系数 1、辛体积的系数 4 和 S⁴=6(S⁺)²(S⁻)²。记录在 pressure_and_compact_measure_checks.json。它们核对符号和归一化，不证明无穷维流的存在、对角线 tempered 性、熵或容量结论；这些步骤已在正文分别证明。
