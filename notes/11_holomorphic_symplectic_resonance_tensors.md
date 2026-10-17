# 全纯辛情形：对称共振张量、有限嵌套阶与局部正则性障碍

日期：2026-10-17。性质：独立推导，未查明新颖性。下述张量结论**需要 C1 分布**；这还没有由原始 Anosov 假设推出。最后的局部例子专门防止把这一缺口隐藏掉。

## 1. 设置与缺陷

设 X 的复维数为 2r，ω 是闭、非退化的全纯 (2,0) 形式，f 是保持 ω 的全纯 Anosov。记 E=E^s，F=E^u。

它们都是复秩 r 的 Lagrangian 子丛，因为 Re ω、Im ω 分别在同一侧上为零。以下暂时假设 E 为 C1。记 Q=T^{1,0}X/E，并使用 06 中的内蕴张量

\[
\mathcal B_E(\bar w,v)=(\bar\partial v)(\bar w)\pmod E,
\qquad
\mathcal B_E\in\operatorname{Hom}_{\mathbb C}
(\overline{T^{1,0}X}\otimes E,Q).
\tag{1}
\]

它连续，且为零当且仅当 E 全纯。

## 2. 只剩横向反全纯变量，而且出现对称性

由于 E 的叶是复子流形，对 \bar w∈\bar E，有

\[
\mathcal B_E(\bar w,v)=0. \tag{2}
\]

证明可以在 C1 分布的局部标架中进行：同一叶的复化切空间 E⊕\bar E 对 Lie 括号封闭，而 [\bar w,v] 的 (1,0) 分量模 E 就是 (1)。

于是 (1) 的第一个变量下降到 \bar Q。定义

\[
C_E(\bar q;v,z)
=\omega\bigl(\mathcal B_E(\bar q,v),z\bigr),
\quad \bar q\in\bar Q,\quad v,z\in E. \tag{3}
\]

这里 ω(Q,E) 的配对良定义且非退化。对恒等式 ω(v,z)=0 沿反全纯方向微分，利用 ω 全纯，得到

\[
0=\omega(\mathcal B_E(\bar q,v),z)
 +\omega(v,\mathcal B_E(\bar q,z)).
\]

因此

\[
C_E(\bar q;v,z)=C_E(\bar q;z,v). \tag{4}
\]

共轭辛配对 \bar\omega:\bar Q\times\bar E→\mathbb C 非退化。故有唯一连续对称复双线性映射

\[
R_E:\operatorname{Sym}^2E\longrightarrow\bar E
\tag{5}
\]

满足

\[
C_E(\bar q;v,z)=\bar\omega\bigl(\bar q,R_E(v,z)\bigr).
\tag{6}
\]

这是本轮的关键改写：缺陷原本含一个不稳定横向反全纯输入，辛配对将它转换为完全在稳定子丛内部的对称二次映射，输出落在其共轭子丛。并且

\[
E\text{ 全纯}\iff R_E=0. \tag{7}
\]

如果两侧均 C1，不稳定侧同样得到 R_F:Sym²F→\bar F。

## 3. 精确动力学方程与周期共振

写 S_x=Df_x|E_x。由 f 全纯、保持 ω，以及 (1) 的自然性，有

\[
R_{E,fx}(S_xv,S_xz)=\bar S_x R_{E,x}(v,z).
\tag{8}
\]

对周期点 p=f^m p，设 S=Df_p^m|E_p，其复谱为 λ_1,…,λ_r，允许非平凡 Jordan 块。则

\[
\bar S R_{E,p}=R_{E,p}(\operatorname{Sym}^2S). \tag{9}
\]

所以非零缺陷只能存在于

\[
\boxed{\bar\lambda_k=\lambda_i\lambda_j}
\tag{10}
\]

这些精确复共轭二次共振中。若两边谱不相交，由广义特征空间或 Sylvester 方程，R_{E,p}=0；不需要 S 可对角化。

全纯辛配对还给出 U 与 S^{-T} 的复线性共轭。因此不稳定侧共振

\[
\bar\mu_k=\mu_i\mu_j
\]

在 μ_j=λ_j^{-1} 的记号下仍是 (10)。于是得到条件性推论：

**若两侧已经 C1，并在稠密周期点上没有 (10)，则两侧全纯；由 10 的分类接口得到复 infra-nil 分类。**

这没有解决本轮原目标：它仍增加 C1 和非共振。它的用途是识别必须保留的缺陷，不能把 (10) 当成原假设自然排除的关系。

## 4. 不需要非共振的有限嵌套阶

以下基本引理允许二次映射非零。

**引理。** 设 V→X 是有限秩实向量丛，S:V→V 覆盖 f，且某个迭代 F=f^m 满足

