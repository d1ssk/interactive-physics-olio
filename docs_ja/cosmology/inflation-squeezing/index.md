# インフレーションの量子揺らぎと squeezing 

## 1. インフレーションは何を生成するのか

現在の宇宙では、銀河や銀河団の分布、CMB の温度・偏光揺らぎとして、さまざまなスケールの密度揺らぎを観測できます。これらを時間をさかのぼっていくと、宇宙初期のごく小さな原始揺らぎへと行き着きます。インフレーション理論では、その起源を量子場の真空揺らぎに求めます。

ただし、「量子揺らぎが引き伸ばされて古典的な密度揺らぎになった」という説明だけでは、そこで何が起きているのかはあまり見えてきません。インフレーション中に時間発展するのは、各 Fourier モードの量子状態です。位相空間で見ると、その変化を幾何学的に捉えることができます。Hubble スケールの十分内側ではほぼ円形だった真空状態の Wigner 分布が、宇宙膨張とともに細長い楕円へと変形していきます。この **squeezing** が、インフレーション中の量子揺らぎと、後に古典的な確率場として扱われる原始揺らぎを結ぶ中心的な構造です。

この記事では、この過程を

- 時間依存調和振動子
- 生成・消滅演算子の Bogoliubov 混合
- Wigner 関数の squeezing 

という三つの視点から追います。さらに、superhorizon で成長モードが優勢になることが、再突入後の音響振動の**時間位相のコヒーレンス**へどうつながるかを見ていきます。

以下の図は、これから詳しく追う時間発展を先取りして示したものです。

![共通の quadrature 座標軸で見た Wigner 等高線の三つの時期](app/teaser.svg)

一つの定在波モードの Wigner 関数の等高線を、三つの時刻について同じ位相空間上に示しています。横軸は場の振幅、縦軸は正準運動量に対応する quadrature です。初期にはほぼ円形だった分布が、時間とともに細長い楕円へ変形していく様子が、この後で扱う squeezing の全体像です。

