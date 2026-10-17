# 对一个取极限步骤的反例：全部固定阶 jet 光滑，holonomy 仍非 Lipschitz

日期：2026-10-17。性质：显式局部／非紧全局反例。**它不反驳紧致保全纯辛 Anosov 的 Ghys 猜想，也没有构造 Anosov 稳定分布。** 它反驳的是从非 Lipschitz 自动抽出非零内部法向差极限的推理。

## 1. 构造

在 C4 的坐标 (z_1,z_2,w_1,w_2) 上取

\[
\omega=dz_1\wedge dw_1+dz_2\wedge dw_2.
\]

对 k≥1，令

\[
m_k=\lceil k^{3/2}\rceil,
\quad A_k=2^{-k^2},
\quad N_k=2^{k^2+m_k},
\]

\[
a_k(t)=A_k\bigl(1-\cos(N_k\operatorname{Re}t)\bigr),
\qquad
B(z,t)=\sum_{k=1}^{\infty}a_k(t)z^k.
\tag{1}
\]

每个 a_k 在实二维 t 平面上 C∞，且周期于 Re t。对任意有限 R，Σ2A_k R^k 收敛，因此 B 对 z 整全纯、整体连续，所有 z 导数在紧域上连续。B(0,t)=0。

定义叶片

\[
\mathcal L_{t_1,t_2}:\quad
w_1=t_1+B(z_1,t_2),\qquad w_2=t_2,
\tag{2}
\]

以及竖直叶片 z=常数。映射

\[
(z,t)\mapsto(z,t_1+B(z_1,t_2),t_2)
\]

是整个 C4 上的同胚，逆映射显式为 t_2=w_2、t_1=w_1−B(z_1,w_2)。所以这确实是两个互补连续叶状结构。

每片 (2) 都双全纯于 C2，并对 ω 为 Lagrangian：在叶上 dw_1=B_z dz_1、dw_2=0，故 ω 限制为零。竖直叶也为复 Lagrangian。

相应分布为

\[
E=\langle\partial_{z_1}+B_z(z_1,w_2)\partial_{w_1},
\partial_{z_2}\rangle,
\quad F=\langle\partial_{w_1},\partial_{w_2}\rangle.
\tag{3}
\]

## 2. holonomy 精确保体积，且属于所有 C^θ、θ<1

从 z=0 到 z=(s,0) 的 holonomy 为

\[
H_s(t_1,t_2)=(t_1+B(s,t_2),t_2).
\tag{4}
\]

对每个固定 t_2，它在 t_1 复平面上只是平移。Fubini 定理给出 H_s 精确保实四维 Lebesgue 测度；其逆把 B 改成 −B。

对任意 0<θ<1，利用 |cos u−cos v|≤C min(1,|u−v|)≤C|u−v|^θ，有

\[
|B(z,t)-B(z,t')|
\le C|t-t'|^\theta
\sum_{k\ge1}R^k2^{-(1-\theta)k^2+\theta m_k}
\quad(|z|\le R).
\tag{5}
\]

因为 m_k=O(k^{3/2})=o(k²)，右侧级数收敛。因此在任何固定紧叶域上，H_s 和逆映射都为 C^θ，对每个 θ<1 都成立。各固定阶 z 导数也有同样性质。

这说明“把 Hölder 指数提高到任意接近 1”仍不能替代 Lipschitz，更不能替代 C1；必须控制随 θ→1 的常数或取得另一种估计。

## 3. 每个非零正实 s 上，holonomy 在 t_2=0 非 Lipschitz

固定 s>0，取 h_k=π/N_k。由于各项非负，且第 k 项的余弦等于 −1，

\[
\frac{B(s,h_k)-B(s,0)}{h_k}
\ge\frac{2}{\pi}A_kN_ks^k
=\frac{2}{\pi}2^{m_k}s^k\longrightarrow\infty.
\tag{6}
\]

最后一步因为 m_k/k→∞。所以 H_s 在原点附近不是 Lipschitz。同样，

\[
\frac{B_z(s,h_k)-B_z(s,0)}{h_k}
\ge\frac{2k}{\pi}2^{m_k}s^{k-1}\to\infty,
\]

故分布 E 在这些点附近也不是 Lipschitz。

## 4. 但每个固定阶叶内 Taylor 系数都横向光滑

在中心叶坐标 z_1=0，

\[
\partial_{z_1}^{k} B(0,t)=k!a_k(t).
\tag{7}
\]

对每个固定 k，右侧是 C∞ 函数。任何固定有限阶 jet 的所有横向导数都存在且连续。

因此，有限阶 jet 检验不能排除本例。缺少的是随叶内阶数增加时统一的横向控制；各 a_k 的 Lipschitz 常数 A_kN_k=2^{m_k} 无界。

这里没有声称完整叶状结构在一个开邻域中 C∞：第 3 节已经证明相反结论。

## 5. 所有候选非零内部粗糙差极限都消失

令 F(z,t)=(t_1+B(z_1,t_2),t_2)。设 t_j、t'_j 趋于任一给定参数，c_j>0，且

\[
|t_j-t'_j|/c_j\to0.
\tag{8}
\]

若 (F(·,t_j)−F(·,t'_j))/c_j 在原点的某个固定连通开叶邻域中局部一致收敛，则极限恒零。

证明：常数 Taylor 项为 (t_j−t'_j)/c_j，趋零。对每个固定 k，a_k 的 Lipschitz 常数是有限的，故

\[
\frac{|a_k(t_{2,j})-a_k(t'_{2,j})|}{c_j}
\le A_kN_k\frac{|t_{2,j}-t'_{2,j}|}{c_j}\to0.
\]

局部一致全纯收敛使每个 Taylor 系数收敛。极限的全部 Taylor 系数都为零，所以极限恒零。证毕。

第 3 节却给出真实的非 Lipschitz holonomy。因此“存在粗糙性 ⇒ 归一化后有非零内部全纯差极限”是错误的，哪怕各叶全局为 C2、差函数整全纯、holonomy 保体积且属于所有 θ<1 的 Hölder 类。

按 17 的二择引理，本例的粗糙序列必通过高阶／边界集中表现，不能经非零退化极限表现。

## 6. 与指定的两个模型对照

notes/05 六维模型的稳定图 F(q,t)=(t_1+\bar t_2q_1,t_2,t_3) 只有一次叶内项，且系数对 t 实线性。差范数由 |t−t'| 控制，无高阶集中。

notes/11 的粗糙模型也只有一次叶内项，但系数 a(t_2)=|t_2|^α 非 Lipschitz。它确有非零极限 (q_1,0)，零点为超平面。因此它揭示的是另一类障碍：退化差极限。

两个局部反模型分别检验两种缺口，不能把其中一个排除后便认为入口已解决。

## 7. 反例的范围与紧致 Anosov 尚可使用的约束

本例没有给出保持 (E,F) 并使它们成为实际稳定／不稳定方向的全局 Anosov 映射。它也不是紧致流形模型：B 对叶变量不是椭圆周期函数，不能直接下降到复环面。

此外 w_2 是 E 的非恒定连续全局第一积分；在紧致保体积 Anosov 中，每片稳定叶稠密，排除这样的全局第一积分。这个事实排除本模型的直接紧致化，但尚未排除同样的局部高阶集中机制在其他系统中出现。

尚需证明的真正动力学命题是：紧致性、一致双曲性及不变全纯辛形式是否给出叶片差的内部范数控制，或其他足以阻止本例高阶集中的估计。当前没有该证明。