\[
0<a\le m(S_F(x))\le\|S_F(x)\|\le b<1
\quad(x\in X).
\tag{11}
\]

设 B:V⊗V→V 为连续、S-等变的双线性映射。对每个二叉括号树，把 B 嵌套组成 d 次多线性映射 P_d:V^{⊗d}→V。如果 b^d<a，则 P_d 恒为零。

**证明。** 每个固定括号树给出的 P_d 连续且等变，紧致性给出统一界 M_d。由迭代等变性，

\[
P_{d,x}=S_{F^n,x}^{-1}\,
P_{d,F^nx}\,(S_{F^n,x})^{\otimes d}.
\]

故

\[
\|P_{d,x}\|
\le M_d\frac{\|S_{F^n,x}\|^d}{m(S_{F^n,x})}
\le M_d(b^d/a)^n\longrightarrow0.
\]

于是 P_d=0。证毕。

因为 b<1，总存在整数 N 使 b^N<a；所有 d≥N、所有括号树均消失。**这里没有 b²<a 的假设，也没有排除二次或更低阶共振。**

把引理用于 (5) 时，需要准确处理共轭输出。将稳定实子丛复化为

\[
V_{\mathbb C}=E\oplus\bar E.
\]

在 E×E 上定义 B=R_E，在 \bar E×\bar E 上定义 B=\overline{R_E}，在混合输入上定义 B=0。这个 B 与实共轭相容，故来自稳定实子丛上的连续实双线性映射；由 (8) 它等变。于是引理适用。

得到：**只要缺陷达到连续张量的正则性，它与共轭组成的对称乘法必在某个统一有限次数后完全消失，尽管 R_E 本身可以非零。** 对 R_F 使用 f^{-1} 同理。

这是逐纤维、可能非结合的对称代数意义上的有限嵌套阶。没有证明结合律、Jacobi 恒等式、横向光滑性、恒定秩，或全局 Lie 群作用。不可直接把它叫成已经构造好的幂零 Lie 代数。

### 4.1 维数决定的统一上界

本设置中周期点稠密，因而还有更强、与收缩速率比无关的上界：

\[
\boxed{d>2^{r-1}\quad\Longrightarrow\quad
\text{每一个 d 次嵌套乘积恒为零}.}
\tag{11a}
\]

**证明。** 固定周期点 p，回归导数在 E_p⊕\bar E_p 上为 D=S⊕\bar S。按特征值模的负对数，把广义特征空间合并为正权空间

\[
V_{\mathbb C,p}=\bigoplus_{\nu\in\mathcal W}V_\nu,
\qquad \nu=-\log|\lambda|>0.
\]

因为共轭不改变模，正权的不同取值数 q=|\mathcal W| 至多为 r。B 的 D-等变性给出

\[
B(V_\alpha,V_\beta)\subseteq V_{\alpha+\beta},
\tag{11b}
\]

其中不存在的权空间视为零。对广义特征空间，(11b) 仍成立：等变双线性映射将特征值 λ、μ 的广义空间送入 λμ 的广义空间，随后再按模合并。

将任一括号树的各输入分别分解到正权空间。若某个这样的齐次输入项给出的树乘积非零，那么树中每一个子树乘积都非零。从任意叶节点沿路径走向根节点，每次权重都严格增加，因为另一个分支的权重为正。所以每条路径最多有 q 个节点权重，亦即树的深度最多 q−1。一棵深度最多 q−1 的二叉树至多有 2^{q-1} 个叶节点。

因此次数 d>2^{r-1} 的每一棵树在每个周期点上都为零。该树给出的张量连续，而周期点稠密，故处处为零。证毕。

这个证明同样允许 Jordan 块，也没有要求周期点之间的具体谱相同。它只使用“稳定权均为正”“不同权至多 r 个”及周期点稠密。

### 4.2 稳定复秩二时的旗标

若 r=2，则所有三次嵌套乘积均为零。在 R_E≠0 的开集上，这强迫

\[
K:=\{v\in E:R_E(v,w)=0\ \forall w\in E\}
\quad\text{为复线子丛},
\]

并且

\[
\operatorname{im}R_E=\bar K,\qquad
R_E:\operatorname{Sym}^2(E/K)\overset{\sim}{\longrightarrow}\bar K.
\tag{11c}
\]

证明：三次乘积 B(B(v,z),\bar w)=0 给出 im R_E⊂Ann(\overline{R_E})=\overline K。若 R_E 非零，则 K 的维数至多一；而左边非零，又迫使 K 的维数至少一。因此 K 是一维，包含关系是等号，余下的因子都是一维。(11c) 随之成立。

