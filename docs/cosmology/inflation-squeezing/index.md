# Inflationary Fluctuations and Squeezing

## 1. What is generated during inflation?

Inflation does not give a vacuum fluctuation a definite classical amplitude. It evolves a quantum state whose mean can remain zero while its correlations change enormously. For each Fourier wavelength, a nearly circular vacuum distribution in phase space becomes a long, thin Gaussian ellipse. The random amplitude that survives in its broad direction later supplies an initial condition for cosmological structure.

This article follows that geometry through three descriptions: a time-dependent oscillator, Bogoliubov mixing of creation and annihilation operators, and squeezing of a Wigner function. It then connects growing-mode dominance to the **temporal** phase coherence of acoustic oscillations. Random spatial Fourier phases remain random.


![Three stages of the same Wigner contour on fixed quadrature axes](app/teaser.svg)

Preview: three times for one standing mode, with the same field-amplitude and canonical-momentum quadratures at each time. The ellipse stretches but preserves its area. [Jump to the main animation](#main-animation), or follow the oscillator and basis changes that explain it.

## 2. Warm-up: a time-dependent harmonic oscillator

Consider a unit-mass oscillator with $H=(p^2+\omega^2(t)q^2)/2$. Choose a fixed positive reference frequency $\omega_0$ and let $b=(\sqrt{\omega_0}q+ip/\sqrt{\omega_0})/\sqrt2$. Then

$$
H=\frac{\omega_0^2+\omega^2}{2\omega_0}
\left(b^\dagger b+\frac12\right)
+\frac{\omega^2-\omega_0^2}{4\omega_0}
\left(b^2+b^{\dagger2}\right).
$$

The pair terms can deform the vacuum covariance. Alternatively, when $\omega(t)>0$, define an instantaneous annihilator with $\omega_0$ replaced by $\omega(t)$. Its total Heisenberg derivative is

$$
\dot b_{\mathrm{inst}}
=-i\omega b_{\mathrm{inst}}
+\frac{\dot\omega}{2\omega}b_{\mathrm{inst}}^\dagger.
$$

Now the mixing is explicit in the changing basis. These are two descriptions of the same evolution. The instantaneous positive-frequency prescription ceases to be available when $\omega^2\leq0$; the fixed canonical variables and their Gaussian covariance still make sense.

## 3. Real fields and independent degrees of freedom

Use a finite periodic box to avoid momentum delta functions in the notation. For a real field, $\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger$; for a classical realization, $v_{-\mathbf k}=v_{\mathbf k}^*$. Choose a half-space $\mathcal K_+$ containing exactly one member of each nonzero pair. Write

$$
v_{\mathbf k}=\frac{q_R+iq_I}{\sqrt2},\qquad
v_{-\mathbf k}=\frac{q_R-iq_I}{\sqrt2}.
$$

With Fourier convention $e^{i\mathbf k\cdot\mathbf x}$, this pair contributes $\sqrt2[q_R\cos(\mathbf k\cdot\mathbf x)-q_I\sin(\mathbf k\cdot\mathbf x)]$, up to the box normalization. It contains two real oscillators, a cosine amplitude and a sine amplitude. It does not contain four independent real field amplitudes.

Traveling-wave **annihilation operators** $a_{\mathbf k}$ and $a_{-\mathbf k}$, however, are independent operators: the field reality condition does **not** imply $a_{-\mathbf k}=a_{\mathbf k}^\dagger$. The field coefficient contains both annihilation and creation operators.

## 4. Inflationary perturbations as oscillators

For a canonical single inflaton with sound speed unity, the Mukhanov–Sasaki variable $v=z\zeta$ has

$$
z=\frac{a\dot\phi_0}{H},\qquad
S=\frac12\int d\eta\,d^3x\,
\left[(v')^2-(\nabla v)^2+\frac{z''}{z}v^2\right],
\qquad
v_k''+\left(k^2-\frac{z''}{z}\right)v_k=0.
$$

Here $\phi_0$ is the homogeneous inflaton, distinct from the test field in the animation. Each real mode is a time-dependent oscillator with effective squared frequency $k^2-z''/z$. Deep inside the Hubble radius, the background term is small and the Bunch–Davies condition selects the Minkowski-like positive-frequency mode. Its importance grows continuously around crossing.

For either real component, an action differing by a boundary term is especially useful for squeezing. Set $s=z'/z$:

$$
L_A=\frac12\left[(q_A'-sq_A)^2-k^2q_A^2\right],\qquad
p_A=q_A'-sq_A,
\qquad
H_{\eta,A}=\frac12(p_A^2+k^2q_A^2)
+\frac{s}{2}(q_Ap_A+p_Aq_A).
$$

The half-space action splits as $S_{\mathbf k}=S[q_R]+S[q_I]$. The symmetrized cross term is essential in the quantum Hamiltonian. Starting instead from the integrated action gives $\widetilde p=q'$ and $\widetilde H_\eta=[\widetilde p^{\,2}+(k^2-z''/z)q^2]/2$. Both yield the same second-order equation, but they assign different phase-space momenta. The animation uses the **first** convention, as in [Polarski and Starobinsky, equations (3)–(4)](https://arxiv.org/pdf/gr-qc/9504030).

For the animated test scalar, substitute $q=a\phi_A$ and $s=\mathcal H=a^\prime/a=-1/\eta$. Then $a''/a=2/\eta^2$, so the solution is exact. It also describes a suitably normalized free tensor polarization. For slow-roll curvature perturbations, $z''/z\simeq2/\eta^2$ and $z'/z\simeq-1/\eta$ give the analogous leading approximation. **An exactly de Sitter background with $\dot\phi_0=0$ has $z=0$**: the test scalar cannot be identified with $\zeta=v/z$ in that limit.

For this exact example, define $x$ and the e-fold time $N$ by

$$
a=-\frac1{H\eta},\qquad
x=-k\eta=\frac{k}{aH},\qquad
N=\ln\frac{a}{a_{\mathrm{cross}}}=-\ln x.
$$

A prime denotes a conformal-time derivative, with $d\eta=dt/a$. Throughout this article $\hbar=c=1$.

### Exact mode functions for the plotted example

For the animated model, let $b^{\mathrm{in}}$ annihilate the initial vacuum of one real mode. The positive-frequency coefficients in $\hat q=f_k b^{\mathrm{in}}+f_k^*b^{\mathrm{in}\dagger}$ and $\hat p=g_k b^{\mathrm{in}}+g_k^*b^{\mathrm{in}\dagger}$ are

$$
f_k=\frac{1+i/x}{\sqrt{2k}}e^{ix},\qquad
 g_k=f_k'-\mathcal H f_k=-i\sqrt{\frac{k}{2}}e^{ix},
\qquad f_kg_k^*-f_k^*g_k=i.
$$

<iframe src="app/supporting.html?lang=en&amp;view=background" title="Background term and exact de Sitter mode functions" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

Switch to **Mode functions** to compare $F_q=\sqrt{2k}f_k$ with $F_\phi=\sqrt{2k^3}f_k/(aH)=xF_q$. These are dimensionless normalizations of the rescaled and original field modes, respectively. Follow the solid curves toward the right: the original field tends to a constant while the rescaled mode grows. The background comparison uses a logarithmic vertical axis and separately marks equality of the two terms and Hubble crossing.

## 5. Traveling waves: two-mode squeezing

For a fixed pair of opposite traveling waves, the background couples creation and annihilation in pairs. With $s=z^\prime/z$ and each wavevector pair counted once, the Hamiltonian is

$$
H_{\eta,\mathbf k}=k\left(a_{\mathbf k}^\dagger a_{\mathbf k}
+a_{-\mathbf k}^\dagger a_{-\mathbf k}+1\right)
+is\left(a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger
-a_{\mathbf k}a_{-\mathbf k}\right).
$$

The interaction creates or annihilates one excitation in each opposite mode. This is the two-mode squeezing description.

In the Heisenberg picture,

$$
a_{\mathbf k}(\eta)=\alpha_k a_{\mathbf k}^{\mathrm{in}}
+\beta_k a_{-\mathbf k}^{\mathrm{in}\dagger},\qquad
|\alpha_k|^2-|\beta_k|^2=1,
\qquad
\alpha_k=e^{-i\theta_k}\cosh r_k,\quad
\beta_k=e^{i(\theta_k+2\varphi_k)}\sinh r_k.
$$

The standing-wave operators introduced in the next section obey the corresponding single-mode transformation with the same coefficients. The magnitude $r_k$ controls the principal widths. Using $Q=\sqrt{k}q$ and $P=p/\sqrt{k}$ (defined in detail with the animation), $\varphi_k=\arg(\alpha_k\beta_k)/2$ is the **broad-axis angle** from the positive $Q$ axis, modulo $\pi$. The rotation phase $\theta_k$ does not affect the covariance of an initial vacuum. Angle conventions in the literature can differ by signs or a right angle.

Using the exact coefficients above gives, without integrating a prescribed ellipse shape,

$$
\alpha_k=\left(1+\frac{i}{2x}\right)e^{ix},\qquad
\beta_k=-\frac{i}{2x}e^{-ix},\qquad
r_k=\operatorname{arsinh}\frac1{2x},\qquad
\varphi_k=-\frac12\arctan(2x).
$$

At $x\ll1$, $r_k\simeq-\ln x=N$: the squeezing grows approximately by one unit per e-fold after Hubble exit. The number $|\beta_k|^2$ is a reference-basis occupation, not a unique particle count in the evolving background. Even the numerical squeezing magnitude depends on the canonical quadratures used; the full covariance and its transformation law describe the state consistently.

<iframe src="app/supporting.html?lang=en&amp;view=squeezing" title="Squeezing magnitude and broad-axis angle versus e-fold time" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

Compare the exact curve with $r_k\simeq N$ after crossing. The second plot shows angle locking without confusing it with a fixed orientation at all times; for an almost circular early vacuum the angle is poorly distinguished geometrically.

## 6. Standing waves: two identical single-mode squeezings

Define $b_A=(\sqrt{k}q_A+ip_A/\sqrt{k})/\sqrt2$. The standing-wave Hamiltonian becomes

$$
H_{\eta,A}=k\left(b_A^\dagger b_A+\frac12\right)
+\frac{is}{2}\left(b_A^{\dagger2}-b_A^2\right),
\qquad A=R,I.
$$

Both real modes experience identical single-mode squeezing. Their relation to traveling-wave operators is

$$
b_R=\frac{a_{\mathbf k}+a_{-\mathbf k}}{\sqrt2},\qquad
b_I=-\frac{i}{\sqrt2}(a_{\mathbf k}-a_{-\mathbf k}),
\qquad
b_R^{\dagger2}+b_I^{\dagger2}
=2a_{\mathbf k}^\dagger a_{-\mathbf k}^\dagger.
$$

The pair term describes two-mode squeezing in the traveling basis. The same state factorizes into two equally squeezed states in the standing basis. The plotted ellipse is the state of **one standing mode**; it is not the reduced state obtained by discarding one member of a traveling pair. Entanglement between the traveling modes depends on this choice of subsystem, as discussed by [Martin and Vennin](https://arxiv.org/abs/1510.04038).

<iframe src="app/supporting.html?lang=en&amp;view=basis" title="Half of Fourier space and traveling-to-standing basis transformation" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1200px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

The shaded half-plane is a two-dimensional schematic of choosing one member of each pair; boundary modes require the same one-per-pair convention. Change the epoch to inspect the covariance matrices. The quadrature order is $(Q_+,P_+,Q_-,P_-)$ on the left and $(Q_R,P_R,Q_I,P_I)$ on the right. A nonzero off-diagonal block on the left becomes two independent identical blocks on the right. Both are complete descriptions of the same state, not successive stages of its time evolution.

<span id="main-animation"></span>

## 7. Main visualization: quadrature-space evolution

The animation follows **one fixed nonzero comoving wavenumber** $k=|\mathbf k|$, and one real standing-wave component $A=R$ or $I$. It is not a plot of different wavelengths, nor a spacetime diagram. The model is a free, massless, minimally coupled scalar field in exact de Sitter spacetime. We use $\hbar=c=1$ and absorb the spatial mode normalization into the real amplitude $\phi_A$.

At **every frame**, the horizontal and vertical axes are

$$
Q=\sqrt{k}\,q=\sqrt{k}\,a\phi_A,
\qquad
P=\frac{p}{\sqrt{k}}
=\frac{q'-\mathcal Hq}{\sqrt{k}}
=\frac{a\phi_A'}{\sqrt{k}},
\qquad \mathcal H=\frac{a'}a.
$$

A prime denotes a conformal-time derivative, $d\eta=dt/a$. Thus $Q$ is a rescaled **field amplitude**, not spatial position; $P$ is its rescaled **canonical momentum**, not the wavenumber $k$ and not $q'/\sqrt{k}$. These quadratures satisfy $[\hat Q,\hat P]=i$. Their definitions, orientation, numerical limits, and equal horizontal/vertical scale stay fixed throughout playback. The factor $a$ in the relation to the original field nevertheless evolves: a growing $Q$ need not mean a growing $\phi_A$.

Time advances with the e-fold variable $N=-\ln x$ defined above.

The slider runs from $x=12$ to $x=0.2$; $N=0$ marks Hubble crossing. Here “inside/outside the horizon” means relative to the Hubble scale, not a separate causal boundary. See [Cosmic Causal Structure](../cosmic-causal-structure/) for that distinction.

<iframe src="app/index.html?lang=en" title="Inflationary squeezing: rotation, squeeze, and total Hamiltonian flow" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

The first two panels split the **instantaneous velocity field** into rotation and squeezing. Only the third panel contains the evolving quantum-state contour. The orange points are markers transported along that contour, not particles with definite quantum trajectories. All arrows share a time-dependent display factor $1/\sqrt{1+x^2}$ and an additional fixed drawing scale. This preserves vector addition within a frame, but arrow lengths across different frames are not unmodified physical speeds. The state itself uses the exact, unscaled dynamics.

Try the following:

1. Play from the beginning. Rotation dominates at large $x$, while the ellipse stretches as $x$ falls below unity. The initial contour is only approximately circular: it is the exact Bunch–Davies state evaluated at a finite starting time.
2. Pause at Hubble crossing. The flow is a nonzero shear, not a stationary field. Squeezing has not suddenly switched on.
3. At late times, switch between the ellipse axes, instantaneous flow directions, and exact solution directions. They answer different questions and generally do not coincide.
4. Inspect the vertical spread. It stays constant even though the ellipse has a shrinking **principal** width. The squeezed variable is a correlated combination of $Q$ and $P$.

### The Wigner contour and its exact flow

Writing $\mathbf Z=(Q,P)^T$ and $\Sigma_{ij}=\langle\{\hat Z_i,\hat Z_j\}\rangle/2$, the zero-mean vacuum evolves to

$$
\Sigma(x)=\frac12
\begin{pmatrix}1+x^{-2}&-x^{-1}\\-x^{-1}&1\end{pmatrix},
\qquad
\det\Sigma=\frac14,\qquad
\sigma_\pm^2=\frac12e^{\pm2r_k}.
$$

The Wigner function is positive in this Gaussian example:

$$
W(\mathbf Z)=\frac{1}{2\pi\sqrt{\det\Sigma}}
\exp\left[-\frac12\mathbf Z^T\Sigma^{-1}\mathbf Z\right].
$$

The outlined ellipse is $\mathbf Z^T\Sigma^{-1}\mathbf Z=1$, where the Wigner density is $e^{-1/2}$ times its central value. Its enclosed Wigner weight is $1-e^{-1/2}\simeq0.393$, not the one-dimensional “one sigma means 68%” value. Its semiaxes are $e^{\pm r_k}/\sqrt2$ and its area is always $\pi/2$. Unitary squeezing conserves area; it is not dissipative cooling. Positivity does not make this a joint probability for simultaneous sharp measurements of noncommuting $Q$ and $P$.

Converting the Hamiltonian from conformal time to $N$ gives

$$
K_N=\frac{x}{2}(Q^2+P^2)+\frac12(QP+PQ),\qquad
\frac{d\mathbf Z}{dN}
=\underbrace{\begin{pmatrix}1&x\\-x&-1\end{pmatrix}}_{A(N)}\mathbf Z
=x\begin{pmatrix}0&1\\-1&0\end{pmatrix}\mathbf Z
+\begin{pmatrix}1&0\\0&-1\end{pmatrix}\mathbf Z.
$$

This is precisely the split shown in the three panels. A quadratic Hamiltonian transports the Wigner function by the same linear flow as the classical Hamilton equations. The covariance obeys $d\Sigma/dN=A\Sigma+\Sigma A^T$; the vanishing trace of $A$ preserves phase-space area.

The instantaneous eigenvalues are $\lambda_\pm=\pm\sqrt{1-x^2}$. They are imaginary for $x>1$ and real for $x<1$. At $x=1$, $A^2=0$ but $A\ne0$: a shear. These statements classify the flow **frozen at one time**. Actual trajectories follow a time-ordered evolution and need not align with instantaneous eigenvectors.

This classification itself depends on the momentum convention. In the integrated-action variables,

$$
\widetilde P=P+\frac Qx,\qquad
\frac{d}{dN}\begin{pmatrix}Q\\\widetilde P\end{pmatrix}
=\begin{pmatrix}0&x\\2/x-x&0\end{pmatrix}
\begin{pmatrix}Q\\\widetilde P\end{pmatrix}.
$$

The eigenvalues now become $\pm\sqrt{2-x^2}$. The time-dependent canonical transformation changes the instantaneous elliptic/hyperbolic boundary, while the physical Hubble crossing remains $x=1$ and the field equation remains unchanged.

## 8. Growing and decaying modes as phase-space directions

Neglecting gradients in the superhorizon equation gives

$$
q=Cz+Dz\int^\eta\frac{d\eta'}{z^2(\eta')},\qquad
p=q'-\frac{z'}zq=\frac Dz.
$$

The integration constant in the primitive can be absorbed into $C$. In an attractor inflationary background, the first solution gives constant $\zeta=q/z$, while the independent second contribution decays. For the test scalar replace $z$ by $a$: $q$ grows approximately as $a$, while $\phi_A=q/a$ freezes.

The zero-gradient formula does not set the finite-$k$ momentum of the growing solution exactly to zero. For the animation, exact growing and decaying solution vectors can be chosen as

$$
\mathbf G(x)=\begin{pmatrix}\sin x+\cos x/x\\-\cos x\end{pmatrix},\qquad
\mathbf D(x)=\begin{pmatrix}\cos x-\sin x/x\\\sin x\end{pmatrix},
\qquad
\mathbf G\sim\begin{pmatrix}x^{-1}\\-1\end{pmatrix},\quad
\mathbf D\sim\begin{pmatrix}-x^2/3\\x\end{pmatrix}.
$$

In the [main animation](#main-animation), choose **Exact growing / decaying solutions** and compare with **Ellipse principal axes** at the same time.

These are solution directions, not eigenvectors of the instantaneous generator. They are not orthogonal. In contrast, covariance principal axes are orthogonal by construction. At late times their broad and narrow directions approach the horizontal and vertical limits of $\mathbf G$ and $\mathbf D$, respectively, but their finite-time slopes differ. “The short axis is the decaying mode” is therefore only a limiting geometric description.

A more precise statement of the narrowing uses the Gaussian conditional relation:

$$
\mathbb E[P\mid Q]=-\frac{x}{1+x^2}Q,\qquad
\operatorname{Var}(P\mid Q)=\frac{x^2}{2(1+x^2)},
\qquad \operatorname{Var}(P)=\frac12.
$$

Here conditioning refers to the positive Wigner density, not a simultaneous projective measurement protocol. It shows why the uncertainty transverse to a classical-looking relation shrinks even though the marginal spread of $P$ does not. Suppression of the decaying **contribution** does not mean that its time-independent integration coefficient must itself disappear.

## 9. Why the perturbation looks classical

The mean remains zero, but the field variance need not vanish. For example, the same exact mode function gives the test-scalar power per logarithmic interval

$$
\mathcal P_\phi(k)=\frac{k^3}{2\pi^2}\left|\frac{f_k}{a}\right|^2
=\frac{H^2}{4\pi^2}(1+x^2)
\longrightarrow\left(\frac{H}{2\pi}\right)^2.
$$

The stretching of $q$ is compatible with a finite frozen variance of the original field. For curvature perturbations the background factor is instead $z$, and its slow-roll dynamics determines the amplitude and spectral tilt.

The positive Wigner function can reproduce equal-time, symmetrically ordered moments by a classical Gaussian ensemble. Large squeezing adds a strong field–momentum relation and growing-mode dominance, allowing the relevant perturbations to be evolved effectively as a stochastic classical field. It does **not** remove the commutator, collapse the wavefunction, or change this pure state into a mixed state. Environmental decoherence is a separate physical process, absent from this calculation; distinguishing these notions matters for claims about observable quantum signatures ([Martin and Vennin](https://arxiv.org/abs/1510.04038)).

<iframe src="app/supporting.html?lang=en&amp;view=samples" title="Wigner samples before and after symplectic evolution" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

Move the time slider from the initial state to the end. The samples do not become less random: their broad amplitude range grows, while their transverse spread about the orange conditional-mean line becomes small. Both panels use the same fixed scale; the analytic contour encloses only about 39% of the Wigner weight, so points outside it are expected.

## 10. Acoustic phase coherence and the CMB

For a statistically homogeneous Gaussian field, the two standing components have equal variances and no preferred orientation in their amplitude plane. Hence

$$
\zeta_{\mathbf k}=\frac{\zeta_R+i\zeta_I}{\sqrt2}
$$

has a stochastic spatial phase $\arg\zeta_{\mathbf k}$. Inflation does not set all these phases equal. Translating the spatial origin changes them; none of this is what acoustic phase coherence means.

After horizon re-entry, a schematic acoustic variable has two temporal solutions,

$$
X_k(\eta)=A_k\cos(kr_s)+B_k\sin(kr_s),\qquad
r_s(\eta)=\int^\eta c_s(\eta')\,d\eta'.
$$

If a single adiabatic growing mode supplies the initial conditions, density and velocity are linked: $A_k$ and $B_k$ are not two arbitrary independent random inputs. In an idealized undriven oscillator one can choose the time origin so that $B_k\simeq0$. Random amplitudes then share a common temporal transfer function. This connection between initial conditions and acoustic peaks is developed by [Hu and White](https://arxiv.org/abs/astro-ph/9602019).

The visualization below uses two ensembles with the same total initial variance. Writing $\sigma^2$ for that variance,

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

Thus random amplitudes do not erase the oscillatory power pattern; independent random temporal quadratures do. Real CMB transfer functions include gravitational driving, baryon loading, neutrino effects, diffusion, recombination, and projection onto the sky. They are not pure cosines. Coherent acoustic peaks test the structure of primordial initial conditions; they are not by themselves a measurement of quantum squeezing or proof of a unique inflationary origin.

<iframe src="app/supporting.html?lang=en&amp;view=acoustic" title="Random acoustic realizations and coherent versus incoherent ensemble power" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

Pause the cursor at a zero of the coherent histories. All eight coherent samples cross zero together, even though their amplitudes and signs differ. The incoherent samples do not. The lower panel separates finite-sample estimates from the exact ensemble predictions; it is the variation across wavenumber at a fixed sound horizon that makes the analogous peak pattern.

## Scope and further reading

The animation uses linear, free Gaussian evolution on a prescribed de Sitter background. It does not model reheating, environmental interactions, non-Gaussianity, or a numerical CMB spectrum. The main animation ends at $x=0.2$ to keep the thin ellipse visible on fixed axes. Greater squeezing would require resolving a much smaller transverse scale, not changing the uncertainty relation.

The familiar growing-mode conclusion assumes an attractor background. In non-attractor inflation the evolution of $\zeta$ can differ; one must solve the appropriate $z(\eta)$ problem rather than transplant this de Sitter example.

- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030): canonical variables, mode functions, and the growing/decaying description.
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038): subsystem choices and distinctions between classical correlators and quantum states.
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019): acoustic initial conditions and the interpretation of peak patterns.
