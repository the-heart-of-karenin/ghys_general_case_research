# 不预设 C1 的充分估计：平均二阶差分可求和 ⇒ 分布 C1

日期：2026-10-17。性质：完整的局部正则性判据，及其在指定模型中的检验。**没有证明保全纯辛 Anosov 自动满足本判据。** 不把它称为分类证明或已确定的最弱额外条件。

## 1. 输入只涉及连续 holonomy 的有限差分

在复叶状图盒中取

\[
w=F(z,t),\quad F(0,t)=t,\qquad
z\in D_{R_0}\subset\mathbb C^r,\quad
t\in U\subset\mathbb R^{2r}.
\tag{1}
\]

只假设 F 整体连续、对 z 全纯，并确实给出叶状坐标同胚。不假设任何横向导数。H_z(t)=F(z,t) 是从中心横截面到 z=常数横截面的 holonomy。

固定 R<R_0。令 \mathbb T_R={|z_i|=R，i=1,…,r} 为多圆盘的 distinguished boundary，σ_R 为其归一化乘积角测度。取 h_j=2^{-j}h_0，取横向实坐标的标准基 e_1,…,e_{2r}。

**附加估计 (DZ)：** 存在非负数列 ε_j，满足

\[
\sum_{j=0}^{\infty}\varepsilon_j<\infty,
\tag{2}
\]

并对每个 ℓ、每个允许的内部参数 t，有

\[
\int_{\mathbb T_R}
\left|F(z,t+h_je_\ell)+F(z,t-h_je_\ell)-2F(z,t)\right|d\sigma_R(z)
\le h_j\varepsilon_j.
\tag{DZ}
\]

参数域可先缩小，h_0 选得足够小，使所用差分点都在 U 内。

**定理。** (DZ) 使 F 在任意较小叶域、内部参数域上为 C1；所有固定阶叶内导数也关于 t 为 C1。进一步缩小叶域后，(z,t)↦(z,F(z,t)) 是 C1 微分同胚，所定义的复切分布为 C1。

引理本身不使用辛形式；因此可以直接用于本研究的全纯辛分支。辛性、紧致性和全局双曲性仍需用于证明输入 (DZ)，这一点未完成。

## 2. Cauchy 公式把平均估计转成内部一致估计

取 ρ<R。对任意全纯向量函数 G，Cauchy 公式给出

\[
\sup_{D_\rho}|\partial_z^\alpha G|
\le C_{\alpha,\rho,R}
\int_{\mathbb T_R}|G|d\sigma_R.
\tag{3}
\]

令 G 为 (DZ) 中的二阶差分，则

\[
\sup_{D_\rho}
|\Delta^2_{h_je_\ell}\partial_z^\alpha F(z,t)|
\le C_{\alpha,\rho,R}h_j\varepsilon_j.
\tag{4}
\]

因此不需要预先在每个 z 上逐点假设一个统一差分估计；边界上的 L1 平均已足够。也只用了 2r 个固定实方向。

## 3. 一阶差商按几何尺度一致收敛

先把 F 看成取值于 Banach 空间 C(闭 D_ρ,C^r) 的连续函数。对固定 ℓ 定义

\[
Q_{j,\ell}(t)=\frac{F(\cdot,t+h_je_\ell)-F(\cdot,t)}{h_j}.
\]

恒等式

\[
Q_{j,\ell}-Q_{j+1,\ell}
=\frac{\Delta^2_{h_{j+1}e_\ell}F
       (\cdot,t+h_{j+1}e_\ell)}{h_j}
\]

及 (4) 给出

\[
\|Q_{j,\ell}-Q_{j+1,\ell}\|_{C^0}
\le\tfrac12 C_{0,\rho,R}\varepsilon_{j+1}.
\tag{5}
\]

由 (2)，Q_{j,ℓ} 在内部参数域上一致收敛到连续函数 L_ℓ。还得到具体尾和估计

\[
\|L_\ell-Q_{j,\ell}\|_{C^0}
\le\tfrac12 C_{0,\rho,R}
\sum_{k\ge j+1}\varepsilon_k.
\tag{6}
\]

L_ℓ 就是 ∂_{t^ℓ}F，而非仅一个沿 dyadic 子列的形式极限。证明可以沿坐标线积分：对固定坐标线段 [a,b]，

\[
\int_a^b Q_{j,\ell}(t)dt
=\frac1{h_j}
\left(\int_b^{b+h_j}F(t)dt-\int_a^{a+h_j}F(t)dt\right)
\to F(b)-F(a).
\]

左侧也趋于 ∫_a^b L_ℓ(t)dt。连续的 L_ℓ 因而给出真正的连续偏导数。所有坐标偏导连续，F 为 C1。

对每个 ∂_z^αF 用同样的 (4)–(6)，得到其 t 导数连续，且与 Cauchy 公式相容。

若 M 是较大闭图盒上 |F| 的上界，则可得

