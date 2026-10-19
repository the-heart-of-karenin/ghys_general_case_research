# 六维模型：固定 Anosov 映射的精确变形族

日期：2026-10-18。性质：实际紧致模型的完整局部计算。固定映射的结果在本文闭合；同时改变映射的完整局部正规形在 62，独立一阶复核及范围在 63。

## 1. 模型与约定

沿用 05 §2 的 M=Γ\G，G=C⁶，实二步群乘法

\[
(x,y,z,a,b,c)(x',y',z',a',b',c')
=(x+x',y+y',z+z'+\bar x y',a+a',b+b',c+c'+\bar a b').
\]

格为 Γ={(r,s,t,σr,σs,σt):r,s,t∈Z[i,√3]}，σ 固定 i、交换 √3 与 −√3。令 λ=2+√3，固定格自同构

\[
F=(\lambda^2x,\lambda^{-1}y,\lambda z,
\lambda^{-2}a,\lambda b,\lambda^{-1}c).
\tag{1.1}
\]

这是 Zhang 原例（来源 01，PDF p.17）；群、格及紧致性已经在 05 逐项核验。下述辛形式与变形计算由本文直接验证，不将它们归为该页已陈述的结论。

原复结构 J₀ 的左不变 (1,0) 标架记为 X,Y,Z,A,B,C，其权重依次为

\[
w=(2,-1,1,-2,1,-1).
\]

复化括号除反对称项外仅有

\[
[\bar X,Y]=Z,\quad [X,\bar Y]=\bar Z,
\quad [\bar A,B]=C,\quad [A,\bar B]=\bar C.
\tag{1.2}
\]

对偶 (1,0) 标架为

\[
\alpha=dx,\quad\beta=dy,\quad\gamma=dz-\bar x\,dy,
\quad\delta=da,\quad\epsilon=db,\quad\zeta=dc-\bar a\,db.
\]

\[
d\gamma=\beta\wedge\bar\alpha,
\quad d\zeta=\epsilon\wedge\bar\delta,
\quad d\bar\gamma=-\alpha\wedge\bar\beta,
\quad d\bar\zeta=-\delta\wedge\bar\epsilon.
\tag{1.3}
\]

其他基本一形式均闭。取

\[
\Omega_0=\alpha\wedge\delta+\gamma\wedge\beta+\zeta\wedge\epsilon.
\tag{1.4}
\]

(1.3) 直接给出 dΩ₀=0，Ω₀³=6α∧β∧γ∧δ∧ε∧ζ≠0；每个加项的权重为零，故 F*Ω₀=Ω₀。

J₀ 是 abelian complex structure，即 [g¹⁰,g¹⁰]=0。它不是复平行化结构；不可套用只适用于复 Lie 群商的结论。

## 2. 为何固定 F 时不遗漏非左不变结构

60 §1–2 已证明：紧致连通仿射 Anosov nil 模型的每个连续不变张量都左不变。应用到 J 和 Ω 可知，任何 F 不变的光滑复结构及二形式都自动左不变。

因此以下有限维计算完整覆盖 J₀ 附近所有固定 F 的复结构，并非预设它们左不变后得到的一个子族。这里已经给定 F 的常系数左标架；不将这个论证用于未知流形上的变系数切导数。

## 3. 全部 F 不变可积复结构：六个复参数

用 graph 约定

\[
T^{0,1}_{J_\mu}=\{\bar V+\mu\bar V:\bar V\in T^{0,1}_{J_0}\}.
\]

μ 充分小时，它与其共轭图横截，给出真实几乎复结构。F 不变等价于 μ 仅有相同权重之间的矩阵项，所以全部十个参数可写成

\[
\begin{aligned}
U&=\bar X+\xi X, &V&=\bar A+\eta A,\\
P&=\bar Z+pZ+rB, &Q&=\bar B+qZ+sB,\\
R&=\bar Y+uY+vC, &S&=\bar C+wY+tC.
\end{aligned}
\tag{3.1}
\]

使用 (1.2)，不恒为零的括号仅有

\[
[U,R]=uZ+\xi\bar Z,\quad [U,S]=wZ,
\quad[V,P]=rC,\quad[V,Q]=sC+\eta\bar C.
\]

图与 T¹⁰₀ 横截，故纯 T¹⁰₀ 向量属于图当且仅当为零。先由中间两式得 r=w=0，再由另外两式得到

\[
\boxed{r=w=0,\qquad u=\xi p,\qquad s=\eta t.}
\tag{3.2}
\]

反过来这些条件也使所有括号封闭。因此全部可积结构由

\[
(\xi,\eta,p,q,v,t)\in\mathbb C^6
\tag{3.3}
\]

在原点附近光滑参数化。一组对偶新 (1,0) 形式为

