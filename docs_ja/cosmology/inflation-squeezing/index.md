---
title: インフレーションの量子揺らぎと squeezing
---

# インフレーションの量子揺らぎと squeezing

<span class="center-material-tables"></span>

CMB の温度異方性や銀河分布の大規模構造は、宇宙初期の小さな原始揺らぎが成長したものです。インフレーション理論は、この原始揺らぎの起源を、加速膨張する時空における量子場の揺らぎに求めます。

この記事で見ていくのは、**場の二点相関**です。量子状態では一般に、場の平均値はゼロでも異なる場所の場の値は相関しています。宇宙膨張のもとでこの相関がどのように決まり、後の宇宙にどのような形で残るのかを、実空間の量子場から出発して追っていきます。

その途中で squeezing が現れます。一様な背景の上では、場を Fourier モードに分けると、反対向きの波数 $\mathbf k$ と $-\mathbf k$ が対になって時間発展します。この対を進行波で表すと **two-mode squeezing** が、同じ二つの自由度を余弦・正弦の定在波で表すと二つの独立な **single-mode squeezing** が見えます。両者の関係を、Hamiltonian の対称性、量子状態の数表示、位相空間の三つの面から確かめます。

<figure style="margin-inline: auto; text-align: center;">
  <img src="app/teaser.svg" alt="一つの定在波モードの量子状態を、同じ正準座標軸の上に三つの時刻について描いたWigner等高線" width="720" height="250" style="display: block; max-width: 100%; height: auto; margin-inline: auto;">
</figure>

図は、一つの定在波モードの量子状態を、三つの時刻について同じ位相空間に描いたものです（§8 の厳密解）。横軸は場の振幅、縦軸は運動量から作った無次元の座標です。Subhorizon ではほぼ円形だった分布が、superhorizon 領域に進むにつれ面積を保ったまま細長い楕円へと変形していきます。

