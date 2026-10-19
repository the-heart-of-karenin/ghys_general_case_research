# 89–91：中央逐点次线性、全纯运动与中心识别

日期：2026-10-19。新增两份旧期刊原始 PDF，当前 manifest 为 71 个唯一条目。四个完整新页已核验；未重跑旧数学套件或旧文献散列。

## 1. 本轮取得的严格结论

在 87 的满辛体积稠密不变开集 Y° 上，公共复线 K 的每张积分盘都被 p_s 压为一点，并准确等于指定中心纤维与实际稳定或不稳定叶的局部交片。

证明链：

1. 82 的 u_r=0 使中央误差 w_r 成为普通交换酉 cocycle。
2. 79 的全群零条件旋转，通过交换投影推出每个单值的零条件旋转；Birkhoff 给 w_{nr}/n→0 几乎处处。
3. K 及所有单值像都属于同一侧真实 Anosov 叶，因而其上慢坐标差准确等于中央误差之差除以 n。
4. 复二维实际叶中的 K 复曲线图构成平面全纯运动，得到所需子叶 Fubini 性质；由连续性传到所有正规局部盘。

90 的 flow box 构造没有将逐点解析芽偷换成跨退化集的统一图。它在一个恒秩正规邻域选择固定实际返回 h，以全纯隐函数定理和解析恒等定理取得共同域；邻域可依赖于点。

## 2. 来源 70：实际只用开集版的 λ 引理

Ricardo Mañé、Paulo Sad、Dennis Sullivan，
*On the dynamics of rational maps*，
Annales scientifiques de l'École Normale Supérieure (4) 16 (1983), 193–217。

- [期刊原始页面](https://www.numdam.org/articles/10.24033/asens.1446/)
- [期刊扫描 PDF](https://www.numdam.org/item/ASENS_1983_4_16_2_193_0.pdf)
- [DOI](https://doi.org/10.24033/asens.1446)
- 本地 26 页，包括 Numdam 封面；PDF 第 2 页为期刊第 193 页。

完整核验 PDF 第 2 页的 λ 引理及第 8 页的子集拟共形定义。实际参数集合是一个平面开盘，因此这里得到普通平面拟共形切片；不需要该文当时尚未给出的任意集合邻域延拓，更不必调用 Słodkowski 的后续全平面延拓。

此处借用的全纯运动结论是经典定理，不作新颖性宣称。

## 3. 来源 71：仅用拟共形的面积零集保持

Kari Astala，
*Area distortion of quasiconformal mappings*，
Acta Mathematica 173 (1994), 37–60。

- [DOI](https://doi.org/10.1007/BF02392568)
- [大学档案中的期刊 PDF](https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6501-11511_2006_Article_BF02392568.pdf)

完整核验 PDF 第 1–2 页的 Theorem 1.1：归一化 K 拟共形圆盘映射的面积失真幂界。应用到映射及其逆，得到二维零集双向保持；一般局部平面开集通过共形坐标处理。90 只用这一零集结论，没有宣称取得全局统一常数或跨退化集面积界。

该零集性质比完整 Astala 定理更早已知；这里选择其清晰原始定理作可核验输入，不声称必须使用最强面积理论。

## 4. 复用的输入与未采用的文献

整个 Anosov 稳定/不稳定叶的绝对连续性属于原有经典输入，复用来源 48 及既有 metric_growth_source_audit.json 的检查。没有由该性质直接推出任意子叶绝对连续；90 的平面全纯运动证明是新增且必要的中间步骤。

检索比较到：

- [Cantat–Dujardin，Hyperbolicity for large automorphism groups of projective surfaces](https://jep.centre-mersenne.org/articles/10.5802/jep.294/) 的原始论文也明确用全纯运动的拟共形 holonomy 解释复曲面上的叶绝对连续性。这里只作已知机制比较，未下载、未核验或套用其主分类定理。
- [Bedford–Dujardin，Topological and geometric hyperbolicity criteria for polynomial automorphisms of C²](https://doi.org/10.1017/etds.2021.47) 的统一图半径与 lamination 机制作为后续退化集比较线索。本轮不调用其多项式自同构结论。
- Sullivan–Thurston、Bers–Royden、Słodkowski 的更强全纯运动延拓结果没有作为本轮证明输入。

有限搜索涉及 holomorphic motion/Fubini/foliation、common stable/solvable Anosov、sublinear cocycle/invariant foliation。一次批量搜索连接失败，随后缩小查询重试；没有以缺少结果宣称首创，也没有依二手汇编页给出数学断言。

## 5. 新颖性与停止点

全纯运动、平面拟共形、普通交换酉 cocycle 的投影与 Birkhoff 机制均为经典。当前独立贡献是将这些机制与 87 的实际公共线、82 的完整中央方程结合，完成特定中心方向的识别。有限检索未确认这一具体应用是否已存在，不能称为新的通用刚性定理。

没有证明：退化集为空、另一侧全体点解析、全纯中心曲面纤维化、w_r=0、第一张闭全纯一形式，或 76 零形式分支排除。

05 的实际代数模型通过；88 的非全纯全纯运动不反驳绝对连续性；85 的 Cantor 粗糙商缺少本轮的完整群 cocycle 和公共叶结构，不是新定理或原问题的反例。

本轮曾尝试仅用 L² 次线性在 K 上代值，明确发现缺口后由 90 补齐；不再将其作为待假设的子叶绝对连续性。另一方面，90 不能被外推成高复余维任意子叶的同样结论。

完整证明分别存于 notes/89–91。PDF 来源、散列、版本、页码与用途见 Common_line_identification_source_audit.json。
