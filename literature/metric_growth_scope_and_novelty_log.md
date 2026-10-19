# 53–54：输入范围、失败步骤及有限新颖性核对

日期：2026-10-18。新颖性尚未确认。此文件记录来源及适用范围；独立证明在 notes/53–54，不把未命中检索当作新颖性证据。

## 已闭合的独立推导

1. 紧 Kähler 全纯 Anosov 的双向拉回形式和具有逐点指数正下界。只用连续不变分裂、紧致性、双曲性和全纯性，不用 pinching 或 C¹ 分布。
2. 从有限维上同调中减去单位模谱部分的多项式有界光滑代表，取得非中性谱部分中的 Kähler 类。在 IHS 上，负定补空间的迭代有界，且双曲平面只有两个互逆实特征值；于是两个 Green 特征射线的任意正组合为 Kähler 类。这是有限时间构造，不主张归一化形式的极限仍有正下界。
3. 因而奇数复维周期解析子簇不存在，允许奇异子簇；没有排除偶数维周期子簇。
4. 复四维的全局导数平方质量界、指数小体积尾界，以及利用稳定 holonomy 的有界 Radon–Nikodym Jacobian 得到的逐不稳定叶行列式尾界。它不比较两个导数矩阵，也不预设 holonomy 可微。

上述分析证明逐步写出，没有用数值核验取代。与文献机制有重合的部分明确按标准理论处理。

## 实际输入及其精确用途

- [20] Jang：PDF pp.7–9 的 BBF Lorentz 型、nef 特征类、null locus 背景；p.11 Proposition 7 中 d₂ 最大特征值的简单性。所有相关完整页已渲染阅读。
- [36] Lesieutre–Satriano：PDF pp.16–17，Corollary 2.23 及 Remark 2.22。只比较一般正熵情形中奇数维周期子簇落在非 ample locus 的结论；未套用算术假设或声称他们已证明本文的 Anosov Kähler 轴结论。
- Cantat 2004 §2.3，历史 PDF pp.7–9：比较其双曲性、正流与正则化机制；没有将它引用为 53 的逐字先行定理。
- [47] de Thélin：PDF pp.1–2，特别是 Corollaire 3。唯一最大动力学次数 d₂=λ²，邻项 d₁=d₃=λ，给最大熵测度的复指数 χ₂≥(log λ)/2 与 χ₃≤−(log λ)/2。临界/不定点距离可积条件在无临界和不定点的自同构中自动满足。结论不要求测度绝对连续。该 PDF 字体编码导致文本提取严重损坏，定理以完整页面图像为准。
- [46] Ledrappier–Young：PDF p.6 Theorem A，熵公式等号当且仅当不稳定条件测度绝对连续。结合此前 52 的唯一 SRB=m 与 θ≠m 才取得严格不等式，不能只用 Ruelle 上界推断严格性。
- [48] Bressaud–Liverani：作者稿 PDF pp.6–7，§4.1 定义与 Proposition 4.1 的 holonomy Jacobian 双边界。取两条不稳定叶为横截面时角度项 γ_U、γ_V 都是零。只用绝对连续性及有界密度，不解释为可微 holonomy 或导数矩阵共轭。

[48] PDF p.7 第一条 Jacobian 比值的 Hölder 公式印成了 exp(−const·d^τ) 的上界；将两点交换便显示这不是可直接采用的表述。本轮**没有使用这条公式**，只用其后明确写出的 exp(−C(...))≤J≤exp(+C(...))。源 PDF 保持原样。

## 额外标题命中的范围核对

Hamilton–Kotschick, *Lagrangian foliations and Anosov symplectomorphisms on Kähler manifolds*, ETDS 41 (2021), 3325–3335，online 2020-10-30，DOI [10.1017/etds.2020.109](https://doi.org/10.1017/etds.2020.109)。仅通过出版社原始 PDF 的前四页核对适用范围，未作为新编号下载来源或 53–54 的证明输入。

其 Theorem 1 预设 Lagrangian foliation 对 Kähler 度量的 Levi-Civita 联络平行；这正是本题未取得的正则性和联络约束。且原复结构下的复稳定分布不会对其 Kähler 形式 Lagrangian：任意非零 v 都有 ω(v,Jv)>0。它对 Re Ω 的 Lagrangian 性不能直接替换为对该 Kähler 形式的 Lagrangian 性。即使改用 hyperkähler 旋转使 Re Ω 成为 Kähler 形式，所缺的平行性仍未得到。因此不能由该定理直接推出本题平坦性；其例子不要求原映射对 Kähler 复结构全纯，亦不构成本题反例。

## 有限检索记录及范围

检索围绕 holomorphic Anosov + Kähler cone/eigenclasses、hyperkähler periodic subvarieties/null locus、de Thélin Lyapunov bounds、Anosov stable holonomy Jacobian、parallel Lagrangian Kähler 展开；回到原作者稿或期刊页核对精确假设。没有使用搜索结果数量或相同措辞的缺失确认新颖性。47、48 均为 2008/2002 期刊文献的作者稿，符合当前阶段可自由检索的授权。

## 尚未闭合的步骤

- Kähler 上同调类具有光滑正代表，不说明特定的 Green 根流或其和是该光滑代表。
- 54 的高导数集在光滑体积或每片叶体积下指数小，却可在假想系统中承载渐近全部 Green 质量。没有取得排除这种集中的 Green 质量或容量估计。
- Hölder 势、满支撑、逐叶弱连续性和幂次小球界不蕴含绝对连续性；52 的非紧模型仍阻止这种形式推论。
- log∥Dfⁿ∥ 的靶丛曲率含 (fⁿ)*Rm，未得到相对于固定背景的统一 quasi-psh 界；不能借 53 的全局 Ricci-flat 度量省略此项。
- 48–50 实际边界例子已有 ample 双曲轴，通过 53 的结论；54 没有计算它的真实导数或周期乘子，仍未判定 Anosov 可能性。

下一步若继续此线，应控制**由真实切导数定义的这些特殊异常集**的 Green 质量，或给出能排除这种集中机制的另一个全局几何约束。继续重复 Chern 数或只证明满支撑没有解决这个缺口。
