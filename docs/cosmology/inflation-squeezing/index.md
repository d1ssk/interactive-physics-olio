# Inflationary Quantum Fluctuations and Squeezing

## 1. From vacuum fluctuations to cosmic structure

The present universe contains fluctuations on many scales, visible in the distribution of galaxies and galaxy clusters and in the temperature and polarization anisotropies of the CMB. Their origins can be traced to tiny primordial fluctuations in the early universe. Inflationary theory attributes these primordial fluctuations to the vacuum fluctuations of quantum fields.

During inflation, each Fourier mode of a quantum field evolves as the universe expands. In phase space, the vacuum's initially almost circular Wigner distribution gradually becomes a long, thin ellipse. This **squeezing** establishes strong correlations between the field amplitude and its momentum, with a single growing mode becoming dominant. This is central to understanding how primordial fluctuations come to admit a description as a classical stochastic field.

We begin with a time-dependent harmonic oscillator, then examine Bogoliubov transformations of creation and annihilation operators and the deformation of the Wigner function. Finally, we consider how superhorizon growing-mode dominance connects to the temporal phase coherence seen in the CMB acoustic peaks.

<figure style="margin-inline: auto; text-align: center;">
  <img src="app/teaser.svg" alt="Wigner contours at three times on common quadrature axes" width="720" height="250" style="display: block; max-width: 100%; height: auto; margin-inline: auto;">
</figure>

The figure shows Wigner-function contours for one real standing-wave mode at three times in the same phase space. The horizontal and vertical axes are quadratures defined from the field amplitude and canonical momentum. Below, we follow the emergence of stretching and contracting directions through the equations.

