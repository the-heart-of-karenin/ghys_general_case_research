# 真正的 Lagrangian 平面场：等价的秩五丛问题

日期：2026-10-18。性质：忘掉动力学之后的精确拓扑归约。它定位 32 中尚未解决的 unstable 结构群 reduction；没有把虚秩二类当成实际平面场。

后续状态更新：notes/36、37 已分别完成 K3^[2] 与 Kummer 四维型的真实 reduction，给出行列式类的必要充分判据；全部既有剩余候选确能实现。本记录中“尚未构造或排除”描述的是本记录完成时的阶段；实际存在性及其证明链见 36–37。可积性与动力学实现仍未解决。

## 1. 秩五实丛 W

令 (TX,Ω) 为复秩四辛丛，选择一个相容的正定 Hermitian 度量，把结构群约化到紧 Sp(2)。这一选择空间可缩，不改变下述拓扑对象的同构类。在 IHS 流形上，也可使用某个 Ricci-flat hyperkähler 度量。

Sp(2)≅Spin(5)。取其五维实标准表示得到一个有 spin 结构的秩五实丛 W，其复化为

\[
W_\mathbf C\simeq\Lambda^2_0(TX),
\tag{1}
\]

右侧是由 Ω contraction 取出的本原外二次幂，复秩为五。

这一秩五实表示及其特征类也可直接对照 23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf 的 §11、Lemma 11.1（PDF p.17），取其中 λ 为平凡线丛。

**等价命题：** (TX,Ω) 有连续复 Lagrangian 秩二子丛，当且仅当 W 有一个有向实秩二子丛 H。

理由是两个相关齐性空间同构：

\[
\operatorname{Lag}_\mathbf C(\mathbf C^4)
\simeq\operatorname{Sp}(2)/U(2)
\simeq SO(5)/(SO(2)\times SO(3))
=\operatorname{Gr}^+_2(\mathbf R^5).
\tag{2}
\]

这给出关联丛的同构及其连续截面的双射。先用任意互补 Lagrangian 丛形成双分裂并不是必要的额外条件；连续 Lagrangian 子丛可用相容度量取得连续互补。

## 2. 行列式与 Chern 关系的解释

若 E 为这样的 Lagrangian 子丛，L=det E，a=c_1(E)，则在对应的 U(2) reduction 下

\[
W\simeq L_\mathbf R\oplus\mathfrak{su}(E).
\tag{3}
\]

确实，TX≅E⊕E*，而 Λ²_0TX 的 U(2) 表示分解为 L⊕End_0(E)⊕L*，取相容实形式即 (3)。可以选择 H 的方向，使 e(H)=a。

设 c=c_2(X)、d=c_4(X)。计算 W 的特征类得

\[
w_2(W)=0,\qquad q_1(W)=p_1(W)/2=-c,
\qquad p_2(W)=c^2-4d.
\tag{4}
\]

例如对 TX 的形式 Chern 根 x,y,−x,−y，W_C 的根为 x+y、−x−y、x−y、−x+y、0；所以 p_1(W)=2(x²+y²)=−2c，p_2(W)=(x²−y²)²=c²−4d。

若 W=H⊕A，其中 H 是有向二平面、e(H)=a，A 为有向秩三，则

\[
w_2(A)=\rho_2(a),\qquad p_1(A)=-2c-a^2,
\qquad p_2(W)=a^2p_1(A).
\tag{5}
\]

(4)、(5) 的比较正好恢复

\[
4d=(c+a^2)^2.
\]

所以 28 的 Chern 恒等式是实际秩五丛二平面 reduction 的必要条件，但不是该 reduction 的充分条件。

## 3. 为什么现有简洁的模 12 判据不能直接用

31 说明两个标准变形类型中 a≡δ≠0 mod 2，因此 (5) 中 A 是非 spin 丛，而基流形 X 是 spin。

23_Cadek_Crabb_Vanzura_2008_Obstruction.pdf 的 Corollary 8.4 / Proposition 9.4 中的简洁判据要求所用的 l 同时约化为基流形的 w_2；当前若取 l=a，这个前提不成立。

因此，下一步真正的有限维拓扑问题是：对于具体的 spin 五维丛 W，能否构造/排除 (5) 所要求的非 spin 三维补丛，并验证 W 的实际分解。32 的复 K 理论实现还没有处理这个问题。

## 4. 动力学没有自动跟随这一归约

f 保持 Ω，但通常不保持所选正定相容度量，因而不能直接说它保持 W 的某个正定联络或由该度量确定的实形式。齐性空间 (2) 的度量描述主要用于忘掉动力学后的截面问题。

即使连续 H 存在，也还须对应到原 f 的真实统一收缩丛，并有可积的复叶片。这些要求不能从 W 的特征类或一个任意截面推出。

本记录完成的是拓扑问题的准确改写，既没有排除 H，也没有构造 H；不存在完整 Ghys 分类的结论。
