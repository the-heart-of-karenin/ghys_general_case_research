# 第一轮检索：已知结果、模型范围与障碍

日期：2026-10-17。范围：阅读摘要、引言、主要定理及一个决定研究方向的例子；没有逐篇验证全部证明，也未开始全力证明一般猜想。

本轮获用户授权后首次使用联网资料，包括 2026 年近期预印本。此前复秩一工作区保留不动；本轮以后的研究不再具有“未接触近期证明”的信息边界。

## 1. 一般目标的模型要足够宽

本次采用的目标是：每个紧致连通复流形上的全纯 Anosov 微分同胚，都双全纯共轭于复 infra-nilmanifold 的双曲仿射自同构。

这里的复 nilmanifold 指实单连通幂零 Lie 群 G 的紧致格商 Γ\G，配备可下降的左不变可积复结构 J。再允许有限群的自由全纯仿射商。不能额外要求 G 的乘法对 J 联合全纯，即不能偷偷把“左不变复结构”缩小成“复 Lie 群结构”。

这一准确范围见：

- Zhang, Invariant complex structures for affine automorphisms: a cocycle viewpoint, §2.2；一般猜想见 Conjecture 1.9。
- https://arxiv.org/html/2606.17794

## 2. 必须修正“普遍证明两侧全纯”的路线

Zhang, Codimension-one holomorphic Anosov diffeomorphisms, v2 (2026-10-05)：

- Theorem A 解决复秩一情形。
- Theorem 1.2 不要求秩一：如果 X 已同胚于实环面，且两侧分布全纯，那么 X 为复环面并有双全纯线性共轭。
- §1.2 明确指出一般余维的障碍。
- §5，PDF 第 17 页，给出复六维、复秩 (3,3) 的全纯 Anosov 代数模型；两侧分布都是 C∞，却都不全纯。

例子中有光滑 (1,0) 标架 Y、Z、B、C，满足

\[
\bar\partial Y=d\bar x\otimes Z,\qquad
\bar\partial B=d\bar a\otimes C,
\]

其中 Y 属于稳定子丛而 Z 不属于；B 属于不稳定子丛而 C 不属于。因此两侧都不是全纯子丛。这个例子符合一般猜想，并不是猜想的反例。

已经阅读完整相关页面并核对页面图像；独立重新验证格、可积性、下降及双曲性的完整计算列为下一轮任务。

后果：C∞ 正则性仍是合理的中间目标；分布全纯性只能作为有额外条件的分支目标，不能成为一般分类的必经步骤。复四维 (2,2) 仍是最低新维数的实验场；不能把复六维例子误说成复四维反例。

来源：https://arxiv.org/html/2609.37695v2 ，§1.2、Theorem 1.2、§5。

## 3. 已有“最后一公里”定理

Zhang, Invariant complex structures for affine automorphisms: a cocycle viewpoint (2026), Corollary D：

若全纯 Anosov 系统通过双 Lipschitz 同胚 h 共轭于实 infra-nilmanifold 上的仿射 Anosov 自同构，则模型上有复 infra-nilmanifold 结构，使同一个 h 双全纯。

这是近期预印本中的定理陈述和证明，尚未在本工作区完成全部独立审查。规划可以将其作为待精读、核验的外部输入；不把它冒充本次新结果。

因此一般目标可拆为：

\[
\text{全纯 Anosov}
\xrightarrow{\ ?\ }\text{infra-nil 拓扑模型}
\xrightarrow{\ ?\ }\text{双 Lipschitz 共轭}
\xrightarrow{\text{Corollary D}}\text{双全纯仿射分类}.
\]

“已有拓扑共轭”不等于“已有双 Lipschitz 共轭”。周期导数数据是后一个缺口需要检查的障碍。

来源：https://arxiv.org/html/2606.17794 ，Corollary D。

## 4. 单叶统一化已有较强输入

Bera–Verma, Uniform non-autonomous basins of attraction, Invent. Math. 238 (2024), 995–1040，证明一致吸引的非自治盆地双全纯于复欧氏空间，并解决相应稳定流形的双全纯类型问题。

对本题的稳定/不稳定叶，需要将 Anosov 的均匀局部叶坐标与其抽象盆地设定逐项匹配。适用后，可取得每片叶分别为 C^s、C^u。

这不自动提供：

- 规范化坐标对基点的连续或光滑依赖；
- 有限维的坐标转移群；
- 横向 holonomy 的正则性；
- 万有覆盖的全局稳定×不稳定乘积。

所以不应重新把“单叶为 C^r”当作主要待攻问题，也不能把它当作全局分类的替代。

期刊原始来源：https://link.springer.com/article/10.1007/s00222-024-01295-9

## 5. 正规形工具

- Kalinin–Sadovskaya, Normal forms on contracting foliations: smoothness and homogeneous structure，https://arxiv.org/abs/1612.03454 。窄带谱下给出叶上相干多项式坐标及有限维转移群；一般只是逐叶光滑，不能直接宣称横向光滑。
- Kalinin, Non-stationary normal forms for contracting extensions，https://arxiv.org/abs/2006.12662 。用于精确区分存在性、唯一性、正规形次数及中心化子。
- Berteloot–Dupont–Molino, Normalization of bundle holomorphic contractions and applications to dynamics, AIF 58 (2008)，https://aif.centre-mersenne.org/articles/10.5802/aif.2409/ 。提供全纯丛收缩的正规形版本，有明确的谱分裂假设。
- Melnick, Nonstationary smooth geometric structures for contracting measurable cocycles，https://arxiv.org/abs/1604.04423 。将正规形解释为不变几何结构，有助于寻找可拼接的有限阶结构。

不同版本的“窄带”“pinching”“可测”假设不能混用。可测或几乎处处的结构不能直接视为整个 X 上的完整结构。

## 6. 可作为检验场的已知刚性

- Kalinin–Sadovskaya, On local and global rigidity of quasiconformal Anosov diffeomorphisms (2003)，Theorem 1.1：在传递、一致拟共形及相应实维数/拓扑假设下取得 C∞ 仿射环面模型。这些是附加假设下的已知结果，不作为本次的新定理。https://doi.org/10.1017/S1474748003000161
- Rodriguez Hertz–Wang, Global rigidity of higher rank Anosov algebraic actions，https://arxiv.org/abs/1304.1234 ，结合 Zhang 2026 Corollary E，给出无秩一因子高秩作用的全纯分类分支。
- 已附 Benoist–Labourie 1993：传递、两侧 C∞、不变光滑仿射连接的组合提供 C∞ infra-nil 分类入口。仅证明两侧光滑不够；连接和传递性必须另行提供。

## 阅读深度边界

本轮核对了前两篇预印本的相关定理、模型定义及障碍，并阅读、渲染核对了非全纯分布例子页面。其余以摘要、引言、定理设定及期刊信息为主。九篇 PDF 已保存；“已下载”不表示“已完成证明审查”。没有据这轮有限检索断言不存在其他相关结果。
