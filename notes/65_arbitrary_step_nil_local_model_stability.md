# 任意步数的局部模型稳定性：撤去二步与 abelian 预设

日期：2026-10-18。性质：完成 64 的高步推广及非 abelian 基点接口。只检查新增步骤，不重做 61–63 的全部核验。重要文献更新：来源 59（Wehler 2026，Theorem 2.1）已有任意复 nilmanifold 间全纯映射的全局仿射性；因此本文的小映射结论在 nil 类别中不是未有文献覆盖的结论。以下保留一个独立的椭圆证明，作为后续闭性论证的局部输入。

## 1. 全局全纯向量场的左不变性自动成立

**引理 1。** 对任意紧致 nilmanifold M=Γ\G 及任意左不变可积 J，全部全局全纯向量场都左不变。不要求 J abelian、有理或幂零型复结构，也不要求 G 二步。

证明。令 h=g⁰¹⊂g_C，E=g_C/h≅g¹⁰。h 通过

\[
\rho(\bar X)[Y]=[\bar X,Y]\bmod h
\]

作用于 E。每个 ad_\barX 在幂零 Lie 代数 g_C 上为幂零算子，h 对它不变，故 ρ(\barX) 在 E 上仍幂零。Engel 定理给出基 e₁,…,eₙ，使

\[
\bar\partial e_j\in
\Lambda^{0,1}\mathfrak g^*\otimes\langle e_1,\ldots,e_{j-1}\rangle.
\tag{1.1}
\]

若 V=∑f_j e_j 全纯，最高分量给出 bar∂fₙ=0，所以 fₙ 常值。归纳假定 j>k 的 f_j 均常值，则 bar∂f_k 为常系数不变 (0,1) 形式。在任意左不变 \barX 上积分，Haar 体积下 ∫\barX(f_k)=0，迫使该常系数形式为零。于是 f_k 全纯，仍常值。归纳完毕。

同一论证适用于由 g¹⁰ 及其对偶的张量运算构成的任意全纯张量丛：对应的 h 表示仍严格三角化。因此任意全局全纯 (p,0) 形式亦左不变。此处是全局截面结论，不是任意 Dolbeault 高阶群的计算。证毕。

## 2. 去平均位移：有限维隐函数代替二步公式

对小映射 h(x)=x exp u(x)，记 P 为 Haar 系数平均。设

\[
\mathcal B(u,a)=P\log(\exp u(x)\exp(-a)).
\]

在 u=0,a=0 处，D_a B=−I，D_u B=P。取整数 s>dim_R M/2+1；B 是 H^{s+1}(M,g)×g 到 g 的光滑映射。有限维未知量 a 的带 Banach 参数隐函数定理给出唯一小解 a=a(u)，满足

\[
\mathcal B(u,a(u))=0,
\quad |a(u)|\le C\|u\|_{H^{s+1}},
\quad a(u)=Pu+O(\|u\|_{H^{s+1}}^2).
\tag{2.1}
\]

令 b=exp a、k=R_b⁻¹h=x exp w(x)，则 Pw=0，且

\[
\|w\|_{H^{s+1}}\le C\|u\|_{H^{s+1}}.
\tag{2.2}
\]

这些是实际小函数的估计。一般三步情形不能直接令 a=Pu；68 的 UT₄ 反检验给出非零三阶平均残量。

## 3. 所有高阶项仍有二次控制

若 G 为 r 步幂零群，Dk 在左标架中精确为

\[
H_w=e^{-\operatorname{ad}w}
+\left(\sum_{j\ge0}\frac{(-1)^j}{(j+1)!}(\operatorname{ad}w)^j\right)\partial w.
\tag{3.1}
\]

两项都因幂零性截断。分离

\[
H_w=I+L(w)+Q(w),\qquad L(w)=\partial w-\operatorname{ad}w,
\]

则

\[
Q(w)=\sum_{j\ge2}\frac{(-1)^j}{j!}(\operatorname{ad}w)^j
+\sum_{j\ge1}\frac{(-1)^j}{(j+1)!}(\operatorname{ad}w)^j\partial w.
\tag{3.2}
\]

