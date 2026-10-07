# インフレーションの量子ゆらぎとスクイージング

## 1. インフレーションは何を生成するのか

インフレーションは、真空のゆらぎに確定した古典的振幅を与えるわけではありません。時間発展するのは量子状態であり、平均値がゼロのままでも、その相関は大きく変化します。各Fourier波長について、位相空間でほぼ円形だった真空の分布が、細長いGaussian楕円へと変形します。広がった方向に残るランダムな振幅が、後の宇宙の構造形成に初期条件を与えます。

この記事では、この幾何学を「時間依存振動子」「生成・消滅演算子のBogoliubov混合」「Wigner関数のスクイージング」という三つの記述で追います。さらに、成長モードの優勢が音響振動の**時間位相**のコヒーレンスにつながることを説明します。空間的なFourier位相のランダムさは失われません。


![共通のquadrature座標軸で見たWigner等高線の三つの時期](app/teaser.svg)

一つの定在波モードを三つの時刻で見た予告図です。横軸は場の振幅、縦軸は正準運動量に対応するquadratureで、全時刻で同じ定義と縮尺を使っています。楕円は伸びても面積を保ちます。[主アニメーションへ進む](#main-animation)か、まず振動子と基底変換の説明をたどってください。

## 2. 準備：時間依存調和振動子

単位質量の振動子 $H=(p^2+\omega^2(t)q^2)/2$ を考えます。固定した正の基準周波数 $\omega_0$ を選び、$b=(\sqrt{\omega_0}q+ip/\sqrt{\omega_0})/\sqrt2$ と定義すると、

$$
H=\frac{\omega_0^2+\omega^2}{2\omega_0}
\left(b^\dagger b+\frac12\right)
+\frac{\omega^2-\omega_0^2}{4\omega_0}
\left(b^2+b^{\dagger2}\right).
$$

となります。対生成・対消滅の項が、真空の共分散を変形させます。一方、$\omega(t)>0$ の範囲では、$\omega_0$ を $\omega(t)$ に置き換えて瞬間的な消滅演算子を定義することもできます。その全Heisenberg微分は

$$
\dot b_{\mathrm{inst}}
=-i\omega b_{\mathrm{inst}}
+\frac{\dot\omega}{2\omega}b_{\mathrm{inst}}^\dagger.
$$

です。この表示では、基底の時間変化によって混合が陽に現れます。どちらも同じ時間発展の記述です。$\omega^2\leq0$ になると、この瞬間的な正周波数の処方は使えなくなりますが、固定した正準変数とGaussian共分散による記述は引き続き有効です。

## 3. 実場と独立な自由度

記号に運動量のデルタ関数を持ち込まないため、有限の周期箱を使います。実場の演算子は $\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger$、古典的な実現値は $v_{-\mathbf k}=v_{\mathbf k}^*$ を満たします。各非零波数対から片方ずつを選ぶ半空間 $\mathcal K_+$ を取り、

$$
v_{\mathbf k}=\frac{q_R+iq_I}{\sqrt2},\qquad
v_{-\mathbf k}=\frac{q_R-iq_I}{\sqrt2}.
$$

と書きます。Fourier展開を $e^{i\mathbf k\cdot\mathbf x}$ の規約で書くと、この対の寄与は、箱の規格化を除いて $\sqrt2[q_R\cos(\mathbf k\cdot\mathbf x)-q_I\sin(\mathbf k\cdot\mathbf x)]$ です。cos成分とsin成分という二つの実振動子であり、独立な実振幅が四つあるわけではありません。

ただし、進行波の**消滅演算子** $a_{\mathbf k}$ と $a_{-\mathbf k}$ は独立です。場の実条件から $a_{-\mathbf k}=a_{\mathbf k}^\dagger$ が従うわけでは**ありません**。場のFourier係数には、消滅演算子と生成演算子の両方が含まれます。

## 4. 振動子としてのインフレーション摂動

音速が1である正準的な単一インフラトンでは、Mukhanov–Sasaki変数 $v=z\zeta$ の作用と方程式は

$$
z=\frac{a\dot\phi_0}{H},\qquad
S=\frac12\int d\eta\,d^3x\,
\left[(v')^2-(\nabla v)^2+\frac{z''}{z}v^2\right],
\qquad
v_k''+\left(k^2-\frac{z''}{z}\right)v_k=0.
$$

となります。$\phi_0$ は一様な背景インフラトンであり、アニメーションのテスト場とは区別します。各実モードは、有効振動数の二乗が $k^2-z''/z$ である時間依存振動子です。Hubble半径の十分内側では背景項が小さく、Bunch–Davies条件がMinkowski真空に近い正周波数モードを選びます。crossingの前後で、背景項の影響が連続的に大きくなります。

各実成分について、境界項だけ異なる次の作用がスクイージングの記述に便利です。$s=z'/z$ と置くと、

$$
L_A=\frac12\left[(q_A'-sq_A)^2-k^2q_A^2\right],\qquad
p_A=q_A'-sq_A,
\qquad
H_{\eta,A}=\frac12(p_A^2+k^2q_A^2)
+\frac{s}{2}(q_Ap_A+p_Aq_A).
$$

です。半空間での作用は $S_{\mathbf k}=S[q_R]+S[q_I]$ に分かれます。量子Hamiltonianでは交差項の対称化が必要です。一方、部分積分後の作用から始めれば、$\widetilde p=q'$ および $\widetilde H_\eta=[\widetilde p^{\,2}+(k^2-z''/z)q^2]/2$ が得られます。二階の運動方程式は同じですが、位相空間で使う運動量は異なります。アニメーションは、[PolarskiとStarobinskyの式(3)–(4)](https://arxiv.org/pdf/gr-qc/9504030)に対応する**前者**の規約を採用しています。

図のテストスカラー場では、$q=a\phi_A$、$s=\mathcal H=a^\prime/a=-1/\eta$ と置きます。$a''/a=2/\eta^2$ なので、ここで使う解は厳密解です。適切に規格化した自由なテンソル偏極にも同じ記述が使えます。slow-roll曲率摂動では、$z''/z\simeq2/\eta^2$、$z'/z\simeq-1/\eta$ とする主要近似が対応します。ただし、**$\dot\phi_0=0$ の厳密de Sitter背景では $z=0$** です。その極限でテストスカラー場を $\zeta=v/z$ と同一視することはできません。

この厳密解の時間変数 $x$ とe-fold数 $N$ を、次のように定義します。

$$
a=-\frac1{H\eta},\qquad
x=-k\eta=\frac{k}{aH},\qquad
N=\ln\frac{a}{a_{\mathrm{cross}}}=-\ln x.
$$

プライムは共形時間微分で、$d\eta=dt/a$ です。以下では $\hbar=c=1$ を使います。

### 図で使うモデルの厳密モード関数

アニメーションのモデルで、一つの実モードの初期真空を消す演算子を $b^{\mathrm{in}}$ とします。$\hat q=f_k b^{\mathrm{in}}+f_k^*b^{\mathrm{in}\dagger}$ および $\hat p=g_k b^{\mathrm{in}}+g_k^*b^{\mathrm{in}\dagger}$ に現れる正周波数係数は

$$
f_k=\frac{1+i/x}{\sqrt{2k}}e^{ix},\qquad
 g_k=f_k'-\mathcal H f_k=-i\sqrt{\frac{k}{2}}e^{ix},
\qquad f_kg_k^*-f_k^*g_k=i.
$$

です。

<iframe src="app/supporting.html?lang=ja&amp;view=background" title="背景項と厳密de Sitterモード関数" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

**モード関数**に切り替え、$F_q=\sqrt{2k}f_k$ と $F_\phi=\sqrt{2k^3}f_k/(aH)=xF_q$ を比較してください。それぞれ再スケールした場と元の場のモードを無次元化したものです。実線を右に追うと、元の場が一定に近づく一方、再スケールしたモードは成長します。背景項の比較では縦軸を対数表示し、二つの項が等しくなる時刻とHubble crossingを別々に示しています。

## 5. 進行波の記述：二モード・スクイージング

逆向きの進行波の対を固定すると、背景は生成・消滅演算子を対として結びつけます。$s=z^\prime/z$ とし、各波数対を一度だけ数えると、Hamiltonianは

$$
H_{\eta,\mathbf k}=k\left(a_{\mathbf k}^\dagger a_{\mathbf k}
+a_{-\mathbf k}^\dagger a_{-\mathbf k}+1\right)
+is\left(a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger
-a_{\mathbf k}a_{-\mathbf k}\right).
$$

となります。この相互作用は、逆向きの各モードに一つずつ励起を生成・消滅します。これが二モード・スクイージングの記述です。

Heisenberg描像では、

$$
a_{\mathbf k}(\eta)=\alpha_k a_{\mathbf k}^{\mathrm{in}}
+\beta_k a_{-\mathbf k}^{\mathrm{in}\dagger},\qquad
|\alpha_k|^2-|\beta_k|^2=1,
\qquad
\alpha_k=e^{-i\theta_k}\cosh r_k,\quad
\beta_k=e^{i(\theta_k+2\varphi_k)}\sinh r_k.
$$

と書けます。次節で導入する定在波の演算子も、同じ係数を持つ単一モードの変換に従います。$r_k$ は主軸方向の幅を決めます。$Q=\sqrt{k}q$、$P=p/\sqrt{k}$（アニメーションとともに詳述）という規約では、$\varphi_k=\arg(\alpha_k\beta_k)/2$ は、正の $Q$ 軸から測った**長軸の角度**です（$\pi$ の不定性を除く）。回転位相 $\theta_k$ は、初期真空の共分散には影響しません。文献によって角度の符号や、長軸・短軸のどちらを基準にするかが異なるので注意が必要です。

上で示した厳密な係数から、

$$
\alpha_k=\left(1+\frac{i}{2x}\right)e^{ix},\qquad
\beta_k=-\frac{i}{2x}e^{-ix},\qquad
r_k=\operatorname{arsinh}\frac1{2x},\qquad
\varphi_k=-\frac12\arctan(2x).
$$

が得られます。$x\ll1$ では $r_k\simeq-\ln x=N$ となり、Hubble exit後の1 e-foldごとに、スクイージングがほぼ1ずつ増えます。$|\beta_k|^2$ は選んだ基準基底での占有数であり、時間依存背景における一意な粒子数ではありません。スクイージングの大きさの数値自体も、正準quadratureの選択に依存します。状態を一貫して記述するのは、共分散全体とその変換則です。

<iframe src="app/supporting.html?lang=ja&amp;view=squeezing" title="e-fold時間に対するスクイージングの大きさと長軸の角度" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

crossing後の厳密な曲線と $r_k\simeq N$ を比べてください。右の図は、初めから向きが固定されているのではなく、時間とともに一定方向へ収束することを示します。真空がほぼ円である初期には、角度の幾何学的な違いは小さくなります。

## 6. 定在波の記述：二つの単一モード・スクイージング

$b_A=(\sqrt{k}q_A+ip_A/\sqrt{k})/\sqrt2$ と定義すると、定在波のHamiltonianは

$$
H_{\eta,A}=k\left(b_A^\dagger b_A+\frac12\right)
+\frac{is}{2}\left(b_A^{\dagger2}-b_A^2\right),
\qquad A=R,I.
$$

となります。二つの実モードは、同一の単一モード・スクイージングを受けます。進行波の演算子との関係は

$$
b_R=\frac{a_{\mathbf k}+a_{-\mathbf k}}{\sqrt2},\qquad
b_I=-\frac{i}{\sqrt2}(a_{\mathbf k}-a_{-\mathbf k}),
\qquad
b_R^{\dagger2}+b_I^{\dagger2}
=2a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger.
$$

です。

進行波基底では対の項が二モード・スクイージングを表し、定在波基底では同じ状態が等しくスクイーズされた二つの状態の積に分かれます。図の楕円は**一つの定在波モード**の状態です。進行波対の片方を捨てた縮約状態ではありません。進行波モード間の量子もつれが部分系の選び方に依存する点は、[MartinとVennin](https://arxiv.org/abs/1510.04038)でも議論されています。

<iframe src="app/supporting.html?lang=ja&amp;view=basis" title="Fourier半空間と進行波・定在波の基底変換" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1200px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

色付きの半平面は、各波数対から一つずつを選ぶ操作の二次元模式図です。境界上でも各対から一つを選ぶ規約が必要です。時期を切り替え、共分散行列を見比べてください。左のquadratureの順番は $(Q_+,P_+,Q_-,P_-)$、右は $(Q_R,P_R,Q_I,P_I)$ です。左のモード間にある非零の相関が、右では独立な同一の二つのブロックになります。時間発展の前後ではなく、同じ状態全体を二通りに記述しています。

<span id="main-animation"></span>

## 7. 主可視化：quadrature位相空間の時間発展

アニメーションが追うのは、**固定した一つのゼロでない共動波数** $k=|\mathbf k|$ と、その実定在波成分 $A=R$ または $I$ の一方です。異なる波長を並べた図でも、時空図でもありません。モデルは厳密de Sitter時空中の、自由・質量ゼロ・最小結合スカラー場です。単位系は $\hbar=c=1$ とし、空間モードの規格化は実振幅 $\phi_A$ に吸収します。

**どのフレームでも**、横軸と縦軸は次の量です。

$$
Q=\sqrt{k}\,q=\sqrt{k}\,a\phi_A,
\qquad
P=\frac{p}{\sqrt{k}}
=\frac{q'-\mathcal Hq}{\sqrt{k}}
=\frac{a\phi_A'}{\sqrt{k}},
\qquad \mathcal H=\frac{a'}a.
$$

プライムは共形時間による微分を表し、$d\eta=dt/a$ です。したがって、$Q$ は再スケールした**場の振幅**であり、空間位置ではありません。$P$ は再スケールした**正準運動量**であり、波数 $k$ でも $q'/\sqrt{k}$ でもありません。これらのquadratureは $[\hat Q,\hat P]=i$ を満たします。軸の定義・向き・表示範囲・縦横で等しい縮尺は、再生中ずっと固定されています。ただし、元の場と結びつける係数 $a$ は時間変化するので、$Q$ が増大しても $\phi_A$ が増大するとは限りません。

時間は先ほど定義したe-fold変数 $N=-\ln x$ で表します。

スライダーの範囲は $x=12$ から $x=0.2$ までで、$N=0$ がHubble crossingです。ここでいう「地平線の内側・外側」はHubbleスケールとの大小関係を指し、別の因果的境界を指すものではありません。この区別については[宇宙の因果構造](../cosmic-causal-structure/)を参照してください。

<iframe src="app/index.html?lang=ja" title="インフレーションのスクイージング：回転・スクイーズ・合成Hamilton流" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

最初の2パネルは、**その時刻の速度場**を回転とスクイーズに分解したものです。量子状態の等高線を重ねているのは、3番目のパネルだけです。オレンジの点は等高線上を流れに沿って運ばれる目印であり、量子粒子の確定した軌道ではありません。矢印には、時間依存の表示係数 $1/\sqrt{1+x^2}$ と、さらに固定の描画縮尺を共通に掛けています。同じフレーム内でのベクトルの加法は保たれますが、異なるフレームの矢印の長さを、そのまま物理的速度として比較することはできません。状態の時間発展には、この表示補正を加えず厳密解を使っています。

次のように操作してみてください。

1. 最初から再生します。$x$ が大きいときは回転が優勢で、$x$ が1より小さくなるにつれて楕円が伸びます。開始時の等高線は完全な円ではありません。有限の開始時刻で評価した厳密なBunch–Davies状態です。
2. Hubble crossingで止めます。流れはゼロにならず、シアーになっています。スクイージングがこの瞬間に突然始まったわけではありません。
3. 晩期に、楕円の主軸・瞬間的な流れの固有方向・厳密解の方向を切り替えます。それぞれ異なる問いに答える方向であり、一般には一致しません。
4. 縦方向の広がりに注目します。楕円の**主軸方向**の幅が縮んでも、縦方向の広がりは一定です。スクイーズされるのは、相関した $Q$ と $P$ の組み合わせです。

### Wigner等高線と厳密な流れ

$\mathbf Z=(Q,P)^T$、$\Sigma_{ij}=\langle\{\hat Z_i,\hat Z_j\}\rangle/2$ と書くと、平均ゼロの真空から時間発展した状態は

$$
\Sigma(x)=\frac12
\begin{pmatrix}1+x^{-2}&-x^{-1}\\-x^{-1}&1\end{pmatrix},
\qquad
\det\Sigma=\frac14,\qquad
\sigma_\pm^2=\frac12e^{\pm2r_k}.
$$

で表されます。このGaussian状態のWigner関数は正です。

$$
W(\mathbf Z)=\frac{1}{2\pi\sqrt{\det\Sigma}}
\exp\left[-\frac12\mathbf Z^T\Sigma^{-1}\mathbf Z\right].
$$

描かれた楕円は $\mathbf Z^T\Sigma^{-1}\mathbf Z=1$、すなわちWigner密度が中心値の $e^{-1/2}$ になる等高線です。内部に含まれるWigner重みは $1-e^{-1/2}\simeq0.393$ であり、一次元Gaussian分布の「1 sigmaは68%」とは異なります。半長軸・半短軸は $e^{\pm r_k}/\sqrt2$、面積は常に $\pi/2$ です。ユニタリなスクイージングは面積を保存し、散逸による冷却ではありません。また、Wigner関数が正であっても、非可換な $Q$ と $P$ を同時に鋭く測定するための同時確率分布になるわけではありません。

共形時間から $N$ に時間変数を変えると、Hamiltonianと流れは

$$
K_N=\frac{x}{2}(Q^2+P^2)+\frac12(QP+PQ),\qquad
\frac{d\mathbf Z}{dN}
=\underbrace{\begin{pmatrix}1&x\\-x&-1\end{pmatrix}}_{A(N)}\mathbf Z
=x\begin{pmatrix}0&1\\-1&0\end{pmatrix}\mathbf Z
+\begin{pmatrix}1&0\\0&-1\end{pmatrix}\mathbf Z.
$$

となります。これが3パネルに示した分解です。二次Hamiltonianの下では、Wigner関数は古典的なHamilton方程式と同じ線形流で運ばれます。共分散は $d\Sigma/dN=A\Sigma+\Sigma A^T$ に従い、$A$ のトレースがゼロであることが位相空間の面積保存に対応します。

瞬間的な固有値は $\lambda_\pm=\pm\sqrt{1-x^2}$ です。$x>1$ では虚数、$x<1$ では実数となります。$x=1$ では $A^2=0$ ですが $A\ne0$ であり、シアーです。これは**時刻を固定した流れ**の分類です。実際の軌道は時間順序付きの発展に従い、瞬間的な固有ベクトルに沿うとは限りません。

この分類自体も運動量の規約に依存します。部分積分後の作用の変数では、

$$
\widetilde P=P+\frac Qx,\qquad
\frac{d}{dN}\begin{pmatrix}Q\\\widetilde P\end{pmatrix}
=\begin{pmatrix}0&x\\2/x-x&0\end{pmatrix}
\begin{pmatrix}Q\\\widetilde P\end{pmatrix}.
$$

となり、固有値は $\pm\sqrt{2-x^2}$ に変わります。時間依存正準変換により、瞬間的な楕円型・双曲型の境目は変わりますが、物理的なHubble crossingは $x=1$ のままで、場の運動方程式も変わりません。

## 8. 成長・減衰モードと位相空間の方向

superhorizonの方程式で勾配項を無視すると、

$$
q=Cz+Dz\int^\eta\frac{d\eta'}{z^2(\eta')},\qquad
p=q'-\frac{z'}zq=\frac Dz.
$$

が得られます。不定積分の積分定数は $C$ に吸収できます。アトラクター型のインフレーション背景では、第1の解が一定の $\zeta=q/z$ を与え、独立な第2の寄与は減衰します。テストスカラー場なら $z$ を $a$ に置き換えます。$q$ はほぼ $a$ に比例して成長し、$\phi_A=q/a$ は凍結します。

勾配を無視した式から、有限の $k$ における成長解の運動量まで厳密にゼロだとはいえません。図で使う厳密な成長解・減衰解のベクトルは、例えば次のように選べます。

$$
\mathbf G(x)=\begin{pmatrix}\sin x+\cos x/x\\-\cos x\end{pmatrix},\qquad
\mathbf D(x)=\begin{pmatrix}\cos x-\sin x/x\\\sin x\end{pmatrix},
\qquad
\mathbf G\sim\begin{pmatrix}x^{-1}\\-1\end{pmatrix},\quad
\mathbf D\sim\begin{pmatrix}-x^2/3\\x\end{pmatrix}.
$$

[主アニメーション](#main-animation)で**厳密な成長解・減衰解の方向**を選び、同じ時刻の**楕円の主軸**と比較してください。

これらは解の方向であり、瞬間的な生成行列の固有ベクトルではありません。また、互いに直交しません。一方、共分散行列の主軸は定義上直交します。晩期には長軸と短軸が、それぞれ $\mathbf G$ と $\mathbf D$ の水平・鉛直の極限方向に近づきますが、有限時刻での傾きは異なります。「短軸が減衰モードである」という表現は、あくまで極限での幾何学的な説明です。

幅が狭まる様子は、Gaussian分布の条件付き関係でより正確に表せます。

$$
\mathbb E[P\mid Q]=-\frac{x}{1+x^2}Q,\qquad
\operatorname{Var}(P\mid Q)=\frac{x^2}{2(1+x^2)},
\qquad \operatorname{Var}(P)=\frac12.
$$

ここでの条件付けは、正のWigner密度に対する操作であり、同時射影測定の手順を表すものではありません。$P$ 自体の周辺分布の幅は一定でも、古典的に見える関係から横に外れる不確定性が縮むことがわかります。減衰する**寄与**が抑えられることは、その時間に依存しない積分係数そのものが消えることを意味しません。

## 9. 摂動が古典的に見える理由

平均値がゼロでも、場の分散はゼロとは限りません。例えば、同じ厳密モード関数から、対数波数間隔あたりのテストスカラー場のパワーは

$$
\mathcal P_\phi(k)=\frac{k^3}{2\pi^2}\left|\frac{f_k}{a}\right|^2
=\frac{H^2}{4\pi^2}(1+x^2)
\longrightarrow\left(\frac{H}{2\pi}\right)^2.
$$

となります。$q$ の伸長と、元の場の分散が有限値に凍結することは両立します。曲率摂動では背景因子が $z$ に置き換わり、そのslow-roll発展が振幅とスペクトルの傾きを決めます。

正のWigner関数を使えば、同時刻で対称順序を取ったモーメントは古典的Gaussian集団で再現できます。大きなスクイージングは、さらに強い場と運動量の関係、および成長モードの優勢をもたらします。そのため、対象とする摂動は実効的に古典的な確率場として時間発展させられます。しかし、交換関係が消えるわけでも、波動関数が収縮するわけでも、この純粋状態が混合状態になるわけでも**ありません**。環境によるデコヒーレンスは別の物理過程であり、この計算には含めていません。観測可能な量子的特徴を論じるには、これらの区別が必要です（[MartinとVennin](https://arxiv.org/abs/1510.04038)）。

<iframe src="app/supporting.html?lang=ja&amp;view=samples" title="シンプレクティック発展の前後におけるWignerサンプル" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

時刻スライダーを初期から最後まで動かしてください。ランダムさが失われるのではなく、広がった方向の振幅の範囲が増し、オレンジの条件付き平均線から横に外れる幅が小さくなります。両パネルの縮尺は共通・固定です。厳密な等高線が囲むWigner重みは約39%なので、その外にも点があるのが自然です。

## 10. 音響振動の位相コヒーレンスとCMB

統計的に一様なGaussian場では、二つの定在波成分の分散は等しく、その振幅平面に特別な向きはありません。したがって、

$$
\zeta_{\mathbf k}=\frac{\zeta_R+i\zeta_I}{\sqrt2}
$$

の空間位相 $\arg\zeta_{\mathbf k}$ はランダムです。インフレーションは、これらの位相をすべて同じ値にするわけではありません。空間の原点を移すだけでも位相は変わります。音響振動の位相コヒーレンスが指しているのは、この空間位相ではありません。

horizon re-entry後の音響変数を模式的に書くと、二つの時間依存解があります。

$$
X_k(\eta)=A_k\cos(kr_s)+B_k\sin(kr_s),\qquad
r_s(\eta)=\int^\eta c_s(\eta')\,d\eta'.
$$

初期条件を一つの断熱的成長モードが与えるなら、密度と速度は結びついています。$A_k$ と $B_k$ は、独立に選べる二つの任意のランダム入力ではありません。外力のない理想化した振動子では、$B_k\simeq0$ となるように時間原点を選べます。振幅がランダムでも、時間方向の伝達関数は共通です。この初期条件と音響ピークの関係は、[HuとWhite](https://arxiv.org/abs/astro-ph/9602019)で詳しく論じられています。

以下の可視化では、初期振幅の分散の総和を揃えた二つの集団を使っています。その総和を $\sigma^2$ とすると、

$$
\begin{aligned}
\langle|A_k|^2\rangle=\sigma^2,\quad B_k=0
&\quad\Rightarrow\quad
\langle|X_k|^2\rangle=\sigma^2\cos^2(kr_s),\\
\langle|A_k|^2\rangle=\langle|B_k|^2\rangle=\frac{\sigma^2}{2},\quad
\langle A_kB_k^*\rangle=0
&\quad\Rightarrow\quad
\langle|X_k|^2\rangle=\frac{\sigma^2}{2}.
\end{aligned}
$$

です。したがって、振幅のランダムさだけではパワーの振動模様は消えませんが、時間方向の二つのquadratureが独立にランダムなら消えます。実際のCMB伝達関数には、重力による駆動、バリオンの慣性、ニュートリノの効果、拡散、再結合、天球への射影が含まれ、純粋なcos関数ではありません。コヒーレントな音響ピークは原始初期条件の構造を検証しますが、それだけで量子スクイージングの測定や、インフレーション起源の一意な証明になるわけではありません。

<iframe src="app/supporting.html?lang=ja&amp;view=acoustic" title="ランダムな音響振動の実現例とコヒーレント・非コヒーレントな平均パワー" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

コヒーレントな実現例の零点でカーソルを止めてください。振幅も符号も異なる8本が、同じ時刻にゼロを通ります。非コヒーレントな実現例では揃いません。下段は有限個のサンプルからの推定と厳密な集団平均を区別しています。一定の音響地平線で波数を変えたとき、このような振動がピークの模様に対応します。

## 適用範囲と参考文献

アニメーションは、与えられたde Sitter背景上での、線形・自由なGaussian状態の時間発展です。再加熱、環境との相互作用、非Gaussian性、CMBスペクトルの数値計算は扱いません。固定軸上でも細い楕円を見分けられるよう、主アニメーションは $x=0.2$ で終えています。さらに強いスクイージングを描くには、より小さな横断方向の幅を分解する必要があります。不確定性関係が変わるわけではありません。

通常の成長モードに関する結論は、アトラクター背景を仮定しています。非アトラクター型のインフレーションでは $\zeta$ の振る舞いが変わりうるため、このde Sitterの例をそのまま当てはめず、適切な $z(\eta)$ に対する方程式を解く必要があります。

- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030)：正準変数、モード関数、成長・減衰解による記述。
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038)：部分系の選択、および古典的な相関関数と量子状態の区別。
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019)：音響振動の初期条件とピーク構造の解釈。
