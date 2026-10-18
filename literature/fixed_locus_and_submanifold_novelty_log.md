# 固定曲面路线：来源、适用范围和新颖性核验

日期：2026-10-18。对应独立证明 notes/39–40。

## 检索范围

本轮先复查 38 的周期影随缺口，再搜索真正使用实际切导数的周期子流形障碍。代表性查询为：

- holomorphic Anosov / hyperkahler / invariant symplectic submanifold;
- generalized or generalised Kummer fourfold / kernel Aut H2 / deformation / fixed K3;
- Anosov / Kummer type / involution / Hassett Tschinkel;
- Kummer fourfold / uniformly hyperbolic / holomorphic Anosov;
- invariant submanifold / Anosov / invariant measure / full support;
- quasi-Anosov / conservative restriction / holomorphic;
- Anosov / pluricanonical / invariant measure.

没有发现直接陈述“所有 Kummer 四维型流形不承认全纯 Anosov”的原始论文。许多命中讨论的是二维 Kummer K3 上从环面诱导的非均匀双曲自同构，或仅在稠密开集上的双曲性；这些并非四维 Kummer 型上的处处 Anosov。它们不支持本轮定理的首创性或否定。

一般满支撑回归引理与经典 quasi-Anosov 理论相通；多重典范密度是标准构造。未获得这些组合推论的首发表述。**结论可完整证明，与确认文献首创是两件事：本轮前者已完成，后者未完成。**

## 实际使用的原始输入

1. Hassett–Tschinkel, Hodge theory and Lagrangian planes on generalized Kummer fourfolds, Moscow Math. J. 13 (2013), 33–56, DOI 10.17323/1609-4514-2013-13-1-33-56。保存为 32，作者托管稿日期 2012-06-11。使用 Theorem 2.1、Proposition 3.1：H²-平凡自同构的群及其实际作用沿整个变形类型延续。全文 §2 明确允许非射影 Kähler IHS。PDF pp.3–6 已整页渲染、阅读。
2. Kapfer–Menet 2018（既有 29），Corollary 7.1、Theorem 7.5：自然核群的精确描述，以及任意 Kummer 四维型上的辛对合固定一张 K3 曲面和 36 个孤立点。PDF pp.27–30 已整页渲染、阅读。
3. Ghys 1995（历史文献 01），Theorem A：全纯 Anosov 紧复曲面是复二维环面。PDF p.1 已重新整页检查。

本轮没有用新的 Chern 数或指标排除候选，也未把 K 理论中的等式当作实际子丛。39 不依赖 36–37 的拓扑存在判据，故即使独立复核拓扑步骤，39 的证明也不受影响。

## 两处材料不一致的处理

- 29 的 PDF p.27 说明句写出 (Z/3)³，而同页正式推论是 A[3]⋊⟨−1⟩；32 pp.5–6 的定义也是 (Z/3)⁴。39 使用正式推论，且只需要有限性和存在对合。
- 32 作者稿 Theorem 4.4(1) 的孤立点描述不完整。29 Theorem 7.5 和 Remark 7.7(2) 明确给出 36 点，并逐项说明另外的 35 点。39 不使用 32 的该固定点计数；固定曲面采用 29 的正式定理。

## 自行闭合的步骤

- 39：有限群的共轭作用取幂后平凡；固定曲面上的平均微分是等变幂等元；它保环境稳定/不稳定子丛，所以限制确为 Anosov。这个链式法则步骤不适用于一个任意抽象 cocycle。
- 40：不变子空间的混合部分给出商空间同构 L；稳定/不稳定分离迫使 ||L(Fx)||≥r⁻²||L(x)||。有界严格单调函数与不变测度矛盾；满支撑及连续性把几乎处处分裂变成全局分裂。多重典范特征截面提供满支撑不变测度。
- 模型检验：E⁴ 上同时存在周期辛环面和周期 Lagrangian 环面，说明不能排除一切周期曲面；CP¹ 上的常值保辛双曲 cocycle 带有混合全纯线子丛，说明紧致全纯本身不替代回归。后者不是切导数模型。

来源身份、SHA256 与九个完整页的检查记录见 fixed_locus_and_submanifold_source_audit.json。检索摘要只作线索，不作数学证明输入。
