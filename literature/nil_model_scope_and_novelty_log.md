# 58–60 的来源范围、有限新颖性核验与未采用路线

日期：2026-10-18。原始 PDF 与独立研究笔记分开存放。源文件散列、版本和完整页图像核验见 `nil_model_source_audit.json`、`nil_model_rendered_pages.json`。

## 一、严格证明及来源归属

- Lauret–Will 的八维 Anosov 实 Lie 代数完备分类是已知定理。本地 53 为带一页大学系列封面的 2007 作者稿，最终期刊为 Trans. AMS 361 (2009), 2377–2395；Theorem 3.2 在 PDF p.14，括号表 p.8，Table 3 在 p.18。51 为同项研究的 2004 arXiv v2 长稿，不能计作另一套独立分类。
- Latorre–Ugarte–Villacampa 的中心约束是已知定理，本地 54 Theorem 3.11 在 p.9、Corollary 3.12 在 p.13。准确内容为八维 SnN 复结构只能有一维实中心，不是“所有中心均 J 不变”。
- Bazzoni–Freibert–Latorre–Meinke 的复辛氧化/八维分类是已知背景。本地 52 为 arXiv:1811.05969v1，2018-11-14，35 页；最终为 JPAA 225(6) (2021), 106585。p.17 的 Theorem 5.9 重述 LUV，p.20 的 Corollary 5.12 是氧化归约。58 的证明不依赖穷举其氧化参数。
- 58 的五类共同保持排除、h 类的对数模二三次矩证明、h₃⊕h₃⊕R² 中中心复线与闭形式的配对矛盾，均完整写出。
- 60 的常系数连续截面引理、仿射内自同构对格约束的准确修正，以及有限商下降均完整写出。
- Zhang 2026 的 Corollary B 已证明弱混合仿射情形的不变复结构左不变，Corollary D 提供已有双 Lipschitz 共轭的双全纯升级。本地 02 pp.3–4 重新渲染核对。60 的连续 Anosov 引理不是把该已知思想冒充新发现；它提供独立且无遍历性输入的证明。

## 二、计算核验与解析证明分开

`notes/eight_dimensional_nil_model_checks.json` 包含五类括号的 Jacobi/中心/导出维数、24 种中心谱配对的 Fraction 消元、对数模矩恒等式、反检验的外代数与权重、二次域格相容性，以及有限自由环面商的精确模二检验。

这些计算不能证明 LW/LUV 完备分类，不能认证新颖性，也没有生成未知连续分布的正则性。58 的关键排除都有计算之外的解析证明。

## 三、反检验与不能删除的输入

59 的真实紧致模型具有可积左不变 J、闭全纯辛 Ω₀ 和保格全纯 Anosov F，但 F 不保 Ω₀。直接计算结合 60 的自动左不变性，进一步排除了任何 F 不变全纯辛形式。这不是保辛 Ghys 反例。

59 的非紧复 Heisenberg×C 模型同时保 J、Ω 且双曲，但二维实导出代数行列式不为单位，无法保格。这说明不能用非紧实 Lie 代数的存在性直接推出紧致例子。

不闭的光滑 (2,0) 张量反检验同时失去全纯性，只说明非退化与不变性本身不够；未宣称它只删除“闭性”这一项。

已知 05 的复六维紧致保辛模型不受本定理排除。因此在模型范围中最小非交换保辛复维数恰为六，但未分类复六维全部模型。

## 四、有限检索及新颖性判断

查询包括：

- `Lauret Will Anosov diffeomorphisms nilmanifolds dimension 8 classification eight dimensional Lie algebras`
- `Bazzoni Freibert Latorre Meinke complex symplectic Lie algebras Anosov eight dimensional`
- `"Anosov" "complex symplectic" nilmanifolds`
- `"holomorphic Anosov" "dimension four" nilmanifolds`
- `"symplectic Anosov" nilmanifolds dimension eight`
- `"holomorphic Anosov" "Kodaira"`
- `"Lipschitz continuous invariant forms for algebraic Anosov systems"`

数学输入只依赖原始论文和作者/大学资料，不依据搜索摘要或二手页面的定理转录。已读 LW、BFLM、LUV 及本地 02 中未定位到完整相同的“八维保复辛共同保持交集”结论。这不足以证明结果未发表；本轮新颖性仍**未确认**。

Foulon–Hasselblatt，*Lipschitz continuous invariant forms for algebraic Anosov systems*，JMD 4(3) (2010), 571–584，DOI 10.3934/jmd.2010.4.571，是明确的平行旧文献。出版社页面与作者论文列表核对了身份、摘要及卷期：

- <https://www.aimsciences.org/article/doi/10.3934/jmd.2010.4.571>
- <https://www.i2m.univ-amu.fr/perso/patrick.foulon/MenuDroite/listepublis.html>

出版社 HTML 中提供的 PDF endpoint `https://www.aimsciences.org/data/article/export-pdf?id=c3e4f131-b89c-4142-9c40-72245f7b6436` 返回零字节；旧数据路径 `https://data.aimsciences.org//aimsmath-upload/jmd/2010/3/PDF/1930-5311_2010_3_571.pdf` 返回 404。因此**没有将该 PDF 计入来源清单，也未将其网上转录的具体更强定理作为本阶段证明输入**。60 的连续版本已直接证明。

## 五、未采用/停止的路线

1. 没有继续枚举 BFLM 的全部连续参数。完整交集可由五类 LW 代数的共同保持障碍解决，参数穷举不是必需步骤。
2. 没有将 LW 中“可以另选半单 Anosov 自同构”用于未知 J、Ω；那样可能破坏共同保持。本文始终用原 A 的广义特征空间或其正次幂。
3. 没有将两个奇异测度的关系引入本阶段；Green 路线工具继续保留，但不再优化同类标量估计。
4. 模型侧证明已闭合；一般系统的模型化、双 Lipschitz 入口或横向光滑性尚未取得。不把最后一项写成已证的 IHS 排除。
