# 65–68：仅新增部分的来源、文献重叠与证明层级

日期：2026-10-18。用户本轮明确允许减少复核，因此复用旧来源 56–57 及 61–63 的核验，不重新审计旧分类。只对实际影响新推导的来源和公式进行检查。

## 新文件

- **58：** Hasegawa–Sillari–Tomassini，Invariant forms compute the Dolbeault cohomology of complex nilmanifolds，arXiv:2607.26786v1，2026-07-29，19 页。下载 https://arxiv.org/pdf/2607.26786v1 。Theorems 7.1–7.2 位于 PDF p.15，p.16 明确写出小变形仍使用同一 g、Γ。PDF pp.1、2、15、16 已按完整图像核对。该一般 Dolbeault 主定理未在本轮独立复证，且文件明确按新预印本登记；67 的全体 nil/infra-nil 普遍开放性使用它。
- **59：** Konstantin Wehler，Teichmüller and moduli spaces for complex nilmanifolds，arXiv:2609.31516v1，2026-09-25，57 页。下载 https://arxiv.org/pdf/2609.31516v1 。Theorem A/2.1 在 PDF pp.3、12；证明 pp.13–16，经多项式增长、Liouville 与格的多项式稠密性得到全局仿射性。上述六个完整页已查看。它比 62/65 的小双全纯映射结论更强，故旧的“首创性未确认”已更新为“这一结论已有更强的文献覆盖”。本文的椭圆证明作为不同机制保留，不继续认领该结论的新颖性。
- **60：** Hasegawa–Rollenske–Sillari–Tomassini–Wehler，Biholomorphism type of left-invariant complex structures on nilpotent Lie groups，arXiv:2606.31448v1，2026-06-30，6 页。下载 https://arxiv.org/pdf/2606.31448v1 。仅查看完整首页定理及在 58、59 中的依赖位置，作统一化背景；不是 66 的证明输入。

共新增三份 PDF，当前 manifest 为 60 份文件。新文件散列及 11 个完整页的查看记录见 nil_progression_source_audit.json。新旧文件编号与 notes 编号分属不同目录，不能把 source 60 与 note60 混淆。

## 证明依赖分层

**65 的分析推广：** 高步 BCH 平均值正规化、所有高阶项二次控制、Engel 的全局 H⁰ 左不变性、仿射平移方程均在正文证明。旧来源 56 保证一批非 abelian/高步基点的小变形完备性；全体基点版本另用 58。

**66 的主结果：** degree-two 周期截面、周期的非退化紧性、同伦恒等连续中心化子及标记保全纯辛模型化集合闭性，由正文独立推导。只使用 Nomizu、Anosov 结构稳定性和标准椭圆估计，不使用新预印本的一般 Dolbeault 或统一化结论。

**67：** 有限商的闭性与等变接口另行给出；“全部模型基点皆开放”，进而整个含模型连通分支皆模型化，使用了 58 的新预印本主定理。不能把这一层说成完全不依赖新文献，也不能由 66 的闭性单独推出一般分支结论。

**未证明：** 全部三元组均位于一个模型分支、一般 Ghys 分类、其他非模型分支不存在、IHS 排除、任意拓扑共轭都自动光滑。

## 新公式核验

UT₄/UT₅ 的 80 组精确矩阵方向微分；三步 naive 平均值的 −E₁₄/48 残差与中心修正；实际紧致非 abelian 的 J♯；原模型固定闭二形式 12 维及 exact 固定部分为零；一个非半单代数反检验。结果见 notes/nil_period_progression_checks.json。

未重跑旧的 61–63 全套计算；没有用这些有限维检查代替 65–67 的分析与闭性证明。

## 有限新颖性检索

检索实际包括：

- Invariant forms compute the Dolbeault cohomology of complex nilmanifolds
- nilmanifolds / biholomorphism / affine
- complex nilmanifolds / biholomorphisms
- nilmanifolds / holomorphic maps / affine
- Moduli spaces for complex nilmanifolds / Wehler / affine
- holomorphic symplectic / Anosov / deformation rigidity
- Anosov / symplectic / period map / nilmanifold
- holomorphic Anosov / deformations / nilmanifolds

网络摘要只用于定位原始文件。没有把 ResearchGate 的全文转录作为定理输入。59、58 对应原始 arXiv 页分别为 https://arxiv.org/abs/2609.31516 和 https://arxiv.org/abs/2607.26786 。

原始 59 的全文关键词检查没有 Anosov 讨论；有限检索未找到 66 的周期闭性和 67 的保辛分支定理的完全对应表述。这仅记录检索边界，不证明首创性。小映射仿射性本身明确已有更强新文献，不能与这个仍需核验的动力学闭性问题混为一谈。

最后核对两份原始 arXiv 摘要页的 submission history：58、59 均显示 v1，所查看页面没有撤稿或替换提示。此状态核对不等于对其整个主证明做独立审定。