記事は次の順に進みます。[メインのアニメーション](#main-animation)は §8 にあります。

1. 実空間での量子論を記述し、正準変数を選ぶ（§1–2）
2. Fourier 展開で波数対に分け、two-mode squeezing と single-mode squeezing の関係を導く（§3–6）
3. squeezing を位相空間の楕円として表し、空間相関との関係を見る（§7）
4. 厳密に解ける模型で、squeezing の発達を計算する（§8）
5. 場の凍結から、原始揺らぎの古典的な記述と音響ピークへ進み、最後に線形理論の先を展望する（§9–10）

## 1. 実空間の量子場と同時刻相関

### 背景と量子化する自由度

標準的な運動項を持つ一つのスカラー場、すなわちインフラトンが、一般相対論に従いインフレーションを駆動する場合を考えます。背景は空間的に平坦な一様等方宇宙

$$
ds_0^2=-dt^2+a^2(t)\,d\mathbf x^2=a^2(\eta)\left(-d\eta^2+d\mathbf x^2\right)\tag{1}\label{eq:inflation-1}
$$

です。$\mathbf x$ は共動座標、$a$ はスケール因子、$\eta$ は共形時間です。$H=\dot a/a$、$\mathcal H=a'/a=aH$ とし、ドットは cosmic time $t$、プライムは $\eta$ による微分を表します。単位は $c=\hbar=1$ です。

スケール因子 $a$ と背景のインフラトン $\phi_0$ は古典的な背景方程式に従う時間の関数として与え、その上の**摂動**を量子化します。

単一場の線形摂動では、重力の拘束条件を解くと、伝播するスカラー自由度が一つ残ります。これを共動曲率摂動 $\hat\zeta$ で表します。インフラトンが一様になる時間切片をとり、空間計量を線形近似の範囲で

$$
\hat g_{ij}=a^2(1-2\hat\zeta)\,\delta_{ij}\tag{2}\label{eq:inflation-2}
$$

と書く符号規約を採用します。$g_{ij}=a^2e^{2\zeta}\delta_{ij}$ と定義する文献の $\zeta$ とは符号が逆ですが、二点関数は共通です。空間的に平坦な時間切片でのインフラトン揺らぎ $\delta\hat\phi_{\mathrm{flat}}$ を使えば、同じ自由度は線形摂動のゲージ変換から

$$
\hat\zeta=\frac{H}{\dot\phi_0}\,\delta\hat\phi_{\mathrm{flat}}\qquad(\dot\phi_0\neq0)\tag{3}\label{eq:inflation-3}
$$

と表せます。

拘束条件を解いた後の二次作用は、

$$
S_2[\zeta]=\frac12\int d\eta\,d^3x\;z^2\left[(\zeta')^2-(\nabla\zeta)^2\right],\qquad z=\frac{a\dot\phi_0}{H}\tag{4}\label{eq:inflation-4}
$$

です。$z$ は背景だけで決まる時間の関数で、宇宙膨張と背景インフラトンの運動の両方を含んでいます。導出は [Baumann の講義](https://arxiv.org/abs/0907.5424)にあります。§9 までは、この二次作用で決まる線形の量子論を扱います。三次以上の相互作用は §10 で取り上げます。

### 正準量子化（Heisenberg 描像）

共役運動量密度を $\hat\Pi_\zeta=z^2\hat\zeta'$ とすると、同時刻の正準交換関係は

$$
[\hat\zeta(\eta,\mathbf x),\hat\Pi_\zeta(\eta,\mathbf y)]=i\,\delta^{(3)}(\mathbf x-\mathbf y)\tag{5}\label{eq:inflation-5}
$$

で、場どうし、運動量どうしは可換です。共形時間の発展を生成する Hamiltonian は

$$
\hat H_\zeta(\eta)=\frac12\int d^3x\left[\frac{\hat\Pi_\zeta^{\,2}}{z^2}+z^2(\nabla\hat\zeta)^2\right]\tag{6}\label{eq:inflation-6}
$$

です。時間依存性は背景の係数 $z(\eta)$ から入ります。Heisenberg 方程式 $\hat O'=i[\hat H_\zeta,\hat O]$ から、場の演算子は局所的な運動方程式

$$
\bigl(z^2\hat\zeta'\bigr)'-z^2\nabla^2\hat\zeta=0\tag{7}\label{eq:inflation-7}
$$

に従います。揺らぎの大きさは、この演算子の積の期待値をとる**量子状態**を指定して決まります。

### 波動汎関数（Schrödinger 描像）

Schrödinger 描像では、演算子 $\hat\zeta_{\mathrm S}(\mathbf x)$、$\hat\Pi_{\zeta,\mathrm S}(\mathbf x)$ を固定し、状態が $i\partial_\eta|\Psi(\eta)\rangle=\hat H_\zeta(\eta)|\Psi(\eta)\rangle$ に従って発展します。$\hat\zeta_{\mathrm S}(\mathbf x)$ の同時固有状態 $|\zeta\rangle$ で表した**波動汎関数** $\Psi_\eta[\zeta]=\langle\zeta|\Psi(\eta)\rangle$ は、空間全体の場の配位 $\zeta(\mathbf x)$ のそれぞれに振幅を与えます。$\hat\Pi_{\zeta,\mathrm S}$ を $-i\,\delta/\delta\zeta(\mathbf x)$ として表すと

$$
i\partial_\eta\Psi_\eta[\zeta]=\frac12\int d^3x\left[-\frac1{z^2}\frac{\delta^2}{\delta\zeta(\mathbf x)^2}+z^2(\nabla\zeta)^2\right]\Psi_\eta[\zeta]\tag{8}\label{eq:inflation-8}
$$

です。これは連続無限個の自由度の形式的な式で、厳密には有限体積や短距離の正則化を伴います。

Hamiltonian が二次式なので、平均ゼロの Gaussian 状態は Gaussian のまま発展します。そのような状態は、複素数値の核 $\mathcal K_\eta$ を用いて

$$
\Psi_\eta[\zeta]=\mathcal N_\eta\exp\left[-\frac12\int d^3x\,d^3y\;\zeta(\mathbf x)\,\mathcal K_\eta(\mathbf x,\mathbf y)\,\zeta(\mathbf y)\right]\tag{9}\label{eq:inflation-9}
$$

と書けます。核の実部が配位の幅を、虚部が波動汎関数の位相、つまり場と運動量の相関を決めます。背景と状態が一様・等方なら、核は距離 $|\mathbf x-\mathbf y|$ だけの関数です。この**並進不変な二次形式**が、§3 以降で squeezing を理解する出発点になります。

### 目標：同時刻の空間相関

この記事の目標は、時刻 $\eta$ における場の二点相関

$$
G_\zeta(\eta;\mathbf x,\mathbf y)=\langle\Psi(\eta)|\hat\zeta_{\mathrm S}(\mathbf x)\hat\zeta_{\mathrm S}(\mathbf y)|\Psi(\eta)\rangle=\langle\Psi_0|\hat\zeta_{\mathrm H}(\eta,\mathbf x)\hat\zeta_{\mathrm H}(\eta,\mathbf y)|\Psi_0\rangle\tag{10}\label{eq:inflation-10}
$$

を求めることです。中辺が Schrödinger 描像、右辺が Heisenberg 描像の表し方です。$U(\eta,\eta_0)$ を $\hat H_\zeta$ が生成する時間発展演算子として、$|\Psi(\eta)\rangle=U|\Psi_0\rangle$、$\hat\zeta_{\mathrm H}=U^\dagger\hat\zeta_{\mathrm S}U$ です。平均ゼロの状態なので、これがそのまま連結二点関数です。

波動汎関数で言えば、$G_\zeta$ は $|\Psi_\eta[\zeta]|^2$ を配位の確率密度とみなしたときの $\zeta(\mathbf x)\zeta(\mathbf y)$ の平均で、核 $\mathcal K_\eta$ の実部から決まります。**場の時間発展と初期状態の両方が、空間相関を決めています。**

### 時間発展描像・正準変数・モード基底

計算の途中では、互いに独立な三種類の選択をします。

<div class="inflation-choices" markdown="1">

| 選択 | 決めること | この記事での使い方 |
| --- | --- | --- |
| 時間発展描像 | 時間発展を状態に担わせるか（Schrödinger）、演算子に担わせるか（Heisenberg） | 演算子の発展と期待値は Heisenberg、状態の形と Wigner 分布は Schrödinger |
| 正準変数 | 状態を表す配位変数と共役運動量 | $\zeta$ から、正準規格化した $v=z\zeta$ へ移る（§2） |
| モード基底 | 場の自由度の分け方 | 一つの波数対を進行波で分けるか、定在波で分けるか（§3） |

</div>

期待値は時間発展描像によらず同じです。正準変数とモード基底は、squeezing の楕円の形やもつれの有無といった状態の**見え方**を左右しますが、$G_\zeta$ のような物理量は共通です。以下では、各節の見出しや冒頭でどの選択をしているかを示します。

## 2. 正準変数 $v=z\zeta$

### Mukhanov–Sasaki 変数

モードの計算には、運動項の係数を 1 にした **Mukhanov–Sasaki 変数**

$$
v=z\zeta=a\,\delta\phi_{\mathrm{flat}}\tag{11}\label{eq:inflation-11}
$$

が便利です。$\zeta$、$\delta\phi_{\mathrm{flat}}$、$v$ は、同じ一つの自由度を異なる背景係数で規格化したものです。

$s(\eta)=z'/z$ と置いて作用を書き直すと、境界項を落とさずに

$$
S_2[v]=\frac12\int d\eta\,d^3x\left[(v'-sv)^2-(\nabla v)^2\right]\tag{12}\label{eq:inflation-12}
$$

となります。共役運動量と Hamiltonian は

$$
\pi=v'-sv=z\zeta'=\frac{\Pi_\zeta}{z},\tag{13}\label{eq:inflation-13}
$$

$$
\hat H_v(\eta)=\frac12\int d^3x\left[\hat\pi^2+(\nabla\hat v)^2+s\,(\hat v\hat\pi+\hat\pi\hat v)\right]\tag{14}\label{eq:inflation-14}
$$

で、交差項は Hermite になるよう対称化しました。$[\hat v(\eta,\mathbf x),\hat\pi(\eta,\mathbf y)]=i\,\delta^{(3)}(\mathbf x-\mathbf y)$ が成り立ち、Heisenberg 方程式から運動量を消去すると Mukhanov–Sasaki 方程式

$$
\hat v''-\nabla^2\hat v-\frac{z''}{z}\hat v=0\tag{15}\label{eq:inflation-15}
$$

が得られます。

### 時間に依存する変数変換と描像

$\hat v=z\hat\zeta$ は係数が時間に依存する変数変換で、描像の変更とは独立の操作です。§1 の Schrödinger 描像のままで $v$ に対応する演算子を作ると、$z(\eta)\hat\zeta_{\mathrm S}(\mathbf x)$ という陽に時間に依存する演算子になります。Heisenberg 演算子 $\hat O_{\mathrm H}=U^\dagger\hat O_{\mathrm S}(\eta)U$ の時間微分は

$$
\frac{d\hat O_{\mathrm H}}{d\eta}=i[\hat H_{\mathrm H},\hat O_{\mathrm H}]+U^\dagger\left(\partial_\eta\hat O_{\mathrm S}\right)U\tag{16}\label{eq:inflation-16}
$$

なので、$\hat v'=z'\hat\zeta+z\hat\zeta'$ の $z'$ の項は陽な時間依存性から来ています。

$v$ を時間に依存しない配置変数とする Schrödinger 描像をとるには、量子論を $v$ で記述し直します。その Hamiltonian が上の $\hat H_v$ で、時間に依存する正準変換の効果は交差項 $s(\hat v\hat\pi+\hat\pi\hat v)$ に現れています。状態も同時に置き換わり、波動汎関数は $\Psi^{(v)}_\eta[v]\propto\Psi_\eta[v/z(\eta)]$ となります。比例係数は規格化を保つように選びます。

**以下で「固定した軸」や「Schrödinger 描像の状態」と言うときは、この $v$ 表現を指します。** Wigner 図は、固定した $v,\pi$ から作った座標軸の上に、$\hat H_v$ で発展する状態を描いたものです。

運動量の選び方にも自由度があります。作用に時間の全微分を加えると、共役運動量を $\tilde\pi=v'=\pi+sv$ とする形にもなります。この場合運動方程式は同じで、位相空間の図はせん断変形の分だけ変わります。この記事は一貫して $\pi=v'-sv$ を使います。§8 の例では、この $\pi$ が元の場の速度に比例するので、凍結の意味が読み取りやすくなります。

## 3. 波数対と二つのモード基底（Schrödinger 描像）

この節では、§2 の $v$ 表現の Schrödinger 演算子 $\hat v,\hat\pi$ から、時間に依存しない演算子の基底を作ります。添字 $\mathrm S$ は省略します。

### Fourier 展開と箱による正則化

一つのモードの量子状態を扱うため、周期境界条件を持つ共動体積 $V$ の箱を正則化として導入します。最後に $V\to\infty$ とし、$V$ によらない量だけを使います。

$$
\hat v(\mathbf x)=\frac1{\sqrt V}\sum_{\mathbf k}\hat v_{\mathbf k}\,e^{i\mathbf k\cdot\mathbf x},\qquad\hat v_{\mathbf k}=\frac1{\sqrt V}\int_V d^3x\,e^{-i\mathbf k\cdot\mathbf x}\,\hat v(\mathbf x)\tag{17}\label{eq:inflation-17}
$$

運動量 $\hat\pi$ も同様に展開します。$\hat v_{\mathbf k}$ は場全体から取り出した一つの成分で、Fourier 展開は量子場全体の基底の取り替えです。一様な成分 $\mathbf k=\mathbf 0$ は背景の再定義に吸収できるので除き、$k=|\mathbf k|>0$ を考えます。場の Hermite 性と正準交換関係から

$$
\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger,\qquad\hat\pi_{-\mathbf k}=\hat\pi_{\mathbf k}^\dagger,\qquad[\hat v_{\mathbf k},\hat\pi_{\mathbf k'}]=i\,\delta_{\mathbf k,-\mathbf k'}\tag{18}\label{eq:inflation-18}
$$

となります。背景の係数は位置によらず、平面波は $-\nabla^2$ の固有関数なので、Hamiltonian は

$$
\hat H_v=\sum_{\mathbf k}\frac12\left[\hat\pi_{\mathbf k}\hat\pi_{-\mathbf k}+k^2\hat v_{\mathbf k}\hat v_{-\mathbf k}+s\left(\hat v_{\mathbf k}\hat\pi_{-\mathbf k}+\hat\pi_{-\mathbf k}\hat v_{\mathbf k}\right)\right]\tag{19}\label{eq:inflation-19}
$$

となります。各項は $\mathbf k$ と $-\mathbf k$ を結んでおり、**反対向きの波数が対になって現れます**。異なる波数対は互いに独立に発展するので、Hilbert 空間を波数対ごとに分けて考えることができます。

### 定在波：余弦・正弦の実振幅

一つの非零の波数対 $(\mathbf k,-\mathbf k)$ をとります。$\hat v_{\mathbf k}$ 自体は Hermite ではありませんが、$\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger$ なので、二つの Fourier 係数を二つの Hermite な配位演算子に組み替えることができます。各波数対から片方を選んだ集合を $\mathcal K_+$ とし、$\mathbf k\in\mathcal K_+$ に対して

$$
\hat q_{c,\mathbf k}=\frac{\hat v_{\mathbf k}+\hat v_{-\mathbf k}}{\sqrt2},\qquad\hat q_{s,\mathbf k}=\frac{i(\hat v_{\mathbf k}-\hat v_{-\mathbf k})}{\sqrt2}\tag{20}\label{eq:inflation-20}
$$

と定義します。$\hat\pi$ から同じ変換で $\hat p_{c,\mathbf k},\hat p_{s,\mathbf k}$ を作ると、$A,B\in\{c,s\}$ について

$$
[\hat q_{A,\mathbf k},\hat p_{B,\mathbf k'}]=i\,\delta_{AB}\,\delta_{\mathbf k,\mathbf k'}\tag{21}\label{eq:inflation-21}
$$

で、他の組は可換です。場は

$$
\hat v(\mathbf x)=\sqrt{\frac2V}\sum_{\mathbf k\in\mathcal K_+}\left[\hat q_{c,\mathbf k}\cos(\mathbf k\cdot\mathbf x)+\hat q_{s,\mathbf k}\sin(\mathbf k\cdot\mathbf x)\right]\tag{22}\label{eq:inflation-22}
$$

と、空間全体に広がった余弦と正弦の**定在波**の重ね合わせになります。こうして、**一つの波数対は二つの独立な量子振動子、すなわち四次元の正準位相空間を持つ**ことがわかります。

### Gaussian 状態の分解

この分解を $\eqref{eq:inflation-9}$ の Gaussian 波動汎関数に入れます。$v$ 表現の核 $\mathcal K_\eta(\mathbf x-\mathbf y)$ の Fourier 変換を $K_k(\eta)$ とすると、

$$
\int d^3x\,d^3y\;v(\mathbf x)\,\mathcal K_\eta(\mathbf x-\mathbf y)\,v(\mathbf y)=\sum_{\mathbf k}K_k\,v_{\mathbf k}v_{-\mathbf k}=\sum_{\mathbf k\in\mathcal K_+}K_k\left(q_{c,\mathbf k}^2+q_{s,\mathbf k}^2\right)\tag{23}\label{eq:inflation-23}
$$

です。よって

$$
\Psi^{(v)}_\eta[v]\propto\prod_{\mathbf k\in\mathcal K_+}\exp\left[-\frac{K_k(\eta)}2q_{c,\mathbf k}^2\right]\exp\left[-\frac{K_k(\eta)}2q_{s,\mathbf k}^2\right].\tag{24}\label{eq:inflation-24}
$$

進行波の複素振幅で書いた二次形式 $K_k\,v_{\mathbf k}v_{-\mathbf k}$ は $\mathbf k$ と $-\mathbf k$ を結び、定在波の実振幅で書くと対角になって、状態は**同じ形の一変数 Gaussian の積**に分かれます。前者が two-mode squeezing、後者が single-mode squeezing の見方の原型で、どちらも並進不変な実場の Gaussian 状態という一つの構造の表れです。

定在波への分け方は座標原点の選び方によります。原点を $\mathbf d$ だけずらすと $v_{\mathbf k}\to e^{i\mathbf k\cdot\mathbf d}v_{\mathbf k}$ で、$(q_c,q_s)$ の組は回転します。二つの成分の Gaussian は同じ幅と位相を持つので、その積は回転で不変です。

### 進行波：生成・消滅演算子

数状態の言葉を使うため、固定した正の基準周波数 $k$ で**進行波の消滅演算子**を定義します。

$$
\hat a_{\mathbf k}=\frac1{\sqrt2}\left(\sqrt k\,\hat v_{\mathbf k}+\frac{i\hat\pi_{\mathbf k}}{\sqrt k}\right),\qquad[\hat a_{\mathbf k},\hat a_{\mathbf k'}^\dagger]=\delta_{\mathbf k,\mathbf k'}\tag{25}\label{eq:inflation-25}
$$

逆に解くと

$$
\hat v_{\mathbf k}=\frac{\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger}{\sqrt{2k}},\qquad\hat\pi_{\mathbf k}=-i\sqrt{\frac k2}\left(\hat a_{\mathbf k}-\hat a_{-\mathbf k}^\dagger\right)\tag{26}\label{eq:inflation-26}
$$

です。$\hat a_{\mathbf k}$ と $\hat a_{-\mathbf k}$ は独立な二つの消滅演算子で、位置表示では $\hat a_{\mathbf k}$ に進行波 $e^{i\mathbf k\cdot\mathbf x}$ が付きます。基準周波数 $k$ は演算子を定義するために選んだ固定の数です。

### 二つの基底の関係

各定在波にも、同じ基準周波数で消滅演算子と無次元の quadrature を定義します。

$$
\hat b_{A,\mathbf k}=\frac{\hat Q_{A,\mathbf k}+i\hat P_{A,\mathbf k}}{\sqrt2},\qquad\hat Q_{A,\mathbf k}=\sqrt k\,\hat q_{A,\mathbf k},\qquad\hat P_{A,\mathbf k}=\frac{\hat p_{A,\mathbf k}}{\sqrt k}\tag{27}\label{eq:inflation-27}
$$

$[\hat Q_{A,\mathbf k},\hat P_{A,\mathbf k}]=i$ で、$Q,P$ が後の Wigner 図の座標軸になります。定義を比べると

$$
\hat a_{\pm\mathbf k}=\frac{\hat b_{c,\mathbf k}\mp i\,\hat b_{s,\mathbf k}}{\sqrt2},\qquad\hat b_{c,\mathbf k}=\frac{\hat a_{\mathbf k}+\hat a_{-\mathbf k}}{\sqrt2},\qquad\hat b_{s,\mathbf k}=\frac{i(\hat a_{\mathbf k}-\hat a_{-\mathbf k})}{\sqrt2}\tag{28}\label{eq:inflation-28}
$$

が成り立ちます。消滅演算子どうしだけを混ぜるユニタリ変換なので、基準周波数 $k$ に対する真空 $|0_{\mathrm{ref}}\rangle$ は両基底で共通です。

$$
\hat a_{\mathbf k}|0_{\mathrm{ref}}\rangle=\hat a_{-\mathbf k}|0_{\mathrm{ref}}\rangle=0\iff\hat b_{c,\mathbf k}|0_{\mathrm{ref}}\rangle=\hat b_{s,\mathbf k}|0_{\mathrm{ref}}\rangle=0\tag{29}\label{eq:inflation-29}
$$

実際の初期状態は §5 で選びます。進行波の二モードと定在波の二モードは、同じ二自由度の二つの基底です。

## 4. 波数対の Hamiltonian：two-mode squeezing と single-mode squeezing

### 進行波による表示（Schrödinger 描像）

$\eqref{eq:inflation-19}$ の Hamiltonian のうち、$\mathbf k$ と $-\mathbf k$ の二項をまとめて $\hat H_{\mathbf k}$ と書き、$\hat v_{\pm\mathbf k},\hat\pi_{\pm\mathbf k}$ を $\hat a_{\pm\mathbf k}$ で表すと

$$
\hat H_v=\sum_{\mathbf k\in\mathcal K_+}\hat H_{\mathbf k},\tag{30}\label{eq:inflation-30}
$$

$$
\hat H_{\mathbf k}=k\left(\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger\hat a_{-\mathbf k}+1\right)+i\,s(\eta)\left(\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger-\hat a_{\mathbf k}\hat a_{-\mathbf k}\right)\tag{31}\label{eq:inflation-31}
$$

を得ます。

第一項は基準周波数 $k$ の二つの振動子です。第二項の $\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger$ は**反対向きの波数に一つずつ励起を作り**、$\hat a_{\mathbf k}\hat a_{-\mathbf k}$ はその逆を行います。

$$
\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger|n_{\mathbf k},n_{-\mathbf k}\rangle=\sqrt{(n_{\mathbf k}+1)(n_{-\mathbf k}+1)}\;|n_{\mathbf k}+1,n_{-\mathbf k}+1\rangle\tag{32}\label{eq:inflation-32}
$$

係数 $s=z'/z$ は背景の時間変化の速さで、励起の対を作る源です。この形の Hamiltonian が生む変換を **two-mode squeezing** と呼びます。

### 対称性からみた一般形

この形は、次の三つの条件から一般に従います。

1. **二次の Hamiltonian：** 自由場の Hamiltonian は生成・消滅演算子の二次式です。
2. **空間並進対称性：** 場の全運動量は基準周波数の選び方によらず $\hat{\mathbf P}=\sum_{\mathbf k}\mathbf k\,\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}$ で、一様な背景では $[\hat{\mathbf P},\hat H_v]=0$ です。運動量を保存する二次の項は、$\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}$ の形の項と、対の項 $\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger$、$\hat a_{\mathbf k}\hat a_{-\mathbf k}$ に限られます。
3. **背景の時間依存性：** 時間に依存しない安定な Hamiltonian なら、適切な基底を一度選ぶと対の項を消せます。背景が時間に依存すると、対角化する基底も時間とともに動くので、固定した基底では対の項が残ります。

したがって、一様等方な時間依存背景の上の自由場では、一つの波数対の Hamiltonian は定数項を除いて

$$
\hat H_{\mathbf k}=\omega_k(\eta)\left(\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger\hat a_{-\mathbf k}\right)+\gamma_k(\eta)\,\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger+\gamma_k^*(\eta)\,\hat a_{\mathbf k}\hat a_{-\mathbf k}\tag{33}\label{eq:inflation-33}
$$

の形をとります。$\pm\mathbf k$ の係数が等しいのは等方性によります。インフレーションでは $\omega_k=k$、$\gamma_k=is$ です。膨張宇宙での粒子生成、パラメトリック共鳴、光学のパラメトリック増幅にも、同じ構造が現れます。

並進対称性は、さらに $\hat H_{\mathbf k}$ が励起数の差

$$
\hat N_{\mathbf k}-\hat N_{-\mathbf k},\qquad\hat N_{\pm\mathbf k}=\hat a_{\pm\mathbf k}^\dagger\hat a_{\pm\mathbf k}\tag{34}\label{eq:inflation-34}
$$

と可換であることを意味します。この差はこの波数対の運動量にあたり、時間発展で保存されます。真空から出発した状態は、**常に $\mathbf k$ と $-\mathbf k$ の励起が同数となります**。two-mode squeezing が全運動量ゼロの「対」を作るというのは、この意味です。

### 定在波による表示

描像はそのままで、基底を定在波に変えます。$\eqref{eq:inflation-28}$ の関係を代入すると

$$
\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger\hat a_{-\mathbf k}=\hat b_{c,\mathbf k}^\dagger\hat b_{c,\mathbf k}+\hat b_{s,\mathbf k}^\dagger\hat b_{s,\mathbf k},\qquad\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger=\frac12\left(\hat b_{c,\mathbf k}^{\dagger2}+\hat b_{s,\mathbf k}^{\dagger2}\right)\tag{35}\label{eq:inflation-35}
$$

となり、$c$ と $s$ を結ぶ項は消えます。したがって

$$
\hat H_{\mathbf k}=\hat H_{c,\mathbf k}+\hat H_{s,\mathbf k},\qquad\hat H_{A,\mathbf k}=k\left(\hat b_{A,\mathbf k}^\dagger\hat b_{A,\mathbf k}+\frac12\right)+\frac{is}2\left(\hat b_{A,\mathbf k}^{\dagger2}-\hat b_{A,\mathbf k}^2\right)\tag{36}\label{eq:inflation-36}
$$

となります。$\hat b_A^{\dagger2}$ は**一つのモードに二つの励起**を作る、**single-mode squeezing** の生成子です。二つの定在波は同じ Hamiltonian を持ち、互いに独立に発展します。正準変数で書けば

$$
\hat H_{A,\mathbf k}=\frac12\left(\hat p_{A,\mathbf k}^2+k^2\hat q_{A,\mathbf k}^2\right)+\frac s2\left(\hat q_{A,\mathbf k}\hat p_{A,\mathbf k}+\hat p_{A,\mathbf k}\hat q_{A,\mathbf k}\right)\tag{37}\label{eq:inflation-37}
$$

で、第二項が位相空間の一方向を伸ばし、共役な方向を縮めます。

この分離は空間反転対称性で説明できます。$\mathbf x\to-\mathbf x$ のもとで余弦は偶、正弦は奇なので、$c$ と $s$ を結ぶ二次の項はすべて反転で符号を変えるため、反転対称な Hamiltonian からは除かれます。さらに並進が $(c,s)$ の組を回転させるので、二つの係数は等しくなります。定在波は $\pm\mathbf k$ の進行波を等しい重みで重ね合わせたもので、運動量の平均はゼロなので、進行波とは違い独立に励起できるモードとなります。

### 生成消滅演算子の Heisenberg 方程式

$\hat a_{\mathbf k}(\eta)=U^\dagger\hat a_{\mathbf k}U$ などとすると、$\hat H_{\mathbf k}$ から

$$
\hat a_{\pm\mathbf k}'=-ik\,\hat a_{\pm\mathbf k}+s\,\hat a_{\mp\mathbf k}^\dagger,\qquad\hat b_{A,\mathbf k}'=-ik\,\hat b_{A,\mathbf k}+s\,\hat b_{A,\mathbf k}^\dagger\tag{38}\label{eq:inflation-38}
$$

が得られます。消滅演算子の時間微分に生成演算子が現れるので、後の時刻の消滅演算子は、初期の消滅演算子と生成演算子の線形結合になります。この形の変換を **Bogoliubov 変換**と呼び、その係数は §5 で求めます。ここで、進行波の消滅演算子は**反対向きの波数の生成演算子**と、定在波の消滅演算子は**自分自身の生成演算子**と混ざります。前者は運動量保存の言い換えでもあります。$[\hat{\mathbf P},\hat a_{\mathbf k}]=-\mathbf k\,\hat a_{\mathbf k}$、$[\hat{\mathbf P},\hat a_{-\mathbf k}^\dagger]=-\mathbf k\,\hat a_{-\mathbf k}^\dagger$ なので、$\hat a_{\mathbf k}$ と同じ運動量を運ぶ線形な演算子は $\hat a_{\mathbf k}$ と $\hat a_{-\mathbf k}^\dagger$ の二つです。

## 5. Bunch–Davies 真空

### モード関数による演算子の展開（Heisenberg 描像）

各定在波成分の正準変数の Heisenberg 方程式は

$$
\hat q_{A,\mathbf k}'=\hat p_{A,\mathbf k}+s\,\hat q_{A,\mathbf k},\qquad\hat q_{A,\mathbf k}''+\left(k^2-\frac{z''}{z}\right)\hat q_{A,\mathbf k}=0\tag{39}\label{eq:inflation-39}
$$

で、係数が c 数の線形方程式です。その解は、方程式の二つの独立解に、時間に依存しない演算子を掛けて重ね合わせたものになります。そこで複素数値の解 $f_k(\eta)$ を一つ選び、その複素共役を第二の解として

$$
\hat q_{A,\mathbf k}(\eta)=f_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}}+f_k^*(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}\dagger},\qquad\hat p_{A,\mathbf k}(\eta)=g_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}}+g_k^*(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}\dagger}\tag{40}\label{eq:inflation-40}
$$

と展開します。ここで、$g_k=f_k'-sf_k$ で、$\hat q$ が Hermite なので第二の係数は $\hat b^{\mathrm{in}\dagger}$ になります。$f_k$ を**モード関数**と呼びます。

正準交換関係 $[\hat q,\hat p]=i$ に代入すると $(f_kg_k^*-f_k^*g_k)\,[\hat b^{\mathrm{in}},\hat b^{\mathrm{in}\dagger}]=i$ です。左の括弧は Wronskian で時間によらないので、

$$
f_kg_k^*-f_k^*g_k=i\tag{41}\label{eq:inflation-41}
$$

と規格化すれば $[\hat b_{A,\mathbf k}^{\mathrm{in}},\hat b_{B,\mathbf k'}^{\mathrm{in}\dagger}]=\delta_{AB}\delta_{\mathbf k,\mathbf k'}$ となり、$\hat b^{\mathrm{in}}$ は消滅演算子になります。展開を逆に解いた形

$$
\hat b_{A,\mathbf k}^{\mathrm{in}}=i\left[f_k^*(\eta)\,\hat p_{A,\mathbf k}(\eta)-g_k^*(\eta)\,\hat q_{A,\mathbf k}(\eta)\right]\tag{42}\label{eq:inflation-42}
$$

も後で使います。こうして、演算子の時間発展は一つの c 数関数 $f_k$ に集約されます。モード関数の選び方は消滅演算子の選び方そのもので、異なる $f_k$ は Bogoliubov 変換で結ばれた異なる $\hat b^{\mathrm{in}}$ を与え、それぞれが別の「真空」を定めます。

### 初期条件：短波長での基底状態

インフレーションの初期には、注目するモードの波長は Hubble 半径よりずっと短く、$k^2\gg|z''/z|$、$|s|\ll k$ です。この領域では §4 の $\hat H_{A,\mathbf k}$ は振動数 $k$ の調和振動子に近づき、各モードの自然な状態はその基底状態です。そこで、初期にこの基底状態を与えるモード関数として、正周波数の解

$$
f_k\longrightarrow\frac{e^{-ik\eta}}{\sqrt{2k}},\qquad g_k\longrightarrow-i\sqrt{\frac k2}\,e^{-ik\eta}\tag{43}\label{eq:inflation-43}
$$

を選びます。このとき上の逆の式から $\hat b_{A,\mathbf k}^{\mathrm{in}}=e^{ik\eta}\,\hat b_{A,\mathbf k}(\eta)$ で、$\hat b^{\mathrm{in}}$ は初期の消滅演算子に位相を除いて一致します。すべての $\hat b^{\mathrm{in}}$ が消す状態

$$
\hat b_{A,\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle=0\qquad(\mathbf k\in\mathcal K_+,\ A=c,s)\tag{44}\label{eq:inflation-44}
$$

が **Bunch–Davies 真空**です。進行波の $\hat a_{\pm\mathbf k}^{\mathrm{in}}=(\hat b_{c,\mathbf k}^{\mathrm{in}}\mp i\hat b_{s,\mathbf k}^{\mathrm{in}})/\sqrt2$ も同じ状態を消すので同じ初期状態を定めます。このようにして、初期には各モードが調和振動子の基底状態であり、その後の時間発展はモード関数 $f_k$ がすべて担うという描像が得られます。有限期間のインフレーションでは、対象とするモードにこの短波長の初期領域があることを仮定しています。

### スペクトルと空間相関

Heisenberg 描像なので固定された状態 $|0_{\mathrm{BD}}\rangle$ で期待値をとると、

$$
\langle\hat q_{A,\mathbf k}^2(\eta)\rangle=|f_k(\eta)|^2,\qquad\langle\hat p_{A,\mathbf k}^2(\eta)\rangle=|g_k(\eta)|^2,\qquad\frac12\langle\{\hat q_{A,\mathbf k}(\eta),\hat p_{A,\mathbf k}(\eta)\}\rangle=\operatorname{Re}(f_k(\eta)g_k^*(\eta))\tag{45}\label{eq:inflation-45}
$$

です。Fourier 係数では $\langle\hat v_{\mathbf k}\hat v_{\mathbf k'}\rangle=\delta_{\mathbf k,-\mathbf k'}|f_k|^2$ なので $\eqref{eq:inflation-10}$ の相関関数は

$$
G_\zeta(\eta;\mathbf x,\mathbf y)=\frac1{z^2V}\sum_{\mathbf k}|f_k|^2e^{i\mathbf k\cdot(\mathbf x-\mathbf y)}\longrightarrow\int\frac{d^3k}{(2\pi)^3}\,P_\zeta(k,\eta)\,e^{i\mathbf k\cdot(\mathbf x-\mathbf y)},\qquad P_\zeta=\frac{|f_k|^2}{z^2}\tag{46}\label{eq:inflation-46}
$$

となります。矢印は $V^{-1}\sum_{\mathbf k}\to\int d^3k/(2\pi)^3$ の極限で、箱の大きさは結果に残りません。この結果から分かるように、**一つのモードの分散 $|f_k|^2$ が、そのまま空間相関のスペクトル密度を与えます。**

### Bogoliubov 係数と squeezing parameter

§3 で定義した消滅演算子を Heisenberg 時間発展させ、in 演算子で展開すると

$$
\hat b_{A,\mathbf k}(\eta)=\alpha_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}}+\beta_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}\dagger},\qquad\hat a_{\pm\mathbf k}(\eta)=\alpha_k(\eta)\,\hat a_{\pm\mathbf k}^{\mathrm{in}}+\beta_k(\eta)\,\hat a_{\mp\mathbf k}^{\mathrm{in}\dagger}\tag{47}\label{eq:inflation-47}
$$