K 连续且 f-不变，但这里不能声称它已光滑，也不能无论证地把它延拓过 R_E=0 的集合。这个旗标为复四维子问题提供更具体的后续入口，并不是对该子问题的分类证明。

## 5. 六维临界模型中的具体值

使用 05 的左不变 (1,0) 标架

\[
X_1=\partial_x,\quad Y=\partial_y+\bar x\partial_z,
\quad Z=\partial_z,
\quad A_1=\partial_a,\quad
B_1=\partial_b+\bar a\partial_c,\quad C=\partial_c.
\]

E=⟨Y,A_1,C⟩，F=⟨X_1,Z,B_1⟩，且

\[
\bar\partial Y=d\bar x\otimes Z,\qquad
\bar\partial B_1=d\bar a\otimes C.
\]

用本文件 (6) 的符号约定，

\[
R_E(Y,Y)=\bar A_1,\qquad
R_F(B_1,B_1)=-\bar X_1,
\tag{12}
\]

其余标架输入的值为零。核查符号：ω(Z,Y)=1，\barω(\bar X_1,\bar A_1)=1；ω(C,B_1)=1，\barω(\bar A_1,\bar X_1)=-1。

动力学权重分别满足

\[
(\lambda^{-1})^2=\lambda^{-2},\qquad
\lambda^2=\lambda^2,
\]

正是 (10)。上述 B 的所有三次嵌套乘积都为零，而 B≠0。因而新的结构结论容纳了原先严格夹逼无法容纳的模型。

## 6. 局部几何本身不提供 C1：显式粗糙模型

在 C4 的坐标 (x_1,x_2,y_1,y_2) 中，取标准全纯辛形式

\[
\omega=dx_1\wedge dy_1+dx_2\wedge dy_2.
\]

取任意连续函数 a:C→C，例如 a(t)=|t|^α，0<α<1。考虑两族叶：

\[
\mathcal L_{(t_1,t_2)}:
\quad y_1=t_1+x_1a(t_2),\quad y_2=t_2,
\tag{13}
\]

以及 x_1、x_2 为常数的竖直叶。映射

\[
(x_1,x_2,t_1,t_2)\longmapsto
(x_1,x_2,t_1+x_1a(t_2),t_2)
\]

是同胚，逆映射显式为 t_2=y_2、t_1=y_1-x_1a(y_2)。故 (13) 确实构成连续叶状结构。

每片叶对 x 变量全纯，并且是复 Lagrangian。两侧切分布为

\[
E=\langle\partial_{x_1}+a(y_2)\partial_{y_1},
\partial_{x_2}\rangle,\qquad
F=\langle\partial_{y_1},\partial_{y_2}\rangle.
\tag{14}
\]

两侧互补、J-不变、Lagrangian。F 全纯，E 在 y_2=0 附近甚至不为 Lipschitz。这是光滑全纯辛环境中“连续横向变化、各叶全纯”的例子。

它**不是**紧致全局 Anosov 的反例，没有构造 f。因此不反驳目标分类。它证明下述局部升级论证无效：

> 光滑全纯辛形式 + 两个互补复 Lagrangian 叶状结构 + 各叶全纯，就自动得到横向 C1。

即使把 a 取成 C1 但不 C∞，也可得到非光滑的 C1 例子。此时 R_E 的唯一可能非零分量为

\[
R_E(v_1,v_1)=
\frac{\partial a}{\partial\bar y_2}\,\bar v_2,
\quad v_1=\partial_{x_1}+a(y_2)\partial_{y_1},
\quad v_2=\partial_{x_2}.
\]

其所有三次嵌套乘积仍为零。可见逐纤维有限嵌套阶本身也不足以推出横向 C∞。

## 7. 仍需真正证明的下一步

原始 Anosov 分布只有连续性，(1) 只可能先作为弱导数讨论。此时不能直接在周期点求值，也不能不加论证地对缺陷反复做乘法。第 4 节的有限阶论证不能倒过来充当 C1 的证明。

值得继续的问题是：全局紧致动力学是否能把局部粗糙模型排除，并给出受控弱缺陷、连续的共振张量或足够规则的横向 holonomy？还需要在允许非零 (10) 的情况下完成这个正则性入口。

到此得到的是新的共振结构约束和一个明确的局部障碍；无夹逼保辛分类尚未证明。

后续连续层研究：17–18 区分退化差极限与高阶集中两类障碍；19 给出平均 Dini 二阶差分的 C1 充分估计。19 的估计在 05 六维共振模型中严格成立（所有横向二阶差分为零），在本文件的 |t|^α 粗糙模型中失败。没有预先使用本文件需要 C1 的张量。
