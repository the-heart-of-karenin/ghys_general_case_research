# 实际 Lagrangian 子丛：来源与有范围的新颖性核验

日期：2026-10-18。独立证明见 notes/36–38；本文件仅记录外部材料的范围。检索结果页、摘要及自动聚合内容均不作为证明输入。未声称检索能够证明首创。

## 1. 检索的具体问题

本轮优先查找 Sp(2)→U(2) 的实际 reduction、八维流形上的非特征行列式秩二丛、KSp 忘却核和标准 IHS 的 Steenrod 运算。没有联网搜索最近 Ghys 猜想的证明。

代表性查询（同义词及拼写变体合并列出）：

- rank two complex bundles eight dimensional manifolds c1 not w2 obstruction;
- complex rank three bundle nowhere-zero section / stable Euler / normal bordism;
- Crabb Steer vector-bundle monomorphisms with finite singularities;
- Paechter V5,2 homotopy / Sp(2) U(2) oriented two-plane;
- KSp / KO Atiyah-Hirzebruch d2 Sq2 / Thom twist;
- K3 Hilbert square tangent splitting / continuous Lagrangian subbundle;
- hyperkahler topological polarization / Lagrangian distribution;
- K3 Lagrangian bundle 6 −26;
- generalized or generalised Kummer fourfold Steenrod squares / Sq2 / odd cohomology;
- integral cohomology Kummer fourfold corrigendum;
- nested Hilbert universal family ramification.

多轮检索返回许多 Lagrangian 子流形、全纯纤维化、EPW 外幂丛或代数模空间的结果；其对象并非 TX 上处处定义的连续复 Lagrangian 子丛，没有用这些命中声称本问题已解决或已有反例。未把非原始聚合网页中的数学陈述作为事实引用。

## 2. 新增保存的原始材料及实际用途

| 编号 | 原始材料 | 使用情况 |
|---|---|---|
| 25 | Sadovek–Schutte, Complex line fields on almost-complex manifolds, Math. Ann. 395, 46 (2026), published 30 April | 检查一般 line-field lifting 工作的范围；其 m 偶数的两个线丛定理带有额外 Sq²/非 spin 条件，不能直接解决当前 spin 八维情形。未作为 36–37 的降秩充分性输入 |
| 26 | Čadek–Crabb–Vanžura, Quaternionic structures, Topology Appl. 157 (2010) | 查询 twisted quaternionic 理论背景；没有据此把稳定丛当成实际子丛。未作为最终判据的新输入 |
| 27 | Klein–Williams, Homotopical intersection theory I, Geom. Topol. 11 (2007), 939–977 | Corollary 3.5 给出 S⁵ 球丛的稳定 Euler 完备范围；Theorem 4.1 给出对偶 |
| 28 | Zibrowius, Witt groups of complex cellular varieties, Doc. Math. 16 (2011), 465–511 | 仅用其通用 KO d₂ 与 Thom 公式；没有假设 IHS 是 cellular variety |
| 29 | Kapfer–Menet, Integral cohomology of the generalized Kummer fourfold, Algebr. Geom. 5 (2018), 523–567 | 整数 H³/H⁵ 对偶基、c₂、H⁴ 饱和格、平方类的二次整除判别 |
| 30 | 同作者 Corrigendum, Algebr. Geom. 7 (2020), 482–485；本地为 2019 author preprint | 必须搭配 29 使用：修正整数上同调无挠的原参考文献缺陷 |
| 31 | Meachan, Derived autoequivalences of generalised Kummer varieties, Math. Res. Lett. 22 (2015) | §2 的 nested Hilbert 对应、通用族分解、吹起描述及 canonical divisor |

沿用 21–24 的 Fujiki/Chern、秩四 realization、K3 Hilbert scheme 整数基。所有 PDF 独立存放在 literature/，下载 URL、版本、SHA256、页数保存在 sources_manifest.json。实际引用的完整定理页已渲染并检查；不是只读搜索摘要。

## 3. 独立推导和已知工具的分界

以下为既有标准输入，不宣称原创：稳定 Euler 完备性、球谱到 ko 的低维比较、KO AHSS 的 d₂、Thom–Gysin 公式、已发表的整数上同调基、Sp(2) 的稳定 cancellation。

notes/36 展开非特征秩六丛截面引理，并计算 K3^[2] 的平方映射及 KSp 忘却单射；notes/37 利用分歧除子推导 Sq²(p_i)=v_i，再以整数对偶基和 Wu 公式证明 Sq²:H³→H⁵ 为同构。这些步骤组合起来给出实际复 Lagrangian 子丛的必要充分判据。

定向检索中未发现直接陈述这两条必要充分判据、或直接陈述 37 中奇数 Steenrod 同构的原始文献。不过，证明可能是已有一般障碍理论的未专门发表的推论；也可能有未被本轮检索覆盖的文献。因此状态为：**已写出独立完整证明稿；同一结论未检出；文献新颖性尚未确认。**

notes/38 的无复切线场是基本最高 Chern 类障碍的特化；每个时间的精确共形点是其有限维谱论推论。不能将这种直接推论的检索未命中解释成已证明首创。

## 4. 没有使用的捷径

- [23] Corollary 8.4 的 characteristic determinant 假设在当前不满足；未套用。
- 25 的两个线丛充分性条件不能直接套在 spin 八维 IHS 上；未套用。
- 32 的复 K⁰ 相等不直接推出 Lagrangian 子丛；先作真实降秩，再用 KSp 忘却单射及实际 cancellation。
- 29 的无挠原引文有错误；改用 30 的修正证明。
- 实际子丛的存在不提供 f-不变性或叶状可积性，也不构成 Ghys 猜想反例。