となり、係数は両基底で共通です。モード関数を使えば

$$
\alpha_k=\frac1{\sqrt2}\left(\sqrt k\,f_k+\frac{ig_k}{\sqrt k}\right),\qquad\beta_k=\frac1{\sqrt2}\left(\sqrt k\,f_k^*+\frac{ig_k^*}{\sqrt k}\right)\tag{48}\label{eq:inflation-48}
$$

で、Wronskian 条件は $|\alpha_k|^2-|\beta_k|^2=1$ にあたります。ここで

$$
|\alpha_k|=\cosh r_k,\qquad|\beta_k|=\sinh r_k\qquad(r_k\ge0)\tag{49}\label{eq:inflation-49}
$$

と書き、$r_k$ を **squeezing parameter** と呼びます。この名前の意味は、§6 で状態を具体的に書き、§7 で Wigner 楕円を描くと明らかになります。初期には $\alpha_k\simeq e^{-ik\eta}$、$\beta_k\simeq0$ で $r_k\simeq0$ です。

## 6. squeezed 状態の具体形（Schrödinger 描像）

§5 の Heisenberg 計算の結果を使って、時刻 $\eta$ の状態 $|\Psi(\eta)\rangle=U|0_{\mathrm{BD}}\rangle$ を基準 $k$ の励起数固有状態で書きます。

