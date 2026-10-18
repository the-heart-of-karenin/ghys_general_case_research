# 49–50：边界模型研究的文献与范围核验

日期：2026-10-18。此文件记录来源和有限新颖性检索，不代替证明。

## 1. 已完成的独立推导

- 49 穷尽 N 中正规化 P 任意正次幂的全部等距，得到二面体群；随后由 7、17 处判别群与简单超越 Hodge 结构的 cyclotomic 约束，精确缩为 ⟨g*⟩。再用已知忠实性得到实际正规化子 ⟨g⟩。没有假设超越 Hodge 自同态环为 Q。
- 50 证明双曲轴中 κ=14v₁−v₂+v₃ 为实际 ample 类；由此无周期曲线、除子，所有迭代固定点集有限。
- 50 的光滑周期 Lagrangian 曲面不存在性适用于全部该周期。关键不等式 12e≥11(e−4χ)² 与实际曲面动力学/法丛公式矛盾，而非再给稳定 K 理论添加必要数值。
- 只有非 Lagrangian 光滑曲面部分采用 End_HS(T)=Q 的 very general 选择；最终反证为无有理点的 U²+30V²=5。没有把这个条件宣称为 Anosov 的推论。
- 固定点的 Lefschetz 总量按局部交数计数。它不是已知的互异周期点数，不给周期乘子，不能直接当作 Anosov 排除。

## 2. 新增的唯一文献：第 41 篇

Keiji Oguiso, *No cohomologically trivial nontrivial automorphism of generalized Kummer manifolds*, Nagoya Mathematical Journal 239 (2020), 110–122；2018 年先在线发表。

- 出版社 DOI：https://doi.org/10.1017/nmj.2018.29
- 下载 PDF：https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0027763018000296
- 本地：41_Oguiso_2020_Cohomologically_trivial_automorphisms.pdf
- 13 页期刊排版；Theorem 5.1 在完整 PDF p.10（印刷页 119），明确给出任意 K3^[n] 型变形上 Aut→GL(H²) 忠实。
- 该文说明这一结果归于 Mongardi；不把它当作本轮新引理。
- PDF p.11 继续的是有限阶辛作用固定集 Proposition 5.2 的证明，是已查看背景页，不是 Theorem 5.1 的后半段，也没有用它推断无限阶 g 的固定集光滑。

## 3. 其他实际输入

- 37 Markman PDF p.21：射影超越 Hodge 等距群的有限性背景；49 已给独立正定度量证明。
- 38 Mongardi Proposition 2.12，PDF pp.7–8：K3^[2] 的精确墙列表，用于 κ 的 ample 性。
- 35 Cantat Introduction，PDF pp.2–3：正熵曲面的双有理分类。配合 Hodge 指数与 Noether 公式，得到 50 中的 χ∈{0,1,2}、e≥12χ。
- 21 O'Grady PDF p.17：c₂α²=30q(α)。Fujiki 四次归一化沿用 41 已核验的同文 pp.5–6；本轮不修改归一化。
- 24 Kapfer PDF p.6：H⁴_Q=Sym²H²_Q 的维数/有限指数输入；奇数上同调为零沿用 41 已核验的 PDF p.4。

本轮重新渲染并查看六篇来源的九个完整页，逐页用途和散列在 boundary_normalizer_source_audit.json；上面明确区分重复使用的既有输入与新查看页。

## 4. 实际检索的查询与结果

查询包括：

- hyperkahler automorphism not reversible normalizer cyclic positive entropy K3 Hilbert square
- "K3" "221" "automorphism"
- "hyperkähler" "centralizer" automorphism positive entropy
- "K3[n]" "faithful" automorphisms Beauville
- "hyperkähler" "normalizer" "entropy"
- "K3" "non-reversible" automorphism
- "K3" "reversible" automorphism entropy
- "Hilbert" "16" "Picard" "involutions" K3
- "hyperkähler" "periodic" "Lagrangian" "surface" entropy
- "hyperkähler" "commensurator" automorphism

找到的一手相关比较文献包括：

- Lee，*Automorphisms of the Hilbert square of a generic Cayley K3 surface*（2025），三 Beauville 对合及其自由积：https://doi.org/10.1080/00927872.2025.2507138 。本轮只读检索摘要，未用作证明输入。
- de Faria–Hutz，*Combinatorics of cycle lengths on Wehler K3 Surfaces over finite fields*，反转对称的相关背景：https://arxiv.org/abs/1309.6598 。仅比较主题，未用于复数域结论。
- Debarre，*Hyperkähler manifolds*，第 4 节的 Picard 数二自同构与 Pell 计算：https://perso.imj-prg.fr/wp-content/uploads/debarre-pub/HKmanifolds.pdf 。本轮只查看检索提要，没有下载或以其具体定理为证明输入。

未定位到与指定 Gram 矩阵、完整正规化子计算或 50 的指定周期曲面结论完全相同的陈述。但检索覆盖有限，部分查询噪声大；**不确认首创性**。循环中心化子的一般思想、Pell 描述、有限域 cyclotomic 规则与 Hodge 简单性均为标准工具，本轮完整计算的意义在于组合后真正穷尽此实际模型。

## 5. 不能越过的结论边界

1. 没有证明 g 为 Anosov 或非 Anosov。
2. 49 是完整正规化子计算，所以 46 的 Chern 类符号检验在此例不再缺少待找的正规化子；但更精细的等变丛或切导数约束仍可能存在。
3. 无周期曲面不是 Anosov 的矛盾；对 very general 代表，它反而说明不能依赖光滑周期 K3 的存在。
4. 不把孤立固定点当作横截固定点；不把带交数总量当作互异点数；没有计算实际周期乘子。
5. 不将法丛自交公式用于奇异周期曲面的解消；奇异曲面仍未排除。
6. 不宣称一般 Kähler 四维 Ghys 刚性已完成。下一步要研究该模型的 Anosov 性，需要新的导数或全局叶状输入；若目标是近期闭合另一刚性子类，应改变实例或聚焦具有实际周期子流形的情形。
