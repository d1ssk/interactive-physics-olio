---
title: Quantum fluctuations in single-field slow-roll inflation
description: Solve curvature and tensor modes on backgrounds fixed by inflaton potentials, and compare the growth of squeezing, de Sitter and Hankel approximations, and the primordial spectra.
---

# Quantum fluctuations and squeezing in single-field slow-roll inflation

<span class="center-material-tables"></span>

The companion article, [Inflationary Quantum Fluctuations and Squeezing](../inflation-squeezing/), started from the quadratic action for the curvature perturbation $\zeta$ and showed in general that the quantum state of one wavevector pair undergoes two-mode squeezing (or, in standing waves, two single-mode squeezings). Its explicit calculation, however, used a massless scalar field on exact de Sitter spacetime—the model obtained by replacing $z$ with $a$—and applied it to the curvature perturbation as the lowest-order approximation (companion article, §8–9).

This article performs the same calculation on **the actual background determined by an inflaton potential**. We solve the background numerically to obtain $z(\eta)$ and follow curvature modes up to the end of inflation. Symbols and conventions are inherited unchanged from the companion article.

<figure style="margin-inline: auto; text-align: center;">
  <img src="app/teaser.svg" alt="Wigner contours of three modes that cross the Hubble radius 1.5 e-folds apart, drawn on identical axes at the Hubble crossing of the middle mode" width="720" height="250" style="display: block; max-width: 100%; height: auto; margin-inline: auto;">
</figure>

The figure shows, for the Starobinsky model, the states of three wavenumbers that leave the Hubble radius 1.5 e-folds apart, at the moment the middle one crosses (§6). The earlier a mode leaves, the more strongly it is squeezed.

Three things change relative to the companion article:

- The squeezing coefficient $s=z'/z$ no longer equals $\mathcal H$; it becomes $\mathcal H(1+\epsilon_2/2)$.
- $\mathcal H=-1/\eta$ no longer holds, and the decrease in $\ln x$ per e-fold is reduced from 1 in de Sitter to $1-\epsilon_1$.
- The slow-roll parameters evolve, and inflation ends at $\epsilon_1=1$.

As a result, the structure of the companion article—rotation and squeezing of the Wigner ellipse—remains intact, while each rate changes by an amount of order the slow-roll parameters. These small differences appear in observations as the spectral tilt $n_s-1$ and the tensor-to-scalar ratio $r$.

| Symbol | Meaning (shared with the companion article) |
| --- | --- |
| $\eta$, $\mathcal H=a'/a$ | Conformal time and conformal Hubble parameter; primes are $\eta$ derivatives |
| $v=z\zeta$, $\pi=v'-sv$, $s=z'/z$ | Mukhanov–Sasaki variable, its conjugate momentum, and the squeezing coefficient |
| $f_k$, $g_k=f_k'-sf_k$ | Mode functions of a standing component $\hat q,\hat p$ (companion eq. (40)) |
| $Q=\sqrt k\,q$, $P=p/\sqrt k$ | Fixed quadratures; the axes of the Wigner plots |
| $\Sigma$, $r_k$, $\varphi_k$ | Covariance matrix, squeezing parameter, and broad-axis angle |
| $\epsilon_1=-\dot H/H^2$, $\epsilon_2=d\ln\epsilon_1/d\ln a$ | Hubble-flow parameters (companion eqs. (83)–(84)) |

As in the companion article, $\eta$ is conformal time. The slow-roll parameters built from the potential are written $\epsilon_V,\eta_V$ to keep them distinct. Units are $c=\hbar=1$, and $M_{\mathrm{Pl}}$ is the reduced Planck mass.

## 1. Background: a slowly rolling inflaton

### Background equations in e-fold time

A homogeneous inflaton $\phi_0(t)$ has energy density $\rho=\frac12\dot\phi_0^2+V$ and pressure $p=\frac12\dot\phi_0^2-V$. For a flat universe dominated by it, the Friedmann equation and the field equation are

$$
H^2=\frac{1}{3M_{\mathrm{Pl}}^2}\left[\frac12\dot\phi_0^2+V(\phi_0)\right],\qquad\ddot\phi_0+3H\dot\phi_0+V_{,\phi}(\phi_0)=0\tag{1}\label{eq:slowroll-1}
$$

Differentiating the first equation in time gives $6M_{\mathrm{Pl}}^2H\dot H=\dot\phi_0\left(\ddot\phi_0+V_{,\phi}\right)$, and the second equation replaces the bracket with $-3H\dot\phi_0$:

$$
\dot H=-\frac{\dot\phi_0^2}{2M_{\mathrm{Pl}}^2}=-\frac{\rho+p}{2M_{\mathrm{Pl}}^2}\tag{2}\label{eq:slowroll-2}
$$

As long as the field moves, $H$ decreases monotonically.

The first Hubble-flow parameter, also used in companion eq. (83), measures this decrease per Hubble time:

$$
\epsilon_1\equiv-\frac{\dot H}{H^2},\qquad\frac{\ddot a}{a}=\dot H+H^2=H^2(1-\epsilon_1)\tag{3}\label{eq:slowroll-3}
$$

The second relation follows from $\ddot a/a=d(\dot a/a)/dt+(\dot a/a)^2$. **Accelerated expansion $\ddot a>0$ is equivalent to $\epsilon_1<1$**, and exact de Sitter spacetime (constant $H$) is the limit $\epsilon_1=0$. Substituting $\eqref{eq:slowroll-2}$ and the first equation of $\eqref{eq:slowroll-1}$ shows that $\epsilon_1$ is set by the ratio of the field's kinetic energy to its potential:

$$
\epsilon_1=\frac{\dot\phi_0^2}{2M_{\mathrm{Pl}}^2H^2}=\frac{3\cdot\frac12\dot\phi_0^2}{\frac12\dot\phi_0^2+V}\tag{4}\label{eq:slowroll-4}
$$

For $V\ge0$ this gives $0\le\epsilon_1\le3$, and $\epsilon_1<1$ is the same as $\dot\phi_0^2<V$. While the potential greatly exceeds the kinetic energy ($\dot\phi_0^2\ll V$), $\epsilon_1\ll1$ and the accelerated expansion is nearly de Sitter.

