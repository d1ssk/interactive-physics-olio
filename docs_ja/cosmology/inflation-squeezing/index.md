# インフレーションの量子揺らぎと squeezing

## 1. 真空揺らぎから宇宙の構造へ

現在の宇宙には、銀河や銀河団の分布、CMB の温度・偏光異方性として、さまざまなスケールの揺らぎが残されています。その起源をたどると、宇宙初期の微小な原始揺らぎに行き着きます。インフレーション理論は、この原始揺らぎの起源を量子場の真空揺らぎに求めます。

インフレーションの間、量子場の各 Fourier モードは宇宙膨張に応じて時間発展します。その量子状態を位相空間で表すと、真空の Wigner 分布は、初めのほぼ円形から次第に細長い楕円へと変形します。この **squeezing** によって、場の振幅と運動量の間に強い相関が生まれ、一つの成長モードが優勢になります。これが、原始揺らぎを古典的な確率場として記述できるようになる過程を理解する鍵です。

この記事では、時間依存調和振動子から出発し、生成・消滅演算子の Bogoliubov 変換、Wigner 関数の変形を順に調べます。最後に、superhorizon での成長モードの優勢化が、CMB の音響ピークに現れる時間位相のコヒーレンスとどう結びつくかを考えます。

<figure style="margin-inline: auto; text-align: center;">
  <img src="app/teaser.svg" alt="共通の quadrature 座標軸で見た Wigner 等高線の三つの時期" width="720" height="250" style="display: block; max-width: 100%; height: auto; margin-inline: auto;">
</figure>

図は、一つの実定在波モードの Wigner 関数の等高線を、三つの時刻について同じ位相空間上に描いたものです。横軸と縦軸には、場の振幅と正準運動量から定義した quadrature を取っています。分布が伸びる方向と縮む方向に分かれていく様子を、この後で数式とともに追います。

