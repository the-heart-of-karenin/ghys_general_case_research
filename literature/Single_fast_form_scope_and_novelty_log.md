# 98–100：单张快谱形式路线的来源、严格成果与停止点

日期：2026-10-19。

## 完成了什么，没有完成什么

本轮没有证明第二张闭全纯一形式必存在，没有排除 dim W_X=1。完成的是从该分支原始假设取得的一组实际结构：

- fast Lefschetz/flux 配对非退化，复流两个实轴的快平均旋转独立，随后由准确缩放升级为逐点常位移；
- 在快 primary 的自然覆盖上，复流自由且 proper，能真正取全纯商；
- 商有到 C 的 proper 全纯映射，纤维为紧致复四维保辛流形；零纤维上的真实返回为 Anosov，同伦标记只含 λ、λ⁻¹；
- 约化族的辛周期恒定，稠密 deck 平移还迫使全部 Hodge 数恒定；
- 若一维分支存在，则该四维约化上必须有非零 κ₀∈H¹(O)，g*κ₀=λ²κ₀，且 W_Y=0、h^{0,1}≥9。该类必须在 Frölicher 的 d₁ 或 d₂ 步被杀掉。

κ₀ 消失则确实产生第二张形式的证明写在 100，不是一个尚未完成的愿望：Grauert base change、稠密平移及 Leray/Cartan B 先使整个主 C 丛全纯平凡，随后全纯辛形式给完整水平流、实际乘积分解和紧致复曲面底。未知的是如何从原始非 Kähler 条件排除 κ₀≠0。

不把一维分支简单地等同于 76：本轮 deck 作用移动不同约化纤维，不提供同一个 Y 上的现成单值群；所以 82–96 的公共线论证不能直接照搬。

## 新增实际来源

75. Hans Grauert，*Ein Theorem der analytischen Garbentheorie und die Modulräume komplexer Strukturen*，Publ. Math. IHÉS 5 (1960)，5–64，[原期刊](https://doi.org/10.1007/BF02684746)。只使用 §7 Satz 3 的上半连续性及 Satz 5 的恒定维数 base-change/局部自由性。PDF 有 63 页及封面/扉页，实际核验 PDF 第 61–63 页，对应期刊 pp.62–64；不能直接套用其他 Numdam 文章的“PDF 比期刊多一页”规律。

76. 同作者 1963 勘误，Publ. Math. IHÉS 16，35–36，[原期刊](https://doi.org/10.1007/BF02684291)。PDF 三页，完整查看第 2–3 页。它更正若干证明估计，并指出 §7 Satz 2 的一般 base-change 非双射点集未必闭。本轮没有使用这个错误断言；使用的闭超水平集来自 Satz 3 的上半连续性。恒定维数的 Satz 5 在本轮光滑底 C 上使用。

新 PDF 和各完整页面保存在 literature，独立推导在 notes/98–100。来源、散列和所用假设见 Single_fast_form_source_audit.json；manifest 现有 76 个唯一 PDF 文件条目。旧曲面判据及 note77 的同速一形式刚性按既有核验复用。

## 有限检索与未采用的线索

实际检索了 Grauert 1960/1963、全纯辛加法群约化、快流与 Albanese、非 Kähler 周期映射及 h^{0,1} 上界等组合。原始数学输入仅为上面两份旧期刊和既有笔记；搜索自动摘要不作为定理证明。

检索定位到 Kaledin–Verbitsky 的 [Period map for non-compact holomorphically symplectic manifolds](https://arxiv.org/abs/math/0005007) 及 Kurnosov–Verbitsky 关于 Bogomolov–Guan 流形的工作。本轮没有下载或核验其完整适用条件，也没有将特殊代数、admissibility 或 BG 类型下的局部 Torelli 当作任意非 Kähler 同伦环面的结论。这里的等周期族是否全纯平凡仍需本系统自己的论证。

针对 h^{0,1} 的最后一次有限检索没有取得适用于当前 Y 的上界，不能据此声称这种上界在文献中不存在，更不能用 Kähler 的 h^{0,1}=b₁/2 来排除当前非 Kähler 候选。

快 flux 的外代数机制、Birkhoff 缩放、proper 主群约化、Grauert 与 Leray 都是经典工具。具体的快形式约化及其非零 Dolbeault 障碍结论是否已有文献覆盖，本轮未确认；不声称首创。

## 失败路线与比较模型的准确范围

1. 快流不能自动取紧致全纯群闭包。05 的真实紧致模型就有线性增长的快流导数；它排除相应全纯映射族的 C⁰ 等度连续性。
2. 98 中剩余普通 cocycle 仅有 O(|z|^{1/2})，没有消失结论。82 的可逆中央剪切配对在这个同侧阿贝尔子群中不存在；本轮通过 proper 约化绕过它。
3. 主 C 丛光滑平凡不意味着全纯平凡。100 §7 给出带闭全纯辛形式、proper C 约化和常周期紧致环面族的非平凡 torsor。该总空间非紧，且不具有原始快归一化 Anosov；它不是 Ghys 反例。
4. 普通 H¹ 的谱没有快特征值，不意味着 H¹(O) 同样没有。新类恰不在自然 H¹(C) 的像中；这里正需要尚未得到的 Hodge/动力学连接。

## 计算角色

只核对本轮新出现的 θ⁶=15H²D⁴、64 个 Lefschetz 配对条目和 fast 块行列式，结果在 notes/single_fast_flux_checks.json。最初发现当前 bundled Python 没有 SymPy，随后改为仅用标准库的整数多项式，不安装额外依赖；最终精确检查通过。

这不验证全纯商、遍历定理、上同调 base-change 或障碍定理；这些论证逐步写在正文。没有重跑旧套件，也没有宣称重新独立审完 71–97 全部证明。