\[
\|D_tF\|_{C^0(D_\rho\times U')}
\le C\left(M/h_0+\sum_j\varepsilon_j\right).
\tag{7}
\]

## 4. 从图函数 C1 到真实分布 C1，检查逆映射

不能只从图函数可微就忽略叶状坐标的逆。这里用归一化 F(0,t)=t：

\[
D_tF(0,t)=Id_{\mathbb R^{2r}}.
\]

D_tF 连续，且其叶内导数受 Cauchy 估计控制，所以在内部紧参数域上，充分小的统一叶域满足

\[
\|D_tF(z,t)-Id\|\le C_*|z|<1/2.
\tag{8}
\]

因此 Ψ(z,t)=(z,F(z,t)) 的实 Jacobian 可逆，Ψ 与其逆均为 C1。在凸的内部参数球上还得到

\[
(1-C_*|z|)|t-t'|
\le |H_z(t)-H_z(t')|
\le(1+C_*|z|)|t-t'|.
\tag{9}
\]

这给出 holonomy 和逆映射的具体 Lipschitz 控制。

切分布在图参数中由 F_z 给出。第 3 节已证明 F_z 关于 (z,t) 为 C1，和 C1 的 Ψ^{-1} 复合后，得到环境中的 C1 子丛。

若这种估计在每个点附近成立，即得到全局 C1；紧致性可在取得局部估计后用于选择有限覆盖和统一常数。不能从一个图盒的估计无论证地推出全流形的估计。

## 5. 该估计的强弱和正确使用方式

若二阶差分为 O(|h|^{1+δ})，δ>0，则 ε_j=O(2^{-jδ})，当然满足 (2)。但 (2) 也允许例如 ε_j=C/(j+1)^{1+δ}，不要求任何固定正 Hölder 余量。因此它弱于假设统一的 C^{1+δ} holonomy。

本判据依然是一个额外估计，当前未从原始假设推出。它也不是 C1 的必要条件：某些 C1 函数的二阶差分上界不具有这种绝对可求和性。这里只给一个足够、可量化、无需先求导的入口。

不可以把 (2) 直接弱化为 ε_j→0，见第 7 节。

## 6. 在两个指定模型中检验

### 六维共振模型

17 中的 Darboux 图为

\[
F(q,t)=(t_1+\bar t_2q_1,t_2,t_3).
\]

它对实参数 t 为仿射，故所有二阶差分严格为零，(DZ) 可取 ε_j=0。输出与原模型两侧分布 C∞ 一致；模型的非零反全纯缺陷与共振并未被排除。

所以本估计没有把 pinching 或非共振换一个名字藏回来。

### 局部粗糙模型

F(q,t)=(t_1+q_1|t_2|^α,t_2)，0<α<1。在 t_2=0、沿实方向 h，二阶差分第一分量为 2q_1|h|^α。边界上 |q_1|=R，故

\[
\frac1{|h|}\int_{\mathbb T_R}|\Delta_h^2F|d\sigma_R
=2R|h|^{\alpha-1}\to\infty.
\]

它不满足 (DZ)，与其非 Lipschitz holonomy 一致。

## 7. “little Zygmund”仍不足：可求和性不可随意删去

取连续实函数

\[
a(x)=\sum_{k=1}^{\infty}\frac{2^{-k}}{k}\sin(2^kx),
\tag{10}
\]

再令局部粗糙模型中的 a(t)=a(Re t)。它仍产生保全纯辛的复 Lagrangian 叶片和精确保体积的剪切 holonomy。

若 2^{-N-1}<|h|≤2^{-N}，将 (10) 按 k≤N 与 k>N 分开，利用

\[
|\Delta_h^2\sin(2^kx)|\le C\min(1,2^{2k}h^2),
\]

得到一致估计

\[
|\Delta_h^2a(x)|
\le C h^2\sum_{k≤N}\frac{2^k}{k}
   +C\sum_{k>N}\frac{2^{-k}}{k}
\le C|h|/(N+1).
\tag{11}
\]

因此 \sup_x|Δ_h²a(x)|/|h|→0；这比普通 Zygmund 上界还强，却只有不可求和的 ε_j≈1/(j+1)。

取 h_N=2^{-N}。对 k≤N，sin(2^kh_N)≥c2^kh_N，尾项除以 h_N 的绝对值至多 C/(N+1)，所以

\[
\frac{a(h_N)-a(0)}{h_N}
\ge c\sum_{k≤N}\frac1k-C/(N+1)\to\infty.
\tag{12}
\]

a 非 Lipschitz，更不为 C1。由此可知，仅证明二阶差分 o(|h|) 还不能解决本研究的 C1 入口。

## 8. 尚未得到的动力学估计

真正的下一步是从紧致保全纯辛 Anosov 的原始条件，推出 (DZ)、其沿动力学重标度的版本，或别的足以替代它的可求和估计。

当前仅有不变生成势方程（13）和差极限的辛对偶自然性（15、17）；它们没有给出 ε_j 的可求和性。辛体积与 holonomy 的测度 Jacobian 控制也没有给出整个向量二阶差分的界。

即便将来由此取得 C1，仍需完成 C1 到全局分类的其余步骤；不能把 14 的已有共轭升级误当成模型共轭的存在性。