[メインのアニメーション](#main-animation)では、この変形を連続的に見ることができます。

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

<details markdown="1">
<summary>Wigner 関数の定義と解釈</summary>

Wigner 関数は、密度演算子 $\hat\rho$ で表される量子状態を位相空間上の実関数に写したものです。$[\hat Q,\hat P]=i$ の規約では、

$$
\begin{aligned}
W(Q,P)&=\frac1{2\pi}\int_{-\infty}^{\infty}d\xi\,e^{-iP\xi}\left\langle Q+\frac\xi2\right|\hat\rho\left|Q-\frac\xi2\right\rangle
\end{aligned}
$$

と定義します。ここで $|Q\rangle$ は $\hat Q$ の固有状態で、$Q,P$ は位相空間上の実数です。時間依存性は $\hat\rho$ に含め、式では省略しています。純粋状態なら、積分内の密度行列は $\psi(Q+\xi/2)\psi^*(Q-\xi/2)$ になります。

全体の積分は $1$ で、一方の座標を積分した周辺分布は、それぞれの quadrature の測定確率密度を与えます。

$$
\int dQ\,dP\,W(Q,P)=1,
$$

$$
\begin{aligned}
\int dP\,W(Q,P)&=\langle Q|\hat\rho|Q\rangle,\\
\int dQ\,W(Q,P)&=\langle P|\hat\rho|P\rangle
\end{aligned}
$$

また、位相空間上のモーメントは、演算子を対称順序（Weyl 順序）に並べた期待値に対応します。例えば、

$$
\int dQ\,dP\,QP\,W(Q,P)
=\frac12\langle\hat Q\hat P+\hat P\hat Q\rangle
$$

です。この性質により、二つの quadrature の揺らぎや相関を、一つの位相空間上で見ることができます。

ただし、一般の量子状態では $W$ が負になることもあるため、通常の確率密度と区別して**準確率分布**と呼びます。Gaussian 状態では $W\geq0$ なので、対称順序の相関関数を古典的な確率分布による平均として計算できます。正の Wigner 関数を持つ真空も、交換関係と不確定性関係に従う量子状態です。定義と基本的性質は [O’Connell](https://arxiv.org/abs/1009.4431) にもまとめられています。

例えば $b=(Q+iP)/\sqrt2$ の真空は、

$$
W_0(Q,P)=\frac1\pi e^{-(Q^2+P^2)}
$$

という円対称の分布です。各 quadrature の分散は $1/2$ であり、真空でも振幅と運動量の揺らぎが残ることが分かります。

</details>

### Heisenberg 描像：演算子の時間発展と Bogoliubov 混合

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

以下では、時間発展の計算には主に Heisenberg 描像を用い、Bogoliubov 係数やモード関数から共分散を求めます。その共分散を使い、Schrödinger 描像での状態の Wigner 関数を、固定した $Q,P$ 軸の上に描きます。ここで「固定した軸」とは、瞬間基底に合わせて座標を取り直さないという意味であり、計算を Schrödinger 描像で行うという意味ではありません。このように、演算子の時間発展を計算し、その結果を状態の分布の変形として表示することで、振動的な領域から superhorizon まで一貫して追うことができます。

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
\frac{\hat q_{c,\mathbf k}-i\hat q_{s,\mathbf k}}{\sqrt2},
\qquad
\hat v_{-\mathbf k}
=
\frac{\hat q_{c,\mathbf k}+i\hat q_{s,\mathbf k}}{\sqrt2}
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

$\hat q_{c,\mathbf k},\hat q_{s,\mathbf k}$ は Hermitian 演算子であり、cos 型と sin 型の二つの実配置自由度を表します。

正準運動量についても同様に

$$
\hat\pi_{\mathbf k}
=
\frac{\hat p_{c,\mathbf k}-i\hat p_{s,\mathbf k}}{\sqrt2}
$$

と分解すると、

$$
[\hat q_{A,\mathbf k},\hat p_{B,\mathbf k^{\prime}}]=i\delta_{AB}\delta_{\mathbf k,\mathbf k^{\prime}},
$$

$$
[\hat q_{A,\mathbf k},\hat q_{B,\mathbf k^{\prime}}]=[\hat p_{A,\mathbf k},\hat p_{B,\mathbf k^{\prime}}]=0
$$

が成り立ちます。ここで $A,B=c,s$、$\mathbf k,\mathbf k^{\prime}\in\mathcal K_+$ です。したがって、各波数対は二つの独立な実調和振動子として扱えます。

それぞれの振動子に対して、進行波基底と同じ基準周波数 $k$ を用いて

$$
b_{A,\mathbf k}
=
\frac1{\sqrt2}
\left(
\sqrt{k}\,\hat q_{A,\mathbf k}
+
\frac{i\hat p_{A,\mathbf k}}{\sqrt{k}}
\right),
\qquad A=c,s
$$

と定義します。$b_{c,\mathbf k},b_{s,\mathbf k}$ は、それぞれ cos 型と sin 型の**定在波モード（standing-wave modes）**の消滅演算子です。

これらと進行波モードの消滅演算子の関係は、

$$
\begin{aligned}
a_{\mathbf k}
&=
\frac{b_{c,\mathbf k}-ib_{s,\mathbf k}}{\sqrt2},\\
a_{-\mathbf k}
&=
\frac{b_{c,\mathbf k}+ib_{s,\mathbf k}}{\sqrt2}
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
b_{c,\mathbf k}|0\rangle
=
b_{s,\mathbf k}|0\rangle
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
\right)+is\left(
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
\frac{b_{c,\mathbf k}-ib_{s,\mathbf k}}{\sqrt2},
\qquad
a_{-\mathbf k}
=
\frac{b_{c,\mathbf k}+ib_{s,\mathbf k}}{\sqrt2}
$$

です。この変換を Hamiltonian に代入すると、

$$
H_{\eta,\mathbf k}
=
\sum_{A=c,s}
\left[
k\left(b_{A,\mathbf k}^\dagger b_{A,\mathbf k}+\frac12\right)
+
\frac{is}{2}
\left(b_{A,\mathbf k}^{\dagger2}-b_{A,\mathbf k}^2\right)
\right]
$$

となります。

進行波基底で二つのモードを結びつけていた項は、定在波基底ではそれぞれのモードの squeezing 項に分かれます。

実際、Heisenberg 方程式は

$$
\frac{db_{A,\mathbf k}(\eta)}{d\eta}
=
-ik\,b_{A,\mathbf k}(\eta)
+s(\eta)b_{A,\mathbf k}^\dagger(\eta)
$$

となり、

$$
b_{A,\mathbf k}(\eta)
=
\alpha_k(\eta)b_{A,\mathbf k}^{\mathrm{in}}
+
\beta_k(\eta)b_{A,\mathbf k}^{\mathrm{in}\dagger}
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
b_{c,\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=
b_{s,\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
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

§3 で導入した二つの実定在波モード $A=c,s$ のそれぞれについて、無次元の正準 quadrature を

$$
Q_{A,\mathbf k}=\sqrt{k}\,a\phi_{A,\mathbf k},
\qquad
P_{A,\mathbf k}=\frac{a\phi_{A,\mathbf k}'}{\sqrt{k}}
$$

と定義します。これらは $[Q_{A,\mathbf k},P_{A,\mathbf k}]=i$ を満たし、§4 の消滅演算子とは

$$
b_{A,\mathbf k}=\frac{Q_{A,\mathbf k}+iP_{A,\mathbf k}}{\sqrt2}
$$

で結ばれます。§4 の $s=z'/z$ を $s=\mathcal H$ に置き換えると、

$$
P_{A,\mathbf k}
=\frac{Q_{A,\mathbf k}'-\mathcal H Q_{A,\mathbf k}}{k},
$$

$$
Q_{A,\mathbf k}''
+
\left(
k^2-\frac2{\eta^2}
\right)Q_{A,\mathbf k}=0
$$

となります。以下では、この $Q,P$ を使って位相空間の議論を進めます。

以下では

$$
x=-k\eta=\frac{k}{aH},
\qquad
N=\ln\frac{a}{a_{\mathrm{cross}}}=-\ln x
$$

を用います。$x\gg1$ は subhorizon、$x=1$ は Hubble crossing、$x\ll1$ は superhorizon に対応します。

§4 で得た Heisenberg 方程式

$$
b_{A,\mathbf k}'(\eta)
=
-ik\,b_{A,\mathbf k}(\eta)
+s(\eta)b_{A,\mathbf k}^\dagger(\eta)
$$

において、今は

$$
s(\eta)=\mathcal H=\frac{k}{x}
$$

です。

Bogoliubov 変換

$$
b_{A,\mathbf k}(\eta)
=
\alpha_k(\eta)b_{A,\mathbf k}^{\mathrm{in}}
+
\beta_k(\eta)b_{A,\mathbf k}^{\mathrm{in}\dagger}
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

波数対 $(\mathbf k,-\mathbf k)$ の実定在波モード $A=c,s$ について、quadrature $Q_{A,\mathbf k}$ を

$$
Q_{A,\mathbf k}(\eta)
=
\sqrt{k}\left[
f_k(\eta)b_{A,\mathbf k}^{\mathrm{in}}
+
f_k^*(\eta)b_{A,\mathbf k}^{\mathrm{in}\dagger}
\right]
$$

と展開すると、Bogoliubov 変換との比較から、

$$
f_k(\eta)
=
\frac{\alpha_k+\beta_k^*}{\sqrt{2k}}
=
\frac{1+i/x}{\sqrt{2k}}e^{ix}
$$

を得ます。$f_k$ は再スケールした場 $a\phi_{A,\mathbf k}$ のモード関数として規格化しています。無次元の $Q_{A,\mathbf k}$ の展開係数は $\sqrt{k}f_k$ です。

元の場 $\phi_{A,\mathbf k}=Q_{A,\mathbf k}/(\sqrt{k}a)$ のモード関数は

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

元の場の揺らぎが一定値に近づく一方、$Q_{A,\mathbf k},P_{A,\mathbf k}$ で見た量子状態は強く squeezing され続けます。保存モードの優勢化と squeezing の発達は、同じ量子時間発展を異なる側面から捉えたものです。

次の図では、$f_k/a$ と $f_k$ の実部・虚部・絶対値を、それぞれ $H/\sqrt{2k^3}$ と $1/\sqrt{2k}$ を単位として示します。「superhorizon の保存・減衰成分」では、$|\operatorname{Im}(f_k/a)|$ と $|\operatorname{Re}(f_k/a)|$ がそれぞれ $1$ と $x^3/3$ に近づく様子を確認できます。実部と虚部の対応はモード関数の位相規約によって変わりますが、保存モードの優勢化は規約によらず成り立ちます。

<iframe src="app/supporting.html?lang=ja&amp;view=background" title="背景項と厳密de Sitterモード関数" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

## 6. Wigner 関数の時間発展：Bogoliubov 変換と Hamilton flow

ここまで求めた時間発展を、一つの実定在波モードの位相空間上で見てみます。以下では波数対と $A=c,s$ の一方を固定し、$Q=Q_{A,\mathbf k}$、$P=P_{A,\mathbf k}$、$\phi=\phi_{A,\mathbf k}$ と略記します。

§5 で定義した無次元の quadrature は

$$
Q=\sqrt{k}\,a\phi,
$$

$$
P=\frac{a\phi'}{\sqrt{k}}
$$

であり、

$$
[\hat Q,\hat P]=i
$$

を満たす正準変数です。

時間発展の計算には Heisenberg 描像の演算子を用いますが、図は Schrödinger 描像に対応させ、**固定した $Q,P$ 軸の上で量子状態の Wigner 関数が変形する様子**を示しています。座標軸の向き、縮尺、表示範囲はすべてのフレームで固定しています。

### 共分散行列と Wigner 楕円

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

§2 の定義から、この平均値ゼロの Gaussian 状態の Wigner 関数は

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

を満たす等高線を描いています。この等高線の時間発展を、[下のアニメーション](#main-animation)の3番目のパネルで確認できます。

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

### Hamilton flow：回転と squeezing

この Wigner 分布の変形を生み出す Hamilton flow を調べます。

§4 の Hamiltonian を固定した quadrature で書き、時間変数を共形時間 $\eta$ から $N$ に変えると、

$$
K_N
=
\frac{x}{2}(Q^2+P^2)
+
\frac12(QP+PQ)
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

<span id="main-animation"></span>

### Wigner 楕円と Hamilton flow をアニメーションで見る

アニメーションでは $x=12$ から $x=0.2$ までを、$N=-\ln x$ を時間として追えます。最初の二つのパネルはそれぞれ回転成分と squeezing 成分のベクトル場、3番目は合成した流れと Wigner 等高線です。

<iframe src="app/index.html?lang=ja" title="インフレーションの squeezing：回転・スクイーズ・合成Hamilton流" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

アニメーションでは、次の変化を追ってみてください。

1. **Subhorizon（$x\gg1$）：** 回転が優勢で、Wigner 分布はほぼ円形です。表示開始時にわずかに楕円なのは、$x=\infty$ ではなく $x=12$ から描いているためです。
2. **Hubble crossing（$x=1$）：** 回転と squeezing の寄与が同程度になり、楕円の変形が明瞭になります。
3. **Superhorizon（$x\ll1$）：** 長軸が伸び、短軸が細くなります。$Q$ と $P$ の相関が強まり、分布は成長解に対応する方向へ集中していきます。

ベクトル場の矢印は見やすさのため、長さに $1/\sqrt{1+x^2}$ と共通の描画倍率を掛けています。Wigner 関数自体は元の Hamilton flow で計算しています。

方向の表示を切り替えると、瞬間的な流れの固有方向、楕円の主軸、成長・減衰解の方向を比較できます。有限の $x$ ではそれぞれ異なる方向を向き、時間発展とともに関係が変わっていきます。

### squeezing の強さと楕円の向き

上のアニメーションで見た楕円の伸びと回転を、squeezing parameter と長軸の角度で定量的に調べます。

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

下の図はアニメーションより遅い時刻まで含め、Hubble crossing 後4 e-foldまでの変化を示しています。

<iframe src="app/supporting.html?lang=ja&amp;view=squeezing" title="e-fold時間に対する squeezing の大きさと長軸の角度" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

### 場の速度の揺らぎと凍結

この楕円の変形は、元の場がほぼ一定の振幅を保つ「凍結」とどう結びつくのでしょうか。まず、図の $P$ は元の場の時間微分そのものではなく、$P=a\phi'/\sqrt{k}$ です。共分散行列から

$$
\operatorname{Var}(P)=\frac12
$$

は一定です。短軸が $P$ 軸へ近づいても、$P$ 方向に射影した分布の幅がゼロになるわけではありません。小さくなるのは、$Q$ を与えたときに残る幅です。正の Gaussian Wigner 密度について、

$$
\mathbb E[P\mid Q]=-\frac{x}{1+x^2}Q,
\qquad
\operatorname{Var}(P\mid Q)=\frac{x^2}{2(1+x^2)}
$$

となり、superhorizon では $P\simeq-xQ$ の近くに分布が集中します。

一方、元の場の速度の揺らぎは、モード関数を微分すれば直接求められます。§5 の厳密解と $dx/d\eta=-k$ から、

$$
\left(\frac{f_k}{a}\right)'
=-\frac{i}{a}\sqrt{\frac{k}{2}}\,e^{ix}
$$

です。Bunch–Davies 真空では $\langle\phi\rangle=\langle\phi'\rangle=0$ なので、速度の二乗期待値はその分散に等しく、

$$
\left\langle(\phi')^2\right\rangle
=\left|\left(\frac{f_k}{a}\right)'\right|^2
=\frac{k}{2a^2}
$$

となります。宇宙時刻での速度 $\dot\phi=\phi'/a$ については、

$$
\left\langle\dot\phi^{\,2}\right\rangle
=\frac{k}{2a^4}
\longrightarrow0
$$

です。これに対して場の振幅は、§5 で求めたように

$$
\langle\phi^2\rangle
=\frac{H^2}{2k^3}(1+x^2)
\longrightarrow\frac{H^2}{2k^3}
$$

という有限の分散を保ちます。Hubble 時間あたりの変化の小ささは、無次元の比

$$
\frac{\sqrt{\langle\dot\phi^{\,2}\rangle}}
{H\sqrt{\langle\phi^2\rangle}}
=\frac{x^2}{\sqrt{1+x^2}}
\simeq x^2
\qquad(x\ll1)
$$

で表せます。例えば $x=0.1$ では約 $0.01$ です。**振幅には有限の幅を持つ重ね合わせが残りながら、元の場の時間変化は小さくなる**。これが、このモデルでの凍結の具体的な意味です。$Q=\sqrt{k}a\phi$ の振幅の幅はその間も広がります。

ここで $\phi$ と $\dot\phi$ は正準共役な組ではなく、$[\hat\phi,\hat{\dot\phi}]=i/a^3$ です。速度の幅が小さくなることは、固定した正準 quadrature の $[\hat Q,\hat P]=i$ や $\det\Sigma=1/4$ と両立します。

減衰解の寄与が抑えられると、その後の線形発展に必要な独立なランダム入力は実効的に一つの振幅に絞られます。この構造が、次に述べる古典的な統計記述と、再突入後の音響振動の時間位相を結びます。

## 7. 摂動が古典的に見える理由

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

したがって、quadrature $Q=\sqrt{k}a\phi$ の分散が大きく伸びることと、元の場 $\phi$ の分散が有限値へ凍結することは両立します。

曲率摂動では $a$ の代わりに $z$ が入り、その slow-roll 発展が振幅とスペクトルの傾きを決めます。

では、なぜこの量子状態を後の宇宙では古典的なランダム場として扱えるのでしょうか。

まず、自由場の Bunch–Davies 真空は時間発展の間も Gaussian 状態であり、Wigner 関数は正です。この正の分布を確率密度とみなすと、同時刻の対称順序（Weyl 順序）相関関数を古典的な Gaussian 集団で再現できます。これは初期真空にも成り立つ性質です。

Squeezing が発達すると、さらに強い構造が現れます。成長モードの寄与が圧倒的に大きくなり、場と運動量の間に相関が生まれます。Wigner 分布は細い楕円となり、その後の線形発展に必要な初期条件は、実効的に一つのランダムな振幅で指定できます。こうして、観測される揺らぎの統計を古典的な確率場として計算できるようになります。

ただし、量子状態そのものが古典状態へ変わったわけではありません。交換関係

$$
[\hat Q,\hat P]=i
$$

は残り、波動関数が自発的に収縮するわけでも、純粋状態が時間発展だけで混合状態へ変わるわけでもありません。

環境との相互作用によるデコヒーレンスは、squeezing とは別の物理過程です。

この「古典的な統計で再現できること」と「量子状態そのものが古典状態になること」の違いは、原始揺らぎの量子的起源を議論するときに重要です。このことは [Martin & Vennin](https://arxiv.org/abs/1510.04038) が詳しく議論しています。

<iframe src="app/supporting.html?lang=ja&amp;view=samples" title="シンプレクティック発展の前後におけるWignerサンプル" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

時刻スライダーを初期から最後まで動かしてください。

時間発展によってランダムさそのものが消えるわけではありません。長軸方向に許される振幅の範囲は大きくなる一方で、オレンジ色の条件付き平均線から $P$ 方向へ外れる幅が小さくなります。

左右のパネルでは同じ座標範囲を使っています。描かれている Wigner 等高線が囲む確率重みは約39%なので、サンプル点の多くが楕円の外側に現れることも自然です。

## 8. 時間位相のコヒーレンスと CMB の音響ピーク

### 成長モードの優勢化から音響振動の初期条件へ

§5–7 では、superhorizon で減衰解の寄与が小さくなると、その後の線形発展に必要なランダム入力が、各実定在波モードにつき実効的に一つの振幅に絞られることを見ました。一般には場の振幅と速度の二つが初期条件として必要ですが、成長解だけが残ると、その比は解の時間依存性によって決まります。§6 の細い Wigner 楕円は、この強い相関を位相空間で見たものです。速度が常にゼロになるという意味ではありません。

この構造を CMB へつなぐには、インフレーション後の摂動についても仮定が必要です。ここでは、通常の単一場・アトラクター型インフレーションから、独立なエントロピー摂動を持たない断熱的な成長モードへつながり、その後も線形に発展する場合を考えます。§5–6 のテストスカラー場の凍結は保存モードの優勢化を示す模型であり、その場をそのまま光子の温度揺らぎと同一視するわけではありません。

この場合、保存された原始曲率摂動を $\zeta_{A,\mathbf k}^{\mathrm{prim}}$ とすると、光子・バリオン流体の各実定在波成分 $A=c,s$ の音響変数は

$$
X_{A,\mathbf k}(\eta)\simeq T_k(\eta)\zeta_{A,\mathbf k}^{\mathrm{prim}},
\qquad
X_{A,\mathbf k}'(\eta)\simeq T_k'(\eta)\zeta_{A,\mathbf k}^{\mathrm{prim}}
$$

と表せます。$T_k$ は、単位の原始曲率摂動を初期条件として、その後の宇宙での摂動方程式を解いた伝達関数です。同じ背景宇宙と同じ波数 $k$ を指定すれば、その時間依存性は決まります。実現ごとのランダムさは、両方の式に共通して掛かる $\zeta_{A,\mathbf k}^{\mathrm{prim}}$ に含まれます。

したがって、ある初期時刻で変位を選んだ後に、速度をもう一つの独立な乱数として選ぶことはしません。原始振幅を2倍にすれば変位も速度も2倍になり、符号を反転すれば両方が反転します。このため同じ $k$ の実現例は零点と極値の時刻を共有し、振幅を二乗したパワーでは符号の違いも消えます。これが時間位相のコヒーレンスにつながります。

### 空間位相と時間位相

このコヒーレンスは、空間的な Fourier 位相を揃えることではありません。統計的に一様・等方的な Gaussian 場では、空間的な cos 型と sin 型の成分 $\zeta_{c,\mathbf k}$、$\zeta_{s,\mathbf k}$ は同じ分散を持ちます。

$$
\zeta_{\mathbf k}=\frac{\zeta_{c,\mathbf k}-i\zeta_{s,\mathbf k}}{\sqrt2}
$$

の $\arg\zeta_{\mathbf k}$ はランダムな空間的 Fourier 位相であり、空間の原点を移せば値が変わります。一方、CMB の音響ピークに関係するのは、各波数 $k$ の摂動が圧縮と希薄化を繰り返すときの時間位相です。空間位相がランダムなままでも、変位と速度が同じ成長モードから決まれば、この時間位相には一定の関係が残ります。

### 単純な振動子で sine 成分が小さくなる理由

この関係を、音速 $c_s$ が一定で、外力と減衰のない振動子で具体的に見ます。以下では一つの実定在波成分を選び、添字 $c,s$ を省略します。$X_k$ は、静的な重力による平衡点から測った温度・密度の変位に対応する模型変数です。

$$
X_k''+(kc_s)^2X_k=0
$$

初期時刻を $\eta_i$ とし、そこから測った音響距離を

$$
r_s(\eta)=\int_{\eta_i}^{\eta}c_s\,d\eta'
=c_s(\eta-\eta_i)
$$

とすると、一般解は

$$
X_k(\eta)=A_k\cos(kr_s)+B_k\sin(kr_s)
$$

です。この cos と sin は時間方向の二つの独立解であり、§3 の空間的な cos・sin 基底とは異なります。初期時刻では $r_s(\eta_i)=0$ なので、解とその微分から

$$
A_k=X_k(\eta_i),
\qquad
B_k=\frac{X_k'(\eta_i)}{kc_s}
$$

が分かります。つまり、cos 成分は初期変位、sin 成分は初速度を表します。

通常の断熱的な成長モードでは、音響振動が進むより十分早い superhorizon の時期に、温度・密度の変位がすでに存在します。一方、その変位はほぼ一定で、流体の速度は空間勾配で抑えられています。これを、重力ポテンシャルの時間変化などを省いた上の模型に対応させると、初期条件は「ランダムな変位から、ほぼ静止して振動を始める」形になります。式では

$$
X_k(\eta_i)=C_k\zeta_k^{\mathrm{prim}},
\qquad
X_k'(\eta_i)\simeq0
$$

と近似します。ここで $C_k$ は原始曲率摂動から初期変位への決まった変換係数で、$\zeta_k^{\mathrm{prim}}$ は選んだ実定在波成分の振幅です。有限の初速度を残す場合には、その大きさを $kc_s$ と変位の積に比べて十分小さいと仮定しています。上の初期条件を係数の式へ代入すると、

$$
A_k=C_k\zeta_k^{\mathrm{prim}},
\qquad B_k\simeq0
$$

となります。したがって、この近似では

$$
X_k(\eta)\simeq C_k\zeta_k^{\mathrm{prim}}\cos(kr_s),
\qquad
T_k(\eta)\simeq C_k\cos(kr_s)
$$

です。振幅の大きさや符号が実現ごとに異なっても、同じ位相から振動を始めるため、零点が揃います。[Hu & White](https://arxiv.org/abs/astro-ph/9602019) は、断熱的な初期条件と cosine 型の音響振動の関係を、重力による駆動も含めて議論しています。

ここで $B_k\simeq0$ は、squeezing だけから直ちに従う式ではありません。成長モードの優勢化が与えるのは、変位と速度が一つのランダム振幅で決まるという関係です。そこに、通常の断熱的な初期条件を、上の振動子のほぼゼロの初速度で近似することで、cosine 型の解が得られます。horizon re-entry の瞬間に速度をゼロに設定しているわけでもありません。

より一般に、成長モードをこの振動子の二つの解で表した結果が

$$
A_k=a_k\zeta_k^{\mathrm{prim}},
\qquad
B_k=b_k\zeta_k^{\mathrm{prim}}
$$

であれば、$a_k,b_k$ は背景宇宙と初期条件から決まる係数です。$b_k\neq0$ でも、比 $b_k/a_k$ が実現ごとに変わらなければ時間位相はコヒーレントです。同じ $k$ の全実現例に共通の位相原点を選ぶことはできますが、異なる $k$ の位相を一つの時間原点の変更で一律に消せるとは限りません。各波数の振幅はランダムでも、その後の時間発展を決める伝達関数は、同じ波数の実現例で共通になります。

### 共通の時間位相がパワーに残すピーク

その効果を、初期振幅の総分散を $\sigma^2$ に揃えた二つの集団で比較します。図では上の単純な cosine 型の近似を使い、コヒーレントな集団を

$$
\langle|A_k|^2\rangle=\sigma^2,
\qquad B_k=0
$$

とします。このとき

$$
\langle|X_k|^2\rangle=\sigma^2\cos^2(kr_s)
$$

となり、ランダムな振幅を平均しても、パワーの振動構造が残ります。

これに対して cos 型と sin 型が独立に励起され、

$$
\langle|A_k|^2\rangle=\langle|B_k|^2\rangle
=\frac{\sigma^2}{2},
\qquad
\langle A_kB_k^*\rangle=0
$$

なら、

$$
\langle|X_k|^2\rangle=\frac{\sigma^2}{2}
$$

となります。二つの時間 quadrature が無相関かつ同じ分散で励起されると、平均パワーから振動が消えます。この比較で重要なのは、振幅がランダムかどうかではなく、初期変位と初速度を独立に選ぶか、一つの成長モードで結びつけるかという違いです。

実際の CMB では、重力ポテンシャルによる駆動、バリオンの慣性、ニュートリノ、Silk damping、再結合、三次元摂動から天球への射影などが伝達関数に組み込まれます。そのため伝達関数は単純な cosine ではなく、位相のずれも生じます。それでも、同じ波数の実現例が共通の伝達関数に従う構造は保たれ、角度パワースペクトル $C_\ell$ の一連の音響ピークにつながります。

<iframe src="app/supporting.html?lang=ja&amp;view=acoustic" title="ランダムな音響振動の実現例とコヒーレント・非コヒーレントな平均パワー" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

コヒーレントな集団では、振幅も符号も異なる実現例が同じ時刻にゼロを通過します。時間位相がランダムな集団では、零点がばらつきます。下段では、有限個の実現例から求めたパワーと集団平均を比較できます。音響地平線 $r_s$ を固定して波数 $k$ を変えると、時間方向の振動に対応する構造が波数空間のピーク列として現れます。

CMB の音響ピークは、原始揺らぎがコヒーレントな成長モードに支配されていたことを強く示しています。その背景にある量子 squeezing を直接検出するには、古典的な相関関数を超えた情報が必要です。

## 補足と参考文献

この記事の図とアニメーションは、de Sitter 背景上の自由な線形 Gaussian 場を扱っています。メインのアニメーションは、短軸の幅まで見えるよう $x=0.2$ で表示を止めています。さらに膨張が進むと squeezing は強まり、位相空間の面積は保たれたまま楕円が細くなっていきます。

曲率摂動の保存については、通常のアトラクター型インフレーションを想定しました。非アトラクター型では superhorizon でも $\zeta$ が時間発展する場合があり、その振る舞いは対応する $z(\eta)$ から求めます。デコヒーレンスや非 Gaussian 性などは、自由場の squeezing を踏まえた次の問題です。

- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030)：正準変数、成長・減衰解と semiclassicality の関係。
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038)：古典的な相関関数と量子状態の違い。
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019)：原始初期条件と CMB 音響ピークの位相構造。
