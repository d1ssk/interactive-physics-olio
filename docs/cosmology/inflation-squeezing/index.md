---
title: Inflationary quantum fluctuations and squeezing
---

# Inflationary quantum fluctuations and squeezing

<span class="center-material-tables"></span>

The temperature anisotropies of the CMB and the large-scale distribution of galaxies grew from small primordial fluctuations in the early universe. Inflationary theory traces these fluctuations to quantum fields in an accelerating spacetime.

This article follows the **two-point correlation of the field**. In a quantum state, field values at different positions are generally correlated even when the mean field vanishes. Starting with the quantum field in real space, we follow how cosmic expansion determines this correlation and how it survives into the later universe.

Squeezing appears along the way. On a homogeneous background, Fourier decomposition organizes the field into pairs of opposite wavevectors $\mathbf k$ and $-\mathbf k$ that evolve together. Traveling waves reveal **two-mode squeezing**; expressing the same two degrees of freedom as cosine and sine standing waves reveals two independent instances of **single-mode squeezing**. We establish their relation through Hamiltonian symmetries, number-state representations, and phase space.

<figure style="margin-inline: auto; text-align: center;">
  <img src="app/teaser.svg" alt="Wigner contours of one standing-wave quantum state at three times on the same canonical axes" width="720" height="250" style="display: block; max-width: 100%; height: auto; margin-inline: auto;">
</figure>

The figure shows the quantum state of one standing-wave mode at three times in the same phase space, using the exact solution in §8. The horizontal and vertical axes are dimensionless coordinates built from the field amplitude and momentum. The nearly circular subhorizon distribution becomes an elongated ellipse in the superhorizon regime while preserving its area.

