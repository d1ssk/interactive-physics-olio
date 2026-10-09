---
title: 単一場 slow-roll インフレーションでの量子揺らぎ
description: インフラトンのポテンシャルから決まる実際の背景の上で曲率摂動とテンソルのモードを解き、squeezing の進み方、de Sitter・Hankel 近似との違い、原始スペクトルを比較する記事。
---

# 単一場 slow-roll インフレーションの量子揺らぎと squeezing

<span class="center-material-tables"></span>

[前編「インフレーションの量子揺らぎと squeezing」](../inflation-squeezing/)では、曲率摂動 $\zeta$ の二次作用から出発して、一つの波数対の量子状態が two-mode squeezing（定在波で見れば二つの single-mode squeezing）を受けることを一般的に導きました。ただし具体的な計算は、厳密な de Sitter 時空の上の質量ゼロのスカラー場、つまり $z$ を $a$ に置き換えた模型で行い、曲率摂動にはその最低次の近似として当てはめました（前編 §8–9）。

この記事では、同じ計算を**インフラトンのポテンシャルから決まる実際の背景**の上で行います。背景を数値的に解いて $z(\eta)$ を求め、曲率摂動のモードをインフレーションの終了まで追います。記号と規約は前編をそのまま引き継ぎます。

<figure style="margin-inline: auto; text-align: center;">
  <img src="app/teaser.svg" alt="1.5 e-fold ずつずれて Hubble 半径を出る三つのモードの Wigner 等高線を、中央のモードの Hubble crossing の時刻に同じ座標軸の上に描いた図" width="720" height="250" style="display: block; max-width: 100%; height: auto; margin-inline: auto;">
</figure>

図は、Starobinsky 模型で 1.5 e-fold ずつずれて Hubble 半径を出る三つの波数の状態を、中央のモードがちょうど Hubble 半径を出る時刻に並べたものです（§6）。先に出たモードほど強く squeezing されています。

前編から変わるのは次の三点です。

- squeezing の係数 $s=z'/z$ が $\mathcal H$ と一致せず、$\mathcal H(1+\epsilon_2/2)$ になります。
- $\mathcal H=-1/\eta$ が成り立たず、$\ln x$ の 1 e-fold あたりの減少量が、de Sitter の1から $1-\epsilon_1$ に小さくなります。
- slow-roll パラメータが時間とともに変化し、インフレーションは $\epsilon_1=1$ で終わります。

その結果、Wigner 楕円の回転と squeezing という前編の構造はそのまま残りますが、それぞれの速さが slow-roll パラメータの程度だけ変わります。この小さな違いが、原始スペクトルの傾き $n_s-1$ やテンソル・スカラー比 $r$ として観測に現れます。

| 記号 | 意味（前編と共通） |
| --- | --- |
| $\eta$、$\mathcal H=a'/a$ | 共形時間と共形 Hubble パラメータ。プライムは $\eta$ 微分 |
| $v=z\zeta$、$\pi=v'-sv$、$s=z'/z$ | Mukhanov–Sasaki 変数、その共役運動量、squeezing の係数 |
| $f_k$、$g_k=f_k'-sf_k$ | 定在波成分 $\hat q,\hat p$ のモード関数（前編の式 (40)） |
| $Q=\sqrt k\,q$、$P=p/\sqrt k$ | 固定した quadrature。Wigner 図の座標軸 |
| $\Sigma$、$r_k$、$\varphi_k$ | 共分散行列、squeezing parameter、長軸の角度 |
| $\epsilon_1=-\dot H/H^2$、$\epsilon_2=d\ln\epsilon_1/d\ln a$ | Hubble flow パラメータ（前編の式 (83)–(84)） |

$\eta$ は前編と同じく共形時間です。ポテンシャルから作る slow-roll パラメータは $\epsilon_V,\eta_V$ と書き、共形時間と区別します。単位は $c=\hbar=1$ で、$M_{\mathrm{Pl}}$ は換算 Planck 質量です。

## 1. 背景：slow-roll するインフラトン

### e-fold 時間での背景方程式

一様なインフラトン $\phi_0(t)$ のエネルギー密度と圧力は $\rho=\frac12\dot\phi_0^2+V$、$p=\frac12\dot\phi_0^2-V$ です。これが支配する平坦な宇宙の Friedmann 方程式と場の運動方程式は

$$
H^2=\frac{1}{3M_{\mathrm{Pl}}^2}\left[\frac12\dot\phi_0^2+V(\phi_0)\right],\qquad\ddot\phi_0+3H\dot\phi_0+V_{,\phi}(\phi_0)=0\tag{1}\label{eq:slowroll-1}
$$

となります。第一式を時間微分すると $6M_{\mathrm{Pl}}^2H\dot H=\dot\phi_0\left(\ddot\phi_0+V_{,\phi}\right)$ が得られ、右辺の括弧を第二式を用いて $-3H\dot\phi_0$ に置き換えると

$$
\dot H=-\frac{\dot\phi_0^2}{2M_{\mathrm{Pl}}^2}=-\frac{\rho+p}{2M_{\mathrm{Pl}}^2}\tag{2}\label{eq:slowroll-2}
$$

が得られます。したがって、場が動いている限り $H$ は単調に減少します。

その減り方を 1 Hubble 時間あたりで測るのが、前編の式 (83) でも使った第一の Hubble flow パラメータ

$$
\epsilon_1\equiv-\frac{\dot H}{H^2},\qquad\frac{\ddot a}{a}=\dot H+H^2=H^2(1-\epsilon_1)\tag{3}\label{eq:slowroll-3}
$$

です。第二式は $\ddot a/a=d(\dot a/a)/dt+(\dot a/a)^2$ から従います。**加速膨張 $\ddot a>0$ は $\epsilon_1<1$ と同値**で、厳密な de Sitter 時空（$H$ が一定）は $\epsilon_1=0$ の極限です。$\eqref{eq:slowroll-2}$ と $\eqref{eq:slowroll-1}$ の第一式を代入すると、

$$
\epsilon_1=\frac{\dot\phi_0^2}{2M_{\mathrm{Pl}}^2H^2}=\frac{3\cdot\frac12\dot\phi_0^2}{\frac12\dot\phi_0^2+V}\tag{4}\label{eq:slowroll-4}
$$

となり、$\epsilon_1$ は場の運動エネルギーとポテンシャルの比で決まると分かります。$V\ge0$ なら $0\le\epsilon_1\le3$ で、$\epsilon_1<1$ は $\dot\phi_0^2<V$ と同じです。ポテンシャルが運動エネルギーより十分大きい間（$\dot\phi_0^2\ll V$）は $\epsilon_1\ll1$ で、ほぼ de Sitter 的な加速膨張が続きます。