[メインのアニメーションへ進む](#main-animation)こともできますが、まずはこの変形がどこから生じるのか、時間依存調和振動子から順に見ていきます。

## 2. 準備：時間依存調和振動子

単位質量の時間依存調和振動子

$$
H(t)=\frac12\left[p^2+\Omega^2(t)q^2\right]
$$

を考えます。ここで $\Omega^2(t)$ は時間に依存する有効振動数の二乗で、正とは限りません。以下では $\hbar=1$ とし、$[q,p]=i$ とします。

### Schrödinger 描像：固定した軸で状態の変化を見る

まず Schrödinger 描像で考えます。この描像では演算子 $q,p$ は時間に依存せず、量子状態 $|\psi(t)\rangle$ が時間発展します。

固定した正の基準周波数 $\omega_0$ を一つ選び、

$$
b=
\frac{1}{\sqrt2}
\left(
\sqrt{\omega_0}q
+\frac{ip}{\sqrt{\omega_0}}
\right)
$$

と定義します。対応する無次元の quadrature を

$$
Q=\frac{b+b^\dagger}{\sqrt2}
=\sqrt{\omega_0}q,
\qquad
P=\frac{b-b^\dagger}{i\sqrt2}
=\frac{p}{\sqrt{\omega_0}}
$$

とします。$\omega_0$ は固定しているので、$Q,P$ は時間とともに動かない位相空間の座標軸です。

この座標を使うと Hamiltonian は

$$
H(t)
=
\frac{\omega_0}{2}P^2
+
\frac{\Omega^2(t)}{2\omega_0}Q^2
$$

となります。

同じ Hamiltonian を $b,b^\dagger$ で書けば、

$$
H(t)=
\frac{\omega_0^2+\Omega^2(t)}{2\omega_0}
\left(b^\dagger b+\frac12\right)
+
\frac{\Omega^2(t)-\omega_0^2}{4\omega_0}
\left(b^2+b^{\dagger2}\right)
$$

です。

$\Omega^2(t)=\omega_0^2$ では、

$$
H=\frac{\omega_0}{2}(Q^2+P^2)=\omega_0\left(b^\dagger b+\frac12\right)
$$

となります。このとき、number state は

$$
|n\rangle
\longrightarrow
e^{-i(n+1/2)\omega_0t}|n\rangle
$$

と時間発展するので、共通の位相を除けば各成分の相対位相は $e^{-in\omega_0t}$ で進みます。

たとえば coherent state

$$
|\alpha\rangle
=
e^{-|\alpha|^2/2}
\sum_{n=0}^\infty
\frac{\alpha^n}{\sqrt{n!}}|n\rangle
$$

は、全体位相を除いて

$$
|\alpha\rangle
\longrightarrow
|\alpha e^{-i\omega_0t}\rangle
$$

と時間発展します。したがって

$$
\alpha(t)=e^{-i\omega_0t}\alpha(0)
$$

です。

coherent state の中心について

$$
\alpha
=
\frac{\langle Q\rangle+i\langle P\rangle}{\sqrt2}
$$

なので、これは固定した $Q,P$ 平面上で半径を保ったまま回転する運動に対応します。一般の状態についても、$\Omega^2=\omega_0^2$ なら Wigner 関数全体が形を変えずに回転します。

一方、$\Omega^2(t)\neq\omega_0^2$ になると、$Q^2$ と $P^2$ の係数が異なります。位相空間の二つの方向が異なる作用を受けるため、単純な回転に加えて分布の変形が生じます。

$b,b^\dagger$ の言葉では、この効果を担うのが

$$
b^2+b^{\dagger2}
$$

の項です。実際、

$$
b^2|n\rangle\propto|n-2\rangle,
\qquad
b^{\dagger2}|n\rangle\propto|n+2\rangle
$$

なので、異なる number state が互いに混ざります。また

$$
b^2+b^{\dagger2}=Q^2-P^2
$$

であることからも、この項が $Q$ と $P$ の二方向を非対称に扱うことが分かります。
位相空間では、この時間発展は

$$
\dot Q=\omega_0P,
\qquad
\dot P=-\frac{\Omega^2(t)}{\omega_0}Q
$$

という Hamilton flow で表されます。ここでの $Q,P$ は位相空間上の座標です。Hamiltonian が二次式であるため、Wigner 関数もこの古典的な流れに沿って正確に時間発展します。$\Omega^2=\omega_0^2$ のときの円形の回転に対し、係数が異なる場合には伸縮を伴う流れになります。

その結果、初めに円形だった Gaussian 状態の Wigner 関数は、一般には回転しながら楕円へと変形します。特に vacuum や coherent state のような等方的な最小不確定状態から出発すると、一方の quadrature の揺らぎが真空揺らぎより小さくなり、共役な方向の揺らぎが大きくなる squeezing が生じます。

### Heisenberg 描像：固定した軸で状態の変化を見る

同じ固定基底を Heisenberg 描像で見てみます。今度は状態を固定し、

$$
b_{\rm H}(t)=U^\dagger(t)bU(t)
$$

とします。

$b$ 自身には陽な時間依存性がないので、Heisenberg 方程式から

$$
\dot b_{\rm H}(t)
=
-i
\frac{\omega_0^2+\Omega^2(t)}{2\omega_0}
b_{\rm H}(t)
-i
\frac{\Omega^2(t)-\omega_0^2}{2\omega_0}
b_{\rm H}^\dagger(t)
$$

を得ます。

したがって $b_{\rm H}(t)$ は一般に

$$
b_{\rm H}(t)
=
\alpha(t)b+\beta(t)b^\dagger
$$

という Bogoliubov 変換の形で時間発展します。交換関係を保つため、

$$
|\alpha(t)|^2-|\beta(t)|^2=1
$$

が成り立ちます。

Schrödinger 描像で $b^2+b^{\dagger2}$ の項が状態を変形させていたことは、Heisenberg 描像では $b_{\rm H}$ の時間発展に $b_{\rm H}^\dagger$ が混ざることとして現れます。

つまり、Schrödinger 描像では「固定した $Q,P$ 軸の上で状態が変形する」と見え、Heisenberg 描像では「固定した状態に対して演算子が Bogoliubov 混合する」と見えます。記述の仕方は異なりますが、両者が与える期待値や共分散は同じです。

### 瞬間基底：その時刻の Hamiltonian を対角化する

ここまでは、固定した基準周波数 $\omega_0$ から定義した $b,b^\dagger$ を使って時間発展を記述してきました。$\Omega^2(t)>0$ の範囲では、その時刻の Hamiltonian を対角化する瞬間基底を考えることもできます。

$$
\omega(t)=\sqrt{\Omega^2(t)}>0
$$

とおき、

$$
b_{\rm inst}(t)
=
\frac{1}{\sqrt2}
\left(
\sqrt{\omega(t)}q
+
\frac{ip}{\sqrt{\omega(t)}}
\right)
$$

と定義すると、

$$
H(t)
=
\omega(t)
\left(
b_{\rm inst}^\dagger(t)b_{\rm inst}(t)
+\frac12
\right)
$$

となります。

ただし、各時刻で Hamiltonian が対角化されても、状態がそれぞれの瞬間固有状態にとどまるとは限りません。状態を

$$
|\psi(t)\rangle
=
\sum_n c_n(t)|n;t\rangle
$$

と展開すると、$b_{\rm inst}(t)$ で定義される各時刻の number state $|n;t\rangle$ 自身が時間変化するため、異なる瞬間固有状態の間に混合が生じます。調和振動子では $n$ と $n\pm2$ が混合し、固定基底で squeezing として見えていた時間発展が、ここでは瞬間 number state 間の混合として現れます。

$\omega(t)$ の変化が十分に遅く、

$$
\frac{|\dot\omega|}{\omega^2}\ll1
$$

であれば、この混合は小さくなります。断熱極限では、初めに瞬間真空にあった状態は、その時々の瞬間真空をほぼ追従します。

一方、$\omega\to0$ ではこの断熱条件は一般に破れ、$\Omega^2=0$ では $b_{\rm inst}$ の定義も特異になります。さらに $\Omega^2(t)<0$ では

$$
H(t)
=
\frac12
\left[
p^2-|\Omega^2(t)|q^2
\right]
$$

となり、系は inverted harmonic oscillator になります。このとき通常の調和振動子のような基底状態や離散的な number state は存在せず、「その時刻の真空」や「その時刻の粒子数」という瞬間粒子描像も使えなくなります。

一方、固定した $Q,P$ による位相空間の記述は、$\Omega^2$ の符号によらず使えます。$\Omega^2<0$ では、位相空間の運動は振動的な回転から、一方向に伸びながらもう一方向に縮む双曲的な流れへ移り、squeezing が発達します。

例えば後に詳しく見るように、インフレーション中の Mukhanov-Sasaki mode では、有効振動数の二乗が正から負へ変化します。subhorizon では通常の振動子として振る舞い、正周波数 mode や粒子・真空の概念が自然に使えますが、superhorizon では振動的な粒子描像は適切でなくなり、growing/decaying mode や squeezing の言葉の方が自然になります。

このような領域まで一貫して Wigner 関数の時間発展を追うには、固定した $Q,P$ 軸による記述が見通しのよい表現になります。以下では主にこの記述を用います。

## 3. 実スカラー場のモードと自由度

### Fourier 展開と実場の条件

実スカラー場 $v(\eta,\mathbf x)$ を、周期境界条件を持つ体積 $V$ の領域で Fourier 展開します。

$$
v(\eta,\mathbf x)
=
\frac1{\sqrt V}
\sum_{\mathbf k}
v_{\mathbf k}(\eta)e^{i\mathbf k\cdot\mathbf x}
$$

場が実数値を取ることから、

$$
v_{-\mathbf k}=v_{\mathbf k}^*
$$

が成り立ちます。したがって、$\mathbf k$ と $-\mathbf k$ の Fourier 係数は独立ではありません。一つの非零波数対 $(\mathbf k,-\mathbf k)$ に注目すると、$v_{\mathbf k}$ は一つの複素数であり、二つの独立な実数によって指定されます。つまり、**一つの波数対には二つの実自由度がある**ことになります。

以下では、この二つの自由度を量子化し、進行波基底と定在波基底で記述します。

### 正準量子化と進行波モード

Schrödinger 描像で量子化します。場の Fourier 係数 $\hat v_{\mathbf k}$ と、正準運動量の Fourier 係数 $\hat\pi_{\mathbf k}$ は、場の Hermite 性から、

$$
\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger,
\qquad
\hat\pi_{-\mathbf k}=\hat\pi_{\mathbf k}^\dagger
$$

を満たします。正準交換関係は

$$
[\hat v_{\mathbf k},\hat\pi_{\mathbf k'}]
=
i\delta_{\mathbf k,-\mathbf k'},
\qquad
[\hat v_{\mathbf k},\hat v_{\mathbf k'}]
=
[\hat\pi_{\mathbf k},\hat\pi_{\mathbf k'}]
=0
$$

です。

§2 の調和振動子と同様に、固定した基準周波数を用いて生成・消滅演算子を定義します。ここでは各波数に対して $k=|\mathbf k|>0$ を使い、

$$
a_{\mathbf k}
=
\frac1{\sqrt2}
\left(
\sqrt{k}\,\hat v_{\mathbf k}
+
\frac{i\hat\pi_{\mathbf k}}{\sqrt{k}}
\right)
$$

とします。このとき、

$$
[a_{\mathbf k},a_{\mathbf k'}^\dagger]
=
\delta_{\mathbf k,\mathbf k'},
\qquad
[a_{\mathbf k},a_{\mathbf k'}]=0
$$

が成り立ちます。逆に、Fourier 係数は

$$
\begin{aligned}
\hat v_{\mathbf k}
&=
\frac{a_{\mathbf k}+a_{-\mathbf k}^\dagger}{\sqrt{2k}},\\
\hat\pi_{\mathbf k}
&=
-i\sqrt{\frac{k}{2}}
\left(
a_{\mathbf k}-a_{-\mathbf k}^\dagger
\right)
\end{aligned}
$$

と表せます。実場の条件によって $\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger$ が成り立ちますが、$a_{\mathbf k}$ と $a_{-\mathbf k}$ は独立な消滅演算子です。

場全体を生成・消滅演算子で表すと、零モードを除いて

$$
\hat v(\mathbf x)
=
\frac1{\sqrt V}
\sum_{\mathbf k\ne\mathbf 0}
\frac1{\sqrt{2k}}
\left(
a_{\mathbf k}e^{i\mathbf k\cdot\mathbf x}
+
a_{\mathbf k}^\dagger e^{-i\mathbf k\cdot\mathbf x}
\right)
$$

となります。

$a_{\mathbf k}$ は空間依存性 $e^{i\mathbf k\cdot\mathbf x}$ を持つモードに対応します。このように、波数ベクトル $\mathbf k$ で区別されるモードを**進行波モード（traveling-wave modes）**と呼ぶことにします。ここで選んだ基準周波数 $k$ は演算子を定義するためのものであり、時間依存する Hamiltonian の下での瞬間的な振動数とは限りません。

### 定在波モードによる記述

同じ場を、今度は cos と sin の実基底で記述します。

各波数対 $(\mathbf k,-\mathbf k)$ から一方だけを選んだ集合を $\mathcal K_+$ とします。一つの波数対について、

$$
\hat v_{\mathbf k}
=
\frac{\hat q_c-i\hat q_s}{\sqrt2},
\qquad
\hat v_{-\mathbf k}
=
\frac{\hat q_c+i\hat q_s}{\sqrt2}
$$

と分解すると、場の演算子は

$$
\hat v(\mathbf x)
=
\sqrt{\frac2V}
\sum_{\mathbf k\in\mathcal K_+}
\left[
\hat q_{c,\mathbf k}\cos(\mathbf k\cdot\mathbf x)
+
\hat q_{s,\mathbf k}\sin(\mathbf k\cdot\mathbf x)
\right]
$$

と書けます。ただしここでも零モードは省略しています。

$\hat q_c,\hat q_s$ は Hermitian 演算子であり、cos 型と sin 型の二つの実配置自由度を表します。

正準運動量についても同様に

$$
\hat\pi_{\mathbf k}
=
\frac{\hat p_c-i\hat p_s}{\sqrt2}
$$

と分解すると、

$$
[\hat q_A,\hat p_B]=i\delta_{AB},
\qquad
[\hat q_A,\hat q_B]=[\hat p_A,\hat p_B]=0,
\qquad A,B=c,s
$$

が成り立ちます。したがって、各波数対は二つの独立な実調和振動子として扱えます。

それぞれの振動子に対して、進行波基底と同じ基準周波数 $k$ を用いて

$$
b_A
=
\frac1{\sqrt2}
\left(
\sqrt{k}\,\hat q_A
+
\frac{i\hat p_A}{\sqrt{k}}
\right),
\qquad A=c,s
$$

と定義します。$b_c,b_s$ は、それぞれ cos 型と sin 型の**定在波モード（standing-wave modes）**の消滅演算子です。

これらと進行波モードの消滅演算子の関係は、

$$
\begin{aligned}
a_{\mathbf k}
&=
\frac{b_c-ib_s}{\sqrt2},\\
a_{-\mathbf k}
&=
\frac{b_c+ib_s}{\sqrt2}
\end{aligned}
$$

となります。

つまり、**進行波基底と定在波基底は、同じ二つの量子振動子を異なる基底で表したもの**です。

この変換では消滅演算子同士が混ざるだけなので、両基底で定義される真空は共通です。

$$
a_{\mathbf k}|0\rangle
=
a_{-\mathbf k}|0\rangle
=0
\quad\Longleftrightarrow\quad
b_c|0\rangle
=
b_s|0\rangle
=0
$$

進行波基底では波数 $\mathbf k$ と $-\mathbf k$ の二つのモードを扱い、定在波基底では cos 型と sin 型の二つのモードを扱います。

この対応は、時間発展による squeezing を理解する上でも重要です。後に見るように、進行波基底での $\mathbf k$ と $-\mathbf k$ の two-mode squeezing は、定在波基底では二つの振動子それぞれの single-mode squeezing として記述できます。


## 4. インフレーションのモード方程式と squeezing

### Mukhanov–Sasaki 方程式

標準的な運動項を持つ単一のスカラー場（インフラトン）がインフレーションを駆動する場合を考えます。Mukhanov–Sasaki 変数

$$
v=z\zeta,
\qquad
z=\frac{a\dot\phi_0}{H}
$$

を導入すると、二次作用は

$$
S
=
\frac12\int d\eta\,d^3x\,
\left[
(v')^2-(\nabla v)^2+\frac{z''}{z}v^2
\right]
$$

となります。ここで $\zeta$ は共動曲率摂動、$\eta$ は共形時間で、プライムは $\eta$ による微分を表します。

Fourier モードの運動方程式は

$$
v_{\mathbf k}''
+
\left(
k^2-\frac{z''}{z}
\right)v_{\mathbf k}
=0
$$

です。したがって、§3 で導入した各実 Fourier 成分は、有効振動数

$$
\Omega_k^2(\eta)=k^2-\frac{z''}{z}
$$

を持つ時間依存調和振動子として振る舞います。

### 進行波基底での two-mode squeezing

ここで

$$
s(\eta)=\frac{z'}{z}
$$

とおきます。$z''/z=s'+s^2$ を使うと、

$$
(v')^2+\frac{z''}{z}v^2
=
(v'-sv)^2+(sv^2)'
$$

と変形できます。最後の項は時間の全微分なので、境界項を除いた作用は

$$
S
=
\frac12\int d\eta\,d^3x\,
\left[
(v'-sv)^2-(\nabla v)^2
\right]
$$

となります。

この形を採用すると、場 $v$ に共役な正準運動量は

$$
\pi=v'-sv
$$

です。対応する Hamiltonian は

$$
H_\eta
=
\frac12\int d^3x\,
\left[
\pi^2+(\nabla v)^2
+s(v\pi+\pi v)
\right]
$$

となります。以下では、この正準変数を使います。

Schrödinger 描像で、§3 の固定した基準周波数 $k$ による進行波モードの消滅演算子

$$
a_{\mathbf k}
=
\frac1{\sqrt2}
\left(
\sqrt{k}\,v_{\mathbf k}
+\frac{i\pi_{\mathbf k}}{\sqrt{k}}
\right)
$$

を用いると、一つの波数対 $(\mathbf k,-\mathbf k)$ に対応する Hamiltonian は

$$
\begin{aligned}
H_{\eta,\mathbf k}
={}&
k\left(
a_{\mathbf k}^\dagger a_{\mathbf k}
+a_{-\mathbf k}^\dagger a_{-\mathbf k}
+1
\right)\\
&+
is\left(
a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger
-a_{\mathbf k}a_{-\mathbf k}
\right)
\end{aligned}
$$

となります。

第1項は周波数 $k$ の自由振動子、第2項は $\mathbf k$ と $-\mathbf k$ に一つずつ励起を生成・消滅させる項です。

一様な背景では空間並進対称性が保たれるため、生成される励起対の全運動量はゼロになります。進行波基底で見ると、この時間発展は **two-mode squeezing** として現れます。

### Bunch–Davies 真空と Bogoliubov 変換

Hubble スケールの十分内側では $k^2\gg |z''/z|$ となり、squeezing 項は自由 Hamiltonian に比べて無視できるようになります。

十分遠い過去で、この自由 Hamiltonian の基底状態を初期状態として選びます。これが **Bunch–Davies 真空**です。

対応する初期消滅演算子を $a_{\mathbf k}^{\mathrm{in}}$ と書くと、Bunch–Davies 真空は

$$
a_{\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle=0
$$

によって定義されます。

ここから Heisenberg 描像で時間発展を追います。先ほどの Hamiltonian から、

$$
\frac{da_{\mathbf k}(\eta)}{d\eta}
=
-ik\,a_{\mathbf k}(\eta)
+s(\eta)a_{-\mathbf k}^\dagger(\eta)
$$

を得ます。

したがって、時間発展は

$$
a_{\mathbf k}(\eta)
=
\alpha_k(\eta)a_{\mathbf k}^{\mathrm{in}}
+
\beta_k(\eta)a_{-\mathbf k}^{\mathrm{in}\dagger}
$$

という Bogoliubov 変換で表されます。正準交換関係を保つため、

$$
|\alpha_k|^2-|\beta_k|^2=1
$$

が成り立ちます。この関係を満たす Bogoliubov 係数の大きさは、非負のパラメータ $r_k$ を使って

$$
|\alpha_k|=\cosh r_k,
\qquad
|\beta_k|=\sinh r_k
$$

と表せます。

$r_k$ は **squeezing parameter** と呼ばれ、squeezing の強さを表します。初期真空では $r_k=0$ であり、時間発展によって $r_k$ が大きくなるほど、消滅演算子への生成演算子の混合が強くなります。

### 定在波基底での single-mode squeezing

ここまでは進行波基底を使い、$\mathbf k$ と $-\mathbf k$ の two-mode squeezing として時間発展を記述しました。しかし、**squeezing が二つのモードの間に生じるという性質は、進行波基底を選んだことによるものです。**

§3 で導入した定在波基底では、

$$
a_{\mathbf k}
=
\frac{b_c-ib_s}{\sqrt2},
\qquad
a_{-\mathbf k}
=
\frac{b_c+ib_s}{\sqrt2}
$$

です。この変換を Hamiltonian に代入すると、

$$
H_{\eta,\mathbf k}
=
\sum_{A=c,s}
\left[
k\left(b_A^\dagger b_A+\frac12\right)
+
\frac{is}{2}
\left(b_A^{\dagger2}-b_A^2\right)
\right]
$$

となります。

進行波基底で二つのモードを結びつけていた項は、定在波基底ではそれぞれのモードの squeezing 項に分かれます。

実際、Heisenberg 方程式は

$$
\frac{db_A(\eta)}{d\eta}
=
-ik\,b_A(\eta)
+s(\eta)b_A^\dagger(\eta)
$$

となり、

$$
b_A(\eta)
=
\alpha_k(\eta)b_A^{\mathrm{in}}
+
\beta_k(\eta)b_A^{\mathrm{in}\dagger}
$$

という single-mode の Bogoliubov 変換が得られます。

cos 型と sin 型の二つのモードは互いに独立で、同じ squeezing を受けます。両基底で初期真空も共通なので、

$$
a_{\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=
a_{-\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=0
$$

は

$$
b_c^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=
b_s^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=0
$$

と等価です。

<iframe src="app/supporting.html?lang=ja&amp;view=basis" title="Fourier半空間と進行波・定在波の基底変換" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1200px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

図では同じ量子状態の共分散行列を、進行波基底と定在波基底で比較しています。進行波基底では二つのモード間に相関が現れますが、定在波基底では互いに独立な二つの同一のブロックに分解されます。

つまり、**two-mode squeezing と二つの single-mode squeezing は、同じ量子状態の時間発展を異なるモード基底で表したもの**です。

進行波基底では空間並進対称性と運動量保存が明瞭になり、定在波基底では各実自由度の位相空間における squeezing を直接調べられます。

以下では後者を使い、一つの実定在波モードの量子状態がどのように変形するかを追います。

## 5. de Sitter 時空での squeezing とモード関数

### de Sitter 背景での Bogoliubov 変換

§4 では、インフレーション中の各 Fourier モードが時間依存調和振動子として振る舞い、その量子状態の時間発展を Bogoliubov 変換で表せることを見ました。ここでは具体的な背景を選び、Bogoliubov 係数と squeezing の時間発展を解析的に求めます。

厳密に解ける例として、de Sitter 時空中の自由・質量ゼロ・最小結合スカラー場 $\phi$ を考えます。これは §4 の曲率摂動 $\zeta$ そのものではありませんが、slow-roll インフレーションの曲率摂動では近似的に同じ時間発展が得られます。また、適切に正準規格化したテンソル摂動も同じモード方程式に従います。

de Sitter 背景では

$$
a(\eta)=-\frac1{H\eta},
\qquad
\mathcal H=\frac{a'}a=-\frac1\eta
$$

です。$H$ は一定の Hubble parameter、$\eta<0$ は共形時間です。

§3 で導入した二つの実定在波モード $A=c,s$ のそれぞれについて、正準変数と運動量を

$$
q_A=a\phi_A,
\qquad
p_A=q_A'-\mathcal Hq_A=a\phi_A'
$$

と定義します。これは §4 の $s=z'/z$ を $s=\mathcal H$ に置き換えたものに対応し、同じ形の Hamiltonian が得られます。モード方程式は

$$
q_A''
+
\left(
k^2-\frac2{\eta^2}
\right)q_A=0
$$

です。

以下では

$$
x=-k\eta=\frac{k}{aH},
\qquad
N=\ln\frac{a}{a_{\mathrm{cross}}}=-\ln x
$$

を用います。$x\gg1$ は subhorizon、$x=1$ は Hubble crossing、$x\ll1$ は superhorizon に対応します。

§4 で得た Heisenberg 方程式

$$
b_A'(\eta)
=
-ik\,b_A(\eta)
+s(\eta)b_A^\dagger(\eta)
$$

において、今は

$$
s(\eta)=\mathcal H=\frac{k}{x}
$$

です。

Bogoliubov 変換

$$
b_A(\eta)
=
\alpha_k(\eta)b_A^{\mathrm{in}}
+
\beta_k(\eta)b_A^{\mathrm{in}\dagger}
$$

を代入すると、

$$
\begin{aligned}
\alpha_k'&=-ik\alpha_k+s\beta_k^*,\\
\beta_k'&=-ik\beta_k+s\alpha_k^*
\end{aligned}
$$

を得ます。

Bunch–Davies 真空に対応する初期条件は、$x\to\infty$ で

$$
\alpha_k\sim e^{ix},
\qquad
\beta_k\to0
$$

となることです。この条件を満たす厳密解は

$$
\begin{aligned}
\alpha_k(\eta)
&=
\left(1+\frac{i}{2x}\right)e^{ix},\\
\beta_k(\eta)
&=
-\frac{i}{2x}e^{-ix}
\end{aligned}
$$

です。

したがって、

$$
|\beta_k|^2=\frac1{4x^2}
$$

であり、§4 で定義した squeezing parameter は

$$
r_k=\operatorname{arsinh}\frac1{2x}
$$

となります。

Subhorizon 極限では

$$
r_k\simeq\frac1{2x}\ll1
\qquad (x\gg1)
$$

なので、量子状態はほぼ初期真空のままです。一方、superhorizon 極限では

$$
r_k\simeq-\ln x=N
\qquad (x\ll1)
$$

となり、squeezing が発達します。

実際、

$$
\frac{dr_k}{dN}
=
\frac1{\sqrt{1+4x^2}}
$$

なので、十分 superhorizon に入ると、1 e-fold の膨張につれて squeezing parameter がほぼ1ずつ増加します。

### モード関数と superhorizon 解

ここまでは Bogoliubov 係数を使って時間発展を記述してきました。同じ時間発展は、場の演算子を初期消滅演算子で展開したときのモード関数としても表せます。

波数対 $(\mathbf k,-\mathbf k)$ の実定在波モード $A=c,s$ について、正準変数 $q_{A,\mathbf k}=a\phi_{A,\mathbf k}$ を

$$
q_{A,\mathbf k}(\eta)
=
f_k(\eta)b_A^{\mathrm{in}}
+
f_k^*(\eta)b_A^{\mathrm{in}\dagger}
$$

と展開すると、Bogoliubov 変換との比較から、

$$
f_k(\eta)
=
\frac{\alpha_k+\beta_k^*}{\sqrt{2k}}
=
\frac{1+i/x}{\sqrt{2k}}e^{ix}
$$

を得ます。$f_k$ は Bunch–Davies 条件を満たす、正準変数のモード関数です。

元の場 $\phi_{A,\mathbf k}=q_{A,\mathbf k}/a$ のモード関数は

$$
\frac{f_k}{a}
=
\frac{H}{\sqrt{2k^3}}(x+i)e^{ix}
$$

です。Superhorizon 極限 $x\ll1$ で展開すると、

$$
\frac{f_k}{a}
=
\frac{H}{\sqrt{2k^3}}
\left[
i\left(1+\frac{x^2}{2}+O(x^4)\right)
-\frac{x^3}{3}+O(x^5)
\right]
$$

となります。虚部は一定値に近づき、実部は $x^3\propto a^{-3}$ で減衰します。

この二つの振る舞いは、モード方程式の独立な解に対応しています。$f_k$ は

$$
f_k''
+
\left(k^2-\frac{a''}{a}\right)f_k
=0
$$

を満たすので、これを $f_k/a$ の方程式に書き換えると、

$$
\left[a^2\left(\frac{f_k}{a}\right)'\right]'
+
k^2a^2\frac{f_k}{a}
=0
$$

となります。Superhorizon で勾配項を無視した方程式の一般解は、

$$
\frac{f_k(\eta)}{a(\eta)}
\simeq
C_1+
C_2\int^\eta\frac{d\tilde\eta}{a^2(\tilde\eta)}
$$

です。de Sitter 背景では第二項が $a^{-3}$ に比例するため、先ほどの厳密解の虚部と実部は、それぞれ保存モード（growing mode）と減衰モード（decaying mode）に対応します。虚部の $O(x^2)$ は、有限波数による保存モードへの補正です。

Superhorizon では保存モードが優勢になります。実際、Bunch–Davies 真空における場の分散は

$$
\begin{aligned}
\langle\phi_{A,\mathbf k}^2\rangle
&=
\left|\frac{f_k}{a}\right|^2\\
&=
\frac{H^2}{2k^3}(1+x^2)
\end{aligned}
$$

なので、

$$
\langle\phi_{A,\mathbf k}^2\rangle
\longrightarrow
\frac{H^2}{2k^3}
\qquad(x\to0)
$$

となります。

元の場の揺らぎが一定値に近づく一方、正準変数 $q_{A,\mathbf k}=a\phi_{A,\mathbf k}$ の量子状態は強く squeezing され続けます。保存モードの優勢化と squeezing の発達は、同じ量子時間発展を異なる側面から捉えたものです。

次節では、この時間発展を固定した quadrature 座標上の Wigner 関数として調べます。

<iframe src="app/supporting.html?lang=ja&amp;view=background" title="背景項と厳密de Sitterモード関数" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

## 6. Visualization

ここまで求めた時間発展を、一つの実定在波モード $A=c,s$ の位相空間上で見てみます。

§2 と同じく、固定した基準周波数 $k$ による無次元の quadrature

$$
Q=\sqrt{k}\,q_A=\sqrt{k}\,a\phi_A,
$$

$$
P=\frac{p_A}{\sqrt{k}}
=
\frac{q_A'-\mathcal Hq_A}{\sqrt{k}}
=
\frac{a\phi_A'}{\sqrt{k}}
$$

を使います。これらは

$$
[\hat Q,\hat P]=i
$$

を満たす正準変数です。

時間発展の計算には Heisenberg 描像の演算子を用いますが、図は Schrödinger 描像に対応させ、**固定した $Q,P$ 軸の上で量子状態の Wigner 関数が変形する様子**を示しています。座標軸の向き、縮尺、表示範囲はすべてのフレームで固定しています。

時間は $N=-\ln x$ で表し、$x=12$ から $x=0.2$ まで動かせます。

<iframe src="app/index.html?lang=ja" title="インフレーションの squeezing：回転・スクイーズ・合成Hamilton流" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

最初の二つのパネルでは Hamilton flow の回転成分と squeezing 成分を別々に示し、3番目のパネルでは合成した流れと Wigner 関数の等高線を重ねています。

### Bogoliubov 変換から Wigner 関数へ

位相空間座標と共分散行列を

$$
\mathbf Z=
\begin{pmatrix}
Q\\
P
\end{pmatrix},
\qquad
\Sigma_{ij}
=
\frac12
\left\langle
\{\hat Z_i,\hat Z_j\}
\right\rangle
$$

とします。Bunch–Davies 真空は平均値ゼロの Gaussian 状態なので、その時間発展は共分散行列によって特徴づけられます。

§5 の Bogoliubov 変換から、

$$
\begin{aligned}
\langle Q^2\rangle
&=
\frac12|\alpha_k+\beta_k^*|^2,\\
\langle P^2\rangle
&=
\frac12|\alpha_k-\beta_k^*|^2,\\
\frac12\langle QP+PQ\rangle
&=
\operatorname{Im}(\alpha_k\beta_k)
\end{aligned}
$$

が得られます。

ここに de Sitter 背景での厳密解を代入すると、

$$
\Sigma(x)
=
\frac12
\begin{pmatrix}
1+x^{-2}&-x^{-1}\\
-x^{-1}&1
\end{pmatrix}
$$

となります。

Gaussian 状態の Wigner 関数は

$$
W(\mathbf Z;x)
=
\frac1{2\pi\sqrt{\det\Sigma}}
\exp\left[
-\frac12\mathbf Z^T\Sigma^{-1}\mathbf Z
\right]
$$

です。図では

$$
\mathbf Z^T\Sigma^{-1}\mathbf Z=1
$$

を満たす等高線を描いています。

共分散行列の固有値は

$$
\sigma_\pm^2
=
\frac12e^{\pm2r_k}
$$

なので、§5 で求めた $r_k$ の増加とともに、Wigner 分布は細長い楕円へと変形します。

一方、

$$
\det\Sigma=\frac14
$$

は時間によらず一定です。Squeezing は、一方向の揺らぎを小さくしながら共役な方向の揺らぎを大きくする、位相空間の面積を保存した変形です。

楕円の長軸が正の $Q$ 軸となす角度を $\varphi_k$ とすると、

$$
\varphi_k
=
\frac12\arg(\alpha_k\beta_k)
=
-\frac12\arctan(2x)
$$

となります。

Squeezing の強さだけでなく、楕円の向きも Bogoliubov 係数から決まります。初期にはほぼ円形だった分布が次第に細長くなり、その長軸は $Q$ 軸へ近づいていきます。

<iframe src="app/supporting.html?lang=ja&amp;view=squeezing" title="e-fold時間に対する squeezing の大きさと長軸の角度" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

### 成長解と Wigner 楕円の関係

§5 では、superhorizon で減衰解の寄与が小さくなり、場の振幅がほぼ一つの初期 quadrature で決まることを見ました。

これが位相空間でどのように現れるかを考えます。

共分散行列から、

$$
\operatorname{Var}(Q)
=
\frac12\left(1+\frac1{x^2}\right),
\qquad
\operatorname{Var}(P)=\frac12
$$

です。

$Q$ 方向の分散は増大しますが、$P$ 方向の周辺分散は一定のままです。小さくなるのは $P$ 単独の揺らぎではなく、$Q$ と $P$ の特定の線形結合の揺らぎです。

実際、

$$
\operatorname{Var}(P+xQ)=\frac{x^2}{2}
$$

が成り立ちます。

この関係は、§5 のモード関数からも直接確認できます。初期 quadrature を使うと、

$$
P+xQ
=
x\left(
\cos x\,Q_A^{\mathrm{in}}
-
\sin x\,P_A^{\mathrm{in}}
\right)
$$

となるためです。

Superhorizon ではこの組合せの揺らぎが小さくなり、位相空間上の分布は

$$
P\simeq-xQ
$$

という関係の近くに集中します。

これは、成長解に支配されたモードの位相空間での振る舞いに対応しています。実際、§5 の $q_g\propto a$ に対して、superhorizon では

$$
Q_g\propto\frac1x,
\qquad
P_g\simeq-xQ_g
$$

となります。

Wigner 楕円の長軸はこの方向へ近づき、直交する方向の幅が小さくなります。

ただし、成長・減衰解は運動方程式の独立な解であり、Wigner 楕円の主軸は量子状態の共分散から定まります。有限時刻では両者の方向は必ずしも一致せず、superhorizon 極限で上の対応が明瞭になります。

### Hamilton flow：回転と squeezing

この Wigner 分布の変形を生み出す Hamilton flow を調べます。

§4 の Hamiltonian を固定した quadrature で書き、時間変数を共形時間 $\eta$ から $N$ に変えると、

$$
\boxed{
K_N
=
\frac{x}{2}(Q^2+P^2)
+
\frac12(QP+PQ)
}
$$

となります。

対応する Hamilton 方程式は

$$
\frac{d\mathbf Z}{dN}
=
A(N)\mathbf Z,
\qquad
A(N)=
\begin{pmatrix}
1&x\\
-x&-1
\end{pmatrix}
$$

です。

この行列は

$$
A(N)
=
x
\begin{pmatrix}
0&1\\
-1&0
\end{pmatrix}
+
\begin{pmatrix}
1&0\\
0&-1
\end{pmatrix}
$$

と分解できます。

第1項は位相空間の回転、第2項は $Q$ 方向の伸長と $P$ 方向の収縮を生む squeezing です。

$x\gg1$ では回転が優勢ですが、宇宙膨張によって $x$ が減少すると、squeezing の寄与が相対的に大きくなります。$x=1$ では二つの寄与が同程度となり、瞬間的な流れはシアー型になります。$x\ll1$ では伸長と収縮が支配的になります。

Hamiltonian が二次式であるため、Wigner 関数はこの古典的な Hamilton flow に沿って正確に時間発展します。共分散行列も

$$
\frac{d\Sigma}{dN}
=
A\Sigma+\Sigma A^T
$$

に従います。

また、

$$
\operatorname{tr}A=0
$$

なので、位相空間の面積が保存されます。これは先ほど得た $\det\Sigma=1/4$ が一定であることとも対応しています。

アニメーションでは、次の変化を追ってみてください。

1. **Subhorizon（$x\gg1$）：** 回転が優勢で、Wigner 分布はほぼ円形です。表示開始時にわずかに楕円なのは、$x=\infty$ ではなく $x=12$ から描いているためです。
2. **Hubble crossing（$x=1$）：** 回転と squeezing の寄与が同程度になり、楕円の変形が明瞭になります。
3. **Superhorizon（$x\ll1$）：** 長軸が伸び、短軸が細くなります。$Q$ と $P$ の相関が強まり、分布は成長解に対応する方向へ集中していきます。

なお、アニメーション中のベクトル場は見やすさのため、矢印の長さに $1/\sqrt{1+x^2}$ と共通の描画倍率を掛けています。Wigner 関数の時間発展にはこの補正を加えていません。

ここまで見てきた Bogoliubov 混合、成長解の優勢化、Wigner 分布の squeezing は、すべて同じ量子時間発展を異なる表現で捉えたものです。

元の場の振幅は superhorizon で一定値に近づきますが、正準変数の位相空間では、一方向の揺らぎが増幅され、共役な方向の揺らぎが抑えられていきます。こうして揺らぎは、ほぼ一つの確率的な振幅と、それに共通する成長解の時間発展によって特徴づけられるようになります。

この構造が、原始揺らぎの古典的な統計記述と、再突入後の音響振動における時間位相のコヒーレンスを理解する出発点になります。

## 8. 成長・減衰モードと位相空間の方向

superhorizon で勾配項を無視すると、

$$
q''
-
\frac{z''}{z}q
\simeq0
$$

です。

一般解は

$$
q
=
Cz
+
Dz
\int^\eta
\frac{d\eta'}{z^2(\eta')}
$$

と書けます。

今回の正準運動量

$$
p=q'-\frac{z'}zq
$$

を使えば、

$$
p=\frac Dz
$$

となります。

積分の積分定数は $C$ に吸収できます。

アトラクター型のインフレーションでは、第1項は

$$
\zeta=\frac qz=C
$$

という一定の曲率摂動を与えます。一方、第2の独立解は時間とともに減衰します。

テストスカラー場では $z$ を $a$ に置き換えればよく、

$$
q\simeq Ca
$$

と成長する一方で、

$$
\phi_A=\frac qa
$$

は一定値へ近づきます。

これが「再スケールした変数は大きく伸びるが、元の場は凍結する」という関係です。

ただし、勾配項を完全に捨てた極限だけから、有限の $k$ における成長解の正準運動量が厳密にゼロだと結論することはできません。

図で用いている厳密な成長解・減衰解のベクトルは、例えば

$$
\mathbf G(x)
=
\begin{pmatrix}
\sin x+\cos x/x\\
-\cos x
\end{pmatrix},
$$

$$
\mathbf D(x)
=
\begin{pmatrix}
\cos x-\sin x/x\\
\sin x
\end{pmatrix}
$$

と取れます。

$x\ll1$ では

$$
\mathbf G
\sim
\begin{pmatrix}
x^{-1}\\
-1
\end{pmatrix},
\qquad
\mathbf D
\sim
\begin{pmatrix}
-x^2/3\\
x
\end{pmatrix}.
$$

[メインのアニメーション](#main-animation)で**厳密な成長解・減衰解の方向**を表示し、同じ時刻の**Wigner 楕円の主軸**と比較してください。

成長・減衰モードは時間発展方程式の二つの独立解です。一方、楕円の主軸は共分散行列の固有ベクトルであり、瞬間的な流れの方向とも別の概念です。

そのため、有限時刻ではこれらは一般に一致しません。また、$\mathbf G$ と $\mathbf D$ は互いに直交しませんが、共分散楕円の長軸と短軸は定義上直交します。

ただし $x\to0$ の極限では、長軸と短軸はそれぞれ成長解と減衰解の極限方向へ近づきます。この意味で「スクイーズされた短軸が減衰モードに対応する」と表現できます。

 squeezing によって狭くなる方向は、条件付き分布を見るとさらに明確になります。

共分散行列から、

$$
\mathbb E[P\mid Q]
=
-\frac{x}{1+x^2}Q
$$

および

$$
\operatorname{Var}(P\mid Q)
=
\frac{x^2}{2(1+x^2)}
$$

が得られます。

一方、

$$
\operatorname{Var}(P)=\frac12
$$

は時間によらず一定です。

つまり、$P$ 自体の周辺分布が細くなるわけではありません。$Q$ が与えられたとき、古典的な軌道に対応する関係

$$
P\simeq-\frac{x}{1+x^2}Q
$$

から外れる幅が小さくなっていきます。

ここでの条件付き分布は、正の Wigner 関数を通常の Gaussian 密度として扱ったときの数学的な条件付けです。$Q$ と $P$ の同時射影測定を表しているわけではありません。

また、減衰モードの**寄与**が相対的に小さくなることは、その解に掛かる時間非依存の積分定数 $D$ 自体が時間とともに消えることを意味しません。

## 9. 摂動が古典的に見える理由

量子状態の平均値がゼロでも、その分散がゼロとは限りません。

同じ厳密モード関数から、対数波数間隔あたりのテストスカラー場のパワーは

$$
\mathcal P_\phi(k)
=
\frac{k^3}{2\pi^2}
\left|
\frac{f_k}{a}
\right|^2
$$

となり、

$$
\mathcal P_\phi(k)
=
\frac{H^2}{4\pi^2}
(1+x^2)
$$

です。

superhorizon 極限 $x\to0$ では

$$
\mathcal P_\phi(k)
\longrightarrow
\left(
\frac{H}{2\pi}
\right)^2.
$$

したがって、再スケール変数 $q=a\phi$ の分散が大きく伸びることと、元の場 $\phi$ の分散が有限値へ凍結することは両立します。

曲率摂動では $a$ の代わりに $z$ が入り、その slow-roll 発展が振幅とスペクトルの傾きを決めます。

では、なぜこの量子状態を後の宇宙では古典的なランダム場として扱えるのでしょうか。

まず、この系は Gaussian 状態のまま時間発展し、その Wigner 関数は正です。そのため、同時刻の対称順序相関関数は、Wigner 関数を確率密度とみなした古典的な Gaussian 集団で再現できます。

さらに大きな squeezing によって、

- 成長モードが圧倒的に優勢になる
- 場と正準運動量の間に強い相関が生じる
- 古典的な成長解から外れる方向の幅が非常に小さくなる

という状況が生まれます。

この意味で、原始揺らぎは後の線形発展を計算する際、実効的には古典的な確率場として扱うことができます。

ただし、量子状態そのものが古典状態へ変わったわけではありません。交換関係

$$
[\hat Q,\hat P]=i
$$

は残り、波動関数が自発的に収縮するわけでも、純粋状態が時間発展だけで混合状態へ変わるわけでもありません。

環境との相互作用によるデコヒーレンスは、 squeezing とは別の物理過程です。

この「古典的な統計で再現できること」と「量子状態そのものが古典状態になること」の違いは、原始揺らぎの量子的起源を議論するときに重要です。詳しくは [Martin & Vennin](https://arxiv.org/abs/1510.04038) を参照してください。

<iframe src="app/supporting.html?lang=ja&amp;view=samples" title="シンプレクティック発展の前後におけるWignerサンプル" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

時刻スライダーを初期から最後まで動かしてください。

時間発展によってランダムさそのものが消えるわけではありません。長軸方向に許される振幅の範囲は大きくなる一方で、オレンジ色の条件付き平均線から横方向へ外れる幅が小さくなります。

左右のパネルでは同じ座標範囲を使っています。描かれている Wigner 等高線が囲む確率重みは約39%なので、サンプル点の多くが楕円の外側に現れることも自然です。

## 10. 音響振動の位相コヒーレンスと CMB

ここまで見てきた squeezing は、CMB の音響ピークとも深く関係しています。

ただし、まず「位相が揃う」という表現の意味を区別する必要があります。

統計的に一様・等方的な Gaussian 場では、二つの定在波成分 $\zeta_R$ と $\zeta_I$ は同じ分散を持ち、その振幅平面に特別な方向はありません。

$$
\zeta_{\mathbf k}
=
\frac{\zeta_R+i\zeta_I}{\sqrt2}
$$

と書けば、

$$
\arg\zeta_{\mathbf k}
$$

という**空間的な Fourier 位相**はランダムです。

インフレーションが、異なる $\mathbf k$ の Fourier 位相を同じ値へ揃えるわけではありません。そもそも空間の原点を平行移動するだけでも、この位相は変化します。

CMB の「位相コヒーレンス」が指しているのは、この空間的な位相ではなく、各 $k$ モードが horizon re-entry 後に始める**時間振動の位相**です。

再突入後の音響変数を模式的に

$$
X_k(\eta)
=
A_k\cos(kr_s)
+
B_k\sin(kr_s)
$$

と書きます。ここで

$$
r_s(\eta)
=
\int^\eta
c_s(\eta')\,d\eta'
$$

は音響地平線です。

一般には、二階の運動方程式には cos 型と sin 型という二つの独立解があります。もし $A_k$ と $B_k$ が互いに独立なランダム変数なら、各 realization は異なる時間位相で振動し、集団平均すると振動構造は消えてしまいます。

しかし、標準的なインフレーションでは superhorizon で一つの断熱的成長モードが圧倒的に優勢になります。そのため、再突入時の密度摂動と速度摂動は独立な二つのランダム変数ではなく、同じ原始振幅から決まります。

理想化した自由振動子なら、時間原点を適切に取ることで

$$
B_k\simeq0
$$

と書けます。

つまり、各モードの**振幅や符号はランダムでも、時間依存する伝達関数は共通**です。

この初期条件と音響ピークの関係については、[Hu & White](https://arxiv.org/abs/astro-ph/9602019)で詳しく議論されています。

以下の表示では、初期振幅の総分散を同じ $\sigma^2$ に揃えた二つの集団を比較します。

時間位相がコヒーレントな場合、

$$
\langle|A_k|^2\rangle=\sigma^2,
\qquad
B_k=0
$$

なので、

$$
\langle|X_k|^2\rangle
=
\sigma^2\cos^2(kr_s)
$$

となります。

一方、cos 型と sin 型が独立に励起され、

$$
\langle|A_k|^2\rangle
=
\langle|B_k|^2\rangle
=
\frac{\sigma^2}{2},
$$

$$
\langle A_kB_k^*\rangle=0
$$

なら、

$$
\langle|X_k|^2\rangle
=
\frac{\sigma^2}{2}
$$

となり、時間振動の模様は平均によって消えます。

したがって、**振幅がランダムであること自体は音響ピークを消しません**。ピークを消すのは、二つの独立な時間 quadrature がランダムに励起されることです。

実際の CMB の伝達関数は、この単純な cos 振動より複雑です。重力ポテンシャルによる駆動、バリオンの慣性、ニュートリノ、Silk damping、再結合、そして三次元摂動から天球への射影などが含まれます。

それでも、多数の Fourier モードが共通の時間位相関係を持つことが、$C_\ell$ に一連の音響ピークを残すという基本構造は変わりません。

<iframe src="app/supporting.html?lang=ja&amp;view=acoustic" title="ランダムな音響振動の実現例とコヒーレント・非コヒーレントな平均パワー" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

コヒーレントな realization の零点でカーソルを止めてみてください。振幅も符号も異なる8本の曲線が、同じ時刻にゼロを通過します。

非コヒーレントな場合には、この零点は揃いません。

下段では、有限個の realization から得た推定パワーと、厳密な集団平均を分けて表示しています。音響地平線を固定して波数 $k$ を変えれば、この時間方向の振動が波数空間のピーク列として現れます。

音響ピークは、原始揺らぎが一つのコヒーレントな成長モードに支配されていたことを強く示します。ただし、それだけで量子 squeezing そのものを直接測定したことになるわけではなく、インフレーションだけを一意に証明するものでもありません。

## 適用範囲と参考文献

この記事のアニメーションが扱うのは、与えられた de Sitter 背景上での、自由な線形 Gaussian 場の時間発展です。再加熱、非 Gaussian 性、環境との相互作用によるデコヒーレンス、実際の CMB スペクトルの数値計算は含めていません。

メインのアニメーションを $x=0.2$ で止めているのは、固定した座標範囲の中で短軸の幅まで視認できるようにするためです。より小さい $x$ まで進めれば squeezing はさらに強くなりますが、不確定性関係や位相空間面積が失われるわけではありません。

また、成長モードが一定の $\zeta$ を与えるという議論では、通常のアトラクター型インフレーションを仮定しています。非アトラクター型では superhorizon の $\zeta$ 自体が時間発展する場合があり、その場合は対応する $z(\eta)$ を用いて改めて方程式を解く必要があります。

- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030)：正準変数、モード関数、成長・減衰解と semiclassicality の関係。
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038)：モード分解と部分系、古典的な相関関数と量子状態の違い。
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019)：原始初期条件と CMB 音響ピークの位相構造。

<!-- # インフレーションの量子揺らぎと squeezing 

## 1. インフレーションは何を生成するのか

インフレーションは、真空の揺らぎに確定した古典的振幅を与えるわけではありません。時間発展するのは量子状態であり、平均値がゼロのままでも、その相関は大きく変化します。各Fourier波長について、位相空間でほぼ円形だった真空の分布が、細長いGaussian楕円へと変形します。広がった方向に残るランダムな振幅が、後の宇宙の構造形成に初期条件を与えます。

この記事では、この幾何学を「時間依存振動子」「生成・消滅演算子のBogoliubov混合」「Wigner関数の squeezing 」という三つの記述で追います。さらに、成長モードの優勢が音響振動の**時間位相**のコヒーレンスにつながることを説明します。空間的なFourier位相のランダムさは失われません。


![共通のquadrature座標軸で見たWigner等高線の三つの時期](app/teaser.svg)

一つの定在波モードを三つの時刻で見た予告図です。横軸は場の振幅、縦軸は正準運動量に対応するquadratureで、全時刻で同じ定義と縮尺を使っています。楕円は伸びても面積を保ちます。[メインのアニメーションへ進む](#main-animation)か、まず振動子と基底変換の説明をたどってください。

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

各実成分について、境界項だけ異なる次の作用が squeezing の記述に便利です。$s=z'/z$ と置くと、

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

## 5. 進行波の記述：二モード・ squeezing 

逆向きの進行波の対を固定すると、背景は生成・消滅演算子を対として結びつけます。$s=z^\prime/z$ とし、各波数対を一度だけ数えると、Hamiltonianは

$$
H_{\eta,\mathbf k}=k\left(a_{\mathbf k}^\dagger a_{\mathbf k}
+a_{-\mathbf k}^\dagger a_{-\mathbf k}+1\right)
+is\left(a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger
-a_{\mathbf k}a_{-\mathbf k}\right).
$$

となります。この相互作用は、逆向きの各モードに一つずつ励起を生成・消滅します。これが二モード・ squeezing の記述です。

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

が得られます。$x\ll1$ では $r_k\simeq-\ln x=N$ となり、Hubble exit後の1 e-foldごとに、 squeezing がほぼ1ずつ増えます。$|\beta_k|^2$ は選んだ基準基底での占有数であり、時間依存背景における一意な粒子数ではありません。 squeezing の大きさの数値自体も、正準quadratureの選択に依存します。状態を一貫して記述するのは、共分散全体とその変換則です。

<iframe src="app/supporting.html?lang=ja&amp;view=squeezing" title="e-fold時間に対する squeezing の大きさと長軸の角度" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

crossing後の厳密な曲線と $r_k\simeq N$ を比べてください。右の図は、初めから向きが固定されているのではなく、時間とともに一定方向へ収束することを示します。真空がほぼ円である初期には、角度の幾何学的な違いは小さくなります。

## 6. 定在波の記述：二つの単一モード・ squeezing 

$b_A=(\sqrt{k}q_A+ip_A/\sqrt{k})/\sqrt2$ と定義すると、定在波のHamiltonianは

$$
H_{\eta,A}=k\left(b_A^\dagger b_A+\frac12\right)
+\frac{is}{2}\left(b_A^{\dagger2}-b_A^2\right),
\qquad A=R,I.
$$

となります。二つの実モードは、同一の単一モード・ squeezing を受けます。進行波の演算子との関係は

$$
b_R=\frac{a_{\mathbf k}+a_{-\mathbf k}}{\sqrt2},\qquad
b_I=-\frac{i}{\sqrt2}(a_{\mathbf k}-a_{-\mathbf k}),
\qquad
b_R^{\dagger2}+b_I^{\dagger2}
=2a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger.
$$

です。

進行波基底では対の項が二モード・ squeezing を表し、定在波基底では同じ状態が等しくスクイーズされた二つの状態の積に分かれます。図の楕円は**一つの定在波モード**の状態です。進行波対の片方を捨てた縮約状態ではありません。進行波モード間の量子もつれが部分系の選び方に依存する点は、[MartinとVennin](https://arxiv.org/abs/1510.04038)でも議論されています。

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

<iframe src="app/index.html?lang=ja" title="インフレーションの squeezing ：回転・スクイーズ・合成Hamilton流" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

最初の2パネルは、**その時刻の速度場**を回転とスクイーズに分解したものです。量子状態の等高線を重ねているのは、3番目のパネルだけです。オレンジの点は等高線上を流れに沿って運ばれる目印であり、量子粒子の確定した軌道ではありません。矢印には、時間依存の表示係数 $1/\sqrt{1+x^2}$ と、さらに固定の描画縮尺を共通に掛けています。同じフレーム内でのベクトルの加法は保たれますが、異なるフレームの矢印の長さを、そのまま物理的速度として比較することはできません。状態の時間発展には、この表示補正を加えず厳密解を使っています。

次のように操作してみてください。

1. 最初から再生します。$x$ が大きいときは回転が優勢で、$x$ が1より小さくなるにつれて楕円が伸びます。開始時の等高線は完全な円ではありません。有限の開始時刻で評価した厳密なBunch–Davies状態です。
2. Hubble crossingで止めます。流れはゼロにならず、シアーになっています。 squeezing がこの瞬間に突然始まったわけではありません。
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

描かれた楕円は $\mathbf Z^T\Sigma^{-1}\mathbf Z=1$、すなわちWigner密度が中心値の $e^{-1/2}$ になる等高線です。内部に含まれるWigner重みは $1-e^{-1/2}\simeq0.393$ であり、一次元Gaussian分布の「1 sigmaは68%」とは異なります。半長軸・半短軸は $e^{\pm r_k}/\sqrt2$、面積は常に $\pi/2$ です。ユニタリな squeezing は面積を保存し、散逸による冷却ではありません。また、Wigner関数が正であっても、非可換な $Q$ と $P$ を同時に鋭く測定するための同時確率分布になるわけではありません。

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

[メインのアニメーション](#main-animation)で**厳密な成長解・減衰解の方向**を選び、同じ時刻の**楕円の主軸**と比較してください。

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

正のWigner関数を使えば、同時刻で対称順序を取ったモーメントは古典的Gaussian集団で再現できます。大きな squeezing は、さらに強い場と運動量の関係、および成長モードの優勢をもたらします。そのため、対象とする摂動は実効的に古典的な確率場として時間発展させられます。しかし、交換関係が消えるわけでも、波動関数が収縮するわけでも、この純粋状態が混合状態になるわけでも**ありません**。環境によるデコヒーレンスは別の物理過程であり、この計算には含めていません。観測可能な量子的特徴を論じるには、これらの区別が必要です（[MartinとVennin](https://arxiv.org/abs/1510.04038)）。

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

です。したがって、振幅のランダムさだけではパワーの振動模様は消えませんが、時間方向の二つのquadratureが独立にランダムなら消えます。実際のCMB伝達関数には、重力による駆動、バリオンの慣性、ニュートリノの効果、拡散、再結合、天球への射影が含まれ、純粋なcos関数ではありません。コヒーレントな音響ピークは原始初期条件の構造を検証しますが、それだけで量子 squeezing の測定や、インフレーション起源の一意な証明になるわけではありません。

<iframe src="app/supporting.html?lang=ja&amp;view=acoustic" title="ランダムな音響振動の実現例とコヒーレント・非コヒーレントな平均パワー" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

コヒーレントな実現例の零点でカーソルを止めてください。振幅も符号も異なる8本が、同じ時刻にゼロを通ります。非コヒーレントな実現例では揃いません。下段は有限個のサンプルからの推定と厳密な集団平均を区別しています。一定の音響地平線で波数を変えたとき、このような振動がピークの模様に対応します。

## 適用範囲と参考文献

アニメーションは、与えられたde Sitter背景上での、線形・自由なGaussian状態の時間発展です。再加熱、環境との相互作用、非Gaussian性、CMBスペクトルの数値計算は扱いません。固定軸上でも細い楕円を見分けられるよう、メインのアニメーションは $x=0.2$ で終えています。さらに強い squeezing を描くには、より小さな横断方向の幅を分解する必要があります。不確定性関係が変わるわけではありません。

通常の成長モードに関する結論は、アトラクター背景を仮定しています。非アトラクター型のインフレーションでは $\zeta$ の振る舞いが変わりうるため、このde Sitterの例をそのまま当てはめず、適切な $z(\eta)$ に対する方程式を解く必要があります。

- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030)：正準変数、モード関数、成長・減衰解による記述。
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038)：部分系の選択、および古典的な相関関数と量子状態の区別。
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019)：音響振動の初期条件とピーク構造の解釈。 -->
