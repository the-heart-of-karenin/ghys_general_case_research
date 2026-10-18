# 46–48：正规化子推广的检索、来源和范围

日期：2026-10-18。本文件为检索记录，不是数学证明。用户已允许联网下载阅读，原先的 2026-06-01 截止不再适用于当前推广工作。

## 1. 本轮重点检索

实际查询包括：

- Anosov hyperkahler automorphism stable bundle first Chern class nonsymplectic normalizer
- hyperkahler Lagrangian splitting Euler characteristic 31 sixfold
- K3 Hilbert square automorphism Picard rank 3 invariant lattice -26 antisymplectic
- "Anosov" "hyperkähler" "Chern"
- "Anosov" "commutator" "stable" centralizer
- "Lagrangian" "splitting" "120960"
- "Anosov" "nonsymplectic"
- "Anosov" "Chern classes" "holomorphic"
- "Anosov" "hyperkähler manifolds"
- "stable bundle" "hyperkähler" "Anosov"
- "K3" "3330" automorphism

返回中相关的一手来源包括 Lee 的 Cayley K3 Hilbert 平方自同构群文章、Boissière–Cattaneo–Markushevich–Sarti 的非保辛对合文章，以及 Kalinin–Sadovskaya 的高秩 Anosov 文献。其标题/摘要表明存在相关的格、对合及中心化子背景；本轮没有把这些检索摘要当作任何证明输入，也没有为增加篇数而下载。

来源链接（仅供后续比较，不等于已阅读全文）：

- https://arxiv.org/abs/2403.07399
- https://arxiv.org/abs/1805.10481
- https://arxiv.org/abs/math/0602175

有限检索没有定位到与 47 的固定 −26 类条件、六维模 31 必要条件或 48 的指定 Gram 矩阵/固定类构造相同的陈述。检索结果稀疏、部分查询噪声很大；不能据此声称首创，也没有系统核查所有相关书目。

46 的有限误差/正规化子观察是经典“交换映射保持双曲分裂”的直接发展，其原创性尤其不应夸大。这里的研究价值在于把这个实际导数机制与 IHS 的非零稳定 Chern 类组合，并核实适用范围与实际边界。

## 2. 唯一新增下载：第 40 篇

Georg Oberdieck, Jieao Song, Claire Voisin,
*Hilbert schemes of K3 surfaces, generalized Kummer, and cobordism classes of hyper-Kähler manifolds*.
Pure and Applied Mathematics Quarterly 18 (2022), 1723–1748。

- 作者提供 PDF：https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/cobordismHKsoumis.pdf
- 正式 DOI：https://doi.org/10.4310/PAMQ.2022.v18.n4.a13
- 作者书目：https://sites.google.com/view/georgo/writing
- 本地：40_Oberdieck_Song_Voisin_2022_Cobordism_HK.pdf
- 作者稿 17 页；仅使用完整 PDF p.12 的 Chern 数矩阵，读到三类六维 Euler 数 3200、448、1920。

该页公式 (13) 实际为 (c₂²−c₄/3)/240，等于标准 (3c₂²−c₄)/720；文本提取若丢失内部的 1/3 会造成误读。已完整渲染检查，没有判为原文错误。47 的六维 Todd 多项式独立展开并做精确分数核验，不从此处的四维公式猜测。

## 3. 重新核验的准确外部输入

- [19] Oguiso，Theorem 1.1，PDF p.1：IHS 动力学次数、h_top=d log d₁。
- [21] O'Grady，(5.3.4)，PDF p.17：K3^[2] 的 c₂²、c₂α² 交数；同页二阶格描述。
- [24] Kapfer，Remark 2.1，PDF p.6：Betti 数，特别是 K3^[3] 的 b₆=2554，而非仅 Sym³H²。
- [37] Markman，PDF p.3：周期满射；p.4 Theorems 1.3–1.4：强 Torelli 与 Kähler chambers；p.5 Theorem 1.5：birational Kähler 锥在基本 exceptional chamber 内开且稠密；p.32 Lemma 9.2：K3^[2] 的 Mon²=O⁺。
- [38] Mongardi，Proposition 2.12，PDF pp.7–8：K3^[2] 墙为平方 −2 或平方 −10 且整除度 2。
- [32] Hassett–Tschinkel，PDF p.3 Theorem 2.1 是核群的变形不变性。本轮特意区分它与一般有限性；46 的一般有限性使用正文 Ricci-flat 等距群证明，不把定理标题替代证明。

上述 7 篇的 11 个完整 PDF 页均渲染查看。页号、散列及核验状态在 normalizer_generalization_source_audit.json。原始 PDF 未修改。

## 4. 数学边界审查

1. 47 的任意 Picard 数定理只排除被检验的非保辛 f；高 Picard 数下没有自动共轴或交换，不能直接排除同一 X 上全部映射。
2. 48 的第一例是实际正则自同构，已被排除为 Anosov。
3. 第二例固定正确的 −26 类，也完成了共同 ample chamber 及实际 Torelli 实现；不只是抽象格等距。
4. 为应用稠密性，先把 NS_R 的 chamber 扩展为整个 H^{1,1}_R 的开 chamber，没有把稠密开集任意限制到低维子空间。
5. 第二例是否 Anosov、完整正规化子是否继续产生障碍均未知；没有构造不变或可积稳定丛。
6. OG6 通过模 31 条件，不能把 K3^[3]/Kummer 六维的非零 c₁ 结论扩展给它。高次 Chern 类必须真的计算 H⁶ 作用。
7. 本轮没有重新开始无 pinching 横向 C¹ 的局部估计，没有取得该正则性或完整 Ghys 分类。