モードの計算では時間変数として e-fold 数 $N=\ln a$ を使います。$dN=H\,dt$ なので、$\epsilon_1$ の定義は $\epsilon_1=-d\ln H/dN$ と書け、$\dot\phi_0=H\phi_{0,N}$ (添字 $N$ は $N$ 微分を表します) を $\eqref{eq:slowroll-4}$ の第一の形に代入すると

$$
\epsilon_1=-\frac{d\ln H}{dN}=\frac{\phi_{0,N}^2}{2M_{\mathrm{Pl}}^2}\tag{5}\label{eq:slowroll-5}
$$

です。したがって、$\epsilon_1$ は、1 e-fold あたりに場が $M_{\mathrm{Pl}}$ 単位でどれだけ動くかだけで決まります。

$H$ を消去した方程式も作っておきます。$\eqref{eq:slowroll-1}$ の第一式に $\dot\phi_0^2=H^2\phi_{0,N}^2=2M_{\mathrm{Pl}}^2H^2\epsilon_1$ を入れると $3M_{\mathrm{Pl}}^2H^2=M_{\mathrm{Pl}}^2H^2\epsilon_1+V$、すなわち $H^2(3-\epsilon_1)M_{\mathrm{Pl}}^2=V$ です。第二式には $\ddot\phi_0=H\,d(H\phi_{0,N})/dN=H^2(\phi_{0,NN}-\epsilon_1\phi_{0,N})$ を代入して $H^2$ で割ると、$H$ を含まない場の方程式

$$
H^2=\frac{V}{M_{\mathrm{Pl}}^2(3-\epsilon_1)},\qquad\phi_{0,NN}+(3-\epsilon_1)\left(\phi_{0,N}+M_{\mathrm{Pl}}^2\frac{V_{,\phi}}{V}\right)=0\tag{6}\label{eq:slowroll-6}
$$

が得られます。$\phi_0,\phi_{0,N}$ を与えれば $\eqref{eq:slowroll-5}$ と $\eqref{eq:slowroll-6}$ の第一式から $\epsilon_1$ と $H$ が代数的に決まるので、第二式は $\phi_0(N)$ についての閉じた二階の常微分方程式です。

この方程式を解くと、次の経過をたどります。ポテンシャルの斜面の上部では $\dot\phi_0^2\ll V$ で $\epsilon_1\ll1$ です。場が谷に近づくと $V$ が下がり、運動エネルギーの割合と $\epsilon_1$ が増えます。$\epsilon_1$ が 1 に達すると $\eqref{eq:slowroll-3}$ の $\ddot a$ の符号が変わり、加速膨張が止まります。そこで**インフレーションの終了を $\epsilon_1=1$ で定義**し、その時刻 $N_{\mathrm{end}}$ まで数値的に積分します。

その後、場はポテンシャルの極小のまわりで振動し、他の場との相互作用によって再加熱が起きますが、それはこの記事では扱いません。注目するモードはすべて $N_{\mathrm{end}}$ より前に Hubble 半径を出ます。Hubble 半径より長い波長の曲率摂動は、エントロピー揺らぎが無視できる単一場の場合にはインフレーション後も保存されるので、終了時刻での値がそのまま後の宇宙の初期条件になります。なお、後の「模型」で $\phi_{\mathrm{end}}$ を見積もるのに使う $\epsilon_V=1$ は近似で、数値計算では厳密な $\epsilon_1=1$ を使います。

### Hubble flow パラメータと slow-roll 近似

$\epsilon_1$ の時間変化は、Hubble flow パラメータの列

$$
\epsilon_{n+1}=\frac{d\ln\epsilon_n}{dN},\qquad\epsilon_2=\frac{2\phi_{0,NN}}{\phi_{0,N}}\tag{7}\label{eq:slowroll-7}
$$

で表します。第二式は $\eqref{eq:slowroll-5}$ の対数微分です。どちらも数値解から厳密に計算できます。

slow-roll 近似では $\eqref{eq:slowroll-6}$ の $\phi_{0,NN}$ を落とし、$\epsilon_1\ll3$ として $\phi_{0,N}\simeq-M_{\mathrm{Pl}}^2V_{,\phi}/V$ とします。これを $\eqref{eq:slowroll-5}$ と $\eqref{eq:slowroll-7}$ に代入すると、ポテンシャルの形だけで決まるパラメータ

$$
\epsilon_1\simeq\epsilon_V\equiv\frac{M_{\mathrm{Pl}}^2}{2}\left(\frac{V_{,\phi}}{V}\right)^2,\qquad\epsilon_2\simeq4\epsilon_V-2\eta_V,\qquad\eta_V\equiv M_{\mathrm{Pl}}^2\frac{V_{,\phi\phi}}{V}\tag{8}\label{eq:slowroll-8}
$$

が得られます。第二式は $\phi_{0,NN}\simeq-M_{\mathrm{Pl}}^2\left[V_{,\phi\phi}/V-(V_{,\phi}/V)^2\right]\phi_{0,N}$ から従います。また、インフレーション終了までの残りの e-fold 数は

$$
N_{\mathrm{end}}-N\simeq\frac{1}{M_{\mathrm{Pl}}^2}\int_{\phi_{\mathrm{end}}}^{\phi_0}\frac{V}{V_{,\phi}}\,d\phi\tag{9}\label{eq:slowroll-9}
$$

です。ある波数 $k_*$（pivot）が Hubble 半径を出る時刻を $N_{\mathrm{cross},*}$、その時刻の残り e-fold 数を $N_*=N_{\mathrm{end}}-N_{\mathrm{cross},*}$ と書きます。今後、図の横軸には crossing からの経過時間 $N-N_{\mathrm{cross},*}$ を使います。CMB で観測されるスケールでは、インフレーション後の再加熱と hot big bang の歴史にから $N_*\approx50$–$60$ と分かっています。

一般的な教科書の表記との対応も記しておきます。例えば松原『宇宙論の物理（下）』（参考文献）の第 8 章は共形時間を $\tau$、ポテンシャルの slow-roll パラメータを $\epsilon,\eta$（この記事の $\epsilon_V,\eta_V$）と書き、$m_{\mathrm{Pl}}=G^{-1/2}=\sqrt{8\pi}\,M_{\mathrm{Pl}}$ を使っています。

### 模型

