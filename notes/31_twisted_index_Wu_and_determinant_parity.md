# 扭曲指标、Wu 公式与稳定丛行列式的奇偶性

日期：2026-10-18。接续 28。范围仍为 Kähler 保全纯辛四维 Anosov 的 IHS 剩余分支。本轮主结论仅用连续复 Lagrangian 分裂；不需要 C1，也不把连续丛当成全纯丛。不宣称新颖性。

## 1. 结论

令 E=E^s，a=c_1(E)，b=c_2(E)。在两个标准变形类型中，除 28 的 BBF 平方条件外，必须有

\[
q(a,\alpha)\in2\mathbf Z\quad\text{对每个 }\alpha\in H^2(X,\mathbf Z).
\tag{1}
\]

在标准格标记 L=L_0⊕Zδ 下，L_0 为偶幺模格，K3^[2] 型的 q(δ)=−2，Kummer 四维型的 q(δ)=−6。进一步有

\[
\boxed{a\equiv\delta\pmod{2L}.}
\tag{2}
\]

精确必要条件如下。

| 变形类型 | q(a) | a 的原始性与格整除度 div(a)=gcd q(a,L) |
|---|---|---|
| K3^[2] | 6 或 −26 | a 原始，div(a)=2 |
| Kummer 四维 | −6 | a 原始，div(a)=2 或 6 |

这排除了 28 中“只检验平方值”的一部分格向量，但尚未排除所有候选。

## 2. 拓扑指标的完整公式

记 c=c_2(X)，e=∫_Xc_4(X)。28 给出

\[
2b=c+a^2,\qquad b^2=c_4(X).
\]

对于任意整数类 α，取**拓扑**复线丛 M_α，c_1(M_α)=α。连续向量丛可在同构类内光滑化，故 Atiyah–Singer 指标定理适用：

\[
I_\alpha:=\int_X\mathrm{ch}(E)e^\alpha\mathrm{Td}(TX)\in\mathbf Z.
\tag{3}
\]

这是扭曲 Spin^c / Dolbeault 符号的拓扑指标。**不写成 holomorphic χ(E⊗M_α)**，因为两个丛都没有被证明全纯。

由 rank(E)=2，

\[
\begin{aligned}
\mathrm{ch}_0(E)&=2,&\mathrm{ch}_1(E)&=a,\\
\mathrm{ch}_2(E)&=-c/2,&
\mathrm{ch}_3(E)&=-a^3/12-ac/4,\\
\mathrm{ch}_4(E)&=(-a^4-2a^2c+2c_4(X))/24.
\end{aligned}
\]

再用 χ(O_X)=3 以及 Td_2=c/12，得到

\[
\boxed{
I_\alpha=6-\frac e{12}
+\int_X\left(\frac{\alpha^4}{12}
+\frac{a\alpha^3}{6}
-\frac{c\alpha^2}{6}
-\frac{a^3\alpha}{12}
-\frac{ca\alpha}{6}\right).}
\tag{4}
\]

特别地，I_0=6−e/12 为整数。这一公式只涉及可定义的拓扑类。

设 t=q(a)，u=q(α)，v=q(a,α)。Fujiki 公式的极化给出：K3^[2] 型 ∫aα³=3uv、∫a³α=3tv；Kummer 型对应常数为 9。结合 28 已核验的 c 交数：

**K3^[2]：**

\[
I_\alpha=-21+\frac{u^2}{4}-5u
+\frac{(2u-t-20)v}{4}.
\tag{5}
\]

q 是偶格，所以 u 偶，前面三项为整数；t=6、−26 时，最后一项的系数均为半整数且不是整数。故 v 必偶。

**Kummer 四维：** t=−6，

\[
I_\alpha=-3+\frac{3u^2}{4}-9u
+\frac{(3u-9)v}{2}.
\tag{6}
\]

u 偶，所以最后的系数仍为严格半整数。故 v 必偶。证明了 (1)。

## 3. 独立的 Steenrod–Wu 检验

同一结论也可不经 (3)，改用 rank 二复丛的关系

\[
\mathrm{Sq}^2\rho_2(b)=\rho_2(ab),
\tag{7}
\]

其中 c_3(E)=0。X 是 spin，w_2(X)=0。对任意 α，Wu 公式与 Cartan 公式给出

\[
0=\langle\mathrm{Sq}^2\rho_2(b\alpha),[X]\rangle
=\int_X(b\alpha^2+ab\alpha)\pmod2.
\tag{8}
\]

这里 Sq¹ 对整数类的 mod 2 约化为零，Sq²ρ_2(α)=ρ_2(α²)。将 b=(c+a²)/2 代入并极化 Fujiki 公式，(8) 左侧的整数分别为：

\[
\begin{array}{c|c}
\text{K3}^{[2]},\ t=6 &18u+v^2+24v\\
\text{K3}^{[2]},\ t=-26 &2u+v^2-24v\\
\text{Kummer},\ t=-6 &18u+3v^2
\end{array}
\]

三者 mod 2 都为 v，故也得到 (1)。这次推导并不假设 b 的某种额外整除性；b 本来就是 E 的整数 Chern 类。

## 4. 从配对偶性到确定的模 2 类

将 a 写作 a=a_0+kδ。由 L_0 幺模及 (1)，a_0=2β，β∈L_0。因为 L_0 偶，

\[
q(a)=4q(\beta)-2d k^2\equiv-2d k^2\pmod8,
\quad d=1\text{ 或 }3.
\]

K3^[2] 的两个 t 均为 6 mod 8，故 k 奇；Kummer 的 t=−6≡2 mod 8 也强迫 k 奇。这证明 (2)。它同时说明 a 在 H² 中不是二倍类。

三个平方值没有大于 1 的平方因子，因此 a 原始。原始向量的整除度在 K3^[2] 格中只能整除 2，在 Kummer 格中只能整除 6；结合 (1)，得到表中的整除度。

## 5. 还活着的候选与不能跳过的步骤

在一个双曲平面 U=Ze⊕Zf、q(e,f)=1 中，以下原始向量均满足本轮和 28 的数值与同余条件：

\[
\begin{array}{c|c|c}
\text{类型}&a&q(a)\\
\text{K3}^{[2]}&2e+2f+\delta&6\\
\text{K3}^{[2]}&2e-6f+\delta&-26\\
\text{Kummer}&\delta&-6.
\end{array}
\]

这只是格数据，不是已经构造了 E，更不是 Anosov 实例。

28 曾用 e+3f、e−13f 说明平方值可以在格中表示。这两个例子 div=1，**现在已被 (1) 排除**；上述三个向量才是更强检验后的候选。

仍未证明 a 为 Hodge (1,1) 类或为挠类。a 不为二倍类，反而说明不能随意取 det(E) 的平方根并套用 SU(2) 指标的偶性。

## 6. 文献范围与下一步

- 23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf：Corollary 2.3，PDF p.4，核对 (7)；§3，PDF pp.5–6，核对任意连续/光滑复丛的 Spin^c 指标整数性。
- 21、22 中的 Fujiki 与 Chern 交数沿用 28；本轮未增加新的正则性输入。
- 同一篇 23 的 Corollary 8.4 要求 ρ_2(c_1(λ))=w_2(X)。本轮 a≡δ≠0 mod 2，而 w_2(X)=0，**不能将 λ=det(E) 直接代入其 mod 12 判据**。无视这个条件会制造虚假的不存在证明。

本轮已取得 (1)、(2) 的无 C1 必要条件；尚需考察完整整数上同调和稳定 K 理论是否排除剩余向量，见 32；动力学不变性本身能否补齐缺口，见 33。