### 進行波：two-mode squeezed vacuum

Bogoliubov 変換を逆に解くと $\hat a_{\mathbf k}^{\mathrm{in}}=\alpha_k^*\hat a_{\mathbf k}(\eta)-\beta_k\hat a_{-\mathbf k}^\dagger(\eta)$ です。$\hat a_{\mathbf k}(\eta)=U^\dagger\hat a_{\mathbf k}U$ を代入すると、in 条件 $\hat a_{\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle=0$ は時間に依存しない Schrödinger 演算子を使って

$$
\left(\alpha_k^*\,\hat a_{\mathbf k}-\beta_k\,\hat a_{-\mathbf k}^\dagger\right)|\Psi(\eta)\rangle=0\tag{50}\label{eq:inflation-50}
$$

と書き直せます。Heisenberg 描像で固定した状態に課した条件が、各時刻の状態に対する条件になりました。波数対の状態を $\sum_{m,n}c_{mn}|m\rangle_{\mathbf k}|n\rangle_{-\mathbf k}$ と展開して、この条件と $\mathbf k\leftrightarrow-\mathbf k$ を入れ替えた条件を解くと、$m=n$ の成分だけが残り、全体の位相を除いて

$$
|\Psi_{\mathbf k}(\eta)\rangle=\frac1{\cosh r_k}\sum_{n=0}^\infty\lambda_k^n\,|n\rangle_{\mathbf k}|n\rangle_{-\mathbf k},\qquad\lambda_k=\frac{\beta_k}{\alpha_k^*},\qquad|\lambda_k|=\tanh r_k\tag{51}\label{eq:inflation-51}
$$

が得られます。全体の状態は、すべての波数対についてこれを掛け合わせたものです。これが **two-mode squeezed vacuum state** で、その性質は式から直接読み取れます。

- **対の生成：** $\mathbf k$ と $-\mathbf k$ の励起数は常に等しく、全運動量はゼロです（§4 の対称性の帰結）。
- **幾何分布：** $n$ 対を見出す確率は $\tanh^{2n}r_k/\cosh^2r_k$、各進行波の平均励起数は $\sinh^2r_k=|\beta_k|^2$ です。
- **もつれ：** $-\mathbf k$ について部分トレースをとると、$\mathbf k$ の進行波は励起数が幾何分布に従う熱的な形の混合状態になります。そのエントロピー

    $$
    S_{\mathbf k|-\mathbf k}=\cosh^2r_k\ln\cosh^2r_k-\sinh^2r_k\ln\sinh^2r_k\tag{52}\label{eq:inflation-52}
    $$

    は $r_k$ とともに増え、その間も波数対全体は純粋状態に保たれます。

### 定在波：二つの single-mode squeezed vacuum

同様に $\hat b_{A,\mathbf k}^{\mathrm{in}}=\alpha_k^*\hat b_{A,\mathbf k}(\eta)-\beta_k\hat b_{A,\mathbf k}^\dagger(\eta)$ から、

$$
\left(\alpha_k^*\,\hat b_{A,\mathbf k}-\beta_k\,\hat b_{A,\mathbf k}^\dagger\right)|\Psi(\eta)\rangle=0\qquad(A=c,s)\tag{53}\label{eq:inflation-53}
$$

です。この条件は $c$ と $s$ を別々に含むので、状態は二つの定在波の状態の積

$$
|\Psi_{\mathbf k}(\eta)\rangle=|\psi_k(\eta)\rangle_c\otimes|\psi_k(\eta)\rangle_s,\qquad|\psi_k(\eta)\rangle=\frac1{\sqrt{\cosh r_k}}\sum_{m=0}^\infty\lambda_k^m\frac{\sqrt{(2m)!}}{2^m\,m!}\,|2m\rangle\tag{54}\label{eq:inflation-54}
$$

になります。これが **single-mode squeezed vacuum** です。二つの定在波は同じ純粋状態にあり、各定在波には**偶数個の励起だけ**が現れます。$\hat b_A^{\dagger2}$ が一つのモードに励起を二つずつ作るからです。平均励起数はやはり $\sinh^2r_k$ です。

二つの表示は同じ状態を表しているので、全励起数も一致する、つまり $\hat N_{\mathbf k}+\hat N_{-\mathbf k}=\hat N_c+\hat N_s$ となるはずで、このことは具体的に確かめられます。進行波では全励起数 $2n$ の確率は $\tanh^{2n}r_k/\cosh^2r_k$ で、定在波では二つの偶数分布の畳み込みが恒等式 $\sum_{m=0}^n\binom{2m}{m}\binom{2n-2m}{n-m}=4^n$ によって同じ結果を与えます。演算子の言葉では、two-mode squeezing の生成子 $\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger=\frac12(\hat b_{c,\mathbf k}^{\dagger2}+\hat b_{s,\mathbf k}^{\dagger2})$ が、互いに可換な二つの single-mode squeezing の生成子の和になっていることの帰結です。

<iframe src="app/supporting.html?lang=ja&amp;view=pairs" title="同じ squeezed 状態の進行波基底と定在波基底での励起数分布" data-auto-height scrolling="no" style="display: block; width: 100%; height: 850px; min-height: 600px; border: 0; overflow: hidden;" loading="eager"></iframe>

$r$ を動かして、一つのモードだけを見た分布を比べてください。進行波は単調に減る熱的な形、定在波は偶数だけの分布で、平均はどちらも $\sinh^2r$ です。波数対の全励起数の分布は、両基底で完全に一致します。

### 部分系の選び方ともつれ

もつれの有無は、状態と**部分系の分け方**の組で決まります。同じ純粋状態が、$\mathbf k$ と $-\mathbf k$ に分ければもつれた状態、$c$ と $s$ に分ければ積状態です。two-mode squeezing と二つの single-mode squeezing は、全状態を保つ基底変換で結ばれた同じ記述です。

空間の領域で分けるのは、さらに別の分け方です。定在波成分が互いに独立でも、実空間の異なる領域の間には相関ともつれがあります。量子的な性質を論じるときは、どの部分系の間の相関を問うのかを明示する必要があります。

### 波動関数と実空間の核

同じ状態を定在波の振幅 $q$ の波動関数で書きます。in 条件の Schrödinger 演算子による表現 $i\left[f_k^*(\eta)\,\hat p-g_k^*(\eta)\,\hat q\right]|\psi_k(\eta)\rangle=0$ に $\hat p=-i\,d/dq$ を代入すると

$$
\psi_k(q;\eta)\propto\exp\left[-\frac{K_k(\eta)}2q^2\right],\qquad K_k=-i\,\frac{g_k^*}{f_k^*}\tag{55}\label{eq:inflation-55}
$$

です。Wronskian 条件から $\operatorname{Re}K_k=1/(2|f_k|^2)$ で、$\langle\hat q^2\rangle=|f_k|^2$ と整合します。初期には $K_k=k$ で、基準真空の波動関数に一致します。

この $K_k$ が、$\eqref{eq:inflation-23}$ の実空間の核 $\mathcal K_\eta(\mathbf x-\mathbf y)$ の Fourier 変換です。Bunch–Davies 状態の波動汎関数は

$$
\Psi^{(v)}_\eta[v]\propto\exp\left[-\frac12\sum_{\mathbf k}K_k(\eta)\,v_{\mathbf k}v_{-\mathbf k}\right]\tag{56}\label{eq:inflation-56}
$$

で、実空間の量子状態とモードごとの squeezed state がここで結びつきます。

## 7. Wigner 楕円と空間相関

Wigner 関数は Schrödinger 描像の状態を位相空間に表示するもので、ここではその中身を §5 の Heisenberg 計算から求めます。両者の期待値は一致し、例えば $\langle\Psi(\eta)|\hat Q_{\mathrm S}^2|\Psi(\eta)\rangle=\langle0_{\mathrm{BD}}|\hat Q_{\mathrm H}^2(\eta)|0_{\mathrm{BD}}\rangle$ です。

### Wigner 関数

一つの定在波成分を固定し、添字 $A,\mathbf k$ を省略します。密度演算子 $\hat\rho$ の Wigner 関数は、$\hat Q$ の固有状態 $|Q\rangle$ を用いて

$$
W(Q,P)=\frac1{2\pi}\int_{-\infty}^{\infty}d\xi\,e^{-iP\xi}\left\langle Q+\frac\xi2\right|\hat\rho\left|Q-\frac\xi2\right\rangle\tag{57}\label{eq:inflation-57}
$$

と定義されます。$Q,P,\xi$ は実数です。一方の座標で積分すると、他方の quadrature の測定確率密度

$$
\int dP\,W(Q,P)=\langle Q|\hat\rho|Q\rangle,\qquad\int dQ\,W(Q,P)=\langle P|\hat\rho|P\rangle\tag{58}\label{eq:inflation-58}
$$

が得られ、位相空間での積の平均は対称順序（Weyl 順序）の期待値を与えます。例えば $\int dQ\,dP\,QP\,W=\frac12\langle\hat Q\hat P+\hat P\hat Q\rangle$ です。一般の状態では $W$ は負の値もとる準確率分布で、Gaussian 状態では $W\ge0$ です。定義と性質は [O’Connell](https://arxiv.org/abs/1009.4431) にまとめられています。

### 共分散行列と楕円

$\hat{\mathbf Z}=(\hat Q,\hat P)^T$ の共分散行列 $\Sigma_{ij}=\frac12\langle\{\hat Z_i,\hat Z_j\}\rangle$ は、§5 の期待値から

$$
\Sigma=\begin{pmatrix}k|f_k|^2&\operatorname{Re}(f_kg_k^*)\\\operatorname{Re}(f_kg_k^*)&|g_k|^2/k\end{pmatrix},\qquad\det\Sigma=\frac14\tag{59}\label{eq:inflation-59}
$$

です。行列式の値は Wronskian 条件から従い、純粋な Gaussian 状態が最小不確定性を保つことを表します。平均ゼロの Gaussian 状態の Wigner 関数は

$$
W(\mathbf Z)=\frac1{2\pi\sqrt{\det\Sigma}}\exp\left[-\frac12\mathbf Z^T\Sigma^{-1}\mathbf Z\right]\tag{60}\label{eq:inflation-60}
$$

で、その等高線は楕円です。

$\Sigma$ の固有値、すなわち長軸方向と短軸方向の分散は

$$
\sigma_\pm^2=\frac12e^{\pm2r_k}\tag{61}\label{eq:inflation-61}
$$

です。つまり、基準真空の円 $\Sigma=I/2$ から、面積を保ったまま一方向が伸び、直交する方向が縮みます。これが squeezing の幾何学的な姿です。長軸が正の $Q$ 軸となす角 $\varphi_k$ は

$$
\varphi_k=\frac12\arg(\alpha_k\beta_k)\tag{62}\label{eq:inflation-62}
$$

で、§6 の対の振幅は $\lambda_k=\tanh r_k\,e^{2i\varphi_k}$ と書けます。数表示の $\lambda_k$ と位相空間の楕円は、同じ二つの数 $r_k,\varphi_k$ で指定されています。

### 空間相関への射影

$\eqref{eq:inflation-46}$ の $P_\zeta=|f_k|^2/z^2$ は、$\Sigma_{QQ}=k|f_k|^2$ を使うと

$$
P_\zeta(k,\eta)=\frac{\Sigma_{QQ}}{k\,z^2},\qquad\Sigma_{QQ}=\frac12\left[e^{2r_k}\cos^2\varphi_k+e^{-2r_k}\sin^2\varphi_k\right]\tag{63}\label{eq:inflation-63}
$$

です。$\Sigma_{QQ}$ は楕円を $Q$ 軸に射影した幅です。等方的な状態では角度積分ができて、共動距離 $R=|\mathbf x-\mathbf y|$ の関数として

$$
G_\zeta(\eta;R)=\int_0^\infty\frac{dk}k\,\mathcal P_\zeta(k,\eta)\,\frac{\sin kR}{kR},\qquad\mathcal P_\zeta=\frac{k^3}{2\pi^2}P_\zeta\tag{64}\label{eq:inflation-64}
$$

となり、squeezing の量を直接入れれば

$$
G_\zeta(\eta;R)=\frac1{4\pi^2z^2}\int_0^\infty dk\,k\left[e^{2r_k}\cos^2\varphi_k+e^{-2r_k}\sin^2\varphi_k\right]\frac{\sin kR}{kR}\tag{65}\label{eq:inflation-65}
$$

です。楕円の**伸びと向きの両方**がスペクトルを決め、その重ね合わせが距離依存性を作ります。元の場へ戻す係数 $z^{-2}$ も含めて、これが §9 の「凍結」を理解する鍵になります。

$G_\zeta$ が見ているのは楕円の $Q$ 方向の射影です。楕円全体を実空間で表すには、場と運動量の相関 $\frac12\langle\{\hat\zeta(\mathbf x),\hat\Pi_\zeta(\mathbf y)\}\rangle$ と運動量どうしの相関の情報を加えます。それらの Fourier 係数はそれぞれ $\Sigma_{QP}$ と $kz^2\Sigma_{PP}$ で、観測的に squeezing の度合いや量子的な起源を論じるには、場の二点関数に加えてこれらの情報が必要となります。

## 8. 厳密に解ける例：de Sitter 背景上の質量ゼロスカラー場

### 模型と対応関係

ここからの図では、厳密な de Sitter 時空

$$
a(\eta)=-\frac1{H\eta},\qquad\eta<0,\qquad\mathcal H=-\frac1\eta\qquad(H\text{ は一定})\tag{66}\label{eq:inflation-66}
$$

の上の、自由・質量ゼロ・最小結合のスカラー場 $\hat\phi$ で計算します。背景は与えられたものとし、$\hat\phi$ の背景への影響は考えません。作用

$$
S_\phi=\frac12\int d\eta\,d^3x\;a^2\left[(\phi')^2-(\nabla\phi)^2\right]\tag{67}\label{eq:inflation-67}
$$

は §1 の曲率摂動の作用で $z$ を $a$ に置き換えた形で、§2–7 の議論は次の対応でそのまま使えます。

| | 曲率摂動 | 図のスカラー場 |
| --- | --- | --- |
| 元の場 | $\zeta$ | $\phi$ |
| 作用の係数 | $z^2$ | $a^2$ |
| 正準変数 | $v=z\zeta$ | $u=a\phi$ |
| 共役運動量 | $\pi=v'-(z'/z)v$ | $\pi_u=u'-\mathcal Hu=a\phi'$ |
| squeezing の係数 $s$ | $z'/z$ | $\mathcal H$ |

モード関数も同じ記号 $f_k,g_k$ で書き、$z$ を $a$ に置き換えた方程式の解とします。適切に正準規格化したテンソル摂動の各偏極も、同じ形の方程式に従います。曲率摂動との関係は §9 で述べます。

### モード関数と squeezing parameter

時間の代わりに

$$
x=-k\eta=\frac{k}{aH},\qquad N=-\ln x\tag{68}\label{eq:inflation-68}
$$

を使います。$x$ は物理的な波数 $k/a$ と $H$ の比で、$x\gg1$ が Hubble 半径より短い波長、$x\ll1$ が長い波長です。$N$ は $x=1$、すなわち慣用的に Hubble crossing と呼ぶ時刻からの e-fold 数です。

過去での正周波数条件と Wronskian 条件を満たすモード関数を解くと

$$
f_k=\frac{1+i/x}{\sqrt{2k}}\,e^{ix},\qquad g_k=f_k'-\mathcal Hf_k=-i\sqrt{\frac k2}\,e^{ix}\tag{69}\label{eq:inflation-69}
$$

となります。$\eqref{eq:inflation-48}$ に代入すると

$$
\alpha_k=\left(1+\frac i{2x}\right)e^{ix},\qquad\beta_k=-\frac i{2x}\,e^{-ix},\tag{70}\label{eq:inflation-70}
$$

$$
r_k=\operatorname{arsinh}\frac1{2x},\qquad\varphi_k=-\frac12\arctan(2x),\qquad\lambda_k=\frac{1-2ix}{1+4x^2}\tag{71}\label{eq:inflation-71}
$$

が得られます。短波長では $r_k\simeq1/(2x)$ で状態はほぼ真空、長波長では $r_k\simeq-\ln x=N$ です。

$$
\frac{dr_k}{dN}=\frac1{\sqrt{1+4x^2}}\tag{72}\label{eq:inflation-72}
$$

なので、Hubble crossing を十分過ぎると、1 e-fold ごとに $r_k$ がほぼ 1 ずつ増えます。

$Q=\sqrt k\,q$ の波動関数は、$\eqref{eq:inflation-55}$ の $K_k$ から

$$
\psi(Q;x)\propto\exp\left[-\frac{x(x+i)}{2(1+x^2)}\,Q^2\right]\tag{73}\label{eq:inflation-73}
$$

です。$x\to0$ では指数の実部が $x^2$ 程度に小さくなって $Q$ 方向の幅が広がり、虚部 $\simeq x$ が与える位相 $e^{-ixQ^2/2}$ が、$Q$ と $P$ の相関 $P\simeq-xQ$ を表します。

### 保存成分と減衰成分

元の場の実振幅は $\hat\phi_{A,\mathbf k}=\hat q_{A,\mathbf k}/a$ なので、そのモード関数は

$$
\frac{f_k}a=\frac H{\sqrt{2k^3}}(x+i)\,e^{ix}=\frac H{\sqrt{2k^3}}\left[i\left(1+\frac{x^2}2+O(x^4)\right)-\frac{x^3}3+O(x^5)\right]\tag{74}\label{eq:inflation-74}
$$

です。最後の式は $x\ll1$ での展開で、虚部は一定値に近づく**保存成分**、実部は $x^3\propto a^{-3}$ で減る**減衰成分**です。勾配を無視した長波長の方程式 $(a^2\phi')'=0$ の一般解 $\phi\simeq C_1+C_2\int^\eta d\tilde\eta/a^2$ の二つの項に対応し、虚部の $x^2/2$ は保存成分への補正です。

Bunch–Davies 真空でのスペクトルは

$$
P_\phi(k,\eta)=\left|\frac{f_k}a\right|^2=\frac{H^2}{2k^3}(1+x^2),\qquad\mathcal P_\phi=\frac{H^2}{4\pi^2}(1+x^2)\longrightarrow\left(\frac H{2\pi}\right)^2\tag{75}\label{eq:inflation-75}
$$

です。正準変数の分散 $|f_k|^2$ は $a^2$ とともに増え続け、元の場のパワーは Hubble crossing の後に一定値 $(H/2\pi)^2$ へ近づきます。

<iframe src="app/supporting.html?lang=ja&amp;view=background" title="正準変数のモード関数と元の場のモード関数の時間発展" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

正準変数のモード $f_k$ と元の場のモード $f_k/a$ を比べてください。表示を切り替えると、保存成分と減衰成分、モード方程式の勾配項と背景項の大小も確認できます。

### 位相空間の流れ

e-fold 数 $N$ を時間にとると、§4 の $\hat H_{A,\mathbf k}$ に $d\eta/dN=x/k$ を掛けて、一つの定在波の Hamiltonian は

$$
\hat K_N=\frac x2\left(\hat Q^2+\hat P^2\right)+\frac12\left(\hat Q\hat P+\hat P\hat Q\right)\tag{76}\label{eq:inflation-76}
$$

です。Heisenberg 方程式は

$$
\frac{d\hat{\mathbf Z}}{dN}=A\,\hat{\mathbf Z},\qquad A=x\begin{pmatrix}0&1\\-1&0\end{pmatrix}+\begin{pmatrix}1&0\\0&-1\end{pmatrix}\tag{77}\label{eq:inflation-77}
$$

で、第一項が位相空間の回転、第二項が $Q$ 方向の伸長と $P$ 方向の収縮です。Hamiltonian が二次式なので、Schrödinger 描像の Wigner 関数は、数値座標 $\mathbf Z$ をこの線形の流れ $d\mathbf Z/dN=A\mathbf Z$ で運んだものに厳密に一致します。共分散は $d\Sigma/dN=A\Sigma+\Sigma A^T$ に従い、$\operatorname{tr}A=0$ なので面積が保たれます。

$x\gg1$ では回転が優勢で、分布はほぼ円のまま回ります。$x$ が減ると伸縮の寄与が相対的に大きくなり、$x=1$ で両者が同程度になります。$x<1$ では $A$ が実固有値 $\pm\sqrt{1-x^2}$ を持つ双曲型の流れです。

<span id="main-animation"></span>

<iframe src="app/index.html?lang=ja" title="固定した正準座標の上のWigner楕円と、回転・squeezingの流れ" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

アニメーションでは、次の三つの段階を比べてください。

1. **$x\gg1$：** 回転が優勢で、Wigner 分布はほぼ円形です。開始時のわずかな楕円は、$x=12$ から描いていることによります。
2. **$x\approx1$：** 回転と伸縮が同程度になり、楕円の変形が目立ち始めます。
3. **$x\ll1$：** 長軸が伸びて短軸が細くなり、長軸は $Q$ 軸に近づきます。

等高線 $\mathbf Z^T\Sigma^{-1}\mathbf Z=1$ が囲む確率は $1-e^{-1/2}\simeq39\%$ です。矢印の長さには表示用の共通倍率と $1/\sqrt{1+x^2}$ を掛けてあり、楕円は元の流れで計算しています。方向の表示を切り替えると、瞬間的な流れの固有方向、楕円の主軸、保存解・減衰解の方向を比べられます。場の分散を決めるのは、主軸とその $Q$ 軸への射影です。

<iframe src="app/supporting.html?lang=ja&amp;view=squeezing" title="e-fold時間に対するsqueezingの大きさと長軸の角度" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

こちらは Hubble crossing 後 4 e-fold までの $r_k$ と $\varphi_k$ です。late time で $r_k\simeq N$ となり、角度が 0 に近づきます。

### 四次元共分散：進行波基底での表示

一つの定在波で見た楕円を、波数対の四次元位相空間に戻します。定在波の座標 $\hat{\mathbf Z}_{\mathrm{st}}=(\hat Q_c,\hat P_c,\hat Q_s,\hat P_s)^T$ では、二成分が同じ状態にあるので

$$
\Sigma_{\mathrm{st}}=\begin{pmatrix}\Sigma&0\\0&\Sigma\end{pmatrix}\tag{78}\label{eq:inflation-78}
$$

です。進行波の quadrature $\hat Q_\pm=(\hat a_{\pm\mathbf k}+\hat a_{\pm\mathbf k}^\dagger)/\sqrt2$、$\hat P_\pm=(\hat a_{\pm\mathbf k}-\hat a_{\pm\mathbf k}^\dagger)/(i\sqrt2)$ は、§3 の関係から $\hat Q_\pm=(\hat Q_c\pm\hat P_s)/\sqrt2$、$\hat P_\pm=(\hat P_c\mp\hat Q_s)/\sqrt2$ です。$\hat{\mathbf Z}_{\mathrm{tr}}=(\hat Q_+,\hat P_+,\hat Q_-,\hat P_-)^T$ の共分散は

$$
\Sigma_{\mathrm{tr}}=\frac12\begin{pmatrix}\cosh2r_k\,I&\sinh2r_k\,R_k\\\sinh2r_k\,R_k&\cosh2r_k\,I\end{pmatrix},\qquad R_k=\begin{pmatrix}\cos2\varphi_k&\sin2\varphi_k\\\sin2\varphi_k&-\cos2\varphi_k\end{pmatrix}\tag{79}\label{eq:inflation-79}
$$

となります。$I$ は $2\times2$ の単位行列です。一つの進行波だけのブロックは等方的で、分散は $\frac12\cosh2r_k=|\beta_k|^2+\frac12$ となります。これが §6 で議論した熱的な状態です。非対角ブロックが、$\mathbf k$ と $-\mathbf k$ の強い相関、すなわち two-mode squeezing を表しています。

<iframe src="app/supporting.html?lang=ja&amp;view=basis" title="同じ純粋状態の進行波・定在波基底での四次元共分散" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1200px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

遅い時刻を選び、定在波では同じ二つのブロックに分かれる共分散が、進行波ではモード間の相関として現れることを確かめてください。どちらの行列も波数対の純粋状態としては同じものを表しています。

## 9. 凍結、古典的な確率場、音響ピーク

§8 で見た squeezing の帰結を、観測される揺らぎまで順にたどります。まず場の揺らぎが凍結し、その振幅が保存された曲率摂動として原始揺らぎに引き継がれる頃を見ます。凍結したモードは、古典的な確率場の初期条件として扱えるようになります。そしてその初期条件がほぼ成長モードだけで決っていることが、CMB の音響ピークとして観測に現れます。

### 条件付きの幅

§8 の模型の共分散は

$$
\Sigma(x)=\frac12\begin{pmatrix}1+x^{-2}&-x^{-1}\\-x^{-1}&1\end{pmatrix}\tag{80}\label{eq:inflation-80}
$$

です。$\Sigma_{PP}=1/2$ は一定で、細くなるのは傾いた短軸の方向です。正の Gaussian Wigner 密度で $Q$ を与えたときの $P$ の条件付き統計は

$$
\mathbb E_W[P\mid Q]=-\frac x{1+x^2}\,Q,\qquad\operatorname{Var}_W(P\mid Q)=\frac{x^2}{2(1+x^2)}\tag{81}\label{eq:inflation-81}
$$

で、$x\ll1$ では分布が直線 $P\simeq-xQ$ の近くに集中します。振幅と運動量の相関が強まり、振幅を与えたときに残る運動量の幅が小さくなるわけです。添字 $W$ は、Wigner 密度の統計であることを示しています。

### 場の速度

cosmic time での場の速度 $\dot\phi=\phi'/a$ の展開係数は $g_k/a^2$ なので、そのスペクトルと振幅に対する比は

$$
P_{\dot\phi}(k,\eta)=\frac{k}{2a^4},\qquad\frac{\sqrt{P_{\dot\phi}}}{H\sqrt{P_\phi}}=\frac{x^2}{\sqrt{1+x^2}}\simeq x^2\quad(x\ll1)\tag{82}\label{eq:inflation-82}
$$

です。Hubble 時間あたりの場の変化は、振幅に比べて $x^2$ 程度に抑えられます。例えば $x=0.1$ では約 1% です。つまり、**場の振幅には有限の幅を持つ重ね合わせが残り、その時間変化が小さくなります。** これが凍結の意味です。$[\hat\phi_{A,\mathbf k},\dot{\hat\phi}_{A,\mathbf k}]=i/a^3$ なので、速度の幅の縮小は $[\hat Q,\hat P]=i$ や $\det\Sigma=1/4$ と両立します。

squeezing と凍結は、inflation における量子的時間発展の同じ側面の異なる見方です。正準変数 $Q$ の分布は長軸方向に $e^{r_k}$ に比例して広がり、元の場の振幅は $Q$ を $\sqrt k\,a$ で割ったもので、その比が一定値に収束します。同時に減衰成分が抑えられ、その後の線形発展に必要なランダムな input は、実効的にモードごとに一つの振幅に絞られます。

### 曲率摂動への適用

この結果を曲率摂動に適用するには、$z$ と $a$ の関係が必要です。Planck 質量を $M_{\mathrm{Pl}}$ とすると、背景の Einstein 方程式から

$$
\epsilon_1=-\frac{\dot H}{H^2}=\frac{\dot\phi_0^2}{2M_{\mathrm{Pl}}^2H^2},\qquad z^2=2a^2\epsilon_1M_{\mathrm{Pl}}^2\tag{83}\label{eq:inflation-83}
$$

で、$\epsilon_2=d\ln\epsilon_1/d\ln a$ を使うと、スローロールパラメータの一次までで

$$
\frac{z''}{z}=\mathcal H^2\left[2-\epsilon_1+\frac32\epsilon_2+O(\epsilon^2)\right],\qquad\frac{a''}{a}=\mathcal H^2(2-\epsilon_1)\tag{84}\label{eq:inflation-84}
$$

です。最低次ではどちらも $2/\eta^2$ に近づくので、曲率摂動の正準モード関数は §8 の $f_k$ で近似でき、squeezing の発達も同じように進みます。曲率の振幅へ戻すときは $z$ で割ります。厳密な de Sitter では $\dot\phi_0=0$、$z=0$ なので、§8 の模型は曲率摂動のスローロール近似の最低次として使えます。

長波長の曲率摂動の演算子は

$$
\hat\zeta_{\mathbf k}(\eta)\simeq\hat C_{1,\mathbf k}+\hat C_{2,\mathbf k}\int^\eta\frac{d\tilde\eta}{z^2(\tilde\eta)}\tag{85}\label{eq:inflation-85}
$$

となり、第二項が減衰する通常のアトラクター背景では $\hat\zeta$ が保存されます。非アトラクター背景では第二項が成長しうるので、$z(\eta)$ から改めて判断します。単一場スローロールと Bunch–Davies 初期条件のもとでは、保存された曲率パワーは最低次で

$$
\mathcal P_\zeta(k)\simeq\left.\frac{\mathcal P_\phi}{2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{k=aH}=\left.\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{k=aH}\tag{86}\label{eq:inflation-86}
$$

です。$\mathcal P_\phi$ は §8 の凍結した値 $(H/2\pi)^2$ で、右辺の背景量は各モードの Hubble crossing で評価します。

### 古典的な確率場による記述

この線形 Gaussian 理論では、同時刻の場どうしは可換なので、配置の確率 $|\Psi_\eta[\zeta]|^2$ から場の配置をサンプルすれば、その時刻の場の相関を再現できます。場と運動量を含む対称順序の相関も、正の Gaussian Wigner 密度から再現できます。ここまでは初期真空でも成り立つ性質です。

squeezing が発達すると、運動量が振幅とほぼ決まった関係を持ち、その後の線形発展の初期条件はモードごとに実効的に一つのランダムな振幅で指定できるようになります。後の宇宙の揺らぎの統計を、古典的な確率場の初期条件から計算できるのはこのためです。

量子状態そのものは、純粋な squeezed state のままです。交換関係 $[\hat Q,\hat P]=i$ も保たれています。また、同じ二点関数を持つ古典的な Gaussian 確率場と純粋な squeezed state は、場の二点関数だけでは見分けられません。「古典的な統計で再現できること」と「量子状態が古典的になること」の区別は [Martin & Vennin](https://arxiv.org/abs/1510.04038) で詳しく論じられています。量子状態そのものを混合状態に変えるのは環境とのもつれ、すなわちデコヒーレンスで、§10 で触れます。

### 時間位相のコヒーレンスと音響ピーク

保存された原始曲率の演算子を $\hat\zeta_{\mathbf k}^{\mathrm{prim}}$ とします。断熱的な成長モードが支配する線形発展では、後の光子・バリオン流体の音響変数 $\hat X$ を、背景の進化と波数で決まる伝達関数 $T_k$ によって

$$
\hat X_{\mathbf k}(\eta)\simeq T_k(\eta)\,\hat\zeta_{\mathbf k}^{\mathrm{prim}},\qquad\hat X_{\mathbf k}'(\eta)\simeq T_k'(\eta)\,\hat\zeta_{\mathbf k}^{\mathrm{prim}}\tag{87}\label{eq:inflation-87}
$$

と表せます。後の空間相関も同じ初期状態で

$$
\langle\hat X(\eta,\mathbf x)\hat X(\eta,\mathbf y)\rangle\simeq\int\frac{d^3k}{(2\pi)^3}\,|T_k(\eta)|^2\,P_\zeta^{\mathrm{prim}}(k)\,e^{i\mathbf k\cdot(\mathbf x-\mathbf y)}\tag{88}\label{eq:inflation-88}
$$

と求まります。成長モードだけを残した近似なので、厳密な正準交換関係の再構成には減衰モードも必要です。

変位 $\hat X$ と速度 $\hat X'$ は、同じ原始振幅に $T_k$ と $T_k'$ を掛けたものです。そのため、原始振幅の値が realization ごとに異なっても、同じ波数の音響振動は零点や極値を取る時刻を共有します。これが**時間位相のコヒーレンス**で、凍結によって減衰成分が抑えられたことの帰結です。空間的な Fourier 位相はランダムなまま、各波数の振動には共通の時間発展が刻まれます。

重力による駆動などを省いた一定音速 $c_s$ の振動子

$$
X_k=A_k\cos(kr_s)+B_k\sin(kr_s),\qquad r_s=c_s(\eta-\eta_i)\tag{89}\label{eq:inflation-89}
$$

で、その効果を見てみます。$r_s$ は初期時刻 $\eta_i$ からの音響距離で、$A_k=X_k(\eta_i)$ が初期変位、$B_k=X_k'(\eta_i)/(kc_s)$ が初速度に対応します。断熱的な成長モードでは長波長の段階ですでに密度の摂動があり、流体を動かす勾配は小さいので、振動子はほぼ静止した状態から動き始めます。つまり $|B_k|\ll|A_k|$ です。

初期の総分散 $\sigma^2$ を等しくした二つの集団を比べます。すべての振動が余弦型で始まるコヒーレントな集団（$\langle A_k^2\rangle=\sigma^2$、$B_k=0$）では

$$
\langle X_k^2\rangle=\sigma^2\cos^2(kr_s)\tag{90}\label{eq:inflation-90}
$$

で、振幅がランダムでも平均パワーに振動が残ります。余弦成分と正弦成分が独立で同じ分散を持つ集団（$\langle A_k^2\rangle=\langle B_k^2\rangle=\sigma^2/2$、$\langle A_kB_k\rangle=0$）では

$$
\langle X_k^2\rangle=\frac{\sigma^2}2\tag{91}\label{eq:inflation-91}
$$

となり、平均するとパワーの振動は消えます。

<iframe src="app/supporting.html?lang=ja&amp;view=acoustic" title="時間位相を共有する場合と共有しない場合の音響振動の統計模型" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

コヒーレントな集団では振動の零点がそろい、平均パワーにも振動が残ります。再結合時の音響距離 $r_s$ を固定して波数 $k$ を変えると、この振動は波数空間の周期的なピーク列になります。

実際の CMB は、重力による駆動、バリオンの慣性、ニュートリノ、拡散減衰、再結合、天球への射影まで含めて計算します。それでも、断熱的な成長モードに由来する摂動が各波数で共通の時間発展に従うことが、角度パワースペクトル $C_\ell$ の音響ピークの起源です。音響ピークが示すのは原始揺らぎの時間位相がそろっていたことで、量子的な起源を判定するには別の情報が要ります。詳しくは [Hu & White](https://arxiv.org/abs/astro-ph/9602019) を参照してください。

## 10. 線形理論の先：相互作用、非 Gaussian 性、粗視化

### モード間の結合と非 Gaussian 性

ここまでは二次作用だけを使ってきました。重力とインフラトンの非線形性を含めると、作用には $\zeta$ の三次以上の項 $S_3,S_4,\dots$ が加わります。単一場スローロールでは、三次の作用の係数はスローロールパラメータの程度に小さくなります（[Maldacena](https://arxiv.org/abs/astro-ph/0210603)）。

これらの項は、運動量の和をゼロに保ちながら異なる波数のモードを結合します。例えば三次の項は $\mathbf k_1+\mathbf k_2+\mathbf k_3=0$ を満たす三つのモードを結び、連続極限で

$$
\langle\hat\zeta_{\mathbf k_1}\hat\zeta_{\mathbf k_2}\hat\zeta_{\mathbf k_3}\rangle=(2\pi)^3\delta^{(3)}(\mathbf k_1+\mathbf k_2+\mathbf k_3)\,B_\zeta(k_1,k_2,k_3)\tag{92}\label{eq:inflation-92}
$$

という三点相関を生成します。平均ゼロの Gaussian 状態では三点関数はゼロなので、$B_\zeta$ は状態の非 Gaussian 性を直接表します。$B_\zeta$ は三つの波数ベクトルが作る三角形の形に依存し、その形が相互作用の種類を反映します。単一場スローロールでは、一つの波数が他の二つより十分小さい極限での $B_\zeta$ が、パワースペクトルの傾き $n_s-1$ で決まります。

量子状態の側から見ると、モード間の結合は §6 の「波数対ごとの積」という構造を崩し、異なる波数の間に相関ともつれを作ります。ある長波長のモードに注目すると、他の短波長のモードは環境として働き、それらについて平均した長波長モードの状態は混合状態になります。これがインフレーション中のデコヒーレンスの一つの機構で、重力の非線形性だけからも生じます（[Nelson](https://arxiv.org/abs/1601.03734)）。squeezing は線形の発展で起こり、デコヒーレンスは相互作用によって起こる、別の段階の現象です。

### in-in 形式（Schwinger–Keldysh 形式）

相互作用があっても、計算したい量は §1 と同じく、初期状態で指定した有限時刻の期待値です。二次の Hamiltonian による発展を相互作用描像の演算子 $\hat\zeta_I$ に含め、残りを $\hat H_{\mathrm{int},I}$ とすると

$$
U_I(\eta,\eta_0)=T\exp\left[-i\int_{\eta_0}^{\eta}d\eta'\,\hat H_{\mathrm{int},I}(\eta')\right],\qquad\langle\hat O(\eta)\rangle=\langle\Psi_0|U_I^\dagger\,\hat O_I(\eta)\,U_I|\Psi_0\rangle\tag{93}\label{eq:inflation-93}
$$

です。$T$ は時間順序で、$\hat O$ は時刻 $\eta$ の場の積です。$\hat H_{\mathrm{int}}$ の一次では

$$
\langle\hat O(\eta)\rangle=i\int_{\eta_0}^{\eta}d\eta'\,\langle\Psi_0|\left[\hat H_{\mathrm{int},I}(\eta'),\hat O_I(\eta)\right]|\Psi_0\rangle\tag{94}\label{eq:inflation-94}
$$

となり、$\hat O$ を三つの場の積にすると三点関数の最低次が得られます。右辺の期待値は、§5 のモード関数 $f_k$ と Bunch–Davies 真空で計算できます。状態を観測時刻まで進めて戻す二本の時間経路としてこの展開を組織するのが **in-in 形式**、あるいは **Schwinger–Keldysh 形式**で、ループ補正や異なる時刻の相関にも同じ方法が使えます（[Weinberg](https://arxiv.org/abs/hep-th/0506236)）。線形理論のモード関数と初期真空が、そのまま摂動計算の出発点になります。

### Stochastic inflation：長波長の有効理論

長波長の揺らぎに相互作用が効く場合、例えばポテンシャルの非線形性が長時間にわたって蓄積する場合には、摂動展開に代わる方法が役立ちます。**Stochastic inflation** は、長波長の場だけを力学変数とし、短波長の自由度の効果を確率的な力として扱う有効理論です。

§8 の場を例にとり、$0<\varepsilon\ll1$ として動く境界 $k_c(\eta)=\varepsilon aH$ を置いて、長波長部分

$$
\hat\phi_<(\eta,\mathbf x)=\int\frac{d^3k}{(2\pi)^3}\,\Theta\bigl(k_c(\eta)-k\bigr)\,\hat\phi_{\mathbf k}(\eta)\,e^{i\mathbf k\cdot\mathbf x}\tag{95}\label{eq:inflation-95}
$$

を定義します。時間とともに境界を越えて長波長側に入るモードは、§9 で見たように強く squeezing され、古典的な確率変数として扱える状態になっています。これらが長波長の場に加わる寄与が、ランダムなノイズになります。軽い場がポテンシャル $V(\phi)$ を持つ準 de Sitter 背景では、粗視化した場は e-fold 数 $N$ について

$$
\frac{d\phi_<}{dN}=-\frac{V'(\phi_<)}{3H^2}+\xi(N),\qquad\langle\xi(N)\xi(N')\rangle=\left(\frac H{2\pi}\right)^2\delta(N-N')\tag{96}\label{eq:inflation-96}
$$

という Langevin 方程式に従います。§8 の質量ゼロの場（$V=0$）では、凍結したスペクトルから粗視化した場の分散が 1 e-fold あたり $(H/2\pi)^2$ ずつ増え、長波長に数えるモードが増え続けることがそのまま分散の成長になります。

対応する Fokker–Planck 方程式を解けば、長波長の場の確率分布を摂動論によらずに求められ、分布の裾のような非 Gaussian な性質も扱えます。ノイズの振幅と時間相関は窓の形、背景、質量で変わり、ホワイトノイズは近似です。また、空間相関を求めるにはノイズの空間相関も必要です。場の量子論から短波長の自由度を積分して導く方法と近似の条件は [Andersen, Eriksson & Tranberg](https://arxiv.org/abs/2111.14503) を参照してください。

## 補足と参考文献

§9 までの具体的な計算は、古典的な一様背景の上の摂動の二次量子論です。初期状態は Bunch–Davies 真空、図の厳密解は de Sitter 上の質量ゼロ・最小結合のスカラー場です。曲率摂動への応用では、スローロールとアトラクターの条件を別に指定しました。有限体積の箱は正則化としてだけ使い、結果は $V\to\infty$ の極限で表しています。§10 は相互作用と粗視化の方法の概観です。メインのアニメーションは短軸の幅が見えるよう $x=0.2$ で止めてあり、その後も楕円は面積を保ったまま細くなり続けます。

- [Baumann, *TASI Lectures on Inflation*](https://arxiv.org/abs/0907.5424)：摂動の作用、正準量子化、原始パワースペクトル。
- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030)：正準変数、保存解と減衰解、準古典的な記述。
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038)：古典的な相関の再現と量子状態の区別。
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019)：原始初期条件と音響ピーク。
- [Maldacena, *Non-Gaussian features of primordial fluctuations in single field inflationary models*](https://arxiv.org/abs/astro-ph/0210603)：三次の作用と単一場の三点関数。
- [Weinberg, *Quantum Contributions to Cosmological Correlations*](https://arxiv.org/abs/hep-th/0506236)：in-in 形式による宇宙論的相関の量子補正。
- [Nelson, *Quantum Decoherence During Inflation from Gravitational Nonlinearities*](https://arxiv.org/abs/1601.03734)：重力の非線形性によるデコヒーレンス。
- [Andersen, Eriksson & Tranberg, *Stochastic inflation from quantum field theory and the parametric dependence of the effective noise amplitude*](https://arxiv.org/abs/2111.14503)：粗視化からの確率的有効理論の導出と近似の条件。