次の三種類のポテンシャルを使います。$\epsilon_1,\epsilon_2$ の欄は $\eqref{eq:slowroll-8}$ と $\eqref{eq:slowroll-9}$ から求めた、残り e-fold 数 $\Delta N=N_{\mathrm{end}}-N\gg1$ での主要項です。数値計算はこれらの近似式を使わず、$\eqref{eq:slowroll-6}$ を直接解いています。

| 模型 | $V(\phi)$ | $\epsilon_1$ | $\epsilon_2$ |
| --- | --- | --- | --- |
| Starobinsky | $V_0\left(1-e^{-\sqrt{2/3}\,\phi/M_{\mathrm{Pl}}}\right)^2$ | $\dfrac{3}{4\Delta N^2}$ | $\dfrac{2}{\Delta N}$ |
| 単項式（$p=2/3,\,2,\,4$） | $\lambda\,\phi^p$ | $\dfrac{p}{4\Delta N+p}$ | $\dfrac{4}{4\Delta N+p}$ |
| べき乗則 | $V_0\,e^{-\lambda\phi/M_{\mathrm{Pl}}}$ | $\dfrac{\lambda^2}{2}$（厳密） | $0$ |

単項式では $\epsilon_V=p^2M_{\mathrm{Pl}}^2/(2\phi_0^2)$、$\eta_V=p(p-1)M_{\mathrm{Pl}}^2/\phi_0^2$ と、$\eqref{eq:slowroll-9}$ から得られる $\phi_0^2/M_{\mathrm{Pl}}^2\simeq2p\Delta N+p^2/2$ を組み合わせます。$\phi_{\mathrm{end}}^2\simeq p^2M_{\mathrm{Pl}}^2/2$ は $\epsilon_V=1$ から決めました。$p=2,4$ は大きな場のインフレーション（カオス的インフレーション）にあたります。Starobinsky 模型は平坦な台地を持つポテンシャルの代表例で、$\epsilon_1$ が $\epsilon_2$ よりずっと小さくなります。べき乗則インフレーションは $\epsilon_1$ が厳密に一定で、§4 の解析解が厳密になる例です。ただしこの模型だけではインフレーションが終わらないので、比較のための参照として使います。

ポテンシャルの全体の大きさ（Starobinsky 模型とべき乗則では $V_0$、単項式では $\lambda$）は $H$ とパワースペクトルの規格化を変えるだけで、$x=k/(aH)$ の関数として見たモードの時間発展には影響しません。べき乗則の $\lambda$ はポテンシャルの傾きを決め、$\epsilon_1=\lambda^2/2$ を通じて背景とモードの時間発展を変えます。スペクトルを描くときだけ、pivot でのスカラーのパワーが $2.1\times10^{-9}$ になるよう規格化します。

<iframe src="app/supporting.html?lang=ja&amp;view=background" title="slow-roll 背景のポテンシャルと Hubble flow パラメータ" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 620px; border: 0; overflow: hidden;" loading="eager"></iframe>

ポテンシャルを切り替えて、$\epsilon_1,\epsilon_2$ がほとんどの期間で小さく、最後の数 e-fold で急に大きくなることを確かめてください。ポテンシャルから見積もった $\epsilon_V$、$4\epsilon_V-2\eta_V$ は、両者が小さい間は厳密な値とよく一致します。

## 2. 曲率摂動の Hamilton 流

### 運動方程式と squeezing の係数

前編の式 (37) の Hamiltonian から、一つの定在波成分の Heisenberg 方程式は

$$
\hat q_{A,\mathbf k}'=\hat p_{A,\mathbf k}+s\,\hat q_{A,\mathbf k},\qquad\hat p_{A,\mathbf k}'=-k^2\hat q_{A,\mathbf k}-s\,\hat p_{A,\mathbf k}\tag{10}\label{eq:slowroll-10}
$$

です。ここまでは $z(\eta)$ の形によりません。前編の式 (83) の $z^2=2a^2\epsilon_1M_{\mathrm{Pl}}^2$ から $\ln|z|=\ln a+\frac12\ln\epsilon_1+\text{const}$ なので、$d/d\eta=\mathcal H\,d/dN$ を使って

