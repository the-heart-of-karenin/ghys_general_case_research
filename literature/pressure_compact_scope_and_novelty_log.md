# 55–57 的文献核验、版本、计算角色及新颖性范围

日期：2026-10-18。独立数学证明保存在 notes/55–57；原始文献与提取、预览、来源散列留在本目录。新增两份旧文献作者 PDF，当前 manifest 共 50 篇。没有确认本轮组合定理的首创性。

## 1. 文献输入与实际使用范围

### [49] Cantat–Dupont

期刊：*Automorphisms of surfaces: Kummer rigidity and measure of maximal entropy*, J. Eur. Math. Soc. 22 (2020), 1289–1351，DOI [10.4171/JEMS/946](https://doi.org/10.4171/JEMS/946)。本地实际保存的是 [arXiv:1410.1202v1](https://arxiv.org/abs/1410.1202)，57 页，边注 2014-10-05，首页日期 2013/2014。

原作者最新页面所链的 70 页 final 稿也通过网页工具核对过关键陈述，但本机下载时 CNRS 站点证书名不匹配，旧 Rennes 入口未能取得所需版本。采用 arXiv 原作者稿，不关闭证书校验，不把旧版本伪称期刊排版。

**编号差别必须保留：** 本地稿 Corollaries 1.6、1.7 对应后稿 1.7、1.8。正文 notes/56 统一引用本地编号。

本轮完整页面核验：

- p.1：版本、题名、作者、日期。
- p.5：Main Theorem 的 projective surface 及绝对连续假设；Classification Theorem 中 K3 的经典 Kummer 性及 Picard 数至少 17。
- p.6：Corollary 1.6 的 Lyapunov 等号等价性、保体积时指数相反，以及 Corollary 1.7 的秩二非 Kummer 奇异性。
- pp.12–13：Hölder Green 势、Green 测度 mixing、唯一最大熵以及复指数的实重数为 2。
- pp.43–44：Proposition 8.1 的 Ruelle 临界界、两侧等号导致绝对连续的原始解释。

不将曲面上的绝对连续 Kummer 刚性直接套用到一般 IHS 四维；四维例子通过真实 Hilbert 平方、有限因子熵及 tempered 导数比较构造。

### [50] Rey–Bellet–Young

期刊：*Large deviations in non-uniformly hyperbolic dynamical systems*, ETDS 28 (2008), 587–612，DOI [10.1017/S0143385707000478](https://doi.org/10.1017/S0143385707000478)。当前作者站点 [journal PDF](https://luc-umass.github.io/pdf/lsy1.pdf)，26 页；旧 UMass 入口 SSL EOF，已切换作者当前公开入口。

完整核验 PDF pp.3、17–18：Theorem A/B、Theorem 4.3、式 (14)、平移压力恒等式，以及严格凸与 coboundary 的关系。**一般无限塔结果只有参数区间上的结论，不能引用成无条件全参数大偏差。** 55 使用混合有限型 Markov 编码，并给出全参数对数矩恒等式的标准柱集证明；只把 [50] 用作原始压力机制比较，不冒称其某条定理逐字就是 55。

### 复用原始来源

- [34] Amerik–Verbitsky，PDF pp.3、10–11：Theorem 1.1、Theorem 3.6、Corollary 3.7 及其证明。构造的是保全纯辛、Picard 数二、无 MBM 的射影变形；“hyperbolic”表示 H¹,¹ 上的 loxodromic 作用，**不表示 Anosov**。用于 56 曲面输入存在性及 57 的 Kähler 轴、体积非最大熵实际例子。
- [17] Beauville，完整查看 PDF pp.8–10、12–14。实际 Hilbert 输入在 pp.12–14：Propositions 5–6、辛形式从对称和下降、H² 分解、单连通性，及射影 S 的 Hilbert scheme 为射影/Kähler 的说明。本稿 Theorem 3 有其历史的“generic K3”措辞；本研究只取射影 S，没有把该历史表述错误升级。扫描件无可用文本提取，整页图像为核验依据。
- [21] O'Grady，PDF pp.15–16，尤其 §5.2：Bl_Δ(S²) 的提升交换对合及其商 S^[2]。未使用文中的模层构造去赋予连续稳定丛额外全纯性。
- [20] Jang，PDF pp.25、27：Proposition 22 的平坦性在该文 m=θ 假设下成立；§5.3 明确指出该假设下双曲轴不能 ample。因此 57 的“Kähler 轴 + 体积非最大熵”是原文加存在性输入的直接组合，**不称为本轮新定理**。p.27 的一般平坦流形措辞不用于声称所有紧致平坦 Kähler 流形都是环面；这里只用正确的“紧致单连通平坦流形不存在”。54 的谱质量计算还复用此前已核验的 p.11，见 metric_growth_source_audit.json。
- [45] Young，PDF pp.3、6：SRB 的 Gibbs 势确为 −log|det(Df|Eu)|，以及稳定叶状结构的绝对连续性。较早记录中 p.2(ii) 漏印 log 的问题仍按原先处理，熵公式以 [46] 原始 Theorem A 为准。
- [48] Bressaud–Liverani，PDF p.7：Propositions 4.1–4.2 的稳定 holonomy Radon–Nikodym Jacobian 双边界及局部乘积坐标的有界正密度。继续避开前一条比值公式的排印负号，不将它解释为 C¹ holonomy。

八篇原始 PDF、26 个完整页面的本轮核验见 pressure_compact_source_audit.json；所有完整页已逐一查看。历史已核验定理仍保留此前 audit，不将其重新计入本轮新下载。

## 2. 已证明部分与来源边界

1. 55 的临界阈值双向指数分离，从一般 Anosov Gibbs 理论推导；压力严格间隙用两端平衡态不同的变分证明，不预设严格凸。逐叶升级只用标量势的稳定 distortion、holonomy 绝对连续性及 51 的 Margulis 测度接口。
2. 56 的紧致反检验在 X=S^[2] 上实际成立，不是假想的 cocycle：有限因子识别 Green 测度、CLN 小球界排除指数过快接近对角线、Hilbert 局部坐标证明切坐标变化 tempered，故严格转移真实 Lyapunov 指数。
3. 56 的容量正下界来自一个明确 admissible bounded ω-psh 势；不依赖未经证明的体积—容量反向比较。
4. 56 的混合规范测度及三种熵的公式逐项计算，认真处理 double-cover 正常数与例外除子不带质量。未断言该混合测度在假想 Anosov 中等于任一端点测度。

## 3. 有限新颖性检索

使用过的关键词组包括：

- hyperkähler automorphism Green measure Lyapunov volume large deviations；
- K3 automorphism maximal entropy singularity exponents；
- unstable Jacobian pressure Gibbs volume、Anosov Pesin defect；
- hyperkähler Green mixed measure symplectic、Hilbert scheme measure maximal entropy。

与原始来源对照的结果：Cantat–Dupont 的曲面严格指数与奇异性、Jang 对 m=θ 时非 ample 轴的解释、一般压力与 Chernoff 机制都是已知输入。检索还命中 Orey–Pelikan 1989 的 *Deviations of trajectory averages and the defect in Pesin's formula for Anosov diffeomorphisms*（Trans. AMS 315, 741–753）及 Kifer/Young 1990；这些进一步说明大偏差—Pesin 缺口不是新主题。本轮未取得它们的可用原始 PDF，不将仅有的引文/摘要当作具体定理证明输入。

没有检索确认或否定 56 全部组合公式的先行出处。尤其“没有命中三种规范测度的同一写法”不等于新颖性证明。该定理的价值在于对当前研究路线提供严格的紧致反检验，不以首创性作为结论。

## 4. 计算核验的角色

notes/check_pressure_and_compact_measure_formulas.py：

- 整数系数外代数核对 MA 展开系数 4、混合测度两个系数 1、辛体积系数 4，以及和的四次幂系数；显式计入 i² 的符号。
- 有理数矩阵核对实环面模型两类固定点的导数迹及行列式。
- 独立 Bernoulli 模型数值核对两个 Chernoff 指数的方向，在 5 个不同长度上通过。

它们不证明流的存在、容量、tempered 性、绝对连续性、结构稳定性邻域大小或新颖性；没有把某个固定 ε 的数字计算说成 Anosov 证明。分析证明在正文单列。

## 5. 未解决与路线判断

本轮没有证明 IHS Anosov 不存在，没有证明横向 C¹、Green 叶测度绝对连续、压力间隙消失，也没有计算 48 实际边界自同构的周期乘子。56 的反例有不变例外除子及非 Kähler 轴，明确不是 Anosov；57 的无墙例仅用于否定“Kähler 轴 ⇒ 体积最大熵”，不声称它满足 56 的严格超临界指数。

严格可说的是：现有标量大偏差/小体积/正性数据尚不足以闭合；若不加入真正耦合 IHS 切丛几何与全局 Anosov 复叶片的新引理，应停止继续优化同类标量估计。这是由具体反检验支持的研究判断，不是不可解性定理。