For the mode calculation we use the e-fold number $N=\ln a$ as time. Since $dN=H\,dt$, the definition of $\epsilon_1$ reads $\epsilon_1=-d\ln H/dN$, and substituting $\dot\phi_0=H\phi_{0,N}$ into the first form of $\eqref{eq:slowroll-4}$ gives

$$
\epsilon_1=-\frac{d\ln H}{dN}=\frac{\phi_{0,N}^2}{2M_{\mathrm{Pl}}^2}\tag{5}\label{eq:slowroll-5}
$$

where the subscript $N$ denotes an $N$ derivative. Thus $\epsilon_1$ depends only on how far the field moves, in units of $M_{\mathrm{Pl}}$, per e-fold.

We also eliminate $H$ from the equations. Inserting $\dot\phi_0^2=H^2\phi_{0,N}^2=2M_{\mathrm{Pl}}^2H^2\epsilon_1$ into the first equation of $\eqref{eq:slowroll-1}$ gives $3M_{\mathrm{Pl}}^2H^2=M_{\mathrm{Pl}}^2H^2\epsilon_1+V$, i.e. $H^2(3-\epsilon_1)M_{\mathrm{Pl}}^2=V$. Substituting $\ddot\phi_0=H\,d(H\phi_{0,N})/dN=H^2(\phi_{0,NN}-\epsilon_1\phi_{0,N})$ into the second equation and dividing by $H^2$ gives a field equation free of $H$:

$$
H^2=\frac{V}{M_{\mathrm{Pl}}^2(3-\epsilon_1)},\qquad\phi_{0,NN}+(3-\epsilon_1)\left(\phi_{0,N}+M_{\mathrm{Pl}}^2\frac{V_{,\phi}}{V}\right)=0\tag{6}\label{eq:slowroll-6}
$$

Given $\phi_0$ and $\phi_{0,N}$, $\eqref{eq:slowroll-5}$ and the first equation of $\eqref{eq:slowroll-6}$ fix $\epsilon_1$ and $H$ algebraically, so the second equation is a closed second-order ordinary differential equation for $\phi_0(N)$.

Its solution proceeds as follows. High on the slope of the potential, $\dot\phi_0^2\ll V$ and $\epsilon_1\ll1$. As the field approaches the valley, $V$ drops, and both the kinetic fraction and $\epsilon_1$ grow. When $\epsilon_1$ reaches 1, $\ddot a$ in $\eqref{eq:slowroll-3}$ changes sign and the accelerated expansion stops. We therefore **define the end of inflation by $\epsilon_1=1$** and integrate numerically up to that time, $N_{\mathrm{end}}$.

Afterwards the field oscillates about the minimum of the potential and reheating occurs through its interactions with other fields; this article does not treat that stage. All modes of interest leave the Hubble radius before $N_{\mathrm{end}}$. In the single-field case, where entropy perturbations are negligible, the curvature perturbation on scales larger than the Hubble radius remains conserved after inflation, so its value at the end is directly the initial condition for the later universe. The condition $\epsilon_V=1$ used to estimate $\phi_{\mathrm{end}}$ under "Models" below is an approximation; the numerical calculation uses the exact $\epsilon_1=1$.

### Hubble-flow parameters and the slow-roll approximation

The evolution of $\epsilon_1$ is described by the sequence of Hubble-flow parameters

$$
\epsilon_{n+1}=\frac{d\ln\epsilon_n}{dN},\qquad\epsilon_2=\frac{2\phi_{0,NN}}{\phi_{0,N}}\tag{7}\label{eq:slowroll-7}
$$

The second expression is the logarithmic derivative of $\eqref{eq:slowroll-5}$. Both can be computed exactly from the numerical solution.

The slow-roll approximation drops $\phi_{0,NN}$ in $\eqref{eq:slowroll-6}$ and takes $\epsilon_1\ll3$, so $\phi_{0,N}\simeq-M_{\mathrm{Pl}}^2V_{,\phi}/V$. Substituting into $\eqref{eq:slowroll-5}$ and $\eqref{eq:slowroll-7}$ yields parameters fixed by the shape of the potential alone,

$$
\epsilon_1\simeq\epsilon_V\equiv\frac{M_{\mathrm{Pl}}^2}{2}\left(\frac{V_{,\phi}}{V}\right)^2,\qquad\epsilon_2\simeq4\epsilon_V-2\eta_V,\qquad\eta_V\equiv M_{\mathrm{Pl}}^2\frac{V_{,\phi\phi}}{V}\tag{8}\label{eq:slowroll-8}
$$

The second relation follows from $\phi_{0,NN}\simeq-M_{\mathrm{Pl}}^2\left[V_{,\phi\phi}/V-(V_{,\phi}/V)^2\right]\phi_{0,N}$. The number of e-folds remaining until the end of inflation is

$$
N_{\mathrm{end}}-N\simeq\frac{1}{M_{\mathrm{Pl}}^2}\int_{\phi_{\mathrm{end}}}^{\phi_0}\frac{V}{V_{,\phi}}\,d\phi\tag{9}\label{eq:slowroll-9}
$$

Write $N_{\mathrm{cross},*}$ for the time when a reference wavenumber $k_*$ (the pivot) leaves the Hubble radius, and $N_*=N_{\mathrm{end}}-N_{\mathrm{cross},*}$ for the number of e-folds remaining then. The plots use $N-N_{\mathrm{cross},*}$ for elapsed time from that crossing. For the scales observed in the CMB, the reheating and subsequent hot big bang history give $N_*\approx50$–$60$.

For readers using textbooks: Chapter 8 of Matsubara, *Physics of Cosmology* (Vol. 2; see References), for example, writes conformal time as $\tau$ and the potential slow-roll parameters as $\epsilon,\eta$ (our $\epsilon_V,\eta_V$), and uses $m_{\mathrm{Pl}}=G^{-1/2}=\sqrt{8\pi}\,M_{\mathrm{Pl}}$.

### Models

