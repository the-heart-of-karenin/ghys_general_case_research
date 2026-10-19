# 96–97：全局中心几何、变形理论与分支排除的来源和新颖性范围

日期：2026-10-19。

## 本轮实际结论

96 以已有全局单侧中心曲线和真实另一侧 Anosov 叶作横截联合，构造整个 Y 上的复超曲面。慢商的单值不变性与辛特征核使另一侧中心线全局等变；叶内全纯 Fubini 与既有逐点次线性再完成指定方向识别。两侧都恢复后，中央误差全消去，每张完整中心纤维成为复 Lagrangian 曲面。

97 用实际紧致曲面和极大连续变形族恢复全纯纤维化，底为复二维环面，产生非零单值不变闭全纯形式，排除 note76 的**完整快谱 Albanese 二维分支**。没有排除原六维系统的 W_X=0 或 1；没有证明完整一般 Ghys 刚性。

旧链 76–95 作为已有成果复用。本轮核对新增接口，没有把它说成对全部旧笔记的独立再审。

## 仅有的新增外部数学输入

1. Nicholas Buchdahl, *On compact Kähler surfaces*, Ann. Inst. Fourier 49 (1999), 287–302，[期刊来源](https://doi.org/10.5802/aif.1674)。只用 Theorem 11 的偶 b₁ 曲面 Kähler 判据。PDF 共 17 页，完整查看 PDF 第 3、12 页。
2. Adrien Douady, *Le problème des modules pour les sous-espaces analytiques compacts d'un espace analytique donné*, Ann. Inst. Fourier 16 (1966), 1–95，[期刊来源](https://doi.org/10.5802/aif.226)。只用 §9 的普遍紧致子空间变形对象、有限维性和切空间 Hom(I,O)，并核对局部 Banach 粘合模型。PDF 共 96 页，完整查看第 78、81、84–85 页。

两份 PDF 均带 Numdam 封面，故 PDF 页与期刊页相差一页。来源与 SHA256 已追加 sources_manifest.json；六个完整页的记录在 Global_central_fibration_source_audit.json。论文原文件保存在 literature，独立论证保存在 notes/96–97，未修改原 PDF。

97 的“极大连续族全纯化”不是在 Douady 原文中找到的同名现成定理。先由小正规图的分裂理想说明分类映射连续，再用不变域定理使解析障碍方程全消失，最后用普遍族的评价映射恢复全纯底坐标。这三项具体论证写在 97 §3，不能用一个未经核对的“平凡正规丛自动无阻碍”替代。

## 检索及比较范围

本轮检索词：

- `Buchdahl 1999 On compact Kahler surfaces even first Betti number pdf`
- `Douady 1966 probleme modules sous espaces analytiques compacts tangent H0 normal pdf`
- `holomorphic symplectic Lagrangian tori Douady space foliation non Kahler continuous family normal bundle`
- `holomorphic Anosov nilmanifold Albanese symplectic unipotent rigidity Ghys`

前两项直接取得上述旧期刊原文。后两项用于有限比较定位；搜索页及其自动摘要本身不充当证明。

比较线索包括 Amerik 的 [On families of lagrangian tori on hyperkähler manifolds](https://www.imo.universite-paris-saclay.fr/~ekaterina.amerik/articles/lagr-tori3.pdf) 及 Lagrangian 环面纤维化相关经典工作。本轮只定位，没有下载或核验其完整证明，也没有将其 hyperkähler/射影背景下的无阻碍结果移用到非 Kähler 的 Y。Douady 变形空间、辛形式识别法丛、偶 b₁ 曲面判据和不变域机制均为已知工具。

搜索还出现近期综述或研究元数据；未打开其新证明、未下载、未用作本轮定理输入。新增实际采用的两项来源分别为 1966、1999 年期刊，不依赖最近的 Ghys 证明。

有限检索没有确认“准确正规化辛 Anosov 悬挂 + 指定中心拓扑”这一应用组合已发表或未发表；因此**不声称首创**。全面查重不属于本轮已经完成的事项。

## 被绕过、失败与尚未解决的步骤

- 原拟对 Y° 内的特征叶空间先证明 Hausdorff、再扩张稠密格平移。该路线没有被否定，本轮由更短的全局横截联合超曲面绕过。
- 95 中两套稳定叶的夹角在 Z 可退化；不能直接把其正规开集论证强行延到 Z。96 更换一套叶，使用 Eu 与全局 Ks 的一致横截，确实移除了这个接口。
- 一般平凡正规丛不自动给无阻碍。97 使用额外的、已经从原始系统得到的满实维实际纤维族；不把它作为新的原始假设。
- 偶 b₁ 判据仅用于实际复曲面 F_b 和全纯化后的底 S，没有把整个复四维 Y 预设为 Kähler。
- 原模型的二维快商仍可存在；排除的是它等于完整 Albanese 的非最大分支。05 的 W_X=4 模型完整保留。
- W_X=0/1 时还没有当前二维悬挂与显式单值群。下一步不能照抄本轮证明，也不能宣布一般分类已完成。

本轮没有数值采样或重跑旧数学套件。辅助文件只记录来源身份、页码、散列和文档结构，不作为数学证明认证。
