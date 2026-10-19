# 单张快谱形式的非退化 flux 与复流的准确快方向正规形

日期：2026-10-19。性质：从 71、74–75 的原始六维系统推出的严格中间定理。不假设第二张形式、完整 Albanese 正维、pinching、共轭可微或 Haar 测度。这里先不要求 dim W_X=1，只要存在一张快谱闭全纯形式。99–100 再处理一维剩余分支。

## 1. 结论

设 X、f、Ω 具有 71 的准确模型拓扑和同伦标记，α≠0 为快谱闭全纯一形式。按需要同时取 f、F 的逆，并记

\[
r=\lambda^2,\quad \lambda=2+\sqrt3,\qquad
f^*\alpha=r^{-1}\alpha.
\tag{1.1}
\]

以 Ω 对偶定义 V，ι_VΩ=α。其完备全纯复流 φ_z 满足

\[
f\phi_zf^{-1}=\phi_{rz}.
\tag{1.2}
\]

用 74 的同一个标记拓扑共轭 H₀f=FH₀，置 ψ_z=H₀φ_zH₀⁻¹。在模型万有覆盖上可准确写

\[
\widetilde\psi_z(g)=g\exp\bigl(b(z)+c_z(g)\bigr),
\tag{1.3}
\]

其中：

- b:C_R→E_r 是实线性同构，E_r 为模型 Lie 代数中实二维的扩张快特征平面；
- c_z 是紧致模型上的连续、Γ 周期函数，取值于实四维 E_λ；该空间包括一个慢水平和一个中心方向；
- G^u=exp(E_r⊕E_λ) 是本模型的阿贝尔扩张子群；
- c 满足普通交换 cocycle 及准确缩放

\[
c_{z+w}=c_z\circ\psi_w+c_w,\qquad
c_{rz}\circ F=\lambda c_z,
\tag{1.4}
\]

且存在系统相关的有限常数 C，使

\[
\boxed{\|c_z\|_\infty\le C|z|^{1/2}\quad(z\in\mathbb C).}
\tag{1.5}
\]

没有证明 c_z=0。真正新增的是 b 非退化且准确恒定；它将使复流在一个自然覆盖上 proper，即便 (1.5) 的临界项保留也可作全纯约化。

## 2. 一个新的 flux 线性代数事实

令 θ=Re Ω，它是实际闭实辛形式。71、70 的模型一阶空间分为实四维 fast 与实四维 slow。70 的 F 固定闭二阶代表给出 θ 的实不变代表

\[
\theta_0=H+B+D,
\quad H\in\Lambda^2\langle x_1,\ldots,x_4\rangle,
\quad B\in\Lambda^2\langle y_1,\ldots,y_4\rangle,
\quad D=\sum_{i=1}^4 d_i y_i\wedge z_i.
\tag{2.1}
\]

这里可使用 70 的复化 Heisenberg coframe 计算，最后取实结构；dx_i=dy_i=0，dz_i=−x_i∧y_i。所用十二参数基是全局固定二阶空间的基，不限于 70 后半部的小周期邻域。

定义实交替型

\[
\mathcal L_\theta(e,a)=\int_X e\wedge a\wedge\theta^5
\quad(e,a\in H^1(X,\mathbb R)).
\tag{2.2}
\]

**引理。** 此型的核恰为 slow primary，且在 fast primary 上非退化。因此 cup 映射 H¹→H¹¹，a↦a[θ]⁵ 的实秩为四。

证明。任何顶次 monomial 都须包含四个 z_i，只能来自四个 D，亦已占满四个 y_i。因此

\[
\theta_0^6=15H^2D^4.
\tag{2.3}
\]

实际 θ 辛，故 ∫θ⁶≠0，同一上同调类使右侧积分非零。于是 H 在 fast 实四维空间非退化，D⁴≠0。

若 a 或 e 属 slow，则 e a θ₀⁵ 的每个可能顶项都因重复 y 而为零。若二者属 fast，唯一可能顶项为

\[
e\wedge a\wedge\theta_0^5
=5e\wedge a\wedge H\wedge D^4.
\tag{2.4}
\]

实四维辛空间上，a↦a∧H 是一次到三次外幂的同构，(e,a)↦e a H 非退化。D⁴ 因子非零，故 (2.2) 的 fast 限制非退化，且没有其他核。∎

这只使用杯积积分，没有从复杂周期代表的复秩恢复 J。69 的复秩反例因此不影响本引理。它反而说明必须区分“Re Ω 的顶次积分足以算 flux”与“Ω 的周期决定未知复结构”。

## 3. 两个实流的快方向平均旋转线性独立

设 U=V+bar V、U'=iV−i bar V。它们分别为复流的两个实生成元，并保持

\[
\nu=\theta^6/\int_X\theta^6,
\]

其与 Ω³barΩ³ 的归一化体积相同。收缩给