We use three families of potentials. The $\epsilon_1,\epsilon_2$ columns list the leading terms for $\Delta N=N_{\mathrm{end}}-N\gg1$, obtained from $\eqref{eq:slowroll-8}$ and $\eqref{eq:slowroll-9}$. The numerical calculation does not use these approximations; it solves $\eqref{eq:slowroll-6}$ directly.

| Model | $V(\phi)$ | $\epsilon_1$ | $\epsilon_2$ |
| --- | --- | --- | --- |
| Starobinsky | $V_0\left(1-e^{-\sqrt{2/3}\,\phi/M_{\mathrm{Pl}}}\right)^2$ | $\dfrac{3}{4\Delta N^2}$ | $\dfrac{2}{\Delta N}$ |
| Monomial ($p=2/3,\,2,\,4$) | $\lambda\,\phi^p$ | $\dfrac{p}{4\Delta N+p}$ | $\dfrac{4}{4\Delta N+p}$ |
| Power law | $V_0\,e^{-\lambda\phi/M_{\mathrm{Pl}}}$ | $\dfrac{\lambda^2}{2}$ (exact) | $0$ |

For monomials, combine $\epsilon_V=p^2M_{\mathrm{Pl}}^2/(2\phi_0^2)$ and $\eta_V=p(p-1)M_{\mathrm{Pl}}^2/\phi_0^2$ with $\phi_0^2/M_{\mathrm{Pl}}^2\simeq2p\Delta N+p^2/2$ from $\eqref{eq:slowroll-9}$, where $\phi_{\mathrm{end}}^2\simeq p^2M_{\mathrm{Pl}}^2/2$ follows from $\epsilon_V=1$. The cases $p=2,4$ are the textbook large-field (chaotic) inflation. The Starobinsky model is the standard example of a plateau potential, with $\epsilon_1$ much smaller than $\epsilon_2$. Power-law inflation has an exactly constant $\epsilon_1$, so the analytic solution of §4 becomes exact; since inflation never ends in this model alone, we use it as a reference.

The overall amplitude of the potential ($V_0$ or $\lambda$) only changes $H$ and the normalization of the power spectra; it does not affect the evolution of a mode as a function of $x=k/(aH)$. Only when drawing spectra do we normalize the scalar power at the pivot to $2.1\times10^{-9}$.

<iframe src="app/supporting.html?lang=en&amp;view=background" title="Potential and Hubble-flow parameters of the slow-roll background" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 620px; border: 0; overflow: hidden;" loading="eager"></iframe>

Switch potentials and check that $\epsilon_1,\epsilon_2$ stay small for most of inflation and grow quickly in the last few e-folds. The potential estimates $\epsilon_V$ and $4\epsilon_V-2\eta_V$ agree well with the exact values while both are small.

## 2. Hamiltonian flow of the curvature perturbation

### Equations of motion and the squeezing coefficient

From the Hamiltonian of companion eq. (37), the Heisenberg equations for one standing component are

$$
\hat q_{A,\mathbf k}'=\hat p_{A,\mathbf k}+s\,\hat q_{A,\mathbf k},\qquad\hat p_{A,\mathbf k}'=-k^2\hat q_{A,\mathbf k}-s\,\hat p_{A,\mathbf k}\tag{10}\label{eq:slowroll-10}
$$

So far nothing depends on the form of $z(\eta)$. Companion eq. (83), $z^2=2a^2\epsilon_1M_{\mathrm{Pl}}^2$, gives $\ln|z|=\ln a+\frac12\ln\epsilon_1+\text{const}$, so with $d/d\eta=\mathcal H\,d/dN$,