The [main animation](#main-animation) shows this deformation continuously.

## 2. Preliminaries: a time-dependent harmonic oscillator

Consider a time-dependent harmonic oscillator of unit mass,

$$
H(t)=\frac12\left[p^2+\Omega^2(t)q^2\right]
$$

where $\Omega^2(t)$ is the time-dependent effective squared frequency and need not be positive. Throughout, we use $\hbar=1$ and $[q,p]=i$.

### Schrödinger picture: an evolving state on fixed axes

We first work in the Schrödinger picture. The operators $q,p$ are time independent, while the quantum state $|\psi(t)\rangle$ evolves.

Choose a fixed positive reference frequency $\omega_0$ and define

$$
b=
\frac{1}{\sqrt2}
\left(
\sqrt{\omega_0}q
+\frac{ip}{\sqrt{\omega_0}}
\right)
$$

with the corresponding dimensionless quadratures

$$
Q=\frac{b+b^\dagger}{\sqrt2}
=\sqrt{\omega_0}q,
\qquad
P=\frac{b-b^\dagger}{i\sqrt2}
=\frac{p}{\sqrt{\omega_0}}
$$

Since $\omega_0$ is fixed, $Q,P$ define phase-space axes that do not move with time.

In these coordinates, the Hamiltonian is

$$
H(t)
=
\frac{\omega_0}{2}P^2
+
\frac{\Omega^2(t)}{2\omega_0}Q^2
$$

In terms of $b,b^\dagger$, the same Hamiltonian becomes

$$
H(t)=
\frac{\omega_0^2+\Omega^2(t)}{2\omega_0}
\left(b^\dagger b+\frac12\right)
+
\frac{\Omega^2(t)-\omega_0^2}{4\omega_0}
\left(b^2+b^{\dagger2}\right)
$$

For $\Omega^2(t)=\omega_0^2$, we have

$$
H=\frac{\omega_0}{2}(Q^2+P^2)=\omega_0\left(b^\dagger b+\frac12\right)
$$

A number state then evolves as

$$
|n\rangle
\longrightarrow
e^{-i(n+1/2)\omega_0t}|n\rangle
$$

so, apart from a common phase, the relative phase of each component advances as $e^{-in\omega_0t}$.

For example, a coherent state

$$
|\alpha\rangle
=
e^{-|\alpha|^2/2}
\sum_{n=0}^\infty
\frac{\alpha^n}{\sqrt{n!}}|n\rangle
$$

evolves, up to an overall phase, as

$$
|\alpha\rangle
\longrightarrow
|\alpha e^{-i\omega_0t}\rangle
$$

Thus,

$$
\alpha(t)=e^{-i\omega_0t}\alpha(0)
$$

For the center of a coherent state,

$$
\alpha
=
\frac{\langle Q\rangle+i\langle P\rangle}{\sqrt2}
$$

This corresponds to rotation at a constant radius in the fixed $Q,P$ plane. More generally, when $\Omega^2=\omega_0^2$, the entire Wigner function of any state rotates without changing shape.

When $\Omega^2(t)\neq\omega_0^2$, however, the coefficients of $Q^2$ and $P^2$ differ. The two phase-space directions are affected differently, deforming the distribution in addition to rotating it.

In terms of $b,b^\dagger$, this effect is carried by the term

$$
b^2+b^{\dagger2}
$$

Indeed,

$$
b^2|n\rangle\propto|n-2\rangle,
\qquad
b^{\dagger2}|n\rangle\propto|n+2\rangle
$$

so different number states mix. The identity

$$
b^2+b^{\dagger2}=Q^2-P^2
$$

also shows that this term treats the $Q$ and $P$ directions asymmetrically.
In phase space, the evolution is described by the Hamiltonian flow

$$
\dot Q=\omega_0P,
\qquad
\dot P=-\frac{\Omega^2(t)}{\omega_0}Q
$$

Here, $Q,P$ are phase-space coordinates. Because the Hamiltonian is quadratic, the Wigner function evolves exactly along this classical flow. For $\Omega^2=\omega_0^2$, the flow is circular rotation; unequal coefficients introduce stretching and contraction.

As a result, the initially circular Wigner function of a Gaussian state generally deforms into a rotating ellipse. In particular, starting from an isotropic minimum-uncertainty state such as the vacuum or a coherent state produces squeezing: fluctuations in one quadrature become smaller than the vacuum fluctuations, while those in the conjugate direction grow.

<details markdown="1">
<summary>Definition and interpretation of the Wigner function</summary>

The Wigner function maps a quantum state described by a density operator $\hat\rho$ to a real function on phase space. With the convention $[\hat Q,\hat P]=i$, it is defined as

$$
\begin{aligned}
W(Q,P)&=\frac1{2\pi}\int_{-\infty}^{\infty}d\xi\,e^{-iP\xi}\left\langle Q+\frac\xi2\right|\hat\rho\left|Q-\frac\xi2\right\rangle
\end{aligned}
$$

Here, $|Q\rangle$ is an eigenstate of $\hat Q$, and $Q,P$ are real phase-space coordinates. Time dependence is contained in $\hat\rho$ and suppressed in the notation. For a pure state, the density-matrix element in the integrand becomes $\psi(Q+\xi/2)\psi^*(Q-\xi/2)$.

The total integral is $1$. Integrating over either coordinate gives the measurement probability density of the other quadrature:

$$
\int dQ\,dP\,W(Q,P)=1,
$$

$$
\begin{aligned}
\int dP\,W(Q,P)&=\langle Q|\hat\rho|Q\rangle,\\
\int dQ\,W(Q,P)&=\langle P|\hat\rho|P\rangle
\end{aligned}
$$

Phase-space moments also correspond to expectation values of symmetrically ordered (Weyl-ordered) operators. For example,

$$
\int dQ\,dP\,QP\,W(Q,P)
=\frac12\langle\hat Q\hat P+\hat P\hat Q\rangle
$$

This property lets us examine the fluctuations and correlations of both quadratures in a single phase space.

For general quantum states, $W$ can be negative, so it is called a **quasiprobability distribution** to distinguish it from an ordinary probability density. Gaussian states have $W\geq0$, allowing symmetrically ordered correlators to be calculated as averages over a classical probability distribution. Even the vacuum, whose Wigner function is positive, remains a quantum state subject to commutation and uncertainty relations. [O’Connell](https://arxiv.org/abs/1009.4431) also reviews the definition and basic properties.

For example, the vacuum of $b=(Q+iP)/\sqrt2$ has the circularly symmetric distribution

$$
W_0(Q,P)=\frac1\pi e^{-(Q^2+P^2)}
$$

Each quadrature has variance $1/2$, showing that amplitude and momentum fluctuations persist even in the vacuum.

</details>

### Heisenberg picture: operator evolution and Bogoliubov mixing

Now consider the same fixed basis in the Heisenberg picture. The state is held fixed, and we define

$$
b_{\rm H}(t)=U^\dagger(t)bU(t)
$$

Since $b$ itself has no explicit time dependence, the Heisenberg equation gives

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

Thus, $b_{\rm H}(t)$ generally evolves through a Bogoliubov transformation,

$$
b_{\rm H}(t)
=
\alpha(t)b+\beta(t)b^\dagger
$$

Preserving the commutation relation requires

$$
|\alpha(t)|^2-|\beta(t)|^2=1
$$

The deformation of the state by the $b^2+b^{\dagger2}$ term in the Schrödinger picture appears in the Heisenberg picture as mixing of $b_{\rm H}^\dagger$ into the evolution of $b_{\rm H}$.

In the Schrödinger picture, the state deforms on fixed $Q,P$ axes. In the Heisenberg picture, the operators undergo Bogoliubov mixing while the state remains fixed. These descriptions give the same expectation values and covariances.

### Instantaneous basis: diagonalizing the Hamiltonian at each time

So far, we have described evolution using $b,b^\dagger$ defined by a fixed reference frequency $\omega_0$. Wherever $\Omega^2(t)>0$, we can also introduce an instantaneous basis that diagonalizes the Hamiltonian at that time.

$$
\omega(t)=\sqrt{\Omega^2(t)}>0
$$

Defining

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

gives

$$
H(t)
=
\omega(t)
\left(
b_{\rm inst}^\dagger(t)b_{\rm inst}(t)
+\frac12
\right)
$$

Diagonalizing the Hamiltonian at each time does not, however, ensure that the state remains in an instantaneous eigenstate. In the expansion

$$
|\psi(t)\rangle
=
\sum_n c_n(t)|n;t\rangle
$$

the number states $|n;t\rangle$ defined by $b_{\rm inst}(t)$ themselves vary with time, producing mixing between instantaneous eigenstates. For a harmonic oscillator, $n$ mixes with $n\pm2$. The evolution seen as squeezing in the fixed basis appears here as mixing between instantaneous number states.

If $\omega(t)$ varies slowly enough that

$$
\frac{|\dot\omega|}{\omega^2}\ll1
$$

this mixing is small. In the adiabatic limit, a state initially in the instantaneous vacuum approximately follows the instantaneous vacuum at later times.

As $\omega\to0$, the adiabatic condition generally fails, and at $\Omega^2=0$ the definition of $b_{\rm inst}$ becomes singular. For $\Omega^2(t)<0$, the Hamiltonian is

$$
H(t)
=
\frac12
\left[
p^2-|\Omega^2(t)|q^2
\right]
$$

and the system is an inverted harmonic oscillator. There is no ground state or discrete set of number states of the ordinary harmonic-oscillator kind, so an instantaneous particle description in terms of a vacuum or particle number at that time is no longer available.

The phase-space description using fixed $Q,P$ remains valid regardless of the sign of $\Omega^2$. For $\Omega^2<0$, oscillatory rotation gives way to hyperbolic flow that stretches in one direction and contracts in another, developing squeezing.

As we will see, the effective squared frequency of a Mukhanov–Sasaki mode during inflation changes from positive to negative. On subhorizon scales, it behaves as an ordinary oscillator, with a natural positive-frequency mode and particle and vacuum concepts. On superhorizon scales, an oscillatory particle picture is no longer appropriate; growing and decaying modes and squeezing provide a more natural description.

Below, we mainly calculate evolution in the Heisenberg picture, obtaining covariances from Bogoliubov coefficients or mode functions. We then use those covariances to draw the state's Wigner function in the Schrödinger picture on fixed $Q,P$ axes. “Fixed axes” means that we do not redefine the coordinates to follow the instantaneous basis; it does not mean that the calculation is performed in the Schrödinger picture. Calculating operator evolution and displaying the result as a deformation of the state's distribution lets us follow the evolution consistently from the oscillatory regime to superhorizon scales.

## 3. Modes and degrees of freedom of a real scalar field

### Fourier expansion and the reality condition

Expand a real scalar field $v(\eta,\mathbf x)$ in Fourier modes in a volume $V$ with periodic boundary conditions:

$$
v(\eta,\mathbf x)
=
\frac1{\sqrt V}
\sum_{\mathbf k}
v_{\mathbf k}(\eta)e^{i\mathbf k\cdot\mathbf x}
$$

Reality of the field implies

$$
v_{-\mathbf k}=v_{\mathbf k}^*
$$

Thus, the Fourier coefficients at $\mathbf k$ and $-\mathbf k$ are not independent. For one nonzero wavevector pair $(\mathbf k,-\mathbf k)$, the complex number $v_{\mathbf k}$ is specified by two independent real numbers. **Each wavevector pair therefore has two real degrees of freedom.**

We now quantize these two degrees of freedom and describe them in traveling-wave and standing-wave bases.

### Canonical quantization and traveling-wave modes

Quantize in the Schrödinger picture. Hermiticity of the field and its canonical momentum imposes the following conditions on their Fourier coefficients $\hat v_{\mathbf k}$ and $\hat\pi_{\mathbf k}$:

$$
\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger,
\qquad
\hat\pi_{-\mathbf k}=\hat\pi_{\mathbf k}^\dagger
$$

The canonical commutation relations are

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

As for the oscillator in §2, define creation and annihilation operators using a fixed reference frequency. For each wavevector, take $k=|\mathbf k|>0$ and set

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

Then,

$$
[a_{\mathbf k},a_{\mathbf k'}^\dagger]
=
\delta_{\mathbf k,\mathbf k'},
\qquad
[a_{\mathbf k},a_{\mathbf k'}]=0
$$

Conversely, the Fourier coefficients are

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

Although the reality condition gives $\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger$, the operators $a_{\mathbf k}$ and $a_{-\mathbf k}$ are independent annihilation operators.

In terms of creation and annihilation operators, the full field, excluding the zero mode, is

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

The operator $a_{\mathbf k}$ corresponds to a mode with spatial dependence $e^{i\mathbf k\cdot\mathbf x}$. We call these modes, labeled by the wavevector $\mathbf k$, **traveling-wave modes**. The reference frequency $k$ defines the operators; it need not be the instantaneous frequency under the time-dependent Hamiltonian.

### Description in standing-wave modes

Now express the same field in a real cosine and sine basis.

Let $\mathcal K_+$ contain one representative from each wavevector pair $(\mathbf k,-\mathbf k)$. For one pair, write

$$
\hat v_{\mathbf k}
=
\frac{\hat q_{c,\mathbf k}-i\hat q_{s,\mathbf k}}{\sqrt2},
\qquad
\hat v_{-\mathbf k}
=
\frac{\hat q_{c,\mathbf k}+i\hat q_{s,\mathbf k}}{\sqrt2}
$$

The field operator then becomes

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

where the zero mode is again omitted.

The Hermitian operators $\hat q_{c,\mathbf k},\hat q_{s,\mathbf k}$ represent the two real configuration degrees of freedom of cosine and sine type.

Similarly, decomposing the canonical momentum as

$$
\hat\pi_{\mathbf k}
=
\frac{\hat p_{c,\mathbf k}-i\hat p_{s,\mathbf k}}{\sqrt2}
$$

gives

$$
[\hat q_{A,\mathbf k},\hat p_{B,\mathbf k^{\prime}}]=i\delta_{AB}\delta_{\mathbf k,\mathbf k^{\prime}},
$$

$$
[\hat q_{A,\mathbf k},\hat q_{B,\mathbf k^{\prime}}]=[\hat p_{A,\mathbf k},\hat p_{B,\mathbf k^{\prime}}]=0
$$

Here, $A,B=c,s$ and $\mathbf k,\mathbf k^{\prime}\in\mathcal K_+$. Each wavevector pair can therefore be treated as two independent real harmonic oscillators.

For each oscillator, use the same reference frequency $k$ as in the traveling-wave basis and define

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

The operators $b_{c,\mathbf k},b_{s,\mathbf k}$ annihilate the cosine and sine **standing-wave modes**, respectively.

Their relation to the traveling-wave annihilation operators is

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

Thus, **the traveling-wave and standing-wave bases describe the same two quantum oscillators in different bases**.

Since this transformation mixes only annihilation operators with one another, the vacuum is shared by both bases:

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

The traveling-wave basis uses the two modes at $\mathbf k$ and $-\mathbf k$, while the standing-wave basis uses the cosine and sine modes.

This correspondence also matters for squeezing during time evolution. As we will see, two-mode squeezing of $\mathbf k$ and $-\mathbf k$ in the traveling-wave basis can be described as single-mode squeezing of each of the two oscillators in the standing-wave basis.

## 4. Inflationary mode equations and squeezing

### The Mukhanov–Sasaki equation

Consider inflation driven by a single scalar field, the inflaton, with a canonical kinetic term. Introducing the Mukhanov–Sasaki variable

$$
v=z\zeta,
\qquad
z=\frac{a\dot\phi_0}{H}
$$

gives the quadratic action

$$
S
=
\frac12\int d\eta\,d^3x\,
\left[
(v')^2-(\nabla v)^2+\frac{z''}{z}v^2
\right]
$$

Here, $\zeta$ is the comoving curvature perturbation, $\eta$ is conformal time, and primes denote derivatives with respect to $\eta$.

The Fourier-mode equation of motion is

$$
v_{\mathbf k}''
+
\left(
k^2-\frac{z''}{z}
\right)v_{\mathbf k}
=0
$$

Thus, each real Fourier component introduced in §3 behaves as a time-dependent harmonic oscillator with effective squared frequency

$$
\Omega_k^2(\eta)=k^2-\frac{z''}{z}
$$

### Two-mode squeezing in the traveling-wave basis

Set

$$
s(\eta)=\frac{z'}{z}
$$

Using $z''/z=s'+s^2$, we can write

$$
(v')^2+\frac{z''}{z}v^2
=
(v'-sv)^2+(sv^2)'
$$

The last term is a total time derivative. Dropping this boundary term gives the action

$$
S
=
\frac12\int d\eta\,d^3x\,
\left[
(v'-sv)^2-(\nabla v)^2
\right]
$$

With this choice, the canonical momentum conjugate to the field $v$ is

$$
\pi=v'-sv
$$

The corresponding Hamiltonian is

$$
H_\eta
=
\frac12\int d^3x\,
\left[
\pi^2+(\nabla v)^2
+s(v\pi+\pi v)
\right]
$$

We use these canonical variables below.

In the Schrödinger picture, use the traveling-wave annihilation operators from §3, defined with the fixed reference frequency $k$:

$$
a_{\mathbf k}
=
\frac1{\sqrt2}
\left(
\sqrt{k}\,v_{\mathbf k}
+\frac{i\pi_{\mathbf k}}{\sqrt{k}}
\right)
$$

The Hamiltonian for one wavevector pair $(\mathbf k,-\mathbf k)$ is then

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

The first term describes free oscillators of frequency $k$. The second creates or annihilates one excitation at $\mathbf k$ and one at $-\mathbf k$.

A homogeneous background preserves spatial translation symmetry, so each created pair has zero total momentum. In the traveling-wave basis, this evolution appears as **two-mode squeezing**.

### The Bunch–Davies vacuum and Bogoliubov transformations

Deep inside the Hubble scale, $k^2\gg |z''/z|$, and the squeezing term becomes negligible compared with the free Hamiltonian.

Choose the ground state of this free Hamiltonian in the distant past as the initial state. This is the **Bunch–Davies vacuum**.

Writing the corresponding initial annihilation operators as $a_{\mathbf k}^{\mathrm{in}}$, the Bunch–Davies vacuum is defined by

$$
a_{\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle=0
$$

We now follow the evolution in the Heisenberg picture. The Hamiltonian above gives

$$
\frac{da_{\mathbf k}(\eta)}{d\eta}
=
-ik\,a_{\mathbf k}(\eta)
+s(\eta)a_{-\mathbf k}^\dagger(\eta)
$$

The evolution can therefore be written as a Bogoliubov transformation,

$$
a_{\mathbf k}(\eta)
=
\alpha_k(\eta)a_{\mathbf k}^{\mathrm{in}}
+
\beta_k(\eta)a_{-\mathbf k}^{\mathrm{in}\dagger}
$$

Preserving the canonical commutation relations requires

$$
|\alpha_k|^2-|\beta_k|^2=1
$$

The magnitudes of Bogoliubov coefficients satisfying this relation can be parameterized by a nonnegative $r_k$:

$$
|\alpha_k|=\cosh r_k,
\qquad
|\beta_k|=\sinh r_k
$$

The **squeezing parameter** $r_k$ measures the strength of squeezing. The initial vacuum has $r_k=0$. As $r_k$ grows during evolution, creation operators mix more strongly into the annihilation operators.

### Single-mode squeezing in the standing-wave basis

So far, we have described the evolution as two-mode squeezing of $\mathbf k$ and $-\mathbf k$ in the traveling-wave basis. **The fact that squeezing couples two modes depends on this choice of basis.**

In the standing-wave basis introduced in §3,

$$
a_{\mathbf k}
=
\frac{b_{c,\mathbf k}-ib_{s,\mathbf k}}{\sqrt2},
\qquad
a_{-\mathbf k}
=
\frac{b_{c,\mathbf k}+ib_{s,\mathbf k}}{\sqrt2}
$$

Substituting this transformation into the Hamiltonian gives

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

The term coupling the two traveling-wave modes separates into a squeezing term for each standing-wave mode.

Indeed, the Heisenberg equation is

$$
\frac{db_{A,\mathbf k}(\eta)}{d\eta}
=
-ik\,b_{A,\mathbf k}(\eta)
+s(\eta)b_{A,\mathbf k}^\dagger(\eta)
$$

which gives the single-mode Bogoliubov transformation

$$
b_{A,\mathbf k}(\eta)
=
\alpha_k(\eta)b_{A,\mathbf k}^{\mathrm{in}}
+
\beta_k(\eta)b_{A,\mathbf k}^{\mathrm{in}\dagger}
$$

The cosine and sine modes are independent and undergo identical squeezing. Since the initial vacuum is shared by both bases,

$$
a_{\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=
a_{-\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=0
$$

is equivalent to

$$
b_{c,\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=
b_{s,\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle
=0
$$

<iframe src="app/supporting.html?lang=en&amp;view=basis" title="Fourier half-space and traveling/standing basis conversion" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1200px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

The figure compares the covariance matrix of the same quantum state in the traveling-wave and standing-wave bases. Correlations between the two modes appear in the traveling-wave basis, while the standing-wave basis separates the covariance into two identical, independent blocks.

Thus, **two-mode squeezing and two single-mode squeezings describe the evolution of the same quantum state in different mode bases**.

The traveling-wave basis makes spatial translation symmetry and momentum conservation explicit. The standing-wave basis lets us examine squeezing directly in the phase space of each real degree of freedom.

Below, we use the latter to follow the deformation of the quantum state of one real standing-wave mode.

## 5. Squeezing and mode functions in de Sitter spacetime

### Bogoliubov transformations in a de Sitter background

In §4, we saw that each Fourier mode during inflation behaves as a time-dependent harmonic oscillator, and that its quantum evolution can be expressed through a Bogoliubov transformation. We now choose a specific background and obtain the evolution of the Bogoliubov coefficients and squeezing analytically.

As an exactly solvable example, consider a free, massless, minimally coupled scalar field $\phi$ in de Sitter spacetime. This is not the curvature perturbation $\zeta$ of §4, but curvature perturbations during slow-roll inflation follow approximately the same evolution. Appropriately canonically normalized tensor perturbations obey the same mode equation as well.

In a de Sitter background,

$$
a(\eta)=-\frac1{H\eta},
\qquad
\mathcal H=\frac{a'}a=-\frac1\eta
$$

where $H$ is the constant Hubble parameter and $\eta<0$ is conformal time.

For each of the two real standing-wave modes $A=c,s$ introduced in §3, define the dimensionless canonical quadratures

$$
Q_{A,\mathbf k}=\sqrt{k}\,a\phi_{A,\mathbf k},
\qquad
P_{A,\mathbf k}=\frac{a\phi_{A,\mathbf k}'}{\sqrt{k}}
$$

They satisfy $[Q_{A,\mathbf k},P_{A,\mathbf k}]=i$ and are related to the annihilation operators of §4 by

$$
b_{A,\mathbf k}=\frac{Q_{A,\mathbf k}+iP_{A,\mathbf k}}{\sqrt2}
$$

Replacing $s=z'/z$ in §4 with $s=\mathcal H$ gives

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

We use these $Q,P$ for the phase-space discussion below.

Introduce

$$
x=-k\eta=\frac{k}{aH},
\qquad
N=\ln\frac{a}{a_{\mathrm{cross}}}=-\ln x
$$

Here, $x\gg1$ is the subhorizon regime, $x=1$ is Hubble crossing, and $x\ll1$ is the superhorizon regime.

The Heisenberg equation derived in §4,

$$
b_{A,\mathbf k}'(\eta)
=
-ik\,b_{A,\mathbf k}(\eta)
+s(\eta)b_{A,\mathbf k}^\dagger(\eta)
$$

now has

$$
s(\eta)=\mathcal H=\frac{k}{x}
$$

Substituting the Bogoliubov transformation

$$
b_{A,\mathbf k}(\eta)
=
\alpha_k(\eta)b_{A,\mathbf k}^{\mathrm{in}}
+
\beta_k(\eta)b_{A,\mathbf k}^{\mathrm{in}\dagger}
$$

gives

$$
\begin{aligned}
\alpha_k'&=-ik\alpha_k+s\beta_k^*,\\
\beta_k'&=-ik\beta_k+s\alpha_k^*
\end{aligned}
$$

The Bunch–Davies initial condition requires, as $x\to\infty$,

$$
\alpha_k\sim e^{ix},
\qquad
\beta_k\to0
$$

The exact solution satisfying this condition is

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

Thus,

$$
|\beta_k|^2=\frac1{4x^2}
$$

and the squeezing parameter defined in §4 is

$$
r_k=\operatorname{arsinh}\frac1{2x}
$$

In the subhorizon limit,

$$
r_k\simeq\frac1{2x}\ll1
\qquad (x\gg1)
$$

so the quantum state remains close to the initial vacuum. In the superhorizon limit,

$$
r_k\simeq-\ln x=N
\qquad (x\ll1)
$$

and squeezing develops.

Indeed,

$$
\frac{dr_k}{dN}
=
\frac1{\sqrt{1+4x^2}}
$$

so, well outside the Hubble scale, the squeezing parameter increases by approximately one unit per e-fold of expansion.

### Mode functions and superhorizon solutions

We have described the evolution using Bogoliubov coefficients. The same evolution can also be expressed through the mode functions that multiply the initial annihilation operators in the field expansion.

For a real standing-wave mode $A=c,s$ of the wavevector pair $(\mathbf k,-\mathbf k)$, expand the quadrature $Q_{A,\mathbf k}$ as

$$
Q_{A,\mathbf k}(\eta)
=
\sqrt{k}\left[
f_k(\eta)b_{A,\mathbf k}^{\mathrm{in}}
+
f_k^*(\eta)b_{A,\mathbf k}^{\mathrm{in}\dagger}
\right]
$$

Comparing with the Bogoliubov transformation gives

$$
f_k(\eta)
=
\frac{\alpha_k+\beta_k^*}{\sqrt{2k}}
=
\frac{1+i/x}{\sqrt{2k}}e^{ix}
$$

Here, $f_k$ is normalized as the mode function of the rescaled field $a\phi_{A,\mathbf k}$. The expansion coefficient of the dimensionless $Q_{A,\mathbf k}$ is $\sqrt{k}f_k$.

The mode function of the original field $\phi_{A,\mathbf k}=Q_{A,\mathbf k}/(\sqrt{k}a)$ is

$$
\frac{f_k}{a}
=
\frac{H}{\sqrt{2k^3}}(x+i)e^{ix}
$$

Expanding in the superhorizon limit $x\ll1$ gives

$$
\frac{f_k}{a}
=
\frac{H}{\sqrt{2k^3}}
\left[
i\left(1+\frac{x^2}{2}+O(x^4)\right)
-\frac{x^3}{3}+O(x^5)
\right]
$$

The imaginary part approaches a constant, while the real part decays as $x^3\propto a^{-3}$.

These two behaviors correspond to independent solutions of the mode equation. The function $f_k$ satisfies

$$
f_k''
+
\left(k^2-\frac{a''}{a}\right)f_k
=0
$$

Rewriting this as an equation for $f_k/a$ gives

$$
\left[a^2\left(\frac{f_k}{a}\right)'\right]'
+
k^2a^2\frac{f_k}{a}
=0
$$

Neglecting the gradient term on superhorizon scales, the general solution is

$$
\frac{f_k(\eta)}{a(\eta)}
\simeq
C_1+
C_2\int^\eta\frac{d\tilde\eta}{a^2(\tilde\eta)}
$$

In de Sitter spacetime, the second term is proportional to $a^{-3}$. The imaginary and real parts of the exact solution therefore correspond to the conserved (growing) mode and the decaying mode, respectively. The $O(x^2)$ term in the imaginary part is a finite-wavenumber correction to the conserved mode.

The conserved mode dominates on superhorizon scales. Indeed, the field variance in the Bunch–Davies vacuum is

$$
\begin{aligned}
\langle\phi_{A,\mathbf k}^2\rangle
&=
\left|\frac{f_k}{a}\right|^2\\
&=
\frac{H^2}{2k^3}(1+x^2)
\end{aligned}
$$

so

$$
\langle\phi_{A,\mathbf k}^2\rangle
\longrightarrow
\frac{H^2}{2k^3}
\qquad(x\to0)
$$

While the fluctuations of the original field approach a constant, the quantum state in $Q_{A,\mathbf k},P_{A,\mathbf k}$ continues to become strongly squeezed. Conserved-mode dominance and the growth of squeezing are two aspects of the same quantum evolution.

The next figure shows the real part, imaginary part, and magnitude of $f_k/a$ and $f_k$, in units of $H/\sqrt{2k^3}$ and $1/\sqrt{2k}$, respectively. In the “Superhorizon components” view, $|\operatorname{Im}(f_k/a)|$ and $|\operatorname{Re}(f_k/a)|$ approach $1$ and $x^3/3$. The assignment of real and imaginary parts depends on the phase convention of the mode function, but conserved-mode dominance is independent of that convention.

<iframe src="app/supporting.html?lang=en&amp;view=background" title="Background terms and exact de Sitter mode functions" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

## 6. Wigner-function evolution: Bogoliubov transformations and Hamiltonian flow

Let us view this evolution in the phase space of one real standing-wave mode. Fix a wavevector pair and one of $A=c,s$, and abbreviate $Q=Q_{A,\mathbf k}$, $P=P_{A,\mathbf k}$, and $\phi=\phi_{A,\mathbf k}$.

The dimensionless quadratures defined in §5 are

$$
Q=\sqrt{k}\,a\phi,
$$

$$
P=\frac{a\phi'}{\sqrt{k}}
$$

These are canonical variables satisfying

$$
[\hat Q,\hat P]=i
$$

We calculate evolution using Heisenberg-picture operators, but display the result in the Schrödinger picture: **the state's Wigner function deforms on fixed $Q,P$ axes**. The orientation, scale, and range of the axes remain fixed in every frame.

### Covariance matrix and Wigner ellipse

Define the phase-space coordinates and covariance matrix as

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

The Bunch–Davies vacuum is a Gaussian state with zero mean, so its evolution is characterized by the covariance matrix.

The Bogoliubov transformation of §5 gives

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

Substituting the exact de Sitter solution yields

$$
\Sigma(x)
=
\frac12
\begin{pmatrix}
1+x^{-2}&-x^{-1}\\
-x^{-1}&1
\end{pmatrix}
$$

From the definition in §2, the Wigner function of this zero-mean Gaussian state is

$$
W(\mathbf Z;x)
=
\frac1{2\pi\sqrt{\det\Sigma}}
\exp\left[
-\frac12\mathbf Z^T\Sigma^{-1}\mathbf Z
\right]
$$

The figures draw the contour

$$
\mathbf Z^T\Sigma^{-1}\mathbf Z=1
$$

You can follow this contour's evolution in the third panel of the [animation below](#main-animation).

The eigenvalues of the covariance matrix are

$$
\sigma_\pm^2
=
\frac12e^{\pm2r_k}
$$

As $r_k$ from §5 increases, the Wigner distribution therefore becomes a long, thin ellipse.

Meanwhile,

$$
\det\Sigma=\frac14
$$

remains constant in time. Squeezing preserves phase-space area while reducing fluctuations in one direction and increasing them in the conjugate direction.

### Hamiltonian flow: rotation and squeezing

We now examine the Hamiltonian flow that produces this deformation of the Wigner distribution.

Writing the Hamiltonian of §4 in fixed quadratures and changing the time variable from conformal time $\eta$ to $N$ gives

$$
K_N
=
\frac{x}{2}(Q^2+P^2)
+
\frac12(QP+PQ)
$$

The corresponding Hamilton equations are

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

This matrix decomposes as

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

The first term generates rotation in phase space. The second generates squeezing through stretching along $Q$ and contraction along $P$.

Rotation dominates for $x\gg1$. As expansion reduces $x$, squeezing becomes relatively more important. At $x=1$, the two contributions are comparable and the instantaneous flow is a shear. For $x\ll1$, stretching and contraction dominate.

Because the Hamiltonian is quadratic, the Wigner function evolves exactly along this classical Hamiltonian flow. The covariance matrix obeys

$$
\frac{d\Sigma}{dN}
=
A\Sigma+\Sigma A^T
$$

Also,

$$
\operatorname{tr}A=0
$$

so phase-space area is conserved, consistent with the constant $\det\Sigma=1/4$ found above.

<span id="main-animation"></span>

### Animating the Wigner ellipse and Hamiltonian flow

The animation follows the evolution from $x=12$ to $x=0.2$, using $N=-\ln x$ as time. The first two panels show the rotation and squeezing vector fields separately; the third shows their combined flow and the Wigner contour.

<iframe src="app/index.html?lang=en" title="Inflationary squeezing: rotation, squeeze, and total Hamiltonian flow" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

Follow these changes in the animation:

1. **Subhorizon ($x\gg1$):** Rotation dominates and the Wigner distribution is nearly circular. The slight ellipticity at the start comes from beginning at $x=12$ rather than $x=\infty$.
2. **Hubble crossing ($x=1$):** Rotation and squeezing become comparable, and the deformation of the ellipse becomes clear.
3. **Superhorizon ($x\ll1$):** The long axis stretches and the short axis narrows. Correlations between $Q$ and $P$ strengthen, concentrating the distribution along the direction associated with the growing solution.

For readability, arrow lengths are multiplied by $1/\sqrt{1+x^2}$ and a common drawing scale. The Wigner function itself is calculated using the original Hamiltonian flow.

Toggle the direction overlays to compare the eigendirections of the instantaneous flow, the principal axes of the ellipse, and the directions of the growing and decaying solutions. At finite $x$, these directions differ, and their relationships change during the evolution.

### Squeezing strength and ellipse orientation

We can quantify the stretching and rotation seen above using the squeezing parameter and the angle of the long axis.

Let $\varphi_k$ be the angle of the ellipse's long axis relative to the positive $Q$ axis. Then,

$$
\varphi_k
=
\frac12\arg(\alpha_k\beta_k)
=
-\frac12\arctan(2x)
$$

The Bogoliubov coefficients determine both the strength of squeezing and the orientation of the ellipse. The initially almost circular distribution becomes progressively more elongated, with its long axis approaching the $Q$ axis.

The figure below extends beyond the animation to four e-folds after Hubble crossing.

<iframe src="app/supporting.html?lang=en&amp;view=squeezing" title="Squeezing magnitude and broad-axis angle versus e-fold time" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

### Field-velocity fluctuations and freeze-out

How does the ellipse's deformation relate to the “freeze-out” of the original field at an almost constant amplitude? The plotted $P$ is a rescaled derivative, $P=a\phi'/\sqrt{k}$. The covariance matrix gives a constant

$$
\operatorname{Var}(P)=\frac12
$$

Even as the short axis approaches the $P$ axis, the width of the distribution projected onto $P$ does not vanish. What shrinks is the remaining width at a given $Q$. For the positive Gaussian Wigner density,

$$
\mathbb E[P\mid Q]=-\frac{x}{1+x^2}Q,
\qquad
\operatorname{Var}(P\mid Q)=\frac{x^2}{2(1+x^2)}
$$

so the superhorizon distribution concentrates near $P\simeq-xQ$.

The velocity fluctuations of the original field can instead be obtained directly by differentiating the mode function. Using the exact solution of §5 and $dx/d\eta=-k$ gives

$$
\left(\frac{f_k}{a}\right)'
=-\frac{i}{a}\sqrt{\frac{k}{2}}\,e^{ix}
$$

In the Bunch–Davies vacuum, $\langle\phi\rangle=\langle\phi'\rangle=0$, so the mean squared velocity equals its variance:

$$
\left\langle(\phi')^2\right\rangle
=\left|\left(\frac{f_k}{a}\right)'\right|^2
=\frac{k}{2a^2}
$$

For the velocity in cosmic time, $\dot\phi=\phi'/a$,

$$
\left\langle\dot\phi^{\,2}\right\rangle
=\frac{k}{2a^4}
\longrightarrow0
$$

Meanwhile, as derived in §5, the field amplitude retains a finite variance:

$$
\langle\phi^2\rangle
=\frac{H^2}{2k^3}(1+x^2)
\longrightarrow\frac{H^2}{2k^3}
$$

The smallness of the change per Hubble time is measured by the dimensionless ratio

$$
\frac{\sqrt{\langle\dot\phi^{\,2}\rangle}}
{H\sqrt{\langle\phi^2\rangle}}
=\frac{x^2}{\sqrt{1+x^2}}
\simeq x^2
\qquad(x\ll1)
$$

For example, at $x=0.1$ this ratio is approximately $0.01$. **The amplitude retains a superposition with a finite spread while the time variation of the original field becomes small.** This is the concrete meaning of freeze-out in this model. Meanwhile, the amplitude spread of $Q=\sqrt{k}a\phi$ continues to grow.

Here, $\phi$ and $\dot\phi$ are not a canonically conjugate pair: $[\hat\phi,\hat{\dot\phi}]=i/a^3$. The shrinking velocity spread is consistent with $[\hat Q,\hat P]=i$ and $\det\Sigma=1/4$ for the fixed canonical quadratures.

As the decaying solution becomes suppressed, the independent random inputs needed for subsequent linear evolution effectively reduce to a single amplitude. This structure connects the classical statistical description below to the temporal phase of acoustic oscillations after re-entry.

## 7. Why perturbations appear classical

A quantum state can have zero mean and nonzero variance.

From the same exact mode function, the test scalar field's power per logarithmic wavenumber interval is

$$
\mathcal P_\phi(k)
=
\frac{k^3}{2\pi^2}
\left|
\frac{f_k}{a}
\right|^2
$$

giving

$$
\mathcal P_\phi(k)
=
\frac{H^2}{4\pi^2}
(1+x^2)
$$

In the superhorizon limit $x\to0$,

$$
\mathcal P_\phi(k)
\longrightarrow
\left(
\frac{H}{2\pi}
\right)^2.
$$

Thus, substantial growth of the variance of the quadrature $Q=\sqrt{k}a\phi$ is consistent with freeze-out of the original field $\phi$ at a finite variance.

For curvature perturbations, $z$ replaces $a$, and its slow-roll evolution determines the amplitude and spectral tilt.

Why, then, can this quantum state be treated as a classical random field in the later universe?

First, the freely evolving Bunch–Davies vacuum remains Gaussian, with a positive Wigner function. Treating this positive distribution as a probability density reproduces equal-time, symmetrically ordered (Weyl-ordered) correlators through a classical Gaussian ensemble. This property already holds for the initial vacuum.

As squeezing develops, a stronger structure emerges. The growing mode dominates, and the field and momentum become correlated. The Wigner distribution becomes a thin ellipse, so the initial conditions needed for subsequent linear evolution can effectively be specified by a single random amplitude. The statistics of observed fluctuations can then be calculated using a classical stochastic field.

The quantum state itself has not become classical, however. The commutation relation

$$
[\hat Q,\hat P]=i
$$

remains. The wavefunction does not spontaneously collapse, nor does a pure state become mixed through this evolution alone.

Environmental decoherence is a separate physical process from squeezing.

The distinction between reproducing statistics classically and the quantum state itself becoming classical matters when discussing the quantum origin of primordial fluctuations. [Martin & Vennin](https://arxiv.org/abs/1510.04038) discuss this distinction in detail.

<iframe src="app/supporting.html?lang=en&amp;view=samples" title="Wigner samples before and after symplectic evolution" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

Move the time slider from the beginning to the end.

Evolution does not eliminate randomness. The range of amplitudes along the long axis grows, while the spread away from the orange conditional-mean line in the $P$ direction shrinks.

The left and right panels use the same coordinate ranges. The plotted Wigner contour encloses approximately 39% of the probability weight, so it is natural for many sample points to lie outside the ellipse.

## 8. Temporal phase coherence and the CMB acoustic peaks

As we saw in §6–7, squeezing makes the Wigner distribution a thin ellipse, with the field amplitude and momentum approximately obeying a common linear relation. At a fixed time, momentum is proportional to the field velocity, so amplitude and velocity are distributed almost along a single straight line rather than varying independently. This correlation is the starting point for understanding the phase of subsequent acoustic oscillations.

As the decaying mode fades, a conserved mode with a random amplitude becomes dominant. For the scalar field in §6, the relative change per Hubble time on superhorizon scales is suppressed to order $x^2\ll1$.

In standard single-field attractor inflation, the superhorizon curvature perturbation $\zeta$ is also approximately conserved. As this perturbation evolves as an adiabatic growing mode, the photon–baryon fluid's acoustic variable in the linear regime can be written, for each real standing-wave component $a=c,s$, as

$$
X_{a,\mathbf k}(\eta)\simeq T_k(\eta)\zeta_{a,\mathbf k}^{\mathrm{prim}},
\qquad
X_{a,\mathbf k}'(\eta)\simeq T_k'(\eta)\zeta_{a,\mathbf k}^{\mathrm{prim}}
$$

Here, $T_k$ is the transfer function determined by the background evolution and wavenumber.

Here too, displacement and velocity are proportional to the same primordial amplitude $\zeta_{a,\mathbf k}^{\mathrm{prim}}$ and obey a common linear relation. A nonzero velocity adds no independent randomness. Thus, although the amplitude varies between realizations, oscillations at the same wavenumber reach their zeros and extrema at the same times. This is **temporal phase coherence**. The spatial Fourier phase $\arg\zeta_{\mathbf k}$, meanwhile, remains random.

Consider this property in a simple oscillator with constant sound speed $c_s$. Neglect gravitational driving and select one real standing-wave component. For the temperature or density displacement $X_k$ from equilibrium, we can write

$$
\begin{aligned}
X_k(\eta)&=A_k\cos(kr_s)+B_k\sin(kr_s),\\
r_s&=c_s(\eta-\eta_i)
\end{aligned}
$$

Here, $\eta_i$ is the initial time and $r_s$ is the acoustic distance measured from it. The relation to the initial conditions is

$$
A_k=X_k(\eta_i),
\qquad
B_k=\frac{X_k'(\eta_i)}{kc_s}
$$

so the cosine component corresponds to initial displacement, and the sine component to initial velocity. The linear relation above corresponds to a coefficient ratio $B_k/A_k$ shared across realizations.

For the adiabatic growing mode, density and temperature perturbations already exist at the superhorizon stage before acoustic oscillations begin. Spatial gradients of pressure and gravitational potential accelerate the fluid, but these gradients are small in this long-wavelength regime, so the resulting fluid velocity is also small. In this simplified model, this corresponds to an oscillator starting almost at rest with a random initial displacement.

Thus, if the initial velocity is sufficiently small compared with $kc_s$ times the initial displacement, then $|B_k|\ll|A_k|$, and we can approximate

$$
X_k(\eta)\simeq A_k\cos(kr_s)
$$

The temporal phase is common even though the amplitude's magnitude and sign are random. [Hu & White](https://arxiv.org/abs/astro-ph/9602019) discuss the connection between these initial conditions and the CMB acoustic peaks in detail.

Compare the effect of aligned temporal phases in two ensembles with the same total initial amplitude variance $\sigma^2$.

First, in a coherent ensemble where every oscillation starts as a cosine,

$$
\langle A_k^2\rangle=\sigma^2,
\qquad B_k=0
$$

so

$$
\langle X_k^2\rangle=\sigma^2\cos^2(kr_s)
$$

The mean power retains clear oscillations despite the random amplitudes.

In an ensemble whose cosine and sine components are independent with equal variances, setting

$$
\langle A_k^2\rangle=\langle B_k^2\rangle
=\frac{\sigma^2}{2},
\qquad
\langle A_kB_k\rangle=0
$$

gives

$$
\langle X_k^2\rangle=\frac{\sigma^2}{2}
$$

Averaging oscillations with random temporal phases removes the oscillatory power pattern.

<iframe src="app/supporting.html?lang=en&amp;view=acoustic" title="Random acoustic realizations and coherent versus incoherent mean power" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

The figure shows how zero crossings align in the coherent ensemble and how oscillations survive in its mean power. Holding the acoustic distance $r_s$ at recombination fixed and varying the wavenumber $k$ produces a periodic sequence of peaks in wavenumber space.

In the actual CMB, gravitational driving, baryon inertia, neutrinos, diffusion damping, and recombination alter amplitudes and phases. Nevertheless, perturbations originating in an adiabatic growing mode share a common time evolution at each wavenumber and, after projection onto the sky, form acoustic peaks in the angular power spectrum $C_\ell$.

**The CMB acoustic peaks reflect primordial perturbations whose amplitudes were random but whose temporal phases were aligned.** This is an important trace of superhorizon growing-mode selection.

## Further notes and references

The figures and animations describe a free, linear Gaussian field on a de Sitter background. The main animation stops at $x=0.2$ so that the short-axis width remains visible. Further expansion strengthens squeezing and narrows the ellipse while preserving its phase-space area.

Conservation of the curvature perturbation assumes standard attractor inflation. In non-attractor models, $\zeta$ can evolve even on superhorizon scales, with its behavior determined by the corresponding $z(\eta)$. Decoherence and non-Gaussianity are further questions beyond the free-field squeezing considered here.

- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030): canonical variables, growing and decaying solutions, and their relation to semiclassicality.
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038): the distinction between classical correlation functions and quantum states.
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019): primordial initial conditions and the phase structure of the CMB acoustic peaks.