每个加项至少含两个 w 或 ∂w 因子，且没有二阶空间导数。Sobolev 乘法直接给出，在一个固定的小球内

\[
\|L(w)\|_{H^s}\le C\|w\|_{H^{s+1}},
\qquad\|Q(w)\|_{H^s}\le C\|w\|_{H^{s+1}}^2.
\tag{3.3}
\]

由 unimodularity，Pw=0 仍精确推出 PL(w)=0。高步并没有为线性项产生未控制的平均误差。

## 4. 任意步数的小映射定理

**定理 2。** 任意紧致 nilmanifold 上，固定左不变可积 J₀。存在 J₀ 的左不变结构邻域和 Id 的 Diff∞ 邻域，使邻域中任何双全纯映射 h:(M,J₁)→(M,J₂) 都为右平移。

证明沿用 62 的 K₀w=[J₀,L(w)]。引理 1 说明其核全部为常系数；故 Pw=0 时，椭圆估计

\[
\|w\|_{H^{s+1}}\le C_0\|K_0w\|_{H^s}
\]

适用。对 J₂H_w=H_wJ₁ 作 I−P 投影，仍得到 62 (3.6) 的精确方程。利用 (3.3)，有

\[
\|w\|_{H^{s+1}}
\le C(\|J_1-J_0\|+\|J_2-J_0\|+\|w\|_{H^{s+1}})
\|w\|_{H^{s+1}}.
\]

小邻域内吸收即得 w=0。所有新增高阶项已由 (3.2)–(3.3) 处理；没有形式级数收敛假设。证毕。

## 5. 一般仿射局部模型定理

设 F(g)=aΦ(g) 在 Γ\G 上给出仿射 Anosov，A=dΦ_e 双曲，J₀ 左不变且由 F 保持。假设 J₀ 具有左不变的带标记完备小变形族，记此已知几何性质为 D。

**定理 3。** (J₀,F) 的每个充分小全纯变形 (J,f) 都可用一个小光滑 h 化为 (J',F)，其中 J' 左不变。小 h 唯一。若还有 f 不变闭全纯辛 Ω，h*Ω 也左不变。

证明：由 D 先选小 χ，使 J₁=χ*J 左不变。g=F⁻¹χ⁻¹fχ 是两种附近左不变结构之间的小双全纯映射，故 g=R_b。选小 c 解

\[
\Phi(c)\Phi(b)=c.
\tag{5.1}
\]

对 c 的微分是 A−I，可逆。直接得到

\[
R_c^{-1}(F\circ R_b)R_c(g)
=a\Phi(g)\Phi(c)\Phi(b)c^{-1}=F(g).
\]

取 h=χR_c。唯一性仍由 expansivity；Ω 左不变由引理 1 或 60 得到。

注意左商下降条件为 aΦ(Γ)a⁻¹=Γ。以上未假设 Φ 单独保持 Γ；也未将仿射 F(c) 错用为 (5.1) 中的 Φ(c)。

## 6. D 的确切来源与文献分层

- **旧文献层：** 来源 56，Theorem 2.4、Corollary 2.5、Theorem 2.6，给出 abelian、Γ-rational、complex parallelisable 和所列迭代主全纯环面丛等类别的 D。因此上述推广已用旧定理覆盖真正非 abelian 基点及任意幂零步数，不只是条件性模板。
- **2026 新预印本层：** 来源 58（Hasegawa–Sillari–Tomassini），Theorems 7.1–7.2 及 PDF p.16 的证明，声称并证明全部 compact complex nilmanifold 都满足所需 Dolbeault 比较，从而给出 D。采用这个外部定理时，定理 3 对任意左不变 J₀ 成立；本文没有独立重证其一般 Dolbeault 主定理。
- **重叠的已知结果：** 来源 59 的 Theorem 2.1 已将任意 nilmanifold 间全纯映射全局化为 R_b∘Φ，比定理 2 更强。本轮不再将定理 2 的结论作为待认领的新颖性；这里只保留不依赖 2026 统一化结果的分析证明。

后续真正的动力学内容在 66：由二阶上同调控制辛形式与复结构，证明模型化集合在保全纯辛 Anosov 空间中的闭性。这一步不使用来源 58 或 59 的新定理。