\[
\begin{aligned}
\theta_1&=\alpha-\xi\bar\alpha,&
\theta_2&=\beta-\xi p\bar\beta,&
\theta_3&=\gamma-p\bar\gamma-q\bar\epsilon,\\
\theta_4&=\delta-\eta\bar\delta,&
\theta_5&=\epsilon-\eta t\bar\epsilon,&
\theta_6&=\zeta-v\bar\beta-t\bar\zeta.
\end{aligned}
\tag{3.4}
\]

每个 θᵢ 仍有权重 wᵢ。所有图系数对参数全纯，因而在 M×B 上取图分布加上 T⁰¹B，括号仍封闭，给出实际复解析族。这与 Rollenske 来源 56，PDF p.14 的图族构造一致。

一般成员不再是 abelian complex structure：例如 p=0 时仍有 [U,R]=ξ\bar Z。本文仅在中心 J₀ 使用 abelian 变形理论，不要求整个变形族保持这一性质。

## 4. 闭不变复辛形式精确切掉两个方向

任意 F 不变 (2,0) 形式只能配对相反权重，故唯一写成

\[
\Omega=K\theta_1\wedge\theta_4
+L\theta_3\wedge\theta_2
+M_s\theta_3\wedge\theta_6
+N\theta_5\wedge\theta_2
+O\theta_6\wedge\theta_5.
\tag{4.1}
\]

有

\[
\Omega^3=6K(LO+M_sN)\,
\theta_1\wedge\theta_2\wedge\theta_3\wedge\theta_4\wedge\theta_5\wedge\theta_6.
\tag{4.2}
\]

又

\[
d\theta_3=\beta\wedge\bar\alpha+p\alpha\wedge\bar\beta,
\quad d\theta_6=\epsilon\wedge\bar\delta+t\delta\wedge\bar\epsilon,
\]

其他 θᵢ 均闭。按旧 coframe (α,β,γ,δ,ε,ζ,\barα,…,\barζ) 展开 dΩ，三个特定分量为

\[
\begin{array}{c|c}
\text{基本三形式}&\text{系数}\\\hline
\beta\wedge\zeta\wedge\bar\alpha&-M_s\\
\alpha\wedge\beta\wedge\bar\beta&-Lp\\
\delta\wedge\epsilon\wedge\bar\epsilon&-Ot.
\end{array}
\tag{4.3}
\]

所以闭性先迫使 M_s=0，非退化性继而给出 KLO≠0，最后迫使 p=t=0。反过来这些条件充分，因为余下各项均闭。这甚至不必假设 Ω 接近 Ω₀；J 接近 J₀ 即足以使用本坐标。

## 5. 精确答案

**固定映射分类定理。** 在固定紧致 M、固定 F 上，J₀ 附近所有 F 不变、承认 F 不变闭全纯辛形式的复结构，恰由四个复参数

\[
(\xi,\eta,q,v)
\]

给出，其 (1,0) coframe 为

\[
\boxed{
\theta=(\alpha-\xi\bar\alpha,\ \beta,\ \gamma-q\bar\epsilon,
\ \delta-\eta\bar\delta,\ \epsilon,\ \zeta-v\bar\beta).
}
\tag{5.1}
\]

所有 F 不变闭全纯辛形式恰为

\[
\boxed{\Omega=K\theta_1\wedge\theta_4
+L\theta_3\wedge\theta_2
+N\theta_5\wedge\theta_2
+O\theta_6\wedge\theta_5,\quad KLO\ne0.}
\tag{5.2}
\]

接近指定三元组 (J₀,Ω₀,F) 的族因而有八个复参数，基点为 (ξ,η,q,v,K,L,N,O)=(0,0,0,0,1,1,0,1)。其中四个描述复结构，另四个描述所指定的辛形式；不将辛形式的改变都计为底层复流形的改变。

整个族在相同紧致光滑流形和相同格上实现，F 不变，所以它始终 Anosov，仍有原来的共振。闭 (2,0) 形式自动全纯；未另加 Kähler、pinching、非共振或体积假设。

F 的 expansivity 还说明：接近恒等且与 F 交换的 homeomorphism 只能为恒等。若 h 与 F 交换且 sup d(hx,x) 小于 expansivity 常数，则 d(Fⁿhx,Fⁿx) 对所有整数 n 均小于该常数，故 hx=x。因此本族中不同参数不能由接近恒等的三元组同构消掉。这里是标记局部参数，不讨论远离恒等的离散中心化子对全局参数的作用。

## 6. 核验与下一步

十参数 graph 括号、D₀/D₁ 秩、(4.2) 的系数及 (4.3) 的独立分量，已由精确有理数稀疏多项式外代数程序复核，见 check_six_dimensional_model_deformations.py 及同名 JSON 结果。程序不代替以上穷尽性证明或全局变形定理。

62 完成同时变化 f 的实际局部正规形。63 用全局 Dolbeault 理论独立复核一阶方向，并记录没有由此解决的全局问题及文献新颖性边界。