$$
s=\frac{z'}{z}=\mathcal H\,\frac{d\ln|z|}{dN}=\mathcal H\left(1+\frac{\epsilon_2}{2}\right)\tag{11}\label{eq:slowroll-11}
$$

The sign of $z=a\dot\phi_0/H$ follows the direction of $\dot\phi_0$, but it does not appear in $s$. **On a background with $\epsilon_2>0$, the squeezing coefficient exceeds the de Sitter test-field value $\mathcal H$ by the fraction $\epsilon_2/2$.**

### Phase-space flow in e-fold time

Passing to $Q=\sqrt k\,q$ and $P=p/\sqrt k$ and dividing $\eqref{eq:slowroll-10}$ by $\mathcal H$ to obtain $N$ derivatives gives

$$
\frac{d\hat{\mathbf Z}}{dN}=A(N)\,\hat{\mathbf Z},\qquad A=x\begin{pmatrix}0&1\\-1&0\end{pmatrix}+\sigma\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad x=\frac{k}{\mathcal H},\qquad\sigma=\frac{s}{\mathcal H}=1+\frac{\epsilon_2}{2}\tag{12}\label{eq:slowroll-12}
$$

with $\hat{\mathbf Z}=(\hat Q,\hat P)^T$. With $N$ instead of $\eta$ as the time variable, the Hamiltonian generating the evolution $d\hat O/dN=i[\hat K_N,\hat O]$ is $\hat H_{A,\mathbf k}$ of companion eq. (37) divided by $\mathcal H$, $\hat K_N=\hat H_{A,\mathbf k}/\mathcal H$ (because $d\eta=dN/\mathcal H$). In the quadratures,

$$
\hat K_N=\frac x2\left(\hat Q^2+\hat P^2\right)+\frac\sigma2\left(\hat Q\hat P+\hat P\hat Q\right)\tag{13}\label{eq:slowroll-13}
$$

The first term generates the rotation $xJ$ and the second the squeeze $\sigma D$.

From the definition $x=k/(aH)$ and $\eqref{eq:slowroll-5}$, the time dependence of $x$ is

$$
\frac{d\ln x}{dN}=-\frac{d\ln(aH)}{dN}=-(1-\epsilon_1)\tag{14}\label{eq:slowroll-14}
$$

Companion eqs. (76)–(77) are the case $\sigma=1$, $x=e^{-N}$. **On any slow-roll background, the flow has the same form: a rotation $xJ$ plus a squeeze $\sigma D$.** Only two things differ:

1. The squeeze rate is $\sigma=1+\epsilon_2/2$.
2. The rotation rate $x$ decreases more slowly, with a logarithmic decrease of $1-\epsilon_1$ per e-fold.

The eigenvalues of $A$ are $\pm\sqrt{\sigma^2-x^2}$: the flow is elliptic (rotation) for $x>\sigma$ and hyperbolic (stretching and contraction) for $x<\sigma$.

Tensor perturbations share this structure. Expanding each polarization with polarization tensors normalized as $e^{(\lambda)}_{ij}e^{(\lambda')}_{ij}=\delta_{\lambda\lambda'}$, the canonical variable is $v_T=(aM_{\mathrm{Pl}}/2)\,h_\lambda$, and $z_T=aM_{\mathrm{Pl}}/2$ is proportional to $a$. Hence **tensors have exactly $\sigma_T=1$**: the test-field flow of the companion article is precisely the tensor flow. On a slow-roll background only the decrease of $x$ in $\eqref{eq:slowroll-14}$ changes.

### The second-order equation: gradient term against background term

Eliminating $\hat p$ from $\eqref{eq:slowroll-10}$ returns companion eq. (39), $\hat q''+(k^2-z''/z)\hat q=0$. Using $z''/z=s'+s^2$, $\mathcal H'=\mathcal H^2(1-\epsilon_1)$, and $d\sigma/dN=\epsilon_2\epsilon_3/2$, we get $z''/z=\mathcal H^2\left[(1-\epsilon_1)\sigma+\sigma^2+\epsilon_2\epsilon_3/2\right]$; substituting $\sigma=1+\epsilon_2/2$ and expanding gives, with no approximation,

$$
\frac{z''}{z}=\mathcal H^2\left[2-\epsilon_1+\frac32\epsilon_2-\frac12\epsilon_1\epsilon_2+\frac14\epsilon_2^2+\frac12\epsilon_2\epsilon_3\right],\qquad\frac{a''}{a}=\mathcal H^2(2-\epsilon_1)\tag{15}\label{eq:slowroll-15}
$$

To first order this agrees with companion eq. (84). The term $a''/a$ is the background term for tensor perturbations.

In the second-order equation, the solution turns from oscillatory to growing and decaying when the gradient term $k^2$ drops below the background term $z''/z$, at $x^2\simeq2$. In the first-order flow $\eqref{eq:slowroll-12}$ the boundary is $x=\sigma\simeq1$. Both "boundaries" are markers of the same smooth evolution written in different forms; nothing special happens at either time.

<iframe src="app/supporting.html?lang=en&amp;view=frequencies" title="Gradient and background terms, and rotation and squeeze rates, for three wavenumbers" data-auto-height scrolling="no" style="display: block; width: 100%; height: 980px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

In the left plot the three $x_j^2$ cross $z''/(z\mathcal H^2)\simeq2$ in turn. The right plot shows the same thing as a comparison of $x_j$ with $\sigma$. Choose a small $N_*$ to look near the end of inflation, where the background terms move away from 2 and 1.

## 3. The Bunch–Davies state and numerical solution

### Dimensionless mode coefficients

Companion eq. (40) expanded the operators of a standing component with in operators as $\hat q=f_k\hat b^{\mathrm{in}}+f_k^*\hat b^{\mathrm{in}\dagger}$ and $\hat p=g_k\hat b^{\mathrm{in}}+g_k^*\hat b^{\mathrm{in}\dagger}$. Matching the quadratures, define the dimensionless coefficients

$$
F_k=\sqrt k\,f_k,\qquad G_k=\frac{g_k}{\sqrt k},\qquad\hat Q=F_k\hat b^{\mathrm{in}}+F_k^*\hat b^{\mathrm{in}\dagger},\qquad\hat P=G_k\hat b^{\mathrm{in}}+G_k^*\hat b^{\mathrm{in}\dagger}\tag{16}\label{eq:slowroll-16}
$$

Because $\eqref{eq:slowroll-12}$ is linear, $(F_k,G_k)^T$ obeys the same equation $d(F_k,G_k)^T/dN=A\,(F_k,G_k)^T$. The Wronskian condition (companion eq. (41)) is

$$
F_kG_k^*-F_k^*G_k=i\tag{17}\label{eq:slowroll-17}
$$

and it is preserved in time because $\operatorname{tr}A=0$: substituting $\eqref{eq:slowroll-12}$, the $x$ and $\sigma$ terms cancel separately.

All quantities of companion §5–7 can be written with $F_k,G_k$:

$$
\Sigma=\begin{pmatrix}|F_k|^2&\operatorname{Re}(F_kG_k^*)\\\operatorname{Re}(F_kG_k^*)&|G_k|^2\end{pmatrix},\qquad\alpha_k=\frac{F_k+iG_k}{\sqrt2},\qquad\beta_k=\frac{F_k^*+iG_k^*}{\sqrt2}\tag{18}\label{eq:slowroll-18}
$$

$\det\Sigma=1/4$ follows from $\eqref{eq:slowroll-17}$, and $r_k=\operatorname{arsinh}|\beta_k|$ and $\varphi_k=\frac12\arg(\alpha_k\beta_k)$ are as in companion eqs. (49) and (62).

### The curvature power spectrum

Inserting $z^2=2a^2\epsilon_1M_{\mathrm{Pl}}^2$ and $k/a=xH$ into companion eq. (46), $P_\zeta=|f_k|^2/z^2$, the dimensionless power spectrum is

$$
\mathcal P_\zeta(k,N)=\frac{k^3}{2\pi^2}\frac{|F_k|^2}{k\,z^2}=\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\cdot2x^2|F_k|^2\tag{19}\label{eq:slowroll-19}
$$

For the de Sitter test field $2x^2|F_k|^2=1+x^2$, so this factor plays the role of $1+x^2$ in companion eq. (75). On a slow-roll background both $2x^2|F_k|^2$ and $H^2/\epsilon_1$ change in time, but their product becomes constant after the mode leaves the Hubble radius (§5).

### Initial conditions and numerical integration

At short wavelengths, $x\gg\sigma$, the rotation in $\eqref{eq:slowroll-12}$ dominates, and as in companion eq. (43) the Bunch–Davies condition is $F_k\to e^{-ik\eta}/\sqrt2$, $G_k\to-ie^{-ik\eta}/\sqrt2$. A global phase affects no physical quantity, so $\eta$ itself is never needed. Numerically we integrate the background $\eqref{eq:slowroll-6}$ together with $\eqref{eq:slowroll-12}$ in $N$, starting at the time when $x=100$. The initial values are the Hankel-function solution of §4 evaluated with the parameters at that time. That solution reproduces the Bunch–Davies state including its $1/x$ corrections, so the initial error is of order the rate of change of the slow-roll parameters times $1/x$.

The phase convention follows the companion article: the global phase is chosen so that the late-time conserved component of $\zeta_k$ is positive imaginary (companion eq. (74)).

## 4. Constant slow-roll approximation: the Hankel-function solution

### Conformal time and the index $\nu$

Locally freezing the slow-roll parameters makes the mode equation analytically solvable. This is an approximation near crossing: an exactly constant $\epsilon_1$ would require $\epsilon_2=0$. Since $\mathcal H'=\mathcal H^2(1-\epsilon_1)$ can be written $d(1/\mathcal H)/d\eta=-(1-\epsilon_1)$, freezing $\epsilon_1$ and choosing the integration constant so that $\eta\to0$ in the infinite future gives

$$
\eta=-\frac{1}{(1-\epsilon_1)\mathcal H}\tag{20}\label{eq:slowroll-20}
$$

Combining this with the first-order terms of $\eqref{eq:slowroll-15}$,

$$
\frac{z''}{z}=\frac{\nu^2-1/4}{\eta^2},\qquad\nu^2=\frac14+\frac{2-\epsilon_1+\frac32\epsilon_2}{(1-\epsilon_1)^2}\simeq\frac94+3\epsilon_1+\frac32\epsilon_2,\qquad\nu\simeq\frac32+\epsilon_1+\frac{\epsilon_2}{2}\tag{21}\label{eq:slowroll-21}
$$

With $\eqref{eq:slowroll-8}$ this is $\nu\simeq3/2+3\epsilon_V-\eta_V$. For tensors, $a''/a$ gives $\nu_T\simeq3/2+\epsilon_1$. In power-law inflation $\epsilon_2=0$ and $\nu=3/2+\epsilon_1/(1-\epsilon_1)$ holds exactly.

### The Hankel-function solution

With $y=-k\eta$ and $f_k=\sqrt{-\eta}\,\mathcal C_\nu(y)$, the mode equation $f_k''+\left[k^2-(\nu^2-1/4)/\eta^2\right]f_k=0$ becomes Bessel's equation of order $\nu$. Choosing the solution that satisfies the Bunch–Davies condition as $y\to\infty$,

$$
F_k=\frac{\sqrt\pi}{2}e^{i\pi(\nu+1/2)/2}\sqrt y\,H^{(1)}_\nu(y),\qquad G_k=-\frac{\sqrt\pi}{2}e^{i\pi(\nu+1/2)/2}\sqrt y\,H^{(1)}_{\nu-1}(y),\qquad y=-k\eta=\frac{x}{1-\epsilon_1}\tag{22}\label{eq:slowroll-22}
$$

The last equality uses $\eqref{eq:slowroll-20}$. $G_k$ is obtained as follows. In this approximation $z\propto(-\eta)^{1/2-\nu}$, so $s=(\nu-\tfrac12)/(-\eta)$, and with $d/d\eta=-k\,d/dy$,

$$
G_k=\frac{f_k'-sf_k}{\sqrt k}=-\frac{dF_k}{dy}-\frac{\nu-1/2}{y}F_k=-\frac{\sqrt\pi}{2}e^{i\pi(\nu+1/2)/2}\sqrt y\left[\frac{dH^{(1)}_\nu}{dy}+\frac\nu yH^{(1)}_\nu\right]\tag{23}\label{eq:slowroll-23}
$$

which takes the form of $\eqref{eq:slowroll-22}$ by the recurrence $dH_\nu/dy+(\nu/y)H_\nu=H_{\nu-1}$.

A few checks:

- **Bunch–Davies condition:** inserting $H^{(1)}_\nu(y)\to\sqrt{2/(\pi y)}\,e^{i(y-\pi\nu/2-\pi/4)}$ gives $F_k\to e^{iy}/\sqrt2$ and $G_k\to-ie^{iy}/\sqrt2$. Since $e^{iy}=e^{-ik\eta}$, this matches the condition of §3.
- **Wronskian:** $H^{(1)}_\nu H^{(2)}_{\nu-1}-H^{(2)}_\nu H^{(1)}_{\nu-1}=-4i/(\pi y)$ implies $\eqref{eq:slowroll-17}$.
- **de Sitter limit:** for $\nu=3/2$, $H^{(1)}_{3/2}(y)=-\sqrt{2/(\pi y)}\,(1+i/y)\,e^{iy}$ and $H^{(1)}_{1/2}(y)=-i\sqrt{2/(\pi y)}\,e^{iy}$, recovering $F_k=(1+i/x)e^{ix}/\sqrt2$ and $G_k=-ie^{ix}/\sqrt2$ of companion eq. (69).

### Long-wavelength behavior and the spectrum

As $y\to0$, $H^{(1)}_\nu(y)\simeq-(i/\pi)\,\Gamma(\nu)\,(2/y)^\nu$, so $|F_k|^2\simeq\Gamma(\nu)^2\,2^{2\nu-2}\,y^{1-2\nu}/\pi$. Inserting this into $\eqref{eq:slowroll-19}$ with $x=(1-\epsilon_1)y$ and $\Gamma(3/2)^2=\pi/4$ gives

$$
\mathcal P_\zeta\simeq\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\,(1-\epsilon_1)^2\left[\frac{2^{\nu-3/2}\,\Gamma(\nu)}{\Gamma(3/2)}\right]^2(-k\eta)^{3-2\nu}\tag{24}\label{eq:slowroll-24}
$$

Within this approximation the right-hand side is time independent, so we evaluate it at $k=aH$, i.e. $-k\eta=1/(1-\epsilon_1)$. Expanding to first order in $\delta=\nu-3/2=\epsilon_1+\epsilon_2/2$ with $2^{\nu-3/2}\simeq1+\delta\ln2$, $\Gamma(\nu)/\Gamma(3/2)\simeq1+\delta\,\psi(3/2)$, $\psi(3/2)=2-\gamma_{\mathrm E}-2\ln2$, and $(1-\epsilon_1)^{2\nu-1}\simeq1-2\epsilon_1$, where $\psi$ is the digamma function, we obtain

$$
\mathcal P_\zeta(k)\simeq\left.\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{k=aH}\left[1-2(C+1)\epsilon_1-C\epsilon_2\right],\qquad C=\gamma_{\mathrm E}+\ln2-2\simeq-0.7296\tag{25}\label{eq:slowroll-25}
$$

where $\gamma_{\mathrm E}$ is the Euler–Mascheroni constant. The bracket is the next-order (Stewart–Lyth) correction.

Because the background quantities are evaluated at $k=aH$, the spectrum depends on $k$ through the crossing time. Let $N_k$ be the Hubble crossing time of wavenumber $k$. Then $k=a(N_k)H(N_k)$, so $\eqref{eq:slowroll-5}$ gives

$$
\frac{d\ln k}{dN_k}=1+\frac{d\ln H}{dN_k}=1-\epsilon_1,\qquad
\frac{d}{d\ln k}=\frac{1}{1-\epsilon_1}\frac{d}{dN_k}.
$$

The lowest-order power spectrum is

$$
\mathcal P_\zeta(k)\simeq\left.\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{N=N_k}
$$

Taking its logarithmic derivative and using $d\ln H/dN=-\epsilon_1$ and $d\ln\epsilon_1/dN=\epsilon_2$ from $\eqref{eq:slowroll-7}$,

$$
\begin{aligned}
\frac{d\ln\mathcal P_\zeta}{d\ln k}
&=\frac{1}{1-\epsilon_1}\left(2\frac{d\ln H}{dN_k}-\frac{d\ln\epsilon_1}{dN_k}\right)+O(\epsilon^2)\\
&=\frac{-2\epsilon_1-\epsilon_2}{1-\epsilon_1}+O(\epsilon^2)\\
&=-2\epsilon_1-\epsilon_2+O(\epsilon^2).
\end{aligned}
$$

All background quantities here are evaluated at $N=N_k$, and $O(\epsilon^2)$ denotes terms of second or higher order in the slow-roll parameters. Since the numerator is already first order, the correction from $1/(1-\epsilon_1)$ starts at second order. Also, $d\epsilon_1/dN=\epsilon_1\epsilon_2$ and $d\epsilon_2/dN=\epsilon_2\epsilon_3$, so differentiating the amplitude correction in $\eqref{eq:slowroll-25}$ contributes only at second order. Finally, using $\nu\simeq3/2+\epsilon_1+\epsilon_2/2$ from $\eqref{eq:slowroll-21}$,

$$
n_s-1\equiv\frac{d\ln\mathcal P_\zeta}{d\ln k}\simeq-2\epsilon_1-\epsilon_2\simeq3-2\nu\tag{26}\label{eq:slowroll-26}
$$

For tensors, replacing $\nu$ with $\nu_T$ and $z$ in $\eqref{eq:slowroll-19}$ with $z_T$, and summing over both polarizations,

$$
\mathcal P_T(k)\simeq\left.\frac{2H^2}{\pi^2M_{\mathrm{Pl}}^2}\right|_{k=aH}\left[1-2(C+1)\epsilon_1\right],\qquad n_T\simeq-2\epsilon_1,\qquad r\equiv\frac{\mathcal P_T}{\mathcal P_\zeta}\simeq16\epsilon_1=-8n_T\tag{27}\label{eq:slowroll-27}
$$

The last relation is the single-field slow-roll consistency relation.

## 5. Mode functions: numerical and approximate solutions

### Growing and decaying solutions at long wavelengths

At zeroth order in a long-wavelength expansion, $\eqref{eq:slowroll-12}$ decouples into $dQ/dN=\sigma Q$ and $dP/dN=-\sigma P$. Since $\sigma=d\ln|z|/dN$, the growing field component and the independent decaying momentum component obey

$$
Q_{\mathrm{grow}}\propto z,\qquad P_{\mathrm{dec}}\propto\frac1z\qquad(x\to0)\tag{28}\label{eq:slowroll-28}
$$

The first keeps $\zeta=v/z$ constant: **the curvature perturbation is conserved**. The independent decaying component satisfies $\pi=z\zeta'\propto1/z$, hence $\zeta'\propto1/z^2$; it gives the term $\int d\eta/z^2$ in companion eq. (85). This does not mean that the full momentum decays as $1/z$. For finite $k$, the growing solution also sources momentum through $-xQ$.
<!-- Retaining the leading gradient correction and locally freezing the flow parameters gives $P_{\mathrm{grow}}\simeq-xQ_{\mathrm{grow}}/(1+\epsilon_1+\epsilon_2)$. Although $x\ll1$, $Q_{\mathrm{grow}}$ is large, so this source need not be negligible in the momentum equation. In the de Sitter test-field limit, for example, the BD mode has $|G_k|=1/\sqrt2$ even at late times. -->

For the de Sitter test field of the companion article, $z\to a$ and the canonical variable grew in proportion to $a$. On a slow-roll background $|F_k|\propto z=a\sqrt{2\epsilon_1}M_{\mathrm{Pl}}$, which grows faster than in de Sitter as $\epsilon_1$ increases. The ratio to the de Sitter solution at the same $x$, $|F_{\mathrm{dS}}|\simeq1/(\sqrt2\,x)$, is proportional to $x\,z\propto\sqrt{\epsilon_1}/H$, and it slowly departs from 1 after crossing.

The frozen magnitude of $\zeta_k=F_k/(\sqrt k\,z)$, on the other hand, is proportional to $H_k/\sqrt{\epsilon_{1,k}}$, fixed near crossing. Its slight variation from one wavenumber to another through the crossing time is the spectral tilt of $\eqref{eq:slowroll-26}$.

The plots compare the numerical solution with the Hankel approximation and the de Sitter solution. Look for agreement near crossing and the drift that develops afterwards ([details of the Hankel reference](#hankel-reference)).

<iframe src="app/supporting.html?lang=en&amp;view=modes" title="Numerical pivot mode compared with the Hankel approximation and the de Sitter test field" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 620px; border: 0; overflow: hidden;" loading="eager"></iframe>

Switch displays and check the following:

- **Canonical variable:** before crossing the three curves nearly coincide; afterwards the numerical and Hankel solutions slowly separate from de Sitter.
- **Curvature perturbation:** after crossing, the imaginary (conserved) part of $\zeta_k$ stays constant to the end of inflation while the real (decaying) part dies away.
- **Ratio:** the Hankel reference agrees well near crossing, but the drift can accumulate over many e-folds and grow strongly near the end. For Starobinsky with $N_*=55$, $|F|/|F_\nu|$ is about $1.004$ at 5 e-folds after crossing, $1.15$ at 25 e-folds, and $51.3$ at the end. A large $N_*$ does not make the constant-$\nu$ approximation valid for the entire history. Selecting $N_*=5$ shows the departure over a shorter interval.

## 6. Squeezing of three wavenumbers

### Late-time squeezing and the growth of $z$

For $x\ll1$ the broad axis points nearly along $Q$ ($\varphi_k\to0$), and $\Sigma_{QQ}=|F_k|^2\simeq\frac12e^{2r_k}$. Combined with $\eqref{eq:slowroll-19}$,

$$
e^{2r_k}\simeq2|F_k|^2=\frac{4\pi^2z^2}{k^2}\,\mathcal P_\zeta(k)\qquad(x\ll1)\tag{29}\label{eq:slowroll-29}
$$

The frozen $\mathcal P_\zeta(k)$ is constant, so up to a constant $r_k$ grows with $\ln z$, at a rate approaching $\sigma=1+\epsilon_2/2$ per e-fold. Inserting the lowest-order $\mathcal P_\zeta\simeq H_k^2/(8\pi^2\epsilon_{1,k}M_{\mathrm{Pl}}^2)$ (subscript $k$ denotes the value at crossing) and $k=a_kH_k$,

$$
r_k\simeq\ln\frac{z}{z_k}=\ln\frac{a}{a_k}+\frac12\ln\frac{\epsilon_1}{\epsilon_{1,k}}\tag{30}\label{eq:slowroll-30}
$$

For the de Sitter test field the second term is absent, and we recover $r_k\simeq N$ of the companion article.

At the end of inflation ($\epsilon_1=1$), this formula estimates for the $N_*=55$ pivot mode $r_{k_*}\simeq55+\frac12\ln\!\left[1/(2.3\times10^{-4})\right]\simeq59.2$ in the Starobinsky model and $57.3$ in the $\phi^2$ model, in good agreement with the numerical values (59.21 and 57.35). That is an extremely thin ellipse, $e^{-2r_k}\sim10^{-51}$.

### Animation

We choose three wavenumbers $k_1<k_2=k_*<k_3$ whose Hubble crossings are 1.5 e-folds apart. The time axis is $N-N_{\mathrm{cross},*}$, with the crossing of $k_*$ at 0.

<span id="main-animation"></span>

<iframe src="app/index.html?lang=en" title="Animation of three Wigner ellipses squeezing in turn, with the gradient and background terms and the squeezing magnitudes over time" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1900px; min-height: 1000px; border: 0; overflow: hidden;" loading="eager"></iframe>

Notice the following:

1. **Order:** in the order in which $x_j^2$ drops below the background term in the upper strip, the ellipses stop rotating and begin to stretch. The three states undergo the same deformation, shifted in time.
2. **Difference from de Sitter:** for $N_*=55$ the dashed curves (the de Sitter test field at the same $x$) are almost indistinguishable. Choose $N_*=5$, or power law with $\epsilon_1=0.3$, and the ellipse is squeezed more strongly at the same $x$; in the lower strip the solid curves separate from the dashed ones.
3. **Area:** at every time the ellipse has the area of the vacuum circle ($\det\Sigma=1/4$).

Compared at the same $x$, the stronger squeezing in power-law inflation comes from the growth rate per unit $\ln(1/x)$, $\sigma/(1-\epsilon_1)\simeq\nu-\frac12$, exceeding 1. It is the same number $\nu$ that sets the spectral tilt in $\eqref{eq:slowroll-26}$.

## 7. Primordial spectra and tensors

For about forty wavenumbers we followed the modes numerically from deep inside the Hubble radius to the end of inflation and computed $\mathcal P_\zeta$ and $\mathcal P_T$ there.

<iframe src="app/supporting.html?lang=en&amp;view=spectrum" title="Scalar and tensor power spectra at the end of inflation, with the spectral index and tensor-to-scalar ratio" data-auto-height scrolling="no" style="display: block; width: 100%; height: 950px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

The shaded band marks an illustrative range of primary-CMB scales, $10^{-4}\lesssim k\lesssim0.2\,\mathrm{Mpc}^{-1}$. We identify the pivot with $k_*=0.05\,\mathrm{Mpc}^{-1}$, the convention used by [Planck 2018](https://arxiv.org/html/1807.06211v2#S2), so the band spans $-6.21\lesssim\ln(k/k_*)\lesssim1.39$. In multipole space, this corresponds roughly to $\ell\simeq2\text{–}3000$.

Select **Relative error near pivot** or **Relative error: full range** in the left plot to show $\mathcal P_{\mathrm{num}}/\mathcal P_{\mathrm{approx}}-1$ for the leading and next-order formulas. Zero means agreement; positive values mean the approximation underestimates the power. Compare the improvement near the pivot with the departure near the end. The last modes also retain finite-wavelength evolution, so their residuals do not measure slow-roll truncation error alone.

The values at $N_*=55$ are listed below. Parentheses give the first-order formulas $\eqref{eq:slowroll-26}$–$\eqref{eq:slowroll-27}$ evaluated with $\epsilon_1,\epsilon_2$ at crossing.

| Model | $\epsilon_1$ | $\epsilon_2$ | $n_s$ | $r$ |
| --- | --- | --- | --- | --- |
| Starobinsky | $2.3\times10^{-4}$ | $0.0351$ | $0.9649$ ($0.9644$) | $0.00355$ ($0.00364$) |
| $\phi^{2/3}$ | $0.00306$ | $0.0183$ | $0.9757$ ($0.9756$) | $0.0483$ ($0.0490$) |
| $\phi^2$ | $0.00912$ | $0.0182$ | $0.9634$ ($0.9636$) | $0.144$ ($0.146$) |
| $\phi^4$ | $0.0181$ | $0.0180$ | $0.9449$ ($0.9458$) | $0.285$ ($0.289$) |

The differences between the numerical results and the first-order formulas are of second order in the slow-roll parameters. Including the next-order correction of $\eqref{eq:slowroll-25}$ (the dotted curves) brings the power amplitudes into agreement to better than $10^{-3}$. For comparison, Planck 2018 gives $n_s=0.9649\pm0.0042$, and the BICEP/Keck data through 2018 give $r<0.036$ (95%); of the models in this table only Starobinsky is consistent with both. The value of $N_*$ depends on the reheating history, so the tabulated values carry the corresponding uncertainty.

Some further features:

- **Tensors are squeezed too:** with $\sigma_T=1$, $r_k$ for each tensor polarization grows with $\ln(a/a_k)$. Compared with $\eqref{eq:slowroll-30}$, the difference from the scalar is $\frac12\ln(\epsilon_1/\epsilon_{1,k})$.
- **Consistency relation:** the difference between the numerical $n_T$ and $-r/8$ is also of second order.
- **Modes exiting near the end:** for modes that leave in the last few e-folds, $\epsilon_1,\epsilon_2$ are large and the slow-roll formulas fail. Modes that leave in the last two e-folds are not yet frozen at the end, so their values only describe the amplitude at that time.
- **Power law:** $\eqref{eq:slowroll-22}$ is exact, and $n_s-1=-2\epsilon_1/(1-\epsilon_1)$ and $r=16\epsilon_1$ hold exactly. Increasing $\epsilon_1$ makes the difference from the first-order formulas clearly visible.

## 8. Conventions and limitations

- Units are $c=\hbar=1$, and $M_{\mathrm{Pl}}$ is the reduced Planck mass. The sign convention of the curvature perturbation follows companion eq. (2); two-point functions do not depend on it.
- The background starts early enough on the slow-roll attractor $\phi_{0,N}=-M_{\mathrm{Pl}}^2V_{,\phi}/V$ for initial transients to die out, and is integrated until $\epsilon_1=1$. Reheating and the subsequent evolution of the perturbations are not treated.
- Modes are integrated from $x=100$ (for spectra, $x=50$), starting from $\eqref{eq:slowroll-22}$ evaluated with the local parameters. Because power-law inflation does not end, its values are taken at least 12 e-folds after crossing.
- The animation runs from the time when the first mode has $x_1=8$ until the last mode reaches $x_3=0.15$. The panels show the fixed quadrature range $|Q|,|P|\le4.4$; longer ellipses extend beyond it.
- The treatment is the linear quantum theory of the quadratic action. Non-Gaussianity from interactions, loop corrections, and decoherence go no further than the overview in companion §10. With a single field there are no isocurvature perturbations.

<span id="hankel-reference"></span>

### Definition of the Hankel reference

The dotted Hankel curve is a **local reference evaluated at the same $x$**, distinct from the first-order formula $\nu\simeq3/2+\epsilon_1+\epsilon_2/2$. At crossing we freeze the full dimensionless background term $B_*=\left.z''/(z\mathcal H^2)\right|_{N_{\mathrm{cross},*}}$ from $\eqref{eq:slowroll-15}$, including its higher-order terms, and set $\nu_{\mathrm{ref}}=\sqrt{1/4+B_* /(1-\epsilon_{1,*})^2}$. We evaluate $\eqref{eq:slowroll-22}$ with this fixed index and $y_{\mathrm{ref}}(N)=x(N)/(1-\epsilon_{1,*})$, using $x(N)$ from the numerical background.

This is not a second background evolved with constant parameters; $y_{\mathrm{ref}}$ is not the exact $-k\eta$ of the evolving background. Keeping terms beyond first order in $B_*$ does not make this a systematically higher-order solution. The reference becomes exact for power-law inflation.

The numerical modes themselves evolve with the changing background; their initial data use the same local prescription at the starting time rather than at crossing.

## References

- T. Matsubara, *Physics of Cosmology* (Vol. 2, in Japanese), University of Tokyo Press (2014), Chapter 8: slow-roll inflation, Hankel-function mode functions, spectral indices, and gravitational waves.
- [Baumann, *TASI Lectures on Inflation*](https://arxiv.org/abs/0907.5424): the Mukhanov–Sasaki equation, slow-roll approximation, and observables.
- [Stewart & Lyth, *A more accurate analytic calculation of the spectrum of cosmological perturbations produced during inflation*](https://arxiv.org/abs/gr-qc/9302019): the next-order correction and the constant $C$.
- [Schwarz, Terrero-Escalante & García, *Higher order corrections to primordial spectra from cosmological inflation*](https://arxiv.org/abs/astro-ph/0106020): expansion in Hubble-flow parameters.
- [Martin, Ringeval & Vennin, *Encyclopædia Inflationaris*](https://arxiv.org/abs/1303.3787): predictions of many single-field models compared.
- [Planck Collaboration, *Planck 2018 results. X. Constraints on inflation*](https://arxiv.org/abs/1807.06211): constraints on $n_s$ and $r$.
- [BICEP/Keck Collaboration, *Improved constraints on primordial gravitational waves using Planck, WMAP, and BICEP/Keck observations through the 2018 observing season*](https://arxiv.org/abs/2110.00483): upper limit on the tensor-to-scalar ratio.
