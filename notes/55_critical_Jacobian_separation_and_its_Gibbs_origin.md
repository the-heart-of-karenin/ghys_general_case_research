# 临界行列式阈值下的双向指数分离：严格估计及其一般 Gibbs 来源

日期：2026-10-18。以 51–54 为基础。本记录给出原始假设下可完整证明的定量加强，同时证明它属于一般保体积 Anosov 理论，不能单独提供 IHS 刚性。下面的证明没有添加 pinching、C¹ 分布、非共振或额外稠密轨道假设。新颖性未确认；核心热力学机制是经典的。

## 1. 设置与结论

沿用假想的射影 IHS 复四维、保全纯辛、全纯 Anosov 分支。设

\[
\lambda=d_1(f)>1,\quad h=2\log\lambda,\quad
\Phi=\log J^u_1,\quad
S_n\Phi=\log J^u_n.
\]

这里 Jᵘ 是**不稳定复二维丛上的实行列式**，不是最大奇异值。Φ 为 Hölder。m 是光滑不变概率体积，θ 是 Green/最大熵概率测度。51 给出每片叶上的 Green 二次测度 νᵘ=Margulis 叶测度；52 给出 θ≠m。

记压力

\[
Q(t)=P_f(-t\Phi).
\]

**定理。** 对每个 0<t<1，令

\[
\delta(t)=(1-t)h-Q(t).
\tag{1}
\]

则 δ(t)>0。对任意 0<c<δ(t)，存在 C，使所有 n≥1 满足

\[
\boxed{
m\{J_n^u>\lambda^{2n}\}
+\theta\{J_n^u\le\lambda^{2n}\}
\le Ce^{-cn}.}
\tag{2}
\]

而且，对统一足够小的不稳定叶片 P，常数可以与叶片无关，使

\[
\boxed{
\operatorname{vol}_{P}\{x\in P:J_n^u(x)>\lambda^{2n}\}
+\nu^u\{x\in P:J_n^u(x)\le\lambda^{2n}\}
\le Ce^{-cn}.}
\tag{3}
\]

叶测度与叶体积均使用固定背景度量及 51 的规范选择；二者在统一叶片上的总质量一致有界。式 (3) 不是对不同测度直接作大小比较，而是对互补事件分别作界。

因此，54 中的额外因子 e^{εn} 可以在**行列式版本**中去掉，且 Green 一侧的收敛也有指数速度。不能将它自动推广成最大奇异值在 λ^{n/2} 处的同类结论。

## 2. 为什么压力中存在严格间隙

f 是传递 Anosov：51 已从保满支撑有限体积及谱分解推出，无需额外假设。也可用 θ mixing 且满支撑推出 topological mixing，因而可直接使用混合有限型编码的 Gibbs 理论。

标准 Anosov 热力学理论给出：θ 是势 0 的唯一平衡态；m 是势 −Φ 的唯一平衡态。[45, PDF p.3] 明确说明 SRB 的 Gibbs 势是 −log|det(Df|Eu)|；[50] 的对数矩机制仅作经典理论比较。因此

\[
Q(0)=h,\qquad Q(1)=0.
\tag{4}
\]

第二个等式也可从 Ruelle 不等式与 m 的 Pesin 公式验证：对任意不变概率 ν，h_ν(f)≤∫Φdν，而 m 取等号。唯一性来自 Hölder 势的 Anosov 平衡态理论。

压力的变分原理给

\[
Q(t)\le(1-t)Q(0)+tQ(1)=(1-t)h.
\]

若某个 0<t<1 取等号，令 ν_t 为 −tΦ 的平衡态，则

\[
\begin{aligned}
Q(t)&=(1-t)h_{\nu_t}(f)
+t\left(h_{\nu_t}(f)-\int\Phi\,d\nu_t\right)\\
&\le(1-t)h+t\cdot0.
\end{aligned}
\]

等号迫使 ν_t 同时为 0 与 −Φ 的平衡态。两端唯一性给 θ=m，与 52 矛盾。故 (1) 严格为正。这里没有把压力“通常严格凸”当作未核验的额外假设；仅用变分原理、存在性和两端唯一性。

## 3. 使用的对数矩恒等式及其证明

若 μ_β 是混合 Anosov 对 Hölder 势 β 的 Gibbs 平衡态，ψ 为 Hölder，则

\[
\lim_{n\to\infty}\frac1n
\log\int e^{S_n\psi}\,d\mu_\beta
=P_f(\beta+\psi)-P_f(\beta).
\tag{5}
\]

为明确其适用范围，给出标准证明。取有限型 Markov 编码，提升 β、ψ 及 Gibbs 测度。编码有限对一，压力与测度熵保持，积分由推前保持。每个长度 n 的柱集上，Hölder 势的 S_n 变化有与 n 无关的界。Gibbs 性给

\[
\mu_\beta([w])\asymp
\exp(S_n\beta(x_w)-nP_f(\beta)).
\]

将积分按柱集相加，得到与

\[
e^{-nP_f(\beta)}
\sum_{|w|=n}\exp(S_n(\beta+\psi)(x_w))
\]

相差固定乘法常数的量。柱集配分和的对数增长率即 P_f(β+ψ)，证明 (5)。不要求 β+ψ 的参数接近零。

这也是大偏差理论的经典输入。文献 [50] §4，PDF pp.17–18 显示对数矩与平移压力的关系；其一般无限塔定理有参数范围限制，**本文没有把该无限塔定理无条件套到任意参数**。这里使用有限 Markov 编码，并已独立写出 (5) 的全参数计算。

