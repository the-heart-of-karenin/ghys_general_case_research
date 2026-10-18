# 紧致 Kähler 底上的全纯保辛双曲 cocycle：稳定 c1 可以非零

日期：2026-10-18。性质：用于检验 c1 消失候选引理的显式模型，不是原 Ghys 目标的反例。这里的双曲线性 cocycle 不等于底流形的切导数。全部构造如下，不依赖未经说明的丛存在性定理。

## 1. 要排除的过强引理

下述说法不成立：

> 紧致 Kähler 底上的全纯复辛向量丛，如果具有全纯且全局一致双曲的保辛 cocycle，并且底映射也是保全纯辛 Anosov，那么稳定丛的第一 Chern 类必为挠类。

本记录给出反例。它说明要证明实际 c1(E^s) 消失，必须使用“该丛就是 TX，且 cocycle 就是 Df”或真实叶状几何，不能仅依靠这些抽象 cocycle 性质。

## 2. 一个 f-不变且非平凡的全纯线丛

取 B=C²/Z[i]²，

\[
A=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
K=\begin{pmatrix}-4&2\\2&4\end{pmatrix},\qquad
H(z,w)=z^TK\bar w.
\]

直接核验 A^TKA=K，det K=−20。A 的特征值为 (3±√5)/2，故 A 在 B 上诱导全纯 Anosov，且 det A=1，所以保持 dz_1∧dz_2。

对 λ∈Z[i]²，定义全纯的非零因子

\[
j_\lambda(z)=\exp\left(\pi H(z,\lambda)
+\frac\pi2H(\lambda,\lambda)\right).
\tag{1}
\]

K 的各项都为偶整数，所以 Im H(λ,μ)∈2Z。于是

\[
\frac{j_\lambda(z+\mu)j_\mu(z)}{j_{\lambda+\mu}(z)}
=\exp\left(\frac\pi2(H(\mu,\lambda)-H(\lambda,\mu))\right)=1.
\]

因此 λ·(z,u)=(z+λ,j_λ(z)u) 是格群作用，其商给出全纯线丛 L→B。

H(Az,Aλ)=H(z,λ) 使 j_{Aλ}(Az)=j_λ(z)，所以

\[
F:L\longrightarrow L,\qquad[(z,u)]\longmapsto[(Az,u)]
\tag{2}
\]

是覆盖 A 的全纯线丛同构。

## 3. 全局相容的度量与非零 c1

覆盖空间上的 Hermitian 范数

\[
\|(z,u)\|^2=|u|^2\exp(-\pi H(z,z))
\tag{3}
\]

在格群作用下不变，因此下降到 L。H 在底方向不正定无妨：指数始终为正，(3) 在每条纤维上都是正定 Hermitian 范数。又因为 A 保持 H，F 对这个纤维度量等长。

该度量的 Chern 曲率为常系数 (1,1) 形式；在通常的 Chern–Weil 约定下 c1 可由

\[
\frac i2\sum K_{ij}\,dz_i\wedge d\bar z_j
\]

代表（改变第一 Chern 类的整体符号约定不影响下述自交）。在高斯整数环面的基本域上，

\[
\int_Bc_1(L)^2=2\det K=-40\ne0.
\tag{4}
\]

故 c_1(L) 非挠，而且由 (2) 可知 A*c_1(L)=c_1(L)。

## 4. 升到复四维底与复秩四丛

令 X=B×B，f=A×A。X 是射影复四维环面；f 是全纯 Anosov，保持

\[
\Omega_X=dz_1\wedge dz_2+dz_3\wedge dz_4.
\]

将 L 从第一个 B 拉回，记号仍为 L。令

\[
E=L\oplus\mathcal O_X,\qquad
\mathcal V=E\oplus E^*.
\]

V 带规范的非退化**纤维**全纯交替配对 ω_V。用 (2) 与平凡线的自然提升，得到 E 上一个等长的全纯 cocycle F_E。固定 0<ε<1，定义 V 上的 cocycle

\[
\Phi_x=\varepsilon(F_E)_x\oplus
\varepsilon^{-1}((F_E)_x^{-1})^*.
\tag{5}
\]

它覆盖 f，保持 ω_V，全纯且可逆。在直和度量下，E 上每次迭代准确缩小 ε，E* 上准确扩大 ε^{-1}。因此全局一致双曲，稳定丛恰为 E，并且 E 本身就是全纯子丛。

但是

\[
c_1(E)=c_1(L)\ne0\quad\text{且非挠}.
\tag{6}
\]

## 5. 为什么不是原问题的反例

原问题要求稳定丛位于 TX，且线性作用是 Df。这里

\[
c_2(\mathcal V)=-c_1(L)^2\ne0,
\qquad c_2(TX)=0,
\]

所以 V 甚至不与 TX 拓扑同构。ω_V 也只是向量丛的纤维辛配对，不是以 V 代替 TX 后得到的底空间微分二形式。

因此这个模型只反驳丢掉真实切导数条件的过强引理。它没有反驳 IHS 四维中的 c1 挠性目标，也不提供粗糙稳定分布：这里的稳定分布是全纯的。

## 6. 对下一步的影响

31–32 已表明复 K 理论数据相容；本模型进一步说明，“紧致 + Kähler + 全纯保辛双曲 cocycle + Anosov 底”这些性质本身也不提供稳定 c1 消失。

应把新证明所必需的输入明确放在：TX 的具体拓扑/辛结构（34），或 Df 是底映射的真实微分，以及两侧积分叶的几何。没有理由把抽象 cocycle 的拓扑收缩直接解释成全局平凡化。

背景核对：Andrew Snowden，Math 679 (2013)，Lecture 3 的 “Line bundles on complex tori” 部分提供相同的标准 Appell–Humbert 因子公式：https://public.websites.umich.edu/~asnowden/teaching/2013/679/L03.html 。这里只使用构造的形式；(1)–(6) 的一致性、曲率与双曲性已直接验证，不需要完整 Appell–Humbert 分类。该网页是讲义，非期刊论文，单列于文献检索记录；不宣称本模型的新颖性。
