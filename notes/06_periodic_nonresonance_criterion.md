# C1 分布的周期非共振判据

日期：2026-10-17。性质：独立推导的另一项条件性结果；未声称文献新颖性。它与 04 的 Lp 充分条件不同：允许缺少统一谱夹逼，但需要先有 C1 分布及稠密的合适周期点。

## 1. 一般子丛判据

设 X 为复流形，f 为全纯自同构，E⊂T^{1,0}X 为 C1 的 f-不变复子丛。记 Q=T^{1,0}X/E。

对局部 C1 截面 v∈E，定义

\[
\mathcal B_E(\bar w,v)
=(\bar\partial v)(\bar w)\pmod E.
\]

这个定义只依赖点上的 v 和 \bar w，给出连续张量

\[
\mathcal B_E\in
\operatorname{Hom}_{\mathbb C}
(\overline{T^{1,0}X}\otimes E,Q).
\]

它就是 Grassmann 截面的内蕴反全纯导数。E 全纯当且仅当 \mathcal B_E=0。

**命题。** 假设存在稠密周期点集 P_0，使每个 p∈P_0（周期 m）满足

\[
\operatorname{Spec}(A_Q)\cap
\left(\operatorname{Spec}(A_E)\,
\overline{\operatorname{Spec}(A)}\right)=\varnothing,
\quad A=Df_p^m.
\tag{1}
\]

则 E 全纯。

**证明。** 全纯链式法则和 E 的不变性给出

\[
A_Q\,\mathcal B_E
=\mathcal B_E(\bar A\otimes A_E)
\quad\text{于周期点 }p.
\tag{2}
\]

右侧表示先对两个输入施以 \bar A 与 A_E。算子 \bar A⊗A_E 的谱正是两个谱的乘积。由 (1)，它与 A_Q 的谱不相交，因此 (2) 的 intertwiner 必为零。这可由广义特征空间分解或 Sylvester 方程证明，不要求 A 可对角化。

所以 \mathcal B_E 在 P_0 上为零；连续性及稠密性给出其处处为零。Grassmann 全纯坐标下这是 C1 系数的 \bar\partial=0，故 E 全纯。证毕。

## 2. 对 Anosov 分布的准确形式

假设 E^s、E^u 为 C1。对周期回归导数 A，将稳定谱记为 S_p，不稳定谱记为 U_p。

要使 E^s 全纯，只需在稠密周期点集上没有关系

\[
\alpha=\beta\,\bar\gamma,
\qquad \alpha,\gamma\in U_p,\quad \beta\in S_p.
\tag{3}
\]

要使 E^u 全纯，只需没有

\[
\alpha=\beta\,\bar\gamma,
\qquad \alpha,\gamma\in S_p,\quad \beta\in U_p.
\tag{4}
\]

原因是同侧反全纯自变量的乘积模长已排除：两个稳定乘子的乘积不可能等于不稳定乘子；两个不稳定乘子的乘积也不可能等于稳定乘子。因此 (1) 只剩这些跨稳定、不稳定方向的混合共振。

这里是复特征值的精确等式，包含复共轭；不是只比较实 Lyapunov 指数。

## 3. 有环面拓扑时的分类

若 X 同胚于实环面，f 全纯 Anosov，E^s、E^u 为 C1，并且在一个稠密周期点集上 (3)、(4) 都不存在，则两侧全纯。接 Zhang 2026 Theorem 1.2，得到双全纯环面分类。

在已知环面拓扑的 Anosov 情形，Franks–Manning 共轭提供传递性和周期点稠密性。一般情形不能无条件假定它们。

## 4. 非全纯分布迫使大量周期共振

若 f 传递、周期点稠密，且 E 是 C1 不变复子丛但不全纯，则 \mathcal B_E 非零的点构成非空开集。由 (2) 的非周期版本及可逆性，该开集双向不变；传递性使其稠密。因此该开集内的周期点稠密于 X，而在每一个这些周期点上都必须发生 (1) 所排除的共振。

应用于两侧分布：一个非全纯的 C1 稳定/不稳定分布，迫使相应混合共振周期点稠密。

这个结论比“某一个周期点上存在共振”更强，但仍不等于识别出一个全局幂零 Lie 代数。

## 5. 边界与不能省略的假设

- 不能用本命题从 C0 分布直接推出全纯：此时 \mathcal B_E 还不是连续张量，周期点上的求值没有依据。
- 不能凭“非共振看起来一般”就说所有全纯 Anosov 都满足它；已有 nil 模型包含系统性的精确共振。
- 即使已证明无周期共振，也不能直接推出共轭双 Lipschitz；那是另一项正则性问题。
- 04 用 Lp 严格收缩从连续分布直接得到全纯；本文件改用 C1 正则性和周期谱信息。二者交换了不同的额外假设。

下一步真正需要的推广，是取得 C1 或更高正则性，同时允许非零共振张量，并研究其几何意义。
