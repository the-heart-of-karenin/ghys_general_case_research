# 43–45：保辛迭代、反辛正熵实现与 Anosov 排除的核验

日期：2026-10-18。本轮起点是去掉 41 的保全纯辛假设。没有继续叠加稳定 K 理论数值条件。

## 1. 已证明与未证明

- **43：** 对任意 K3^[2] 型、ρ=2、正熵自同构，X 自动射影，f*|T=±I，因此 f² 保辛。原 41 的光滑周期曲面非存在性及奇异周期曲面的必要条件全部成立，不再要求保辛或额外射影。
- **44：** 以 N=diag(58,−116) 和 M=[[3363,4756],[2378,3363]] 构造整数等距 A=M⊕(−I_T)。通过周期满射、无 Kähler 墙、Mon²=O⁺ 及强 Torelli，得到实际正则反辛正熵自同构；没有止步于形式 Hodge 格数据。
- **45：** 对 ρ=2 的 K3^[2] 型 X，如果存在反辛正熵自同构 g，则 X 不承认任何全纯 Anosov。实际导数的有限核交换误差迫使 g 保持任意假设 Anosov 的稳定丛，因而固定其非零 c₁；g 在 H² 上无固定类，矛盾。
- 没有排除所有保辛正熵分支，没有推出横向 C¹ 或体积为最大熵测度，没有处理全部奇异周期曲面。

## 2. 标准 Hodge 事实并非新结果

“奇秩简单 K3 型有理 Hodge 结构的等距只有 ±I”是标准事实。Huybrechts [39] 的作者稿 Proposition 3.11 证明，PDF p.22，明确使用该事实，并引用其 K3 讲义 Corollary 3.3.5。期刊版本对应 Proposition 3.12；当前保存作者稿 40 页，不混用两个版本的命题编号。

43 给出谱按倒数配对、非零有理 Hodge 核及简单性的独立证明。对非射影但 NS 非退化的情况，特别补写 q|R 的根空间为纯有理 (1,1) 的论证；没有假定 T^{1,1} 负定。NS 退化时另用 Lorentz 滤过，不将退化的 T 当成非退化简单结构。

任意射影 IHS 的超越格自同构像有限也为标准事实；43 用正定 Hodge 内积与格离散性直接证明。此处不主张新的 Hodge 理论。

## 3. 原始来源与实际用途

1. **18 Huybrechts 2003 erratum**，Theorem 2，PDF p.3：存在正 BBF 平方线丛当且仅当射影。本轮重新整页核验；用于 43 排除非射影分支及 44 的实际例子。
2. **39 Huybrechts 2017**，*The K3 category of a cubic fourfold*，Compositio Mathematica 153，DOI [10.1112/S0010437X16008137](https://doi.org/10.1112/S0010437X16008137)。只用于确认奇秩 Hodge 等距事实为既有内容，不借用范畴论作为证明黑箱。
3. **37 Markman 2011**，*A survey of Torelli and monodromy results for holomorphic-symplectic varieties*，Springer Proceedings in Mathematics 8，257–322，DOI [10.1007/978-3-642-20300-8_15](https://doi.org/10.1007/978-3-642-20300-8_15)。作者稿 46 页，arXiv v3，2011-12-18。PDF p.3 周期满射，p.4 Theorem 1.3(2)，p.32 Theorem 9.1、Lemma 9.2；后者明确允许 n=2，给出 Mon²=O⁺。用于 44 的实际正则自同构实现。
4. **38 Mongardi 2015**，*A note on the Kähler and Mori cones of hyperkähler manifolds*，Asian J. Math. 19，583–592，DOI [10.4310/AJM.2015.v19.n4.a1](https://doi.org/10.4310/AJM.2015.v19.n4.a1)。作者稿 9 页，arXiv v3，2014-03-25；Proposition 2.12 在 PDF pp.7–8，列出 K3^[2] 型的 −2、−10/div2 墙。44 因 N 全部平方为 58 的倍数而没有墙。
5. **21 O'Grady 2022、24 Kapfer 2016**，重新核验 c₂²=828、Betti 数及奇数次为零。45 只沿用一个基本结论：实际 Lagrangian 切分裂的稳定 c₁ 不为零。新增排除机制是实际切导数的等变性，不是更多指标数。

六篇实际使用来源、十个完整页的图像阅读记录及 SHA256 在 symplectic_power_source_audit.json。精确算术核验见 notes/symplectic_power_and_actual_example_checks.json；它不代替实际实现定理或导数证明。

## 4. 有限新颖性检索

代表性查询：

- projective hyperkähler / transcendental lattice / finite action / symplectic power；
- odd rank / Hodge isometry / ±id；
- Picard number two / anti-symplectic / positive entropy；
- holomorphic Anosov / anti-symplectic；
- Anosov / Picard / hyperkähler；
- Anosov / Chern / centralizer。

明确核验到：奇秩 Hodge 等距事实已知；非射影 NS 格的三种签名及相关熵/群结构属于经典 Oguiso 理论。43 提供所需特殊情形的独立证明，没有称作新分类。

没有检索到与 45 完全同一表述的原始定理，但这不确认首创性。有限核误差保持双曲分布是直接的导数估计；它可能是熟知的中心化子思想的推论。44 的格—Torelli 构造也采用标准方法，不凭参数选择声称新颖性。

## 5. 反检验与失败边界

- 反辛全纯 Anosov 在复环面上真实存在。45 给出 B=[[2,1],[1,0]] 的紧致例子；其稳定 c₁ 和所有切丛 Chern 数为零，不具有 IHS 数值矛盾。
- 反辛有限阶对合可以反转正熵映射，交换稳定、不稳定，从而只给 g*c₁=−c₁。不能省去 45 中 g 正熵的前提。
- 只构造 M∈O(NS) 不足以实际实现。44 逐项证明 A 的整数延拓、正三平面定向、monodromy 和 Kähler 锥保持，之后才调用强 Torelli。
- 不将 43 的平方保辛声明扩展到所有非射影 Picard 数二零熵情形；NS 退化时该 Hodge 简单性证明不适用。
- 41 的奇异 Lagrangian 曲面缺口没有因这些约化消失，42 的局部孤立锥面依然与所有当前结论相容。
