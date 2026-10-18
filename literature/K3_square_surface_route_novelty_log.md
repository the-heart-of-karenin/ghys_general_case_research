# K3^[2] 型周期曲面：来源、适用边界与有限新颖性检索

日期：2026-10-18。对应独立证明 notes/41–42。原始文献不与独立笔记混放。

**后续修订：** 本文保留 41 初版的来源比较。43 已证明原来的保辛和额外射影前提都可删除，并已更新 41 的正式陈述；44–45 又完成实际反辛正熵实现及其所在 X 上全部 Anosov 的排除。最新核验见 symplectic_power_and_antisymplectic_novelty_log.md。原 41 的文献首创性仍未确认。

## 1. 本轮结果的准确身份

41 独立证明了一个几何动力学定理：射影 K3^[2] 型、Picard 数二、保全纯辛且正熵的自同构没有光滑周期复曲面。证明不使用 Anosov，也不使用 very general 假设。它说明一般正熵几何不能普遍提供光滑周期 K3；它没有排除该类型上的 Anosov。

42 从已知辛对合固定 K3 定理得到有限共轭轨道排除准则，并给出 ρ≥9 / ρ≥10 的适用边界。孤立 Lagrangian Veronese 锥面是显式局部反检验模型，不是紧致反例。

上述证明是否已在别处发表仍未确认。有限检索没有命中同一完整表述，不足以确认首创性。

## 2. 实际阅读的原始来源

1. **33 Mongardi**，*Symplectic involutions on deformations of K3^[2]*，Central European Journal of Mathematics 10 (2012), 1472–1485，DOI [10.2478/s11533-012-0073-z](https://doi.org/10.2478/s11533-012-0073-z)。Theorem 4.1：固定一张 K3 和 28 点；Theorem 5.2：反不变格 E₈(−2)；Lemma 3.4 的证明提供最小超越 Hodge 结构方法。实际下载稿 17 页，边注为 arXiv v3、2012-05-09，而标题页日期为 2021-03-08；已记录这一版本差别，不把它当期刊原始排版。41 的保辛无限阶 f 在 T 上恒等由核的 Hodge 论证重新证明，没有套用只针对有限群的引理。
2. **34 Amerik–Verbitsky**，*Construction of automorphisms of hyperkähler manifolds*，Compositio Mathematica 153 (2017)，DOI [10.1112/S0010437X17007138](https://doi.org/10.1112/S0010437X17007138)。Theorem 1.1、Corollary 3.7：每个 b₂≥5 的 IHS 变形类型都有射影、Picard 数二且带保辛双曲自同构的变形。作者稿版本 2016-04-08。用来保证 41 的假设确有实际例子；这些例子没有被称为 Anosov。
3. **35 Cantat**，*Dynamique des automorphismes des surfaces K3*，Acta Mathematica 187 (2001), 1–57，DOI [10.1007/BF02392831](https://doi.org/10.1007/BF02392831)。引言 PDF pp.2–3 回顾正熵曲面分类，推出 χ(O)≤2。使用期刊原始 PDF；没有使用其最大熵测度定理作为任意 Anosov 的输入。
4. **24 Kapfer**，*Computing cup products in integral cohomology of Hilbert schemes of points on K3 surfaces*，LMS Journal of Computation and Mathematics 19 (2016)，DOI [10.1112/S1461157016000012](https://doi.org/10.1112/S1461157016000012)。PDF pp.4、6：奇数上同调为零，b₂=23、b₄=276，Sym²H²→H⁴ 有有限指数。41 只使用其有理同构，不误认整数杯积满射。
5. **21 O'Grady**，*Modular sheaves on hyperkähler varieties*，Algebraic Geometry 9 (2022)，DOI [10.14231/AG-2022-001](https://doi.org/10.14231/AG-2022-001)。PDF pp.5–6、17：标准 Fujiki 归一化、K3^[2] 的归一化常数 1，以及 ∫c₂x²=30q(x)。本轮只为 41 中被动力学压缩到一维的实际周期曲面类计算，不再为任意连续子丛堆叠数值障碍。

Ghys 曲面定理及固定子流形实际切投影沿用 39 已核验的历史来源和证明，没有新增未经说明的限制 Anosov 原理。

## 3. 最接近的周期子簇文献及其不能覆盖的步骤

新增 **36 Lesieutre–Satriano**，*Canonical Heights on Hyper-Kähler Varieties and the Kawaguchi–Silverman Conjecture*，IMRN 2021, no.10，DOI [10.1093/imrn/rnz067](https://doi.org/10.1093/imrn/rnz067)。保存的是 2019 年 online-first 期刊 PDF，38 页。完整阅读、渲染 PDF pp.15–17 的 Theorem 2.21、Remark 2.22、Corollary 2.23、Example 2.24。

这一比较来源给出周期子簇与两个 nef 特征类之和的增广基点集之间的判据；Picard 数二时该和为 ample。它与 41 的“没有奇数维周期子簇、曲面限制有正熵”的基本现象相容，但没有在所核验部分排除所有光滑偶数维周期曲面。其自然 Hilbert scheme 例子确有很多偶数维周期子簇；对应底 K3 有正熵时，Hilbert 平方的 Picard 数至少三，不满足 41 的秩二前提。41 的非 Lagrangian Hodge 维数矛盾及 Lagrangian 一维类—正常丛—χ 矛盾没有被这里的周期子簇判据直接替代。

36 的算术部分总体工作在 Qbar 上；本轮没有把它擅自套到任意复数域的 X。41 的证明独立在 C 上成立，36 仅用作新颖性比较和寻找冲突，不作其证明输入。

## 4. 有限检索范围

代表性检索：

- K3^[2] / hyperkähler / holomorphic Anosov / symplectic involution / periodic K3 surface；
- Picard number two / positive entropy / periodic surfaces / periodic subvarieties；
- smooth periodic surfaces / Lagrangian / Euler characteristic / positive entropy；
- K3^[2] / symplectic involution / E8(-2) / finite conjugacy orbit。

只采用作者、期刊或论文的原始页面作为数学来源。检索中的非数学 Lagrangian 噪声、非原始转载与只谈 birational maps 的结果没有进入证明。最接近且逐页检查的是上述 36；没有由“未搜到”宣称一个已确认的新定理。

## 5. 尚未闭合的内容

- 未从 Anosov 本身推出周期光滑曲面、周期奇异曲面或辛对合有限共轭轨道的存在。
- 未排除 41 剩下的孤立奇点 Lagrangian 曲面；不能把其解消切丛嵌入 TX，也不能把光滑正常丛等式套到解消。
- 42 的局部正规锥面说明双曲辛周期点与孤立 Lagrangian 奇点相容；尚未得到紧致性带来的新矛盾。
- 未获得无 pinching 的横向 C¹、体积熵等号或任意 K3^[2] 型的 Ghys 分类。

17 个完整页的渲染与阅读记录、文件 SHA256 见 K3_square_surface_source_audit.json。独立公式和局部模型的精确核验在 notes/rank_two_periodic_surface_checks.json；它们不替代 41 的证明。