$$
s=\frac{z'}{z}=\mathcal H\,\frac{d\ln|z|}{dN}=\mathcal H\left(1+\frac{\epsilon_2}{2}\right)\tag{11}\label{eq:slowroll-11}
$$

です。$z=a\dot\phi_0/H$ の符号は $\dot\phi_0$ の向きで決まりますが、$s$ には現れません。**$\epsilon_2>0$ の背景では、squeezing の係数が de Sitter のテスト場の $\mathcal H$ より $\epsilon_2/2$ の割合だけ大きくなります。**

### e-fold 時間での位相空間の流れ

$Q=\sqrt k\,q$、$P=p/\sqrt k$ に移り、$\eqref{eq:slowroll-10}$ を $\mathcal H$ で割って $N$ 微分に直すと

$$
\frac{d\hat{\mathbf Z}}{dN}=A(N)\,\hat{\mathbf Z},\qquad A=x\begin{pmatrix}0&1\\-1&0\end{pmatrix}+\sigma\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad x=\frac{k}{\mathcal H},\qquad\sigma=\frac{s}{\mathcal H}=1+\frac{\epsilon_2}{2}\tag{12}\label{eq:slowroll-12}
$$

を得ます。$\hat{\mathbf Z}=(\hat Q,\hat P)^T$ です。時間変数を $\eta$ から $N$ に替えると、時間発展 $d\hat O/dN=i[\hat K_N,\hat O]$ を生成する Hamiltonian は、前編の式 (37) の $\hat H_{A,\mathbf k}$ を $\mathcal H$ で割った $\hat K_N=\hat H_{A,\mathbf k}/\mathcal H$ になります（$d\eta=dN/\mathcal H$ のため）。quadrature で書くと

$$
\hat K_N=\frac x2\left(\hat Q^2+\hat P^2\right)+\frac\sigma2\left(\hat Q\hat P+\hat P\hat Q\right)\tag{13}\label{eq:slowroll-13}
$$

です。第一項が回転 $xJ$ を、第二項が squeeze $\sigma D$ を生みます。

$x$ の時間変化は $x=k/(aH)$ の定義と $\eqref{eq:slowroll-5}$ から

$$
\frac{d\ln x}{dN}=-\frac{d\ln(aH)}{dN}=-(1-\epsilon_1)\tag{14}\label{eq:slowroll-14}
$$

です。

前編の式 (76)–(77) は $\sigma=1$、$x=e^{-N}$ の場合でした。**一般の slow-roll 背景でも、流れは「回転 $xJ$」と「スクイーズ $\sigma D$」の和という同じ形をしています。** 違いは次の二点だけです。

1. スクイーズの速さが $\sigma=1+\epsilon_2/2$ になる。
2. 回転の速さ $x$ の減り方が $1-\epsilon_1$ に遅くなる。

$A$ の固有値は $\pm\sqrt{\sigma^2-x^2}$ で、$x>\sigma$ では楕円型（回転）、$x<\sigma$ では双曲型（伸長と収縮）の流れです。

ここまでスカラー揺らぎで論じてきましたが、テンソル揺らぎも同じ構造となります。各偏極を $e^{(\lambda)}_{ij}e^{(\lambda')}_{ij}=\delta_{\lambda\lambda'}$ の偏極テンソルで展開すると、正準変数は $v_T=(aM_{\mathrm{Pl}}/2)\,h_\lambda$ で、$z_T=aM_{\mathrm{Pl}}/2$ は $a$ に比例します。したがって**テンソルでは厳密に $\sigma_T=1$** で、前編のスカラー場のモードの流れがそのままテンソル揺らぎのモードの流れになります。slow-roll 背景で変わるのは、$\eqref{eq:slowroll-14}$ の $x$ の減り方だけです。

### 二階の方程式：勾配項と背景項の競合

$\eqref{eq:slowroll-10}$ から $\hat p$ を消去すると、前編の式 (39) の $\hat q''+(k^2-z''/z)\hat q=0$ に戻ります。$z''/z=s'+s^2$ と、$\mathcal H'=\mathcal H^2(1-\epsilon_1)$、$d\sigma/dN=\epsilon_2\epsilon_3/2$ を使うと $z''/z=\mathcal H^2\left[(1-\epsilon_1)\sigma+\sigma^2+\epsilon_2\epsilon_3/2\right]$ で、$\sigma=1+\epsilon_2/2$ を代入して展開すれば、近似なしに

$$
\frac{z''}{z}=\mathcal H^2\left[2-\epsilon_1+\frac32\epsilon_2-\frac12\epsilon_1\epsilon_2+\frac14\epsilon_2^2+\frac12\epsilon_2\epsilon_3\right],\qquad\frac{a''}{a}=\mathcal H^2(2-\epsilon_1)\tag{15}\label{eq:slowroll-15}
$$

が得られます。一次までとると前編の式 (84) に一致します。$a''/a$ はテンソル摂動の場合の背景項です。

二階の方程式で見ると、勾配項 $k^2$ が背景項 $z''/z$ を下回る $x^2\simeq2$ を境に、振動解から成長・減衰解へ移ります。一階の流れ $\eqref{eq:slowroll-12}$ で見ると、境目は $x=\sigma\simeq1$ です。どちらの「境目」も同じ滑らかな時間発展を別の形で書いたときの目安で、その時刻に何か特別なことが起きるわけではありません。

<iframe src="app/supporting.html?lang=ja&amp;view=frequencies" title="三つの波数の勾配項と背景項、回転とスクイーズの速さの比較" data-auto-height scrolling="no" style="display: block; width: 100%; height: 980px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

左の図では、三つの $x_j^2$ が順に $z''/(z\mathcal H^2)\simeq2$ を横切ります。右の図は同じことを $x_j$ と $\sigma$ の比較で表したものです。$N_*$ を小さくしてインフレーションの終わり近くを選ぶと、背景項が 2 や 1 から離れていく様子が見えます。

## 3. Bunch–Davies 状態と数値解

### 無次元のモード係数

前編の式 (40) では、定在波成分の演算子を in 演算子で $\hat q=f_k\hat b^{\mathrm{in}}+f_k^*\hat b^{\mathrm{in}\dagger}$、$\hat p=g_k\hat b^{\mathrm{in}}+g_k^*\hat b^{\mathrm{in}\dagger}$ と展開しました。quadrature に合わせて無次元のモード関数

$$
F_k=\sqrt k\,f_k,\qquad G_k=\frac{g_k}{\sqrt k},\qquad\hat Q=F_k\hat b^{\mathrm{in}}+F_k^*\hat b^{\mathrm{in}\dagger},\qquad\hat P=G_k\hat b^{\mathrm{in}}+G_k^*\hat b^{\mathrm{in}\dagger}\tag{16}\label{eq:slowroll-16}
$$

を定義します。$\eqref{eq:slowroll-12}$ は線形なので、$(F_k,G_k)^T$ も同じ方程式 $d(F_k,G_k)^T/dN=A\,(F_k,G_k)^T$ に従います。Wronskian 条件（前編の式 (41)）は

$$
F_kG_k^*-F_k^*G_k=i\tag{17}\label{eq:slowroll-17}
$$

で、$\operatorname{tr}A=0$ のため時間によらず保たれます。実際、$\eqref{eq:slowroll-12}$ を代入すると $x$ の項も $\sigma$ の項も打ち消し合います。

前編 §5–7 の量はすべて $F_k,G_k$ で書けます。

$$
\Sigma=\begin{pmatrix}|F_k|^2&\operatorname{Re}(F_kG_k^*)\\\operatorname{Re}(F_kG_k^*)&|G_k|^2\end{pmatrix},\qquad\alpha_k=\frac{F_k+iG_k}{\sqrt2},\qquad\beta_k=\frac{F_k^*+iG_k^*}{\sqrt2}\tag{18}\label{eq:slowroll-18}
$$

$\det\Sigma=1/4$ は $\eqref{eq:slowroll-17}$ から従い、$r_k=\operatorname{arsinh}|\beta_k|$、$\varphi_k=\frac12\arg(\alpha_k\beta_k)$ は前編の式 (49)、(62) の通りです。

### 曲率のパワースペクトル

前編の式 (46) の $P_\zeta=|f_k|^2/z^2$ に $z^2=2a^2\epsilon_1M_{\mathrm{Pl}}^2$ と $k/a=xH$ を入れると、無次元のパワースペクトルは

$$
\mathcal P_\zeta(k,N)=\frac{k^3}{2\pi^2}\frac{|F_k|^2}{k\,z^2}=\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\cdot2x^2|F_k|^2\tag{19}\label{eq:slowroll-19}
$$

です。de Sitter のテスト場では $2x^2|F_k|^2=1+x^2$ なので、この因子は前編の式 (75) の $1+x^2$ にあたります。slow-roll 背景では、因子 $2x^2|F_k|^2$ も $H^2/\epsilon_1$ も時間とともに変化しますが、Hubble 半径を出た後は積が一定になります（§5）。

### 初期条件と数値積分

短波長 $x\gg\sigma$ では $\eqref{eq:slowroll-12}$ の回転が優勢で、前編の式 (43) と同じく $F_k\to e^{-ik\eta}/\sqrt2$、$G_k\to-ie^{-ik\eta}/\sqrt2$ が Bunch–Davies 条件です。全体の位相は物理量に効かないので、$\eta$ そのものは必要ありません。数値計算では背景の $\eqref{eq:slowroll-6}$ と $\eqref{eq:slowroll-12}$ を $N$ について同時に積分し、$x=100$ の時刻から始めます。初期値には、§4 の Hankel 関数の解をその時刻のパラメータで評価したものを使います。この解は $1/x$ の補正まで Bunch–Davies 状態を再現するので、初期値の誤差は slow-roll パラメータの変化率と $1/x$ の積の程度に抑えられます。

位相の規約は前編に合わせ、晩期に保存される $\zeta_k$ の成分が正の虚部になるよう全体の位相を選びます（前編の式 (74)）。

## 4. 定数 slow-roll 近似：Hankel 関数による解

### 共形時間と指数 $\nu$

slow-roll パラメータを局所的に固定する近似で、モード方程式を解析的に解きます。これは crossing 付近の近似です。$\epsilon_1$ が厳密に一定なら、定義から $\epsilon_2=0$ でなければなりません。$\mathcal H'=\mathcal H^2(1-\epsilon_1)$ は $d(1/\mathcal H)/d\eta=-(1-\epsilon_1)$ と書けるので、$\epsilon_1$ を固定し、無限の未来で $\eta\to0$ となるよう積分定数を選ぶと

$$
\eta=-\frac{1}{(1-\epsilon_1)\mathcal H}\tag{20}\label{eq:slowroll-20}
$$

です。これを $\eqref{eq:slowroll-15}$ の一次の項と組み合わせると

$$
\frac{z''}{z}=\frac{\nu^2-1/4}{\eta^2},\qquad\nu^2=\frac14+\frac{2-\epsilon_1+\frac32\epsilon_2}{(1-\epsilon_1)^2}\simeq\frac94+3\epsilon_1+\frac32\epsilon_2,\qquad\nu\simeq\frac32+\epsilon_1+\frac{\epsilon_2}{2}\tag{21}\label{eq:slowroll-21}
$$

となります。$\eqref{eq:slowroll-8}$ を使えば $\nu\simeq3/2+3\epsilon_V-\eta_V$ です。テンソル揺らぎでは $a''/a$ から $\nu_T\simeq3/2+\epsilon_1$ です。べき乗則インフレーションでは $\epsilon_2=0$ で、$\nu=3/2+\epsilon_1/(1-\epsilon_1)$ が厳密に成り立ちます。

### Hankel 関数の解

モード方程式 $f_k''+\left[k^2-(\nu^2-1/4)/\eta^2\right]f_k=0$ は、$y=-k\eta$ として $f_k=\sqrt{-\eta}\,\mathcal C_\nu(y)$ と置くと $\nu$ 次の Bessel 方程式になります。$y\to\infty$ で Bunch–Davies 条件を満たす解を選ぶと

$$
F_k=\frac{\sqrt\pi}{2}e^{i\pi(\nu+1/2)/2}\sqrt y\,H^{(1)}_\nu(y),\qquad G_k=-\frac{\sqrt\pi}{2}e^{i\pi(\nu+1/2)/2}\sqrt y\,H^{(1)}_{\nu-1}(y),\qquad y=-k\eta=\frac{x}{1-\epsilon_1}\tag{22}\label{eq:slowroll-22}
$$

です。最後の等号は $\eqref{eq:slowroll-20}$ によります。$G_k$ は次のように求めます。この近似では $z\propto(-\eta)^{1/2-\nu}$ なので $s=(\nu-\tfrac12)/(-\eta)$ で、$d/d\eta=-k\,d/dy$ から

$$
G_k=\frac{f_k'-sf_k}{\sqrt k}=-\frac{dF_k}{dy}-\frac{\nu-1/2}{y}F_k=-\frac{\sqrt\pi}{2}e^{i\pi(\nu+1/2)/2}\sqrt y\left[\frac{dH^{(1)}_\nu}{dy}+\frac\nu yH^{(1)}_\nu\right]\tag{23}\label{eq:slowroll-23}
$$

となり、漸化式 $dH_\nu/dy+(\nu/y)H_\nu=H_{\nu-1}$ で $\eqref{eq:slowroll-22}$ の形になります。

いくつか確かめておきます。

- **Bunch–Davies 条件：** $H^{(1)}_\nu(y)\to\sqrt{2/(\pi y)}\,e^{i(y-\pi\nu/2-\pi/4)}$ を代入すると、$F_k\to e^{iy}/\sqrt2$、$G_k\to-ie^{iy}/\sqrt2$ です。$e^{iy}=e^{-ik\eta}$ なので、§3 の条件と一致します。
- **Wronskian：** $H^{(1)}_\nu H^{(2)}_{\nu-1}-H^{(2)}_\nu H^{(1)}_{\nu-1}=-4i/(\pi y)$ から $\eqref{eq:slowroll-17}$ が成り立ちます。
- **de Sitter 極限：** $\nu=3/2$ では $H^{(1)}_{3/2}(y)=-\sqrt{2/(\pi y)}\,(1+i/y)\,e^{iy}$、$H^{(1)}_{1/2}(y)=-i\sqrt{2/(\pi y)}\,e^{iy}$ で、前編の式 (69) の $F_k=(1+i/x)e^{ix}/\sqrt2$、$G_k=-ie^{ix}/\sqrt2$ に戻ります。

### 長波長での振る舞いとスペクトル

$y\to0$ では $H^{(1)}_\nu(y)\simeq-(i/\pi)\,\Gamma(\nu)\,(2/y)^\nu$ なので $|F_k|^2\simeq\Gamma(\nu)^2\,2^{2\nu-2}\,y^{1-2\nu}/\pi$ です。$x=(1-\epsilon_1)y$ と $\Gamma(3/2)^2=\pi/4$ を使って $\eqref{eq:slowroll-19}$ に入れると

$$
\mathcal P_\zeta\simeq\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\,(1-\epsilon_1)^2\left[\frac{2^{\nu-3/2}\,\Gamma(\nu)}{\Gamma(3/2)}\right]^2(-k\eta)^{3-2\nu}\tag{24}\label{eq:slowroll-24}
$$

となります。この近似の範囲で右辺は時間によらないので、$k=aH$、すなわち $-k\eta=1/(1-\epsilon_1)$ で評価します。$\delta=\nu-3/2=\epsilon_1+\epsilon_2/2$ について一次まで展開すると、$2^{\nu-3/2}\simeq1+\delta\ln2$、$\Gamma(\nu)/\Gamma(3/2)\simeq1+\delta\,\psi(3/2)$、$\psi(3/2)=2-\gamma_{\mathrm E}-2\ln2$、$(1-\epsilon_1)^{2\nu-1}\simeq1-2\epsilon_1$ なので ($\psi$ は digamma 関数)

$$
\mathcal P_\zeta(k)\simeq\left.\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{k=aH}\left[1-2(C+1)\epsilon_1-C\epsilon_2\right],\qquad C=\gamma_{\mathrm E}+\ln2-2\simeq-0.7296\tag{25}\label{eq:slowroll-25}
$$

です。$\gamma_{\mathrm E}$ は Euler–Mascheroni 定数です。角括弧が次の次数の補正（Stewart–Lyth の補正）です。

背景量を $k=aH$ で評価するので、スペクトルの $k$ 依存性は crossing の時刻を通じて入ります。波数 $k$ の Hubble crossing 時刻を $N_k$ とすると、$k=a(N_k)H(N_k)$ なので、$\eqref{eq:slowroll-5}$ から

$$
\frac{d\ln k}{dN_k}=1+\frac{d\ln H}{dN_k}=1-\epsilon_1,\qquad
\frac{d}{d\ln k}=\frac{1}{1-\epsilon_1}\frac{d}{dN_k}.
$$

一方、最低次のパワースペクトルは

$$
\mathcal P_\zeta(k)\simeq\left.\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{N=N_k}
$$

です。その対数を微分し、$d\ln H/dN=-\epsilon_1$ と $\eqref{eq:slowroll-7}$ の $d\ln\epsilon_1/dN=\epsilon_2$ を使うと、

$$
\begin{aligned}
\frac{d\ln\mathcal P_\zeta}{d\ln k}
&=\frac{1}{1-\epsilon_1}\left(2\frac{d\ln H}{dN_k}-\frac{d\ln\epsilon_1}{dN_k}\right)+O(\epsilon^2)\\
&=\frac{-2\epsilon_1-\epsilon_2}{1-\epsilon_1}+O(\epsilon^2)\\
&=-2\epsilon_1-\epsilon_2+O(\epsilon^2).
\end{aligned}
$$

ここで背景量はすべて $N=N_k$ で評価し、$O(\epsilon^2)$ は slow-roll パラメータの二次以上の項を表します。分子がすでに一次なので、分母の $1/(1-\epsilon_1)$ による補正は二次からです。また、$d\epsilon_1/dN=\epsilon_1\epsilon_2$、$d\epsilon_2/dN=\epsilon_2\epsilon_3$ より、$\eqref{eq:slowroll-25}$ の振幅補正を微分した寄与も二次から現れます。さらに $\eqref{eq:slowroll-21}$ の $\nu\simeq3/2+\epsilon_1+\epsilon_2/2$ を使うと、

$$
n_s-1\equiv\frac{d\ln\mathcal P_\zeta}{d\ln k}\simeq-2\epsilon_1-\epsilon_2\simeq3-2\nu\tag{26}\label{eq:slowroll-26}
$$

です。テンソルでは $\nu_T$ と $\eqref{eq:slowroll-19}$ の $z$ を $z_T$ に置き換えて、二つの偏極の和について

$$
\mathcal P_T(k)\simeq\left.\frac{2H^2}{\pi^2M_{\mathrm{Pl}}^2}\right|_{k=aH}\left[1-2(C+1)\epsilon_1\right],\qquad n_T\simeq-2\epsilon_1,\qquad r\equiv\frac{\mathcal P_T}{\mathcal P_\zeta}\simeq16\epsilon_1=-8n_T\tag{27}\label{eq:slowroll-27}
$$

となります。最後の関係が単一場 slow-roll の無矛盾性関係です。

## 5. モード関数：数値解と近似解の比較

### 長波長での成長解と減衰解

長波長展開の勾配の零次では、$\eqref{eq:slowroll-12}$ は $dQ/dN=\sigma Q$、$dP/dN=-\sigma P$ に分かれます。$\sigma=d\ln|z|/dN$ なので、場の成長成分と、独立な運動量の減衰成分は

$$
Q_{\mathrm{grow}}\propto z,\qquad P_{\mathrm{dec}}\propto\frac1z\qquad(x\to0)\tag{28}\label{eq:slowroll-28}
$$

です。第一の成分は $\zeta=v/z$ が一定、すなわち**曲率摂動の保存**を表します。独立な減衰成分は $\pi=z\zeta'\propto1/z$、したがって $\zeta'\propto1/z^2$ を満たし、前編の式 (85) の項 $\int d\eta/z^2$ にあたります。ただし、運動量全体が $1/z$ に比例して減衰するわけではありません。有限の $k$ では、成長解も $-xQ$ を通じて運動量を持ちます。
<!-- 勾配の主要な補正を残して flow パラメータを局所的に固定すると、$P_{\mathrm{grow}}\simeq-xQ_{\mathrm{grow}}/(1+\epsilon_1+\epsilon_2)$ です。$x\ll1$ でも $Q_{\mathrm{grow}}$ は大きいので、運動量の方程式でこの項が無視できるとは限りません。例えば de Sitter 背景のスカラー場の極限では、BD モードは晩期にも $|G_k|=1/\sqrt2$ を保ちます。 -->

前編の de Sitter 背景のスカラー場では $z\to a$ で、正準変数は $a$ に比例して増えました。slow-roll 背景では $|F_k|\propto z=a\sqrt{2\epsilon_1}M_{\mathrm{Pl}}$ なので、$\epsilon_1$ が大きくなるにつれて de Sitter の場合より速く増えます。同じ $x$ での de Sitter の解 $|F_{\mathrm{dS}}|\simeq1/(\sqrt2\,x)$ との比は $x\,z\propto\sqrt{\epsilon_1}/H$ に比例し、crossing の後に少しずつ 1 から離れていきます。

一方、凍結した $\zeta_k=F_k/(\sqrt k\,z)$ の大きさは、crossing の付近で決まる $H_k/\sqrt{\epsilon_{1,k}}$ に比例します。この値が crossing の時刻を通じて波数ごとに少しずつ異なることが、$\eqref{eq:slowroll-26}$ のスペクトルの傾きになります。

図では、数値解を Hankel 近似と de Sitter の解と比較します。crossing 付近での一致と、その後に生じるずれに注目してください（[Hankel 近似の詳しい定義](#hankel-reference)）。

<iframe src="app/supporting.html?lang=ja&amp;view=modes" title="pivot モードの数値解と Hankel 近似、de Sitter テスト場の比較" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 620px; border: 0; overflow: hidden;" loading="eager"></iframe>

表示を切り替えて、次の点を確かめてください。

- **正準変数：** crossing の前は三つの曲線がほぼ重なり、後では数値解と Hankel 近似が de Sitter から少しずつ離れます。
- **曲率摂動：** crossing の後、$\zeta_k$ の虚部（保存成分）がインフレーションの終了まで一定に保たれ、実部（減衰成分）は消えていきます。
- **比：** Hankel 参照解は crossing 付近ではよく一致しますが、多くの e-fold にわたってずれが蓄積し、終了付近で大きくなります。Starobinsky 模型の $N_*=55$ では、$|F|/|F_\nu|$ は crossing の 5 e-fold 後で約 $1.004$、25 e-fold 後で $1.15$、終了時には $51.3$ です。$N_*$ が大きくても、定数 $\nu$ の近似が全履歴にわたって有効なわけではありません。$N_*=5$ では、このずれを短い時間範囲で確認できます。

## 6. 三つの波数の squeezing

### late time の squeezing と $z$ の成長

$x\ll1$ では楕円の長軸がほぼ $Q$ 軸を向き（$\varphi_k\to0$）、$\Sigma_{QQ}=|F_k|^2\simeq\frac12e^{2r_k}$ です。$\eqref{eq:slowroll-19}$ と組み合わせると

$$
e^{2r_k}\simeq2|F_k|^2=\frac{4\pi^2z^2}{k^2}\,\mathcal P_\zeta(k)\qquad(x\ll1)\tag{29}\label{eq:slowroll-29}
$$

です。凍結した $\mathcal P_\zeta(k)$ は一定なので、$r_k$ は定数を除いて $\ln z$ とともに増え、1 e-fold あたりの増え方は $\sigma=1+\epsilon_2/2$ に近づきます。最低次の $\mathcal P_\zeta\simeq H_k^2/(8\pi^2\epsilon_{1,k}M_{\mathrm{Pl}}^2)$（添字 $k$ は crossing での値）を入れると、$k=a_kH_k$ から

$$
r_k\simeq\ln\frac{z}{z_k}=\ln\frac{a}{a_k}+\frac12\ln\frac{\epsilon_1}{\epsilon_{1,k}}\tag{30}\label{eq:slowroll-30}
$$

となります。de Sitter のテスト場では第二項がなく、前編の $r_k\simeq N$ に戻ります。

インフレーションの終了時（$\epsilon_1=1$）には、$N_*=55$ の pivot モードについて、この式から Starobinsky 模型で $r_{k_*}\simeq55+\frac12\ln\!\left[1/(2.3\times10^{-4})\right]\simeq59.2$、$\phi^2$ 模型で $57.3$ と見積もられ、数値解の値（59.21、57.35）とよく一致します。$e^{-2r_k}\sim10^{-51}$ という極端に細い楕円です。

### アニメーション

三つの波数 $k_1<k_2=k_*<k_3$ を、Hubble crossing が 1.5 e-fold ずつずれるように選びます。時間軸は $N-N_{\mathrm{cross},*}$ で、$k_*$ の crossing を 0 とします。

<span id="main-animation"></span>

<iframe src="app/index.html?lang=ja" title="三つの波数の Wigner 楕円が順に squeezing されるアニメーションと、勾配項・背景項・squeezing の大きさの時間変化" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1900px; min-height: 1000px; border: 0; overflow: hidden;" loading="eager"></iframe>

次の点に注目してください。

1. **順番：** 上の帯グラフで $x_j^2$ が背景項を下回る順に、パネルの楕円が回転をやめて伸び始めます。三つの状態は同じ形の変形を、時間をずらして受けます。
2. **de Sitter との差：** $N_*=55$ では破線（同じ $x$ での de Sitter テスト場）とほとんど区別できません。$N_*=5$ や、べき乗則で $\epsilon_1=0.3$ を選ぶと、同じ $x$ でも楕円がより強く squeezing され、下の帯グラフで実線が破線から離れます。
3. **面積：** どの時刻でも楕円の面積は真空の円と同じです（$\det\Sigma=1/4$）。

同じ $x$ で比べると、べき乗則での squeezing の強まりは $\ln(1/x)$ あたりの増え方 $\sigma/(1-\epsilon_1)\simeq\nu-\frac12$ が 1 より大きいことから来ています。これは $\eqref{eq:slowroll-26}$ のスペクトルの傾きと同じ数 $\nu$ です。

## 7. 原始スペクトルとテンソル

約 40 個の波数について、Hubble 半径の十分内側からインフレーションの終了までモードを数値的に追い、終了時の $\mathcal P_\zeta$ と $\mathcal P_T$ を求めました。

<iframe src="app/supporting.html?lang=ja&amp;view=spectrum" title="インフレーション終了時のスカラーとテンソルのパワースペクトル、スペクトル指数とテンソル・スカラー比" data-auto-height scrolling="no" style="display: block; width: 100%; height: 950px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

薄い帯は、CMB の一次異方性で見るスケールの目安として $10^{-4}\lesssim k\lesssim0.2\,\mathrm{Mpc}^{-1}$ を示します。pivot は [Planck 2018](https://arxiv.org/html/1807.06211v2#S2) と同じ $k_*=0.05\,\mathrm{Mpc}^{-1}$ に対応づけているので、帯の範囲は $-6.21\lesssim\ln(k/k_*)\lesssim1.39$ です。多重極ではおおよそ $\ell\simeq2\text{–}3000$ に対応します。

左の図を「相対誤差（pivot 付近）」または「相対誤差（全範囲）」に切り替えると、最低次の式と次の次数の補正それぞれに対する $\mathcal P_{\mathrm{num}}/\mathcal P_{\mathrm{approx}}-1$ が見られます。零は一致、正の値は近似がパワーを過小評価していることを表します。pivot 付近での改善と、終了付近でのずれを比べてください。最後のモードには有限波長での発展も残るので、その差は slow-roll 展開の打切り誤差だけを表すものではありません。

$N_*=55$ での値は次の通りです。括弧内は crossing での $\epsilon_1,\epsilon_2$ から求めた一次の式 $\eqref{eq:slowroll-26}$–$\eqref{eq:slowroll-27}$ の値です。

| 模型 | $\epsilon_1$ | $\epsilon_2$ | $n_s$ | $r$ |
| --- | --- | --- | --- | --- |
| Starobinsky | $2.3\times10^{-4}$ | $0.0351$ | $0.9649$（$0.9644$） | $0.00355$（$0.00364$） |
| $\phi^{2/3}$ | $0.00306$ | $0.0183$ | $0.9757$（$0.9756$） | $0.0483$（$0.0490$） |
| $\phi^2$ | $0.00912$ | $0.0182$ | $0.9634$（$0.9636$） | $0.144$（$0.146$） |
| $\phi^4$ | $0.0181$ | $0.0180$ | $0.9449$（$0.9458$） | $0.285$（$0.289$） |

数値解と一次の式の差は slow-roll パラメータの二次の程度で、図の点線、すなわち $\eqref{eq:slowroll-25}$ の次の次数の補正を入れると、パワーの振幅も $10^{-3}$ 以下の精度で一致します。比べると、例えば Planck 2018 は $n_s=0.9649\pm0.0042$、BICEP/Keck 2018 のデータは $r<0.036$（95%）を与えており、この表の中では Starobinsky 模型だけがどちらとも整合します。$N_*$ の値は再加熱の歴史に依存するので、表の値には $N_*$ の不定性の分だけ幅があります。

いくつかの特徴を挙げておきます。

- **テンソル揺らぎも squeezing される：** $\sigma_T=1$ なので、テンソル揺らぎの各偏極の $r_k$ は $\ln(a/a_k)$ とともに増えます。$\eqref{eq:slowroll-30}$ と比べると、スカラー揺らぎとの差は $\frac12\ln(\epsilon_1/\epsilon_{1,k})$ です。
- **無矛盾性関係：** 数値解の $n_T$ と $-r/8$ の差も二次の程度です。
- **終了間際のモード：** 最後の数 e-fold で出るモードでは $\epsilon_1,\epsilon_2$ が大きく、slow-roll の式が合わなくなります。最後の 2 e-fold で出るモードは終了時にまだ凍結していないので、その値は終了時刻の振幅を表すだけです。
- **べき乗則：** $\eqref{eq:slowroll-22}$ が厳密に成り立ち、$n_s-1=-2\epsilon_1/(1-\epsilon_1)$、$r=16\epsilon_1$ が厳密に成り立ちます。$\epsilon_1$ を大きくすると、一次の式との差がはっきり見えます。

## 8. 規約と限界

- 単位は $c=\hbar=1$、$M_{\mathrm{Pl}}$ は換算 Planck 質量です。曲率摂動の符号規約は前編の式 (2) に従い、二点関数はこの符号によりません。
- 背景は slow-roll のアトラクター $\phi_{0,N}=-M_{\mathrm{Pl}}^2V_{,\phi}/V$ から十分早く始めて初期の過渡的な振る舞いを消し、$\epsilon_1=1$ まで積分しています。インフレーション後の再加熱と、その後の宇宙での揺らぎの発展は扱いません。
- モードは $x=100$（スペクトルでは $x=50$）から、局所的なパラメータで評価した $\eqref{eq:slowroll-22}$ を初期値として積分しています。べき乗則インフレーションでは、終了がないので crossing から 12 e-fold 以上後の値を使います。
- アニメーションは最初のモードが $x_1=8$ の時刻から、最後のモードが $x_3=0.15$ に達する時刻までを表示します。図のパネルは固定した quadrature の範囲 $|Q|,|P|\le4.4$ を描いており、それより細長い楕円ははみ出します。
- 扱っているのは二次作用による線形の量子論です。相互作用による非 Gaussian 性、ループ補正、デコヒーレンスは前編 §10 で概観した範囲を超えません。単一場なので等曲率揺らぎはありません。

<span id="hankel-reference"></span>

### Hankel 参照解の定義

点線の Hankel 曲線は、一次の式 $\nu\simeq3/2+\epsilon_1+\epsilon_2/2$ とは区別した、**同じ $x$ で評価する局所的な参照解**です。crossing での無次元の背景項 $B_*=\left.z''/(z\mathcal H^2)\right|_{N_{\mathrm{cross},*}}$ を $\eqref{eq:slowroll-15}$ の高次項も含めて固定し、$\nu_{\mathrm{ref}}=\sqrt{1/4+B_* /(1-\epsilon_{1,*})^2}$ とします。この指数と、数値背景から求めた $x(N)$ による $y_{\mathrm{ref}}(N)=x(N)/(1-\epsilon_{1,*})$ を $\eqref{eq:slowroll-22}$ に入れています。

定数パラメータで別の背景を時間発展させたものではなく、$y_{\mathrm{ref}}$ は変化する背景の厳密な $-k\eta$ でもありません。$B_*$ の高次項を残すだけでは、系統的な高次近似にはなりません。べき乗則インフレーションでは、この参照解が厳密になります。

数値モードそのものは変化する背景に従って発展し、その初期値には crossing ではなく積分開始時の同じ局所的な処方を使います。

## 参考文献

- 松原隆彦『宇宙論の物理（下）』東京大学出版会（2014）第 8 章：slow-roll インフレーション、Hankel 関数によるモード関数、スペクトル指数と重力波。
- [Baumann, *TASI Lectures on Inflation*](https://arxiv.org/abs/0907.5424)：Mukhanov–Sasaki 方程式、slow-roll 近似、観測量。
- [Stewart & Lyth, *A more accurate analytic calculation of the spectrum of cosmological perturbations produced during inflation*](https://arxiv.org/abs/gr-qc/9302019)：次の次数の補正と定数 $C$。
- [Schwarz, Terrero-Escalante & García, *Higher order corrections to primordial spectra from cosmological inflation*](https://arxiv.org/abs/astro-ph/0106020)：Hubble flow パラメータによる展開。
- [Martin, Ringeval & Vennin, *Encyclopædia Inflationaris*](https://arxiv.org/abs/1303.3787)：多数の単一場模型の予言の比較。
- [Planck Collaboration, *Planck 2018 results. X. Constraints on inflation*](https://arxiv.org/abs/1807.06211)：$n_s$ と $r$ の制限。
- [BICEP/Keck Collaboration, *Improved constraints on primordial gravitational waves using Planck, WMAP, and BICEP/Keck observations through the 2018 observing season*](https://arxiv.org/abs/2110.00483)：テンソル・スカラー比の上限。
