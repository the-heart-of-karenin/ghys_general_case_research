# 双 Lipschitz 到双全纯接口的核验

日期：2026-10-17。原始来源：J. Zhang, Invariant complex structures for affine automorphisms: a cocycle viewpoint, arXiv:2606.17794v1，Theorem A、§3.2、§3.4、Corollary D。

已阅读相关定理及证明段落。以下独立复核本研究实际需要的“混合 nil 仿射模型”情形；不另行使用论文中更一般的“遍历但不弱混合”的分支。

## 1. 输入与结论

输入：

- X 紧致复，f 全纯 Anosov；
- N 为实 infra-nilmanifold，A 为仿射 Anosov 自同构；
- h:X→N 是双 Lipschitz 同胚，且 hf=Ah。

结论：N 有复 infra-nilmanifold 结构，使同一个 h 双全纯，A 全纯仿射。

不额外要求 X Kähler、X 上保体积、两侧分布全纯或任何不可约性。

## 2. 先处理 nilmanifold

设 N=Γ\G。左不变标架使仿射 A 的导数表示为一个常实矩阵 D。仿射 nilmanifold Anosov 自动对 Haar 概率测度混合：在交换化环面上的线性部分无单位模特征值，使用 nil 自同构的标准遍历/混合判据。

双 Lipschitz 的 h 和 h^{-1} 几乎处处可微，并保持零测集。因此

\[
J'(h(x))=Dh_xJ_X(x)(Dh_x)^{-1}
\]

定义本质有界可测张量，满足 (J')²=−I，并由共轭及 f 全纯性满足

\[
J'(Ay)=D\,J'(y)D^{-1}
\quad\text{几乎处处}. \tag{1}
\]

## 3. 混合性迫使 J' 为常矩阵

将线性算子 L(B)=DBD^{-1} 复化后作广义特征空间分解。

由于 J' 本质有界，且 A 保 Haar，选 A 双向不变的满测集后，(1) 给出每条轨道上的 L^mJ' 在所有整数 m 下有统一界。

- 模长不等于 1 的广义特征分量为零；
- 单位模特征值中的非平凡 Jordan 部分也为零，否则出现多项式增长；
- 剩余每个标量系数满足 φ(Ay)=ρφ(y)，|ρ|=1。

混合性排除除常数以外的单位模 Koopman 特征函数，故只剩 ρ=1 的常数分量。因此 J'=J_0 几乎处处，其中 J_0 是左不变光滑概复结构，J_0²=−I。

到这一步尚未直接宣称 J_0 可积。

## 4. 可积性与 h 的光滑性

在 X 上取全纯坐标 φ:U→C^n，令

\[
\psi=\phi\circ h^{-1}:h(U)\longrightarrow\mathbb C^n.
\]

它是局部双 Lipschitz 映射，且

\[
D\psi\circ J_0=iD\psi
\quad\text{几乎处处}. \tag{2}
\]

对光滑概复结构 J_0，(2) 是具有单射主符号的过定椭圆一阶方程。对相应算子 P，P*P 是强椭圆二阶算子；弱解的椭圆正则性使 ψ 光滑。

双 Lipschitz 的下界在 ψ 已光滑后使 Dψ 处处单射，从而处处可逆。因此 ψ 为光滑坐标；坐标转移是原来 X 上的全纯坐标转移。故这些 ψ 是 J_0 的全纯坐标，J_0 可积，h 双全纯。

这没有对原本仅可测的 J' 直接套光滑 Newlander–Nirenberg 定理，而是先取得光滑 J_0，再用弱椭圆方程提升坐标。

## 5. infra-nil 有限覆盖的下降

选 A-不变的有限 nilmanifold 覆盖；可进一步取正规覆盖，使 deck 群为有限仿射群。沿 h 拉回得到 X 的对应有限覆盖。

提升 h 仍双 Lipschitz，提升 f 仍全纯 Anosov。nil 情形给出模型覆盖上的左不变可积复结构与双全纯提升共轭。

共轭将 X 覆盖的全纯 deck 群搬到模型上的原仿射 deck 群，所以所得复结构对其不变，下降为 N 的复 infra-nilmanifold 结构。原 h 因而双全纯。

## 6. 后续真正还缺什么

该接口本身没有留下需要在本研究中重新解决的主要缺口。一般分类仍缺：

1. 无预设拓扑时，为什么存在 infra-nil 仿射模型；
2. 为什么共轭能达到双 Lipschitz，而非只有 Hölder。

不能将任意 Anosov 的一般 Hölder 共轭代入上述推导：其导数不必几乎处处存在且可逆，h_*J_X 的本质有界性也无从得到。