The article proceeds as follows. The [main animation](#main-animation) is in §8.

1. Describe the quantum theory in real space and choose canonical variables (§1–2).
2. Decompose into wavevector pairs and derive the relation between two-mode and single-mode squeezing (§3–6).
3. Represent squeezing as a phase-space ellipse and connect it to spatial correlations (§7).
4. Calculate the development of squeezing in an exactly solvable model (§8).
5. Follow field freezing to a classical description of primordial fluctuations and acoustic peaks, then look beyond linear theory (§9–10).

## 1. Quantum fields in real space and equal-time correlations

### Background and the degree of freedom to quantize

Consider inflation driven by one scalar field with a standard kinetic term, the inflaton, in general relativity. The background is a spatially flat, homogeneous, isotropic universe,

$$
ds_0^2=-dt^2+a^2(t)\,d\mathbf x^2=a^2(\eta)\left(-d\eta^2+d\mathbf x^2\right)\tag{1}\label{eq:inflation-1}
$$

where $\mathbf x$ denotes comoving coordinates, $a$ the scale factor, and $\eta$ conformal time. We write $H=\dot a/a$ and $\mathcal H=a'/a=aH$; dots denote derivatives with respect to cosmic time $t$, and primes derivatives with respect to $\eta$. We use $c=\hbar=1$.

The scale factor $a$ and background inflaton $\phi_0$ are prescribed functions of time obeying the classical background equations. We quantize the **perturbations** on this background.

For linear perturbations of a single field, solving the gravitational constraints leaves one propagating scalar degree of freedom. We describe it by the comoving curvature perturbation $\hat\zeta$. On time slices where the inflaton is homogeneous, we adopt the sign convention

$$
\hat g_{ij}=a^2(1-2\hat\zeta)\,\delta_{ij}\tag{2}\label{eq:inflation-2}
$$

for the spatial metric at linear order. Our $\zeta$ has the opposite sign to the convention $g_{ij}=a^2e^{2\zeta}\delta_{ij}$, but the two-point function is the same. In terms of the inflaton fluctuation $\delta\hat\phi_{\mathrm{flat}}$ on spatially flat slices, the linear gauge transformation expresses the same degree of freedom as

$$
\hat\zeta=\frac{H}{\dot\phi_0}\,\delta\hat\phi_{\mathrm{flat}}\qquad(\dot\phi_0\neq0)\tag{3}\label{eq:inflation-3}
$$

This is the same scalar perturbation in a different slicing.

After solving the constraints, the quadratic action is

$$
S_2[\zeta]=\frac12\int d\eta\,d^3x\;z^2\left[(\zeta')^2-(\nabla\zeta)^2\right],\qquad z=\frac{a\dot\phi_0}{H}\tag{4}\label{eq:inflation-4}
$$

Here $z$ depends only on the background and incorporates both cosmic expansion and the motion of the background inflaton. A derivation is given in [Baumann’s lectures](https://arxiv.org/abs/0907.5424). Through §9 we use the linear quantum theory defined by this quadratic action. Cubic and higher interactions enter in §10.

### Canonical quantization (Heisenberg picture)

With conjugate momentum density $\hat\Pi_\zeta=z^2\hat\zeta'$, the equal-time canonical commutator is

$$
[\hat\zeta(\eta,\mathbf x),\hat\Pi_\zeta(\eta,\mathbf y)]=i\,\delta^{(3)}(\mathbf x-\mathbf y)\tag{5}\label{eq:inflation-5}
$$

while fields commute with fields and momenta with momenta. The Hamiltonian generating conformal-time evolution is

$$
\hat H_\zeta(\eta)=\frac12\int d^3x\left[\frac{\hat\Pi_\zeta^{\,2}}{z^2}+z^2(\nabla\hat\zeta)^2\right]\tag{6}\label{eq:inflation-6}
$$

Its time dependence enters through the background coefficient $z(\eta)$. The Heisenberg equation $\hat O'=i[\hat H_\zeta,\hat O]$ gives the local field equation

$$
\bigl(z^2\hat\zeta'\bigr)'-z^2\nabla^2\hat\zeta=0\tag{7}\label{eq:inflation-7}
$$

The fluctuation amplitude is determined by specifying the **quantum state** in which products of these operators are averaged.

### Wave functional (Schrödinger picture)

In the Schrödinger picture, the operators $\hat\zeta_{\mathrm S}(\mathbf x)$ and $\hat\Pi_{\zeta,\mathrm S}(\mathbf x)$ are fixed, and the state evolves according to $i\partial_\eta|\Psi(\eta)\rangle=\hat H_\zeta(\eta)|\Psi(\eta)\rangle$. The **wave functional** $\Psi_\eta[\zeta]=\langle\zeta|\Psi(\eta)\rangle$, expressed in simultaneous eigenstates $|\zeta\rangle$ of $\hat\zeta_{\mathrm S}(\mathbf x)$, assigns an amplitude to each field configuration $\zeta(\mathbf x)$ across space. Representing $\hat\Pi_{\zeta,\mathrm S}$ by $-i\,\delta/\delta\zeta(\mathbf x)$ gives

$$
i\partial_\eta\Psi_\eta[\zeta]=\frac12\int d^3x\left[-\frac1{z^2}\frac{\delta^2}{\delta\zeta(\mathbf x)^2}+z^2(\nabla\zeta)^2\right]\Psi_\eta[\zeta]\tag{8}\label{eq:inflation-8}
$$

This is a formal expression for a continuum of infinitely many degrees of freedom; a precise treatment includes finite-volume or short-distance regularization.

Because the Hamiltonian is quadratic, a zero-mean Gaussian state remains Gaussian. Using a complex kernel $\mathcal K_\eta$, such a state can be written as

$$
\Psi_\eta[\zeta]=\mathcal N_\eta\exp\left[-\frac12\int d^3x\,d^3y\;\zeta(\mathbf x)\,\mathcal K_\eta(\mathbf x,\mathbf y)\,\zeta(\mathbf y)\right]\tag{9}\label{eq:inflation-9}
$$

The real part of the kernel determines the width in configuration space; its imaginary part determines the wave-functional phase, and hence field–momentum correlations. If the background and state are homogeneous and isotropic, the kernel depends only on the distance $|\mathbf x-\mathbf y|$. This **translation-invariant quadratic form** is our starting point for understanding squeezing from §3 onward.

### Goal: equal-time spatial correlations

Our goal is to calculate the field’s two-point correlation at time $\eta$,

$$
G_\zeta(\eta;\mathbf x,\mathbf y)=\langle\Psi(\eta)|\hat\zeta_{\mathrm S}(\mathbf x)\hat\zeta_{\mathrm S}(\mathbf y)|\Psi(\eta)\rangle=\langle\Psi_0|\hat\zeta_{\mathrm H}(\eta,\mathbf x)\hat\zeta_{\mathrm H}(\eta,\mathbf y)|\Psi_0\rangle\tag{10}\label{eq:inflation-10}
$$

The middle expression uses the Schrödinger picture, and the right-hand expression the Heisenberg picture. With $U(\eta,\eta_0)$ the evolution operator generated by $\hat H_\zeta$, we have $|\Psi(\eta)\rangle=U|\Psi_0\rangle$ and $\hat\zeta_{\mathrm H}=U^\dagger\hat\zeta_{\mathrm S}U$. Since the mean vanishes, this is also the connected two-point function.

In wave-functional language, $G_\zeta$ is the average of $\zeta(\mathbf x)\zeta(\mathbf y)$ with configuration probability density $|\Psi_\eta[\zeta]|^2$, determined by the real part of $\mathcal K_\eta$. **Both field evolution and the initial state determine spatial correlations.**

### Picture, canonical variables, and mode basis

The calculation involves three independent choices.

| Choice | What it determines | Use in this article |
| --- | --- | --- |
| Picture | Whether states (Schrödinger) or operators (Heisenberg) carry time evolution | Heisenberg for operator evolution and expectation values; Schrödinger for the state and Wigner distribution |
| Canonical variables | Configuration variable and conjugate momentum used to describe the state | From $\zeta$ to the canonically normalized $v=z\zeta$ (§2) |
| Mode basis | How field degrees of freedom are divided | Traveling or standing waves for one wavevector pair (§3) |

Expectation values are independent of the picture. Canonical variables and mode basis affect **how the state appears**, including the shape of its squeezing ellipse and whether subsystems are entangled, but physical quantities such as $G_\zeta$ are common to all descriptions. Section headings or opening paragraphs specify the choices below.

## 2. The canonical variable $v=z\zeta$

### The Mukhanov–Sasaki variable

For mode calculations, it is convenient to use the **Mukhanov–Sasaki variable**, whose kinetic term has unit coefficient,

$$
v=z\zeta=a\,\delta\phi_{\mathrm{flat}}\tag{11}\label{eq:inflation-11}
$$

The variables $\zeta$, $\delta\phi_{\mathrm{flat}}$, and $v$ describe the same degree of freedom with different background normalizations.

Setting $s(\eta)=z'/z$ and rewriting the action without dropping a boundary term gives

$$
S_2[v]=\frac12\int d\eta\,d^3x\left[(v'-sv)^2-(\nabla v)^2\right]\tag{12}\label{eq:inflation-12}
$$

The conjugate momentum and Hamiltonian are

$$
\pi=v'-sv=z\zeta'=\frac{\Pi_\zeta}{z},\tag{13}\label{eq:inflation-13}
$$

$$
\hat H_v(\eta)=\frac12\int d^3x\left[\hat\pi^2+(\nabla\hat v)^2+s\,(\hat v\hat\pi+\hat\pi\hat v)\right]\tag{14}\label{eq:inflation-14}
$$

The cross term is symmetrized to make it Hermitian. We have $[\hat v(\eta,\mathbf x),\hat\pi(\eta,\mathbf y)]=i\,\delta^{(3)}(\mathbf x-\mathbf y)$; eliminating momentum from the Heisenberg equations gives the Mukhanov–Sasaki equation,

$$
\hat v''-\nabla^2\hat v-\frac{z''}{z}\hat v=0\tag{15}\label{eq:inflation-15}
$$

This is the equation governing the canonical field.

### Time-dependent changes of variables and pictures

The transformation $\hat v=z\hat\zeta$ has a time-dependent coefficient and is independent of a change of picture. Constructing the operator corresponding to $v$ while retaining the Schrödinger picture of §1 gives the explicitly time-dependent operator $z(\eta)\hat\zeta_{\mathrm S}(\mathbf x)$. The time derivative of a Heisenberg operator $\hat O_{\mathrm H}=U^\dagger\hat O_{\mathrm S}(\eta)U$ is

$$
\frac{d\hat O_{\mathrm H}}{d\eta}=i[\hat H_{\mathrm H},\hat O_{\mathrm H}]+U^\dagger\left(\partial_\eta\hat O_{\mathrm S}\right)U\tag{16}\label{eq:inflation-16}
$$

Thus the $z'$ term in $\hat v'=z'\hat\zeta+z\hat\zeta'$ comes from explicit time dependence.

To use a Schrödinger picture with $v$ as a time-independent configuration variable, we reformulate the quantum theory in terms of $v$. Its Hamiltonian is $\hat H_v$ above, with the time-dependent canonical transformation encoded in the cross term $s(\hat v\hat\pi+\hat\pi\hat v)$. The state changes representation at the same time: $\Psi^{(v)}_\eta[v]\propto\Psi_\eta[v/z(\eta)]$, with the proportionality factor chosen to preserve normalization.

**Below, “fixed axes” and “the Schrödinger-picture state” refer to this $v$ representation.** The Wigner plots show a state evolving under $\hat H_v$ on coordinate axes built from fixed $v,\pi$.

There is also freedom in the momentum choice. Adding a total time derivative to the action allows the conjugate momentum $\tilde\pi=v'=\pi+sv$. The equation of motion stays the same, while phase-space plots change by a shear. Throughout this article we use $\pi=v'-sv$. In the example of §8, this $\pi$ is proportional to the original field’s velocity, making freezing easier to interpret.

## 3. Wavevector pairs and two mode bases (Schrödinger picture)

In this section we construct a basis of time-independent operators from the Schrödinger operators $\hat v,\hat\pi$ in the $v$ representation of §2. We omit the subscript $\mathrm S$.

### Fourier expansion and box regularization

To discuss the quantum state of an individual mode, introduce a box of comoving volume $V$ with periodic boundary conditions as a regulator. At the end we take $V\to\infty$ and retain only quantities independent of $V$.

$$
\hat v(\mathbf x)=\frac1{\sqrt V}\sum_{\mathbf k}\hat v_{\mathbf k}\,e^{i\mathbf k\cdot\mathbf x},\qquad\hat v_{\mathbf k}=\frac1{\sqrt V}\int_V d^3x\,e^{-i\mathbf k\cdot\mathbf x}\,\hat v(\mathbf x)\tag{17}\label{eq:inflation-17}
$$

Expand the momentum $\hat\pi$ in the same way. The coefficient $\hat v_{\mathbf k}$ is one component extracted from the entire field; Fourier expansion changes the basis of the full quantum field. We exclude the homogeneous component $\mathbf k=\mathbf 0$, which can be absorbed into the background, and consider $k=|\mathbf k|>0$. Hermiticity and the canonical commutator imply

$$
\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger,\qquad\hat\pi_{-\mathbf k}=\hat\pi_{\mathbf k}^\dagger,\qquad[\hat v_{\mathbf k},\hat\pi_{\mathbf k'}]=i\,\delta_{\mathbf k,-\mathbf k'}\tag{18}\label{eq:inflation-18}
$$

The background coefficients are position independent, and plane waves are eigenfunctions of $-\nabla^2$, so the Hamiltonian becomes

$$
\hat H_v=\sum_{\mathbf k}\frac12\left[\hat\pi_{\mathbf k}\hat\pi_{-\mathbf k}+k^2\hat v_{\mathbf k}\hat v_{-\mathbf k}+s\left(\hat v_{\mathbf k}\hat\pi_{-\mathbf k}+\hat\pi_{-\mathbf k}\hat v_{\mathbf k}\right)\right]\tag{19}\label{eq:inflation-19}
$$

Each term connects $\mathbf k$ to $-\mathbf k$: **opposite wavevectors appear in pairs**. Different pairs evolve independently, allowing us to factor the Hilbert space by wavevector pair.

### Standing waves: real cosine and sine amplitudes

Take one nonzero pair $(\mathbf k,-\mathbf k)$. Although $\hat v_{\mathbf k}$ is not Hermitian, $\hat v_{-\mathbf k}=\hat v_{\mathbf k}^\dagger$ allows the two Fourier coefficients to be recombined into two Hermitian configuration operators. Let $\mathcal K_+$ contain one member of each pair. For $\mathbf k\in\mathcal K_+$ define

$$
\hat q_{c,\mathbf k}=\frac{\hat v_{\mathbf k}+\hat v_{-\mathbf k}}{\sqrt2},\qquad\hat q_{s,\mathbf k}=\frac{i(\hat v_{\mathbf k}-\hat v_{-\mathbf k})}{\sqrt2}\tag{20}\label{eq:inflation-20}
$$

Applying the same transformation to $\hat\pi$ gives $\hat p_{c,\mathbf k},\hat p_{s,\mathbf k}$. For $A,B\in\{c,s\}$,

$$
[\hat q_{A,\mathbf k},\hat p_{B,\mathbf k'}]=i\,\delta_{AB}\,\delta_{\mathbf k,\mathbf k'}\tag{21}\label{eq:inflation-21}
$$

with all other pairs commuting. The field becomes

$$
\hat v(\mathbf x)=\sqrt{\frac2V}\sum_{\mathbf k\in\mathcal K_+}\left[\hat q_{c,\mathbf k}\cos(\mathbf k\cdot\mathbf x)+\hat q_{s,\mathbf k}\sin(\mathbf k\cdot\mathbf x)\right]\tag{22}\label{eq:inflation-22}
$$

a superposition of cosine and sine **standing waves** extending throughout space. Thus **one wavevector pair contains two independent quantum oscillators, with a four-dimensional canonical phase space**.

### Decomposing the Gaussian state

Insert this decomposition into the Gaussian wave functional $\eqref{eq:inflation-9}$. Let $K_k(\eta)$ be the Fourier transform of the kernel $\mathcal K_\eta(\mathbf x-\mathbf y)$ in the $v$ representation. Then

$$
\int d^3x\,d^3y\;v(\mathbf x)\,\mathcal K_\eta(\mathbf x-\mathbf y)\,v(\mathbf y)=\sum_{\mathbf k}K_k\,v_{\mathbf k}v_{-\mathbf k}=\sum_{\mathbf k\in\mathcal K_+}K_k\left(q_{c,\mathbf k}^2+q_{s,\mathbf k}^2\right)\tag{23}\label{eq:inflation-23}
$$

Consequently,

$$
\Psi^{(v)}_\eta[v]\propto\prod_{\mathbf k\in\mathcal K_+}\exp\left[-\frac{K_k(\eta)}2q_{c,\mathbf k}^2\right]\exp\left[-\frac{K_k(\eta)}2q_{s,\mathbf k}^2\right].\tag{24}\label{eq:inflation-24}
$$

Written in complex traveling-wave amplitudes, the quadratic form $K_k\,v_{\mathbf k}v_{-\mathbf k}$ connects $\mathbf k$ and $-\mathbf k$. In real standing-wave amplitudes it is diagonal, and the state factors into **identical one-variable Gaussians**. These are the prototypes of the two-mode and single-mode squeezing descriptions: both express the same structure of a translation-invariant Gaussian state of a real field.

The standing-wave split depends on the choice of coordinate origin. Shifting the origin by $\mathbf d$ sends $v_{\mathbf k}\to e^{i\mathbf k\cdot\mathbf d}v_{\mathbf k}$ and rotates $(q_c,q_s)$. The two Gaussians have the same width and phase, so their product is invariant under this rotation.

### Traveling waves: creation and annihilation operators

To use number states, define **traveling-wave annihilation operators** with a fixed positive reference frequency $k$.

$$
\hat a_{\mathbf k}=\frac1{\sqrt2}\left(\sqrt k\,\hat v_{\mathbf k}+\frac{i\hat\pi_{\mathbf k}}{\sqrt k}\right),\qquad[\hat a_{\mathbf k},\hat a_{\mathbf k'}^\dagger]=\delta_{\mathbf k,\mathbf k'}\tag{25}\label{eq:inflation-25}
$$

Inverting these definitions gives

$$
\hat v_{\mathbf k}=\frac{\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger}{\sqrt{2k}},\qquad\hat\pi_{\mathbf k}=-i\sqrt{\frac k2}\left(\hat a_{\mathbf k}-\hat a_{-\mathbf k}^\dagger\right)\tag{26}\label{eq:inflation-26}
$$

The operators $\hat a_{\mathbf k}$ and $\hat a_{-\mathbf k}$ are independent annihilation operators. In position space, $\hat a_{\mathbf k}$ multiplies the traveling wave $e^{i\mathbf k\cdot\mathbf x}$. The reference frequency $k$ is a fixed number chosen to define these operators.

### Relation between the two bases

For each standing wave, define an annihilation operator and dimensionless quadratures using the same reference frequency.

$$
\hat b_{A,\mathbf k}=\frac{\hat Q_{A,\mathbf k}+i\hat P_{A,\mathbf k}}{\sqrt2},\qquad\hat Q_{A,\mathbf k}=\sqrt k\,\hat q_{A,\mathbf k},\qquad\hat P_{A,\mathbf k}=\frac{\hat p_{A,\mathbf k}}{\sqrt k}\tag{27}\label{eq:inflation-27}
$$

We have $[\hat Q_{A,\mathbf k},\hat P_{A,\mathbf k}]=i$, and $Q,P$ will be the axes of the Wigner plots. Comparing definitions gives

$$
\hat a_{\pm\mathbf k}=\frac{\hat b_{c,\mathbf k}\mp i\,\hat b_{s,\mathbf k}}{\sqrt2},\qquad\hat b_{c,\mathbf k}=\frac{\hat a_{\mathbf k}+\hat a_{-\mathbf k}}{\sqrt2},\qquad\hat b_{s,\mathbf k}=\frac{i(\hat a_{\mathbf k}-\hat a_{-\mathbf k})}{\sqrt2}\tag{28}\label{eq:inflation-28}
$$

This unitary transformation mixes only annihilation operators, so the vacuum $|0_{\mathrm{ref}}\rangle$ for reference frequency $k$ is common to both bases.

$$
\hat a_{\mathbf k}|0_{\mathrm{ref}}\rangle=\hat a_{-\mathbf k}|0_{\mathrm{ref}}\rangle=0\iff\hat b_{c,\mathbf k}|0_{\mathrm{ref}}\rangle=\hat b_{s,\mathbf k}|0_{\mathrm{ref}}\rangle=0\tag{29}\label{eq:inflation-29}
$$

We choose the actual initial state in §5. The two traveling-wave modes and the two standing-wave modes are two bases for the same two degrees of freedom.

## 4. The wavevector-pair Hamiltonian: two-mode and single-mode squeezing

### Traveling-wave representation (Schrödinger picture)

Combine the $\mathbf k$ and $-\mathbf k$ terms of the Hamiltonian $\eqref{eq:inflation-19}$ into $\hat H_{\mathbf k}$, and express $\hat v_{\pm\mathbf k},\hat\pi_{\pm\mathbf k}$ in terms of $\hat a_{\pm\mathbf k}$:

$$
\hat H_v=\sum_{\mathbf k\in\mathcal K_+}\hat H_{\mathbf k},\tag{30}\label{eq:inflation-30}
$$

$$
\hat H_{\mathbf k}=k\left(\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger\hat a_{-\mathbf k}+1\right)+i\,s(\eta)\left(\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger-\hat a_{\mathbf k}\hat a_{-\mathbf k}\right)\tag{31}\label{eq:inflation-31}
$$

This separates the reference oscillators from the pair interaction.

The first term describes two oscillators of reference frequency $k$. In the second term, $\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger$ **creates one excitation at each of the opposite wavevectors**, and $\hat a_{\mathbf k}\hat a_{-\mathbf k}$ reverses that process.

$$
\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger|n_{\mathbf k},n_{-\mathbf k}\rangle=\sqrt{(n_{\mathbf k}+1)(n_{-\mathbf k}+1)}\;|n_{\mathbf k}+1,n_{-\mathbf k}+1\rangle\tag{32}\label{eq:inflation-32}
$$

The coefficient $s=z'/z$ measures the rate of background evolution and sources excitation pairs. The transformation generated by this Hamiltonian is called **two-mode squeezing**.

### The general form from symmetry

This structure follows generally from three conditions.

1. **Quadratic Hamiltonian:** a free-field Hamiltonian is quadratic in creation and annihilation operators.
2. **Spatial translation symmetry:** the total field momentum is $\hat{\mathbf P}=\sum_{\mathbf k}\mathbf k\,\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}$ independently of the reference frequency, and $[\hat{\mathbf P},\hat H_v]=0$ on a homogeneous background. Momentum-conserving quadratic terms are restricted to terms of the form $\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}$ and pair terms $\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger$, $\hat a_{\mathbf k}\hat a_{-\mathbf k}$.
3. **Time-dependent background:** for a stable, time-independent Hamiltonian, one fixed choice of basis can eliminate the pair terms. When the background changes, the diagonalizing basis also changes, so pair terms remain in a fixed basis.

Thus, for a free field on a homogeneous, isotropic, time-dependent background, the Hamiltonian of one wavevector pair takes the following form, up to a constant:

$$
\hat H_{\mathbf k}=\omega_k(\eta)\left(\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger\hat a_{-\mathbf k}\right)+\gamma_k(\eta)\,\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger+\gamma_k^*(\eta)\,\hat a_{\mathbf k}\hat a_{-\mathbf k}\tag{33}\label{eq:inflation-33}
$$

Isotropy makes the coefficients for $\pm\mathbf k$ equal. For inflation, $\omega_k=k$ and $\gamma_k=is$. The same structure appears in particle production in an expanding universe, parametric resonance, and optical parametric amplification.

Translation symmetry also implies that $\hat H_{\mathbf k}$ commutes with the difference in occupation numbers,

$$
\hat N_{\mathbf k}-\hat N_{-\mathbf k},\qquad\hat N_{\pm\mathbf k}=\hat a_{\pm\mathbf k}^\dagger\hat a_{\pm\mathbf k}\tag{34}\label{eq:inflation-34}
$$

This difference represents the momentum of the pair and is conserved. A state evolving from the vacuum **always has equal occupation numbers at $\mathbf k$ and $-\mathbf k$**. This is the sense in which two-mode squeezing creates “pairs” of zero total momentum.

### Standing-wave representation

Keep the same picture and change to the standing-wave basis. Substituting the relations $\eqref{eq:inflation-28}$ gives

$$
\hat a_{\mathbf k}^\dagger\hat a_{\mathbf k}+\hat a_{-\mathbf k}^\dagger\hat a_{-\mathbf k}=\hat b_{c,\mathbf k}^\dagger\hat b_{c,\mathbf k}+\hat b_{s,\mathbf k}^\dagger\hat b_{s,\mathbf k},\qquad\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger=\frac12\left(\hat b_{c,\mathbf k}^{\dagger2}+\hat b_{s,\mathbf k}^{\dagger2}\right)\tag{35}\label{eq:inflation-35}
$$

The terms connecting $c$ and $s$ cancel. Therefore,

$$
\hat H_{\mathbf k}=\hat H_{c,\mathbf k}+\hat H_{s,\mathbf k},\qquad\hat H_{A,\mathbf k}=k\left(\hat b_{A,\mathbf k}^\dagger\hat b_{A,\mathbf k}+\frac12\right)+\frac{is}2\left(\hat b_{A,\mathbf k}^{\dagger2}-\hat b_{A,\mathbf k}^2\right)\tag{36}\label{eq:inflation-36}
$$

Here $\hat b_A^{\dagger2}$ creates **two excitations in one mode** and generates **single-mode squeezing**. The two standing waves have identical Hamiltonians and evolve independently. In canonical variables,

$$
\hat H_{A,\mathbf k}=\frac12\left(\hat p_{A,\mathbf k}^2+k^2\hat q_{A,\mathbf k}^2\right)+\frac s2\left(\hat q_{A,\mathbf k}\hat p_{A,\mathbf k}+\hat p_{A,\mathbf k}\hat q_{A,\mathbf k}\right)\tag{37}\label{eq:inflation-37}
$$

The second term stretches one phase-space direction and compresses its conjugate direction.

Spatial reflection symmetry explains this separation. Under $\mathbf x\to-\mathbf x$, cosine is even and sine is odd, so every quadratic term connecting $c$ to $s$ changes sign and is excluded from a reflection-symmetric Hamiltonian. Translations rotate $(c,s)$, requiring equal coefficients for the two components. A standing wave is an equal-weight superposition of traveling waves at $\pm\mathbf k$ and has zero mean momentum, so unlike traveling waves these modes can be excited independently.

### Heisenberg equations for creation and annihilation operators

Writing $\hat a_{\mathbf k}(\eta)=U^\dagger\hat a_{\mathbf k}U$ and similarly for the other operators, $\hat H_{\mathbf k}$ gives

$$
\hat a_{\pm\mathbf k}'=-ik\,\hat a_{\pm\mathbf k}+s\,\hat a_{\mp\mathbf k}^\dagger,\qquad\hat b_{A,\mathbf k}'=-ik\,\hat b_{A,\mathbf k}+s\,\hat b_{A,\mathbf k}^\dagger\tag{38}\label{eq:inflation-38}
$$

Because creation operators enter the time derivatives of annihilation operators, a later annihilation operator is a linear combination of initial annihilation and creation operators. This is a **Bogoliubov transformation**, whose coefficients we obtain in §5. A traveling-wave annihilation operator mixes with the **creation operator at the opposite wavevector**, whereas a standing-wave annihilation operator mixes with **its own creation operator**. The former also expresses momentum conservation: $[\hat{\mathbf P},\hat a_{\mathbf k}]=-\mathbf k\,\hat a_{\mathbf k}$ and $[\hat{\mathbf P},\hat a_{-\mathbf k}^\dagger]=-\mathbf k\,\hat a_{-\mathbf k}^\dagger$, so the two linear operators carrying the same momentum as $\hat a_{\mathbf k}$ are $\hat a_{\mathbf k}$ and $\hat a_{-\mathbf k}^\dagger$.

## 5. The Bunch–Davies vacuum

### Expanding operators in mode functions (Heisenberg picture)

The Heisenberg equations for the canonical variables of each standing-wave component are

$$
\hat q_{A,\mathbf k}'=\hat p_{A,\mathbf k}+s\,\hat q_{A,\mathbf k},\qquad\hat q_{A,\mathbf k}''+\left(k^2-\frac{z''}{z}\right)\hat q_{A,\mathbf k}=0\tag{39}\label{eq:inflation-39}
$$

These are linear equations with c-number coefficients. Their solutions superpose two independent solutions multiplied by time-independent operators. Choose a complex solution $f_k(\eta)$ and its complex conjugate as the two solutions, and write

$$
\hat q_{A,\mathbf k}(\eta)=f_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}}+f_k^*(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}\dagger},\qquad\hat p_{A,\mathbf k}(\eta)=g_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}}+g_k^*(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}\dagger}\tag{40}\label{eq:inflation-40}
$$

Here $g_k=f_k'-sf_k$; Hermiticity of $\hat q$ makes the second operator coefficient $\hat b^{\mathrm{in}\dagger}$. We call $f_k$ the **mode function**.

Substituting into $[\hat q,\hat p]=i$ gives $(f_kg_k^*-f_k^*g_k)\,[\hat b^{\mathrm{in}},\hat b^{\mathrm{in}\dagger}]=i$. The first factor is the time-independent Wronskian, so normalizing it as

$$
f_kg_k^*-f_k^*g_k=i\tag{41}\label{eq:inflation-41}
$$

gives $[\hat b_{A,\mathbf k}^{\mathrm{in}},\hat b_{B,\mathbf k'}^{\mathrm{in}\dagger}]=\delta_{AB}\delta_{\mathbf k,\mathbf k'}$, making $\hat b^{\mathrm{in}}$ an annihilation operator. We will also use the inverse expansion,

$$
\hat b_{A,\mathbf k}^{\mathrm{in}}=i\left[f_k^*(\eta)\,\hat p_{A,\mathbf k}(\eta)-g_k^*(\eta)\,\hat q_{A,\mathbf k}(\eta)\right]\tag{42}\label{eq:inflation-42}
$$

Operator evolution is thus encoded in one c-number function $f_k$. Choosing a mode function is precisely choosing an annihilation operator: different $f_k$ give different $\hat b^{\mathrm{in}}$ related by Bogoliubov transformations, each defining a different “vacuum.”

### Initial condition: the short-wavelength ground state

Early in inflation, the wavelengths of interest are much shorter than the Hubble radius, with $k^2\gg|z''/z|$ and $|s|\ll k$. In this regime, $\hat H_{A,\mathbf k}$ of §4 approaches a harmonic oscillator of frequency $k$, whose ground state is the natural state of each mode. We therefore select the positive-frequency solution giving this initial ground state,

$$
f_k\longrightarrow\frac{e^{-ik\eta}}{\sqrt{2k}},\qquad g_k\longrightarrow-i\sqrt{\frac k2}\,e^{-ik\eta}\tag{43}\label{eq:inflation-43}
$$

The inverse relation then gives $\hat b_{A,\mathbf k}^{\mathrm{in}}=e^{ik\eta}\,\hat b_{A,\mathbf k}(\eta)$, so $\hat b^{\mathrm{in}}$ agrees with the initial annihilation operator up to a phase. The state annihilated by all $\hat b^{\mathrm{in}}$,

$$
\hat b_{A,\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle=0\qquad(\mathbf k\in\mathcal K_+,\ A=c,s)\tag{44}\label{eq:inflation-44}
$$

is the **Bunch–Davies vacuum**. The traveling-wave operators $\hat a_{\pm\mathbf k}^{\mathrm{in}}=(\hat b_{c,\mathbf k}^{\mathrm{in}}\mp i\hat b_{s,\mathbf k}^{\mathrm{in}})/\sqrt2$ annihilate the same state and therefore define the same initial state. Each mode starts in a harmonic-oscillator ground state, while all subsequent evolution is carried by $f_k$. For inflation of finite duration, we assume that the modes under consideration possess this initial short-wavelength regime.

### Spectrum and spatial correlation

Taking expectation values in the fixed Heisenberg-picture state $|0_{\mathrm{BD}}\rangle$ gives

$$
\langle\hat q_{A,\mathbf k}^2(\eta)\rangle=|f_k(\eta)|^2,\qquad\langle\hat p_{A,\mathbf k}^2(\eta)\rangle=|g_k(\eta)|^2,\qquad\frac12\langle\{\hat q_{A,\mathbf k}(\eta),\hat p_{A,\mathbf k}(\eta)\}\rangle=\operatorname{Re}(f_k(\eta)g_k^*(\eta))\tag{45}\label{eq:inflation-45}
$$

For the Fourier coefficients, $\langle\hat v_{\mathbf k}\hat v_{\mathbf k'}\rangle=\delta_{\mathbf k,-\mathbf k'}|f_k|^2$, so the correlation function $\eqref{eq:inflation-10}$ becomes

$$
G_\zeta(\eta;\mathbf x,\mathbf y)=\frac1{z^2V}\sum_{\mathbf k}|f_k|^2e^{i\mathbf k\cdot(\mathbf x-\mathbf y)}\longrightarrow\int\frac{d^3k}{(2\pi)^3}\,P_\zeta(k,\eta)\,e^{i\mathbf k\cdot(\mathbf x-\mathbf y)},\qquad P_\zeta=\frac{|f_k|^2}{z^2}\tag{46}\label{eq:inflation-46}
$$

The arrow denotes the limit $V^{-1}\sum_{\mathbf k}\to\int d^3k/(2\pi)^3$; the box volume drops out. **The variance $|f_k|^2$ of a single mode directly supplies the spectral density of spatial correlations.**

### Bogoliubov coefficients and the squeezing parameter

Evolve the annihilation operators defined in §3 in the Heisenberg picture and expand them in the in operators:

$$
\hat b_{A,\mathbf k}(\eta)=\alpha_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}}+\beta_k(\eta)\,\hat b_{A,\mathbf k}^{\mathrm{in}\dagger},\qquad\hat a_{\pm\mathbf k}(\eta)=\alpha_k(\eta)\,\hat a_{\pm\mathbf k}^{\mathrm{in}}+\beta_k(\eta)\,\hat a_{\mp\mathbf k}^{\mathrm{in}\dagger}\tag{47}\label{eq:inflation-47}
$$

The coefficients are common to both bases. In terms of mode functions,

$$
\alpha_k=\frac1{\sqrt2}\left(\sqrt k\,f_k+\frac{ig_k}{\sqrt k}\right),\qquad\beta_k=\frac1{\sqrt2}\left(\sqrt k\,f_k^*+\frac{ig_k^*}{\sqrt k}\right)\tag{48}\label{eq:inflation-48}
$$

The Wronskian condition becomes $|\alpha_k|^2-|\beta_k|^2=1$. Write

$$
|\alpha_k|=\cosh r_k,\qquad|\beta_k|=\sinh r_k\qquad(r_k\ge0)\tag{49}\label{eq:inflation-49}
$$

and call $r_k$ the **squeezing parameter**. The name becomes clear from the explicit state in §6 and the Wigner ellipse in §7. Initially $\alpha_k\simeq e^{-ik\eta}$ and $\beta_k\simeq0$, so $r_k\simeq0$.

## 6. Explicit squeezed states (Schrödinger picture)

Using the Heisenberg calculation in §5, express the state $|\Psi(\eta)\rangle=U|0_{\mathrm{BD}}\rangle$ at time $\eta$ in occupation-number eigenstates of reference frequency $k$.

### Traveling waves: the two-mode squeezed vacuum

Inverting the Bogoliubov transformation gives $\hat a_{\mathbf k}^{\mathrm{in}}=\alpha_k^*\hat a_{\mathbf k}(\eta)-\beta_k\hat a_{-\mathbf k}^\dagger(\eta)$. Substituting $\hat a_{\mathbf k}(\eta)=U^\dagger\hat a_{\mathbf k}U$ rewrites the in condition $\hat a_{\mathbf k}^{\mathrm{in}}|0_{\mathrm{BD}}\rangle=0$ in terms of time-independent Schrödinger operators as

$$
\left(\alpha_k^*\,\hat a_{\mathbf k}-\beta_k\,\hat a_{-\mathbf k}^\dagger\right)|\Psi(\eta)\rangle=0\tag{50}\label{eq:inflation-50}
$$

A condition on the fixed Heisenberg-picture state has become a condition on the state at each time. Expand the pair state as $\sum_{m,n}c_{mn}|m\rangle_{\mathbf k}|n\rangle_{-\mathbf k}$ and solve this condition together with the one obtained by interchanging $\mathbf k\leftrightarrow-\mathbf k$. Only $m=n$ components survive, giving, up to an overall phase,

$$
|\Psi_{\mathbf k}(\eta)\rangle=\frac1{\cosh r_k}\sum_{n=0}^\infty\lambda_k^n\,|n\rangle_{\mathbf k}|n\rangle_{-\mathbf k},\qquad\lambda_k=\frac{\beta_k}{\alpha_k^*},\qquad|\lambda_k|=\tanh r_k\tag{51}\label{eq:inflation-51}
$$

The full state is the product over all wavevector pairs. This is the **two-mode squeezed vacuum state**; its properties follow directly from the expression.

- **Pair production:** occupation numbers at $\mathbf k$ and $-\mathbf k$ are always equal, and the total momentum is zero, as required by the symmetry in §4.
- **Geometric distribution:** the probability of $n$ pairs is $\tanh^{2n}r_k/\cosh^2r_k$; each traveling mode has mean occupation $\sinh^2r_k=|\beta_k|^2$.
- **Entanglement:** tracing out $-\mathbf k$ leaves the $\mathbf k$ traveling mode in a thermal-form mixed state with geometrically distributed occupation numbers. Its entropy,

    $$
    S_{\mathbf k|-\mathbf k}=\cosh^2r_k\ln\cosh^2r_k-\sinh^2r_k\ln\sinh^2r_k\tag{52}\label{eq:inflation-52}
    $$

    grows with $r_k$, while the complete pair remains pure.

### Standing waves: two single-mode squeezed vacua

Likewise, $\hat b_{A,\mathbf k}^{\mathrm{in}}=\alpha_k^*\hat b_{A,\mathbf k}(\eta)-\beta_k\hat b_{A,\mathbf k}^\dagger(\eta)$ gives

$$
\left(\alpha_k^*\,\hat b_{A,\mathbf k}-\beta_k\,\hat b_{A,\mathbf k}^\dagger\right)|\Psi(\eta)\rangle=0\qquad(A=c,s)\tag{53}\label{eq:inflation-53}
$$

These conditions involve $c$ and $s$ separately, so the state is a product of the two standing-wave states,

$$
|\Psi_{\mathbf k}(\eta)\rangle=|\psi_k(\eta)\rangle_c\otimes|\psi_k(\eta)\rangle_s,\qquad|\psi_k(\eta)\rangle=\frac1{\sqrt{\cosh r_k}}\sum_{m=0}^\infty\lambda_k^m\frac{\sqrt{(2m)!}}{2^m\,m!}\,|2m\rangle\tag{54}\label{eq:inflation-54}
$$

This is the **single-mode squeezed vacuum**. Both standing waves are in the same pure state, and each contains **only even occupation numbers**, because $\hat b_A^{\dagger2}$ creates two excitations in one mode. The mean occupation is again $\sinh^2r_k$.

Since both representations describe the same state, the total occupation must agree: $\hat N_{\mathbf k}+\hat N_{-\mathbf k}=\hat N_c+\hat N_s$. This can be checked explicitly. In traveling waves, the probability of total occupation $2n$ is $\tanh^{2n}r_k/\cosh^2r_k$. In standing waves, convolving the two even-number distributions gives the same result by the identity $\sum_{m=0}^n\binom{2m}{m}\binom{2n-2m}{n-m}=4^n$. In operator language, the two-mode squeezing generator $\hat a_{\mathbf k}^\dagger\hat a_{-\mathbf k}^\dagger=\frac12(\hat b_{c,\mathbf k}^{\dagger2}+\hat b_{s,\mathbf k}^{\dagger2})$ is a sum of two commuting single-mode squeezing generators.

<iframe src="app/supporting.html?lang=en&amp;view=pairs" title="Occupation-number distributions of the same squeezed state in traveling-wave and standing-wave bases" data-auto-height scrolling="no" style="display: block; width: 100%; height: 850px; min-height: 600px; border: 0; overflow: hidden;" loading="eager"></iframe>

Move $r$ and compare the single-mode distributions. Traveling waves have a monotonically decreasing thermal form, while standing waves have only even occupation numbers; both have mean $\sinh^2r$. The total occupation distribution of the pair agrees exactly in both bases.

### Subsystem choice and entanglement

Entanglement depends on both the state and **how subsystems are defined**. The same pure state is entangled when divided into $\mathbf k$ and $-\mathbf k$, but is a product when divided into $c$ and $s$. Two-mode squeezing and two single-mode squeezings are equivalent descriptions related by a basis transformation that preserves the full state.

Dividing space into regions is yet another partition. Even when standing-wave components are independent, different regions of real space have correlations and entanglement. A discussion of quantum properties must specify which subsystems’ correlations are at issue.

### The wavefunction and real-space kernel

Write the same state as a wavefunction of standing-wave amplitude $q$. Substitute $\hat p=-i\,d/dq$ into the Schrödinger-operator version of the in condition, $i\left[f_k^*(\eta)\,\hat p-g_k^*(\eta)\,\hat q\right]|\psi_k(\eta)\rangle=0$, to obtain

$$
\psi_k(q;\eta)\propto\exp\left[-\frac{K_k(\eta)}2q^2\right],\qquad K_k=-i\,\frac{g_k^*}{f_k^*}\tag{55}\label{eq:inflation-55}
$$

The Wronskian condition gives $\operatorname{Re}K_k=1/(2|f_k|^2)$, consistent with $\langle\hat q^2\rangle=|f_k|^2$. Initially $K_k=k$, recovering the reference-vacuum wavefunction.

This $K_k$ is the Fourier transform of the real-space kernel $\mathcal K_\eta(\mathbf x-\mathbf y)$ in $\eqref{eq:inflation-23}$. The Bunch–Davies wave functional is

$$
\Psi^{(v)}_\eta[v]\propto\exp\left[-\frac12\sum_{\mathbf k}K_k(\eta)\,v_{\mathbf k}v_{-\mathbf k}\right]\tag{56}\label{eq:inflation-56}
$$

This connects the real-space quantum state to the squeezed state of each mode.

## 7. Wigner ellipses and spatial correlations

The Wigner function represents the Schrödinger-picture state in phase space; here we obtain it from the Heisenberg calculation of §5. The expectation values agree in both pictures, for example $\langle\Psi(\eta)|\hat Q_{\mathrm S}^2|\Psi(\eta)\rangle=\langle0_{\mathrm{BD}}|\hat Q_{\mathrm H}^2(\eta)|0_{\mathrm{BD}}\rangle$.

### The Wigner function

Fix one standing-wave component and omit $A,\mathbf k$. Using eigenstates $|Q\rangle$ of $\hat Q$, the Wigner function of a density operator $\hat\rho$ is defined by

$$
W(Q,P)=\frac1{2\pi}\int_{-\infty}^{\infty}d\xi\,e^{-iP\xi}\left\langle Q+\frac\xi2\right|\hat\rho\left|Q-\frac\xi2\right\rangle\tag{57}\label{eq:inflation-57}
$$

Here $Q,P,\xi$ are real. Integrating over one coordinate gives the measurement probability density of the other quadrature,

$$
\int dP\,W(Q,P)=\langle Q|\hat\rho|Q\rangle,\qquad\int dQ\,W(Q,P)=\langle P|\hat\rho|P\rangle\tag{58}\label{eq:inflation-58}
$$

Phase-space averages of products give symmetrically ordered (Weyl-ordered) expectation values; for example, $\int dQ\,dP\,QP\,W=\frac12\langle\hat Q\hat P+\hat P\hat Q\rangle$. For general states, $W$ is a quasiprobability distribution that can be negative; for Gaussian states, $W\ge0$. Definitions and properties are reviewed by [O’Connell](https://arxiv.org/abs/1009.4431).

### Covariance matrix and ellipse

For $\hat{\mathbf Z}=(\hat Q,\hat P)^T$, the covariance matrix $\Sigma_{ij}=\frac12\langle\{\hat Z_i,\hat Z_j\}\rangle$ follows from §5:

$$
\Sigma=\begin{pmatrix}k|f_k|^2&\operatorname{Re}(f_kg_k^*)\\\operatorname{Re}(f_kg_k^*)&|g_k|^2/k\end{pmatrix},\qquad\det\Sigma=\frac14\tag{59}\label{eq:inflation-59}
$$

The determinant follows from the Wronskian condition and expresses the preservation of minimum uncertainty in a pure Gaussian state. A zero-mean Gaussian state has Wigner function

$$
W(\mathbf Z)=\frac1{2\pi\sqrt{\det\Sigma}}\exp\left[-\frac12\mathbf Z^T\Sigma^{-1}\mathbf Z\right]\tag{60}\label{eq:inflation-60}
$$

whose contours are ellipses.

The eigenvalues of $\Sigma$, the variances along the major and minor axes, are

$$
\sigma_\pm^2=\frac12e^{\pm2r_k}\tag{61}\label{eq:inflation-61}
$$

Starting from the reference-vacuum circle $\Sigma=I/2$, one direction stretches while its perpendicular direction contracts, preserving area. This is the geometry of squeezing. The angle $\varphi_k$ of the major axis from the positive $Q$ axis is

$$
\varphi_k=\frac12\arg(\alpha_k\beta_k)\tag{62}\label{eq:inflation-62}
$$

The pair amplitude of §6 is then $\lambda_k=\tanh r_k\,e^{2i\varphi_k}$. Both the number-state amplitude $\lambda_k$ and the phase-space ellipse are specified by the same two numbers $r_k,\varphi_k$.

### Projection onto spatial correlations

Using $\Sigma_{QQ}=k|f_k|^2$, the relation $P_\zeta=|f_k|^2/z^2$ in $\eqref{eq:inflation-46}$ becomes

$$
P_\zeta(k,\eta)=\frac{\Sigma_{QQ}}{k\,z^2},\qquad\Sigma_{QQ}=\frac12\left[e^{2r_k}\cos^2\varphi_k+e^{-2r_k}\sin^2\varphi_k\right]\tag{63}\label{eq:inflation-63}
$$

Here $\Sigma_{QQ}$ gives the width of the ellipse projected onto the $Q$ axis. For an isotropic state, angular integration expresses the correlation as a function of comoving distance $R=|\mathbf x-\mathbf y|$:

$$
G_\zeta(\eta;R)=\int_0^\infty\frac{dk}k\,\mathcal P_\zeta(k,\eta)\,\frac{\sin kR}{kR},\qquad\mathcal P_\zeta=\frac{k^3}{2\pi^2}P_\zeta\tag{64}\label{eq:inflation-64}
$$

Inserting the squeezing variables directly gives

$$
G_\zeta(\eta;R)=\frac1{4\pi^2z^2}\int_0^\infty dk\,k\left[e^{2r_k}\cos^2\varphi_k+e^{-2r_k}\sin^2\varphi_k\right]\frac{\sin kR}{kR}\tag{65}\label{eq:inflation-65}
$$

**Both elongation and orientation** of the ellipse determine the spectrum, whose superposition determines the distance dependence. Together with the factor $z^{-2}$ returning to the original field, this is key to understanding “freezing” in §9.

The function $G_\zeta$ probes the ellipse’s projection along $Q$. Representing the entire ellipse in real space also requires the field–momentum correlation $\frac12\langle\{\hat\zeta(\mathbf x),\hat\Pi_\zeta(\mathbf y)\}\rangle$ and the momentum–momentum correlation. Their Fourier coefficients are $\Sigma_{QP}$ and $kz^2\Sigma_{PP}$, respectively. Observational statements about the degree of squeezing or a quantum origin require this information beyond the field two-point function.

## 8. An exactly solvable example: a massless scalar on de Sitter space

### Model and correspondence

The following figures use exact de Sitter spacetime,

$$
a(\eta)=-\frac1{H\eta},\qquad\eta<0,\qquad\mathcal H=-\frac1\eta\qquad(H\text{ constant})\tag{66}\label{eq:inflation-66}
$$

with a free, massless, minimally coupled scalar field $\hat\phi$. The background is prescribed, and the backreaction of $\hat\phi$ is neglected. Its action,

$$
S_\phi=\frac12\int d\eta\,d^3x\;a^2\left[(\phi')^2-(\nabla\phi)^2\right]\tag{67}\label{eq:inflation-67}
$$

is the curvature-perturbation action of §1 with $z$ replaced by $a$. The arguments of §2–7 apply directly with the following correspondence.

| | Curvature perturbation | Scalar field in the figures |
| --- | --- | --- |
| Original field | $\zeta$ | $\phi$ |
| Action coefficient | $z^2$ | $a^2$ |
| Canonical variable | $v=z\zeta$ | $u=a\phi$ |
| Conjugate momentum | $\pi=v'-(z'/z)v$ | $\pi_u=u'-\mathcal Hu=a\phi'$ |
| Squeezing coefficient $s$ | $z'/z$ | $\mathcal H$ |

We retain the notation $f_k,g_k$ for solutions of the mode equations with $z$ replaced by $a$. Each appropriately normalized tensor polarization obeys an equation of the same form. The relation to curvature perturbations is discussed in §9.

### Mode functions and squeezing parameter

Instead of time, use

$$
x=-k\eta=\frac{k}{aH},\qquad N=-\ln x\tag{68}\label{eq:inflation-68}
$$

Here $x$ is the ratio of physical wavenumber $k/a$ to $H$: $x\gg1$ corresponds to wavelengths shorter than the Hubble radius, and $x\ll1$ to longer wavelengths. The variable $N$ counts e-folds from $x=1$, conventionally called Hubble crossing.

Solving for the mode functions with past positive-frequency behavior and Wronskian normalization gives

$$
f_k=\frac{1+i/x}{\sqrt{2k}}\,e^{ix},\qquad g_k=f_k'-\mathcal Hf_k=-i\sqrt{\frac k2}\,e^{ix}\tag{69}\label{eq:inflation-69}
$$

Substitution into $\eqref{eq:inflation-48}$ gives

$$
\alpha_k=\left(1+\frac i{2x}\right)e^{ix},\qquad\beta_k=-\frac i{2x}\,e^{-ix},\tag{70}\label{eq:inflation-70}
$$

$$
r_k=\operatorname{arsinh}\frac1{2x},\qquad\varphi_k=-\frac12\arctan(2x),\qquad\lambda_k=\frac{1-2ix}{1+4x^2}\tag{71}\label{eq:inflation-71}
$$

At short wavelengths, $r_k\simeq1/(2x)$ and the state is nearly vacuum; at long wavelengths, $r_k\simeq-\ln x=N$.

$$
\frac{dr_k}{dN}=\frac1{\sqrt{1+4x^2}}\tag{72}\label{eq:inflation-72}
$$

Well after Hubble crossing, $r_k$ therefore increases by approximately one per e-fold.

For $Q=\sqrt k\,q$, the kernel $K_k$ in $\eqref{eq:inflation-55}$ gives the wavefunction

$$
\psi(Q;x)\propto\exp\left[-\frac{x(x+i)}{2(1+x^2)}\,Q^2\right]\tag{73}\label{eq:inflation-73}
$$

As $x\to0$, the real part of the exponent decreases as $x^2$, broadening the distribution along $Q$. The imaginary part $\simeq x$ supplies a phase $e^{-ixQ^2/2}$ encoding the correlation $P\simeq-xQ$ between $Q$ and $P$.

### Conserved and decaying components

The original field’s real amplitude is $\hat\phi_{A,\mathbf k}=\hat q_{A,\mathbf k}/a$, so its mode function is

$$
\frac{f_k}a=\frac H{\sqrt{2k^3}}(x+i)\,e^{ix}=\frac H{\sqrt{2k^3}}\left[i\left(1+\frac{x^2}2+O(x^4)\right)-\frac{x^3}3+O(x^5)\right]\tag{74}\label{eq:inflation-74}
$$

The last expression expands at $x\ll1$. The imaginary part is the **conserved component**, approaching a constant; the real part is the **decaying component**, decreasing as $x^3\propto a^{-3}$. These correspond to the two terms of the general long-wavelength solution $\phi\simeq C_1+C_2\int^\eta d\tilde\eta/a^2$ of $(a^2\phi')'=0$ with gradients neglected. The imaginary $x^2/2$ term is a correction to the conserved component.

The Bunch–Davies spectrum is

$$
P_\phi(k,\eta)=\left|\frac{f_k}a\right|^2=\frac{H^2}{2k^3}(1+x^2),\qquad\mathcal P_\phi=\frac{H^2}{4\pi^2}(1+x^2)\longrightarrow\left(\frac H{2\pi}\right)^2\tag{75}\label{eq:inflation-75}
$$

The canonical variance $|f_k|^2$ continues to grow as $a^2$, while the original field’s power approaches the constant $(H/2\pi)^2$ after Hubble crossing.

<iframe src="app/supporting.html?lang=en&amp;view=background" title="Evolution of the canonical-variable and original-field mode functions" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

Compare the canonical mode $f_k$ with the original-field mode $f_k/a$. Switching views also shows the conserved and decaying components and the relative sizes of the gradient and background terms in the mode equation.

### Phase-space flow

Using e-fold number $N$ as time and multiplying $\hat H_{A,\mathbf k}$ of §4 by $d\eta/dN=x/k$, the Hamiltonian for one standing wave becomes

$$
\hat K_N=\frac x2\left(\hat Q^2+\hat P^2\right)+\frac12\left(\hat Q\hat P+\hat P\hat Q\right)\tag{76}\label{eq:inflation-76}
$$

The Heisenberg equations are

$$
\frac{d\hat{\mathbf Z}}{dN}=A\,\hat{\mathbf Z},\qquad A=x\begin{pmatrix}0&1\\-1&0\end{pmatrix}+\begin{pmatrix}1&0\\0&-1\end{pmatrix}\tag{77}\label{eq:inflation-77}
$$

The first term generates phase-space rotation; the second stretches $Q$ and contracts $P$. Because the Hamiltonian is quadratic, the Schrödinger-picture Wigner function is exactly transported by the linear flow $d\mathbf Z/dN=A\mathbf Z$ of numerical coordinates $\mathbf Z$. The covariance obeys $d\Sigma/dN=A\Sigma+\Sigma A^T$, and $\operatorname{tr}A=0$ preserves area.

For $x\gg1$, rotation dominates and the distribution remains nearly circular. As $x$ decreases, stretching and contraction become relatively stronger, reaching the same order as rotation at $x=1$. For $x<1$, $A$ has real eigenvalues $\pm\sqrt{1-x^2}$ and the flow is hyperbolic.

<span id="main-animation"></span>

<iframe src="app/index.html?lang=en" title="Wigner ellipse on fixed canonical axes with rotation and squeezing flows" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1800px; min-height: 900px; border: 0; overflow: hidden;" loading="eager"></iframe>

Compare three stages in the animation.

1. **$x\gg1$:** rotation dominates, and the Wigner distribution is nearly circular. Its slight initial ellipticity comes from starting at $x=12$.
2. **$x\approx1$:** rotation and stretching become comparable, and the ellipse’s deformation becomes noticeable.
3. **$x\ll1$:** the major axis lengthens, the minor axis narrows, and the major axis approaches the $Q$ axis.

The contour $\mathbf Z^T\Sigma^{-1}\mathbf Z=1$ encloses probability $1-e^{-1/2}\simeq39\%$. Arrow lengths include a common display scale and $1/\sqrt{1+x^2}$; the ellipse is computed with the original flow. Switch the direction display to compare instantaneous flow eigendirections, ellipse principal axes, and conserved/decaying solution directions. The principal axes and their projection onto $Q$ determine the field variance.

<iframe src="app/supporting.html?lang=en&amp;view=squeezing" title="Squeezing magnitude and major-axis angle as functions of e-fold time" data-auto-height scrolling="no" style="display: block; width: 100%; height: 900px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

These plots follow $r_k$ and $\varphi_k$ to four e-folds after Hubble crossing. At late times, $r_k\simeq N$ and the angle approaches zero.

### Four-dimensional covariance in the traveling-wave basis

Return from the ellipse of one standing wave to the four-dimensional phase space of the pair. In standing-wave coordinates $\hat{\mathbf Z}_{\mathrm{st}}=(\hat Q_c,\hat P_c,\hat Q_s,\hat P_s)^T$, the two components have the same state, so

$$
\Sigma_{\mathrm{st}}=\begin{pmatrix}\Sigma&0\\0&\Sigma\end{pmatrix}\tag{78}\label{eq:inflation-78}
$$

The traveling-wave quadratures $\hat Q_\pm=(\hat a_{\pm\mathbf k}+\hat a_{\pm\mathbf k}^\dagger)/\sqrt2$ and $\hat P_\pm=(\hat a_{\pm\mathbf k}-\hat a_{\pm\mathbf k}^\dagger)/(i\sqrt2)$ obey $\hat Q_\pm=(\hat Q_c\pm\hat P_s)/\sqrt2$ and $\hat P_\pm=(\hat P_c\mp\hat Q_s)/\sqrt2$ by §3. The covariance of $\hat{\mathbf Z}_{\mathrm{tr}}=(\hat Q_+,\hat P_+,\hat Q_-,\hat P_-)^T$ is

$$
\Sigma_{\mathrm{tr}}=\frac12\begin{pmatrix}\cosh2r_k\,I&\sinh2r_k\,R_k\\\sinh2r_k\,R_k&\cosh2r_k\,I\end{pmatrix},\qquad R_k=\begin{pmatrix}\cos2\varphi_k&\sin2\varphi_k\\\sin2\varphi_k&-\cos2\varphi_k\end{pmatrix}\tag{79}\label{eq:inflation-79}
$$

Here $I$ is the $2\times2$ identity matrix. The block for one traveling mode is isotropic, with variance $\frac12\cosh2r_k=|\beta_k|^2+\frac12$: the thermal state discussed in §6. The off-diagonal blocks encode strong correlations between $\mathbf k$ and $-\mathbf k$, namely two-mode squeezing.

<iframe src="app/supporting.html?lang=en&amp;view=basis" title="Four-dimensional covariance of the same pure state in traveling-wave and standing-wave bases" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1200px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

Choose a late time and check how the two identical standing-wave covariance blocks become correlations between traveling modes. Both matrices describe the same pure state of the pair.

## 9. Freezing, classical random fields, and acoustic peaks

We now follow the consequences of squeezing in §8 through to observed fluctuations. Field fluctuations freeze, and their amplitudes pass into primordial fluctuations as conserved curvature perturbations. Frozen modes can be treated as initial conditions for a classical random field. Those initial conditions being dominated by the growing mode then manifests as the CMB acoustic peaks.

### Conditional width

The model in §8 has covariance

$$
\Sigma(x)=\frac12\begin{pmatrix}1+x^{-2}&-x^{-1}\\-x^{-1}&1\end{pmatrix}\tag{80}\label{eq:inflation-80}
$$

The variance $\Sigma_{PP}=1/2$ is constant: narrowing occurs along the tilted minor axis. In the positive Gaussian Wigner density, the conditional statistics of $P$ given $Q$ are

$$
\mathbb E_W[P\mid Q]=-\frac x{1+x^2}\,Q,\qquad\operatorname{Var}_W(P\mid Q)=\frac{x^2}{2(1+x^2)}\tag{81}\label{eq:inflation-81}
$$

For $x\ll1$, the distribution concentrates near $P\simeq-xQ$. Amplitude and momentum become strongly correlated, and the remaining momentum width at a given amplitude becomes small. The subscript $W$ denotes statistics of the Wigner density.

### Field velocity

The expansion coefficient for the cosmic-time field velocity $\dot\phi=\phi'/a$ is $g_k/a^2$. Its spectrum and its ratio to the field amplitude are

$$
P_{\dot\phi}(k,\eta)=\frac{k}{2a^4},\qquad\frac{\sqrt{P_{\dot\phi}}}{H\sqrt{P_\phi}}=\frac{x^2}{\sqrt{1+x^2}}\simeq x^2\quad(x\ll1)\tag{82}\label{eq:inflation-82}
$$

The change in the field over a Hubble time is suppressed by order $x^2$ relative to its amplitude—about 1% at $x=0.1$. Thus **a superposition with finite amplitude width remains, while its time variation becomes small**. This is freezing. Since $[\hat\phi_{A,\mathbf k},\dot{\hat\phi}_{A,\mathbf k}]=i/a^3$, the narrowing velocity distribution is compatible with $[\hat Q,\hat P]=i$ and $\det\Sigma=1/4$.

Squeezing and freezing are different views of the same aspect of quantum evolution during inflation. The canonical $Q$ distribution broadens along the major axis in proportion to $e^{r_k}$. The original field amplitude is $Q$ divided by $\sqrt k\,a$, and that ratio approaches a constant. At the same time, the decaying component is suppressed, leaving effectively one random amplitude per mode as input for subsequent linear evolution.

### Application to curvature perturbations

Applying this result to curvature perturbations requires the relation between $z$ and $a$. Writing the Planck mass as $M_{\mathrm{Pl}}$, the background Einstein equations give

$$
\epsilon_1=-\frac{\dot H}{H^2}=\frac{\dot\phi_0^2}{2M_{\mathrm{Pl}}^2H^2},\qquad z^2=2a^2\epsilon_1M_{\mathrm{Pl}}^2\tag{83}\label{eq:inflation-83}
$$

Using $\epsilon_2=d\ln\epsilon_1/d\ln a$, to first order in slow-roll parameters,

$$
\frac{z''}{z}=\mathcal H^2\left[2-\epsilon_1+\frac32\epsilon_2+O(\epsilon^2)\right],\qquad\frac{a''}{a}=\mathcal H^2(2-\epsilon_1)\tag{84}\label{eq:inflation-84}
$$

At leading order, both approach $2/\eta^2$, so the canonical curvature mode function is approximated by $f_k$ of §8 and develops squeezing in the same way. Returning to the curvature amplitude requires division by $z$. Exact de Sitter has $\dot\phi_0=0$ and $z=0$, so the §8 model serves as the leading slow-roll approximation for curvature perturbations.

The long-wavelength curvature operator is

$$
\hat\zeta_{\mathbf k}(\eta)\simeq\hat C_{1,\mathbf k}+\hat C_{2,\mathbf k}\int^\eta\frac{d\tilde\eta}{z^2(\tilde\eta)}\tag{85}\label{eq:inflation-85}
$$

On an ordinary attractor background the second term decays and $\hat\zeta$ is conserved. On a non-attractor background it may grow, requiring a fresh assessment from $z(\eta)$. For single-field slow roll with Bunch–Davies initial conditions, the conserved curvature power at leading order is

$$
\mathcal P_\zeta(k)\simeq\left.\frac{\mathcal P_\phi}{2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{k=aH}=\left.\frac{H^2}{8\pi^2\epsilon_1M_{\mathrm{Pl}}^2}\right|_{k=aH}\tag{86}\label{eq:inflation-86}
$$

Here $\mathcal P_\phi$ is the frozen value $(H/2\pi)^2$ from §8, and the background quantities on the right are evaluated at each mode’s Hubble crossing.

### Description by a classical random field

In this linear Gaussian theory, equal-time fields commute. Sampling field configurations from $|\Psi_\eta[\zeta]|^2$ therefore reproduces field correlations at that time. Symmetrically ordered correlations involving fields and momenta can likewise be reproduced by the positive Gaussian Wigner density. These properties already hold for the initial vacuum.

As squeezing develops, momentum becomes almost fixed by the amplitude. Initial conditions for subsequent linear evolution can then be specified effectively by one random amplitude per mode. This is why the statistics of later cosmic fluctuations can be calculated from classical random-field initial conditions.

The quantum state itself remains a pure squeezed state, with $[\hat Q,\hat P]=i$ preserved. A classical Gaussian random field and a pure squeezed state having the same two-point function cannot be distinguished by that field two-point function alone. The distinction between reproducing classical statistics and a quantum state becoming classical is discussed in detail by [Martin & Vennin](https://arxiv.org/abs/1510.04038). Entanglement with an environment—decoherence—turns the subsystem state into a mixed state, as discussed in §10.

### Temporal phase coherence and acoustic peaks

Let $\hat\zeta_{\mathbf k}^{\mathrm{prim}}$ denote the conserved primordial curvature operator. In linear evolution dominated by the adiabatic growing mode, an acoustic variable $\hat X$ of the later photon–baryon fluid is expressed through a transfer function $T_k$, determined by the background evolution and wavenumber, as

$$
\hat X_{\mathbf k}(\eta)\simeq T_k(\eta)\,\hat\zeta_{\mathbf k}^{\mathrm{prim}},\qquad\hat X_{\mathbf k}'(\eta)\simeq T_k'(\eta)\,\hat\zeta_{\mathbf k}^{\mathrm{prim}}\tag{87}\label{eq:inflation-87}
$$

The later spatial correlation follows from the same initial state:

$$
\langle\hat X(\eta,\mathbf x)\hat X(\eta,\mathbf y)\rangle\simeq\int\frac{d^3k}{(2\pi)^3}\,|T_k(\eta)|^2\,P_\zeta^{\mathrm{prim}}(k)\,e^{i\mathbf k\cdot(\mathbf x-\mathbf y)}\tag{88}\label{eq:inflation-88}
$$

This approximation retains only the growing mode; reconstructing the exact canonical commutators also requires the decaying mode.

The displacement $\hat X$ and velocity $\hat X'$ multiply the same primordial amplitude by $T_k$ and $T_k'$. Consequently, even when primordial amplitudes differ between realizations, acoustic oscillations of the same wavenumber share the times of their zero crossings and extrema. This **temporal phase coherence** follows from the suppression of the decaying component during freezing. Spatial Fourier phases remain random, while oscillations at each wavenumber share a common time evolution.

To see the effect, consider an oscillator with constant sound speed $c_s$, omitting gravitational driving and other effects,

$$
X_k=A_k\cos(kr_s)+B_k\sin(kr_s),\qquad r_s=c_s(\eta-\eta_i)\tag{89}\label{eq:inflation-89}
$$

Here $r_s$ is the sound-travel distance since $\eta_i$, $A_k=X_k(\eta_i)$ is the initial displacement, and $B_k=X_k'(\eta_i)/(kc_s)$ corresponds to the initial velocity. In the adiabatic growing mode, density is already perturbed at long wavelengths, while the gradients driving the fluid are small. The oscillator therefore starts nearly at rest: $|B_k|\ll|A_k|$.

Compare two ensembles with the same initial total variance $\sigma^2$. In a coherent ensemble where all oscillations start as cosines ($\langle A_k^2\rangle=\sigma^2$, $B_k=0$),

$$
\langle X_k^2\rangle=\sigma^2\cos^2(kr_s)\tag{90}\label{eq:inflation-90}
$$

Oscillations survive in the mean power despite random amplitudes. For an ensemble with independent cosine and sine components of equal variance ($\langle A_k^2\rangle=\langle B_k^2\rangle=\sigma^2/2$, $\langle A_kB_k\rangle=0$),

$$
\langle X_k^2\rangle=\frac{\sigma^2}2\tag{91}\label{eq:inflation-91}
$$

The power oscillations disappear on averaging.

<iframe src="app/supporting.html?lang=en&amp;view=acoustic" title="Statistical acoustic-oscillator model with and without shared temporal phase" data-auto-height scrolling="no" style="display: block; width: 100%; height: 1400px; min-height: 650px; border: 0; overflow: hidden;" loading="eager"></iframe>

In the coherent ensemble, zero crossings align and oscillations remain in the mean power. Fixing the sound-travel distance $r_s$ at recombination and varying $k$ turns these oscillations into a periodic sequence of peaks in wavenumber space.

A full CMB calculation includes gravitational driving, baryon inertia, neutrinos, diffusion damping, recombination, and projection onto the sky. Still, the common time evolution at each wavenumber inherited from the adiabatic growing mode is the origin of acoustic peaks in the angular power spectrum $C_\ell$. Acoustic peaks indicate coherent temporal phases of primordial fluctuations; identifying a quantum origin requires additional information. See [Hu & White](https://arxiv.org/abs/astro-ph/9602019).

## 10. Beyond linear theory: interactions, non-Gaussianity, and coarse graining

### Mode coupling and non-Gaussianity

So far we have used only the quadratic action. Including nonlinearities in gravity and the inflaton adds cubic and higher terms $S_3,S_4,\dots$ in $\zeta$. In single-field slow roll, cubic-action coefficients are suppressed by slow-roll parameters ([Maldacena](https://arxiv.org/abs/astro-ph/0210603)).

These terms couple different wavevectors while keeping their total momentum zero. For example, a cubic term connects three modes with $\mathbf k_1+\mathbf k_2+\mathbf k_3=0$ and generates the continuum three-point correlation

$$
\langle\hat\zeta_{\mathbf k_1}\hat\zeta_{\mathbf k_2}\hat\zeta_{\mathbf k_3}\rangle=(2\pi)^3\delta^{(3)}(\mathbf k_1+\mathbf k_2+\mathbf k_3)\,B_\zeta(k_1,k_2,k_3)\tag{92}\label{eq:inflation-92}
$$

The three-point function of a zero-mean Gaussian state vanishes, so $B_\zeta$ directly measures non-Gaussianity. $B_\zeta$ depends on the shape of the triangle formed by the three wavevectors, reflecting the type of interaction. In single-field slow roll, the limit of $B_\zeta$ where one wavenumber is much smaller than the other two is determined by the power-spectrum tilt $n_s-1$.

For the quantum state, mode coupling breaks the product-over-pairs structure of §6 and generates correlations and entanglement between different wavevectors. For a selected long-wavelength mode, other short-wavelength modes act as an environment; tracing over them leaves a mixed long-wavelength state. This is one mechanism of decoherence during inflation and arises even from gravitational nonlinearities alone ([Nelson](https://arxiv.org/abs/1601.03734)). Squeezing occurs during linear evolution, while decoherence arises from interactions: they are distinct stages.

### The in-in (Schwinger–Keldysh) formalism

With interactions, the target remains the finite-time expectation value specified by an initial state, as in §1. Include quadratic-Hamiltonian evolution in the interaction-picture operators $\hat\zeta_I$ and denote the remainder by $\hat H_{\mathrm{int},I}$. Then

$$
U_I(\eta,\eta_0)=T\exp\left[-i\int_{\eta_0}^{\eta}d\eta'\,\hat H_{\mathrm{int},I}(\eta')\right],\qquad\langle\hat O(\eta)\rangle=\langle\Psi_0|U_I^\dagger\,\hat O_I(\eta)\,U_I|\Psi_0\rangle\tag{93}\label{eq:inflation-93}
$$

Here $T$ denotes time ordering and $\hat O$ a product of fields at time $\eta$. At first order in $\hat H_{\mathrm{int}}$,

$$
\langle\hat O(\eta)\rangle=i\int_{\eta_0}^{\eta}d\eta'\,\langle\Psi_0|\left[\hat H_{\mathrm{int},I}(\eta'),\hat O_I(\eta)\right]|\Psi_0\rangle\tag{94}\label{eq:inflation-94}
$$

Taking $\hat O$ to be a product of three fields gives the leading three-point function. The expectation value on the right is computed using the mode functions $f_k$ and Bunch–Davies vacuum of §5. Organizing this expansion along two time branches, evolving the state forward to the observation time and back, is the **in-in formalism**, or **Schwinger–Keldysh formalism**. The same method applies to loop corrections and unequal-time correlations ([Weinberg](https://arxiv.org/abs/hep-th/0506236)). The linear mode functions and initial vacuum directly provide the starting point for perturbation theory.

### Stochastic inflation: a long-wavelength effective theory

When interactions affect long-wavelength fluctuations—for example, when potential nonlinearities accumulate over long times—an alternative to perturbative expansion can be useful. **Stochastic inflation** is an effective theory retaining only long-wavelength fields as dynamical variables and treating the effects of short-wavelength degrees of freedom as a random force.

For the field in §8, introduce a moving boundary $k_c(\eta)=\varepsilon aH$ with $0<\varepsilon\ll1$ and define the long-wavelength part

$$
\hat\phi_<(\eta,\mathbf x)=\int\frac{d^3k}{(2\pi)^3}\,\Theta\bigl(k_c(\eta)-k\bigr)\,\hat\phi_{\mathbf k}(\eta)\,e^{i\mathbf k\cdot\mathbf x}\tag{95}\label{eq:inflation-95}
$$

Modes crossing into the long-wavelength sector over time are strongly squeezed and can be treated as classical random variables, as in §9. Their contributions to the long-wavelength field act as random noise. For a light field with potential $V(\phi)$ on a quasi-de Sitter background, the coarse-grained field obeys a Langevin equation in e-fold number $N$,

$$
\frac{d\phi_<}{dN}=-\frac{V'(\phi_<)}{3H^2}+\xi(N),\qquad\langle\xi(N)\xi(N')\rangle=\left(\frac H{2\pi}\right)^2\delta(N-N')\tag{96}\label{eq:inflation-96}
$$

For the massless field of §8 ($V=0$), the frozen spectrum makes the coarse-grained variance increase by $(H/2\pi)^2$ per e-fold: the continually increasing number of modes counted as long wavelength produces variance growth.

Solving the corresponding Fokker–Planck equation gives the long-wavelength probability distribution without a perturbative expansion and can describe non-Gaussian features such as distribution tails. Noise amplitude and temporal correlations depend on the window, background, and mass; white noise is an approximation. Spatial correlations also require the noise’s spatial correlations. For derivation by integrating out short-wavelength degrees of freedom in quantum field theory and the conditions of the approximation, see [Andersen, Eriksson & Tranberg](https://arxiv.org/abs/2111.14503).

## Conventions, limitations, and references

The explicit calculations through §9 use the quadratic quantum theory of perturbations on a classical homogeneous background. The initial state is the Bunch–Davies vacuum, and the figures use the exact massless, minimally coupled scalar solution on de Sitter space. Slow-roll and attractor conditions were stated separately for curvature perturbations. The finite-volume box is only a regulator, with results expressed in the $V\to\infty$ limit. Section 10 surveys interactions and coarse graining. The main animation stops at $x=0.2$ so the minor-axis width remains visible; afterward the ellipse keeps narrowing while preserving area.

- [Baumann, *TASI Lectures on Inflation*](https://arxiv.org/abs/0907.5424): perturbation action, canonical quantization, and primordial power spectrum.
- [Polarski & Starobinsky, *Semiclassicality and Decoherence of Cosmological Perturbations*](https://arxiv.org/abs/gr-qc/9504030): canonical variables, conserved and decaying solutions, and the semiclassical description.
- [Martin & Vennin, *Quantum Discord of Cosmic Inflation*](https://arxiv.org/abs/1510.04038): reproducing classical correlations versus distinguishing quantum states.
- [Hu & White, *Acoustic Signatures in the Cosmic Microwave Background*](https://arxiv.org/abs/astro-ph/9602019): primordial initial conditions and acoustic peaks.
- [Maldacena, *Non-Gaussian features of primordial fluctuations in single field inflationary models*](https://arxiv.org/abs/astro-ph/0210603): cubic action and the single-field three-point function.
- [Weinberg, *Quantum Contributions to Cosmological Correlations*](https://arxiv.org/abs/hep-th/0506236): quantum corrections to cosmological correlations using the in-in formalism.
- [Nelson, *Quantum Decoherence During Inflation from Gravitational Nonlinearities*](https://arxiv.org/abs/1601.03734): decoherence from gravitational nonlinearities.
- [Andersen, Eriksson & Tranberg, *Stochastic inflation from quantum field theory and the parametric dependence of the effective noise amplitude*](https://arxiv.org/abs/2111.14503): deriving the stochastic effective theory by coarse graining and the conditions of its approximations.
