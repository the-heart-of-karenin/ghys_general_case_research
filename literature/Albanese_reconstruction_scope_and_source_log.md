# 71–73：Albanese 重构的外部输入、已知覆盖与未解决范围

日期：2026-10-18。仅核验新增输入，不重做此前全部文献审计。新增 PDF 61–62；现有 PDF 总数 62。它们是 ICM 会议论文及原作者预印本，不将二者冒称为新近审稿期刊成果。

## 1. 新增且实际使用的两个输入

### 61：Pink–Roessler，不变子簇

- [官方条目](https://arxiv.org/abs/math/0212408)，下载固定 v1；2002-12-01 arXiv 边注，ICM 2002, Vol. I, 539–546。
- Theorem 2.4，PDF 第 4 页；证明延续至第 5 页：特征零阿贝尔簇上的 endomorphism，若 Lie 代数上无单位根特征值，其不变闭子簇为阿贝尔子簇平移的有限并。
- 本文先独立用指定 H¹ 谱构造极化，证明 Albanese 实为阿贝尔簇，才应用它。没有直接将只述阿贝尔簇的定理用于任意非射影复环面。
- 仿射平移用线性部分 I−B 的 isogeny 消去，才使用群 endomorphism 版本。
- PDF 第 5 页 remark 将条件加强为“无代数单位”的替代证明不适用于本题，因为 λ 本身是单位；本文使用原 Theorem 2.4 的无单位根版本。
- 新查看完整页：1、4、5。

### 62：Catanese–Frediani，主环面丛的 complete Appell–Humbert 族

- [官方条目](https://arxiv.org/abs/math/0507508)，固定 v1；arXiv 边注 2005-07-25，首页正文日期 2005-05-18。日期差异保留。
- Theorem 3.6，PDF 第 11 页：任意固定扩张类的 principal holomorphic torus bundle 都在 complete Appell–Humbert family 中出现，不限于底维二、纤维维一。
- Proposition 3.7、Lemma 3.9、Corollary 3.10，PDF 第 12–13 页：对应实二步 nil 群上的不变可积复结构、Riemann bilinear relations 与 deck cocycle 的明确联系。
- 论文中的 Theorem 4.11 和一般大变形结论有特定维数限制；**没有**把它们用于本题的底维四、纤维维二。
- 完整参数 φ 不遗漏：它的中心常数 cocycle 可通过实线性中心 shear 搬回复结构，见 73 §1。
- Remark 3.8 明确指出反演一般不是同一不变复结构的自全纯映射。本文改写左右商时同时运输复结构，不反驳或忽略这一提醒。
- 新查看完整页：1、11、12、13。

七个完整页已渲染并视觉查看。散列、页数及查看记录见 Albanese_source_audit.json 与 Albanese_rendered_pages.json。

## 2. 复用的旧输入与严格分层

- 65 全局 H⁰ 不变性，仅用于 73 中已经重构为左不变 nil 结构后的 Ω，不用于未知 X。
- 来源 59（Wehler 2026，Theorem 2.1）的全局 holomorphic-map 仿射性：复用 nil_progression_source_audit.json 中第 3、12–16 页的已完成核验。**仅 73 的实际共轭出口使用这份新预印本。** 71 的一般 Albanese 结论与 72 的主丛定理不依赖它。
- 来源 58 的一般 nil Dolbeault/小变形主定理，本轮没有使用。
- 标准工具：一阶 de Rham 周期、Remmert proper mapping、Chow、Ehresmann、Hartogs、紧致复流形最大值原理及自由紧致复 Lie 群作用的商。72 对每个接口的实际假设逐项检查；未用参数 C¹ 分布或光滑拓扑共轭。

## 3. 哪些是已知机制，哪些是本轮组合

不变子簇平移性、主环面丛的 nil 描述以及来源 59 的仿射性为外部已知结论，不作为新发现。W⊕barW 的注入、闭形式对应交换辛向量场及 Hartogs 延拓本身也是标准机制。

本轮工作的完整组合是：指定 H¹ 谱强制 Albanese 的维数与极化；全纯等变性排除临界值除子；五次一阶杯积消失与 Ω 的正性迫使规则纤维各向同性；全局辛向量场、中心 π₁ 标记及 Hartogs 产生固定紧致环面作用；中心本原性排除稳定子，下降体积排除剩余 modification。这个组合在 dim W=4 下真正恢复主丛，而不预设它。

## 4. 有限新颖性检索

检索关键词包括 holomorphic Anosov / Albanese / closed holomorphic one-forms / nilmanifold / principal torus bundle / symplectic / Hartogs。

找到的相邻结果包括 Rollenske 2009 关于已给定左不变结构和大变形的工作，Fino–Grantcharov–Verbitsky 2016 关于已给定 complex nilmanifold 的 holomorphic differentials，以及带 ∂bar∂ 前提的 complex symplectic Albanese/local Torelli 理论。它们的“J 已左不变”或附加 Hodge 前提不能自动用于未知系统。除上述两个直接输入外，本轮未为这些比较项新增全文审计，也没有据摘要声称不存在等价定理。

未确认“05 底层流形、指定 H¹ 双曲作用、最大闭一形式 ⇒ 无奇异主环面丛”的已有完整出处。**首创性尚未确认。** 若对外整理，应继续集中核验这一具体定理的文献覆盖，而不是扩大一般关键词下载量。

## 5. 没有闭合的步骤

dim W=4 尚未由全部原始假设推出，连一般 dim W>0 都未证明。71 的 dim Alb∈{0,2,4} 没有排除前两种情形；非离散周期也不能忽略。原始系统的完整分类未解决。

73 的实际模型出口有清楚条件和外部输入；不得把它称为无条件解决 05 拓扑上的 Ghys 问题。其价值在于最大一阶分支的后续几何步骤不再是额外假设。