特别地，

\[
\begin{aligned}
\lim_n\frac1n\log\int e^{(1-t)S_n\Phi}\,dm&=Q(t),\\
\lim_n\frac1n\log\int e^{-tS_n\Phi}\,d\theta&=Q(t)-h.
\end{aligned}
\tag{6}
\]

## 4. 临界阈值的全局指数估计

对 E_n={S_nΦ>nh}，由 Markov 不等式，

\[
\begin{aligned}
m(E_n)&\le e^{-(1-t)nh}
\int e^{(1-t)S_n\Phi}\,dm,\\
\theta(X\setminus E_n)&\le e^{tnh}
\int e^{-tS_n\Phi}\,d\theta.
\end{aligned}
\tag{7}
\]

两项的对数上增长率都至多 −δ(t)。对任意 c<δ(t)，把有限个小 n 吸收到常数 C，即得 (2)。例如 t=1/2 时可取任意

\[
0<c<\frac h2-P_f(-\Phi/2).
\]

这解释为什么 54 的原始一阶 Markov 界在 ε=0 处退化为常数界，而 Gibbs 输入仍能取得严格指数界。

## 5. 从全局传播至每一片不稳定叶

两片匹配不稳定叶之间的稳定 holonomy 记为 H。稳定收缩及 Φ 的 Hölder 性给

\[
|S_n\Phi(Hx)-S_n\Phi(x)|
\le C\sum_{j\ge0}e^{-\gamma\kappa j}
\le D,
\tag{8}
\]

常数不依赖 n。它只比较**标量行列式势**，没有比较导数矩阵。

对 m，稳定 holonomy 的 Radon–Nikodym Jacobian 及其倒数一致有界；小乘积盒内，m 相对于两条参考叶的乘积坐标也有有界正密度。这是 C² Anosov 的绝对连续性结论，[48, Propositions 4.1–4.2, PDF p.7] 明确给出。它不意味着 holonomy C¹。

因此，对固定统一大小的匹配叶片族与任意实 a，(8) 给

\[
\int_{P}e^{aS_n\Phi}\,d\operatorname{vol}_{P}
\le C_a\int_X e^{aS_n\Phi}\,dm.
\tag{9}
\]

证明是先将各匹配叶片上的积分通过 holonomy 作一致比较，再对固定正质量的横向参数盒积分，最后用全局积分控制。有限盒覆盖及稍缩小叶片使常数统一。

对 θ，51 已给出 Margulis 精确乘积以及 νᵘ 的精确稳定 holonomy 不变性。以同样方式，用固定横向 Margulis 测度盒的正有限质量，得到

\[
\int_{P}e^{aS_n\Phi}\,d\nu^u
\le C'_a\int_Xe^{aS_n\Phi}\,d\theta.
\tag{10}
\]

取 (9) 的 a=1−t、(10) 的 a=−t，再重复 (7)，得到每片叶上的 (3)。这些是确定的叶测度，不是任选的“几乎处处条件测度版本”；51 已完成其逐叶识别与延拓。

对 f⁻¹ 的稳定侧完全同理。

## 6. 为什么它还不是 IHS 特有的刚性

到第二节以后，证明仅用“光滑保体积混合 Anosov，且其最大熵测度不同于体积”。IHS 的作用只是提供 h=2logλ、θ 的 Green 表示以及 θ≠m。故更强的指数分离本身仍与一般 Anosov 的正常行为相容。

一个明确的紧致实解析反检验如下。令

\[
A=\begin{pmatrix}5&2\\2&1\end{pmatrix},\quad
H_\varepsilon(x,y)=
\left(x,y+\frac{\varepsilon}{2\pi}\sin(2\pi x)\right),
\quad F_\varepsilon=A\circ H_\varepsilon
\]

作用于实二维环面。H_ε 保面积，ε 足够小时 F_ε 为保面积混合 Anosov，并与 A 拓扑共轭。四个点 (x,y)∈{0,1/2}² 仍是固定点。其导数行列式为 1，迹分别为

\[
6+2\varepsilon\quad(x=0),
\qquad 6-2\varepsilon\quad(x=1/2).
\]

ε≠0 时两类固定点的不稳定特征值不同。因此不稳定势不可能与同一个常数上同调。若面积就是最大熵测度，两种 Gibbs 柱集估计作用于周期字并重复任意多次，会迫使每个固定点的不稳定 Jacobian 都等于 e^{h_top}，矛盾。因此 m≠θ，(2) 的相同临界指数分离确实发生。

该模型是实面积保持动力学，不是全纯 IHS 例子；不把它称为 Ghys 反例。线性环面 ε=0 则有 m=θ、压力为直线、δ=0，正确地不满足严格估计。

## 7. 本轮获得和未获得的内容

已证明：从原始假设取得临界行列式阈值下、全局及每片叶上的双向指数分离，不要求额外 ε。它是 54 的严格加强。

未证明：使这种分离不可能的 IHS 特有约束。继续改善这类标量大偏差界，并不会自动给出绝对连续性、C¹ 或分类。56 将在真实的紧致 IHS 四维中进一步检验这个障碍，而不再只使用非紧局部模型。

符号与模型的辅助核验见 check_pressure_and_compact_measure_formulas.py 及 pressure_and_compact_measure_checks.json；其中 Bernoulli 模型只检查两个 Chernoff 指数的方向，实环面矩阵只检查固定点导数的代数式，均不代替本证明或断言某个固定数值 ε 已在 Anosov 结构稳定邻域内。