\[
\iota_U\theta=\operatorname{Re}\alpha,
\qquad\iota_{U'}\theta=-\operatorname{Im}\alpha.
\tag{3.1}
\]

对任意闭实一形式 η，

\[
\int_X\eta(U)\,d\nu
=\frac6{\int_X\theta^6}
\int_X\eta\wedge\operatorname{Re}\alpha\wedge\theta^5,
\tag{3.2}
\]

U' 同理。

71 的 W⊕bar W 注入使 Re α、Im α 在 H¹(X,R) 中独立；因二者属于同一个实二维快特征空间，它们恰张满该空间。§2 的非退化型以及 f* 的谱配对遂使 U、U' 的 Schwartzman 平均旋转为同一相反快特征平面中的两个独立向量 v₁、v₂。

慢 primary 上所有旋转均为零。这不能单独消去慢位移；这里只取得所需的非退化快旋转。

## 4. 完整位移先落入阿贝尔扩张子群

对 ψ 的从恒等开始的准确提升定义右位移

\[
u_z(g)=g^{-1}\widetilde\psi_z(g).
\tag{4.1}
\]

Γ 等变性使 u_z(γg)=u_z(g)，故它是紧致模型上的连续 G 值函数。正规化准确给

\[
u_{rz}(Fg)=F(u_z(g)).
\tag{4.2}
\]

固定 z，令 n→∞，

\[
F^{-n}u_z(g)=u_{r^{-n}z}(F^{-n}g)\longrightarrow e
\tag{4.3}
\]

一致成立。因此 u_z(g)∈G^u。

05 模型两侧 horospherical Lie 子代数都阿贝尔：原 F 的扩张侧为〈∂_x,∂_z,∂_b〉，收缩侧为〈∂_y,∂_a,∂_c〉，括号都为零。取逆只是交换二者。所以这里

\[
\log u_z=a_z+c_z\in E_r\oplus E_\lambda
\tag{4.4}
\]

为普通向量值流 cocycle，且 a_{rz}∘F=r a_z、c_{rz}∘F=λc_z。

这也解释了为何不能照抄 82 的完整中央椭圆配对：本轮位移已在阿贝尔的同侧子群内，剩余临界慢方向与快方向的括号为零，没有 82 所需的可逆中央剪切项。

## 5. 快分量准确成为常平移

a_z 是阿贝尔化位移在快特征平面的投影。对任一固定复参数 ζ，沿实流 t↦ψ_{tζ} 有

\[
\|a_{t\zeta}\|_\infty\le C_\zeta |t|+C'\quad(t\in\mathbb R).
\tag{5.1}
\]

因为原流光滑、闭一形式沿生成元有界，而 H₀ 与恒等同伦所添加的阿贝尔化修正有界。75 §4 的 Birkhoff 与准确缩放论证可直接用于这个**最高速投影**：

\[
\frac{a_{T\zeta}}T\longrightarrow v_\zeta
\quad\text{几乎处处及 }L^1,
\]

其极限因 F-不变和光滑保体积 Anosov 的遍历性为常向量。于是

\[
\|a_{t\zeta}-tv_\zeta\|_1
=t\left\|\frac{a_{r^nt\zeta}}{r^nt}-v_\zeta\right\|_1
\longrightarrow0.
\tag{5.2}
\]

这里 μ=H₀*ν，不假设是 Haar。满支撑和连续性使等式处处成立。分别用 ζ=1、i，加上两个流交换，得到

\[
a_z=b(z),\qquad b(u+iv)=u v_1+v v_2.
\tag{5.3}
\]

§3 使 v₁、v₂ 独立，故 b 为实线性同构。这不是“平均非零”代替逐点等式，(5.2) 是不可省略的升级。

这还独立排除 V 的零点：若 V 在 X 的某点为零，其提升复流在覆盖上也固定该点，对应的快位移却必须等于非零的 b(z)，矛盾。因此 α 处处非零。对于本轮快形式，这个无零结论不必再调用 74 的 A'Campo 步骤；99 使用的 Φ=LH 只是 74 中由双向有界差取得的准确发展映射恒等式。

## 6. 临界项的全局平方根上界

c_z 在紧致模型上连续。令

\[
C_0=\sup_{1\le|z|\le r}\|c_z\|_\infty<\infty.
\]

F 满射以及 (4.4) 的缩放给 ∥c_{r^n z}∥∞=λⁿ∥c_z∥∞。将任意 z≠0 缩放到上述环域，并用 r=λ²，得到 (1.5)。同时由 G^u 阿贝尔得到 (1.4)。

没有新的可求和性或 c=0 结论。单凭一个连续的 r:λ 次线性 cocycle，平方根恰是临界阶；不得把该界称为它自己的消去证明。99 的全纯约化不需要先消去 c。

## 7. 模型与失败路线

05 中取 α=dx，原 f=F，V 是 ±∂_a。按本篇取逆后，流在 H=id 中为快 a 平移，b 非退化、c=0。其快 flux 非零，而 75 的慢形式 flux 为零；二者准确区分。

原计划“对快流取 Homeo(X) 中的紧致闭包，产生第二张形式”不能默认成立。在该已知紧致模型，右快平移 a↦a+t 的导数在左不变标架中把 B=∂_b+bar a∂_c 送为 B−bar t C，因此随 |t| 至少线性增长。更直接地，在慢坐标不为零处，快方向在 nilmanifold 中会积累中心剪切；它没有 75 的纯中心平移结构。故应先证明等度连续，不能把轨道闭包和自同构群中的紧致闭包混为一谈。

对全纯映射族，C⁰ 等度连续会使较小坐标盒的像统一落入固定复坐标盒，再由 Cauchy 估计给统一一阶导数界；上述实际导数增长因此也严格排除该模型快流族的 C⁰ 等度连续性。

本轮改用 b 的非退化性取得覆盖上的 proper 作用，绕过这个未闭合步骤。既有 74 的无零定理、75 的保辛遍历性和标记共轭作为已完成输入沿用；没有重跑旧数值套件。flux 及本应用的新颖性未确认。

仅对本轮新增外代数公式作了独立精确核验：θ⁶=15H²D⁴、64 个 Lefschetz 配对条目及 fast 块行列式全部通过，见 check_single_fast_flux.py、single_fast_flux_checks.json。这只核对 monomial 系数与核维数，不验证遍历性、全纯商或 100 的障碍定理。
