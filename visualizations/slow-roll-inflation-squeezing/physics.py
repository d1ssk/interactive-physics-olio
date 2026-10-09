"""Single-field slow-roll inflation: background and squeezing of curvature and tensor modes.

Units: reduced Planck mass M_Pl = 1 and hbar = c = 1. The overall potential amplitude only
rescales H and the power spectra; every quadrature result depends on the potential's shape.

Time is the e-fold number N = ln a, measured from the start of the background integration.
For one comoving wavenumber k, x = k/(aH). As in the companion article, one standing mode has
the fixed quadratures Q = sqrt(k) q and P = p/sqrt(k), where p = q' - (z'/z) q. The coefficients
F = sqrt(k) f_k and G = g_k/sqrt(k) of the in annihilator obey

    dF/dN = x G + sigma F,    dG/dN = -x F - sigma G,

with sigma = (z'/z)/(aH) = 1 + eps2/2 for the curvature perturbation (z = a sqrt(2 eps1)) and
sigma = 1 for each canonically normalized tensor polarization (z_T = a/2).
"""

from __future__ import annotations

import math
from collections.abc import Callable
from dataclasses import dataclass

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
from scipy.special import hankel1

EULER_GAMMA = 0.5772156649015329
# C in the next-order (Stewart–Lyth) amplitude correction; psi(3/2) = 2 - gamma - 2 ln 2.
STEWART_LYTH_C = EULER_GAMMA + math.log(2) - 2
REDUCED_PLANCK_MASS_GEV = 2.435e18
PIVOT_EFOLDS = 55.0
SCALAR_AMPLITUDE = 2.1e-9
# Physical-scale identification for the illustrative primary-CMB window, not a sharp cutoff.
PIVOT_WAVENUMBER_MPC_INV = 0.05
CMB_WAVENUMBER_RANGE_MPC_INV = (1e-4, 0.2)
STAROBINSKY_SLOPE = math.sqrt(2 / 3)
# Large enough that the earliest plotted mode starts deep inside the Hubble radius.
TOTAL_EFOLDS = 85.0
POWER_LAW_SPAN = 140.0


def log_wavenumber_ratio(wavenumber, pivot=PIVOT_WAVENUMBER_MPC_INV):
    """Natural-log spectrum coordinate for comoving wavenumbers in the same units."""

    return np.log(np.asarray(wavenumber) / pivot)


@dataclass(frozen=True)
class Model:
    """A potential V(phi) with its first two derivatives; the amplitude is set to one."""

    key: str
    potential: Callable[[float], float]
    slope: Callable[[float], float]
    curvature: Callable[[float], float]
    phi_start: float
    ends: bool = True


def monomial(p: float, key: str) -> Model:
    """Large-field V ∝ phi^p rolling toward phi = 0; phi^2 ≈ 2 p (N_end - N) + p^2/2."""

    return Model(
        key,
        lambda f: f**p,
        lambda f: p * f ** (p - 1),
        lambda f: p * (p - 1) * f ** (p - 2),
        math.sqrt(2 * p * TOTAL_EFOLDS + p * p / 2),
    )


def starobinsky() -> Model:
    """Plateau V ∝ (1 - exp(-sqrt(2/3) phi))^2 of R^2 inflation in the Einstein frame."""

    b = STAROBINSKY_SLOPE

    def potential(f: float) -> float:
        return (1 - math.exp(-b * f)) ** 2

    def slope(f: float) -> float:
        e = math.exp(-b * f)
        return 2 * b * e * (1 - e)

    def curvature(f: float) -> float:
        e = math.exp(-b * f)
        return 2 * b * b * e * (2 * e - 1)

    return Model("starobinsky", potential, slope, curvature, math.log(4 * TOTAL_EFOLDS / 3) / b)


def power_law(eps1: float, key: str) -> Model:
    """V ∝ exp(-lambda phi): the exact attractor has constant eps1 = lambda^2/2 and never ends."""

    lam = math.sqrt(2 * eps1)
    return Model(
        key,
        lambda f: math.exp(-lam * f),
        lambda f: -lam * math.exp(-lam * f),
        lambda f: lam * lam * math.exp(-lam * f),
        0.0,
        ends=False,
    )


MODELS = {
    "starobinsky": starobinsky(),
    "phi23": monomial(2 / 3, "phi23"),
    "phi2": monomial(2.0, "phi2"),
    "phi4": monomial(4.0, "phi4"),
    "powerlaw005": power_law(0.05, "powerlaw005"),
    "powerlaw015": power_law(0.15, "powerlaw015"),
    "powerlaw030": power_law(0.30, "powerlaw030"),
}


def flow_parameters(model: Model, phi, phi_n) -> dict:
    """Exact H, eps1, eps2 = dln eps1/dN, and d eps2/dN = eps2 eps3 from (phi, dphi/dN).

    Uses H^2 = V/(3 - eps1) and phi_NN + (3 - eps1)(phi_N + V'/V) = 0.
    """

    phi = np.asarray(phi, dtype=float)
    phi_n = np.asarray(phi_n, dtype=float)
    potential = np.vectorize(model.potential)(phi)
    log_slope = np.vectorize(model.slope)(phi) / potential
    log_curvature = np.vectorize(model.curvature)(phi) / potential
    eps1 = phi_n**2 / 2
    phi_nn = -(3 - eps1) * (phi_n + log_slope)
    eps1_n = phi_n * phi_nn
    phi_nnn = eps1_n * (phi_n + log_slope) - (3 - eps1) * (
        phi_nn + (log_curvature - log_slope**2) * phi_n
    )
    eps2 = 2 * phi_nn / phi_n
    eps2_n = 2 * (phi_nnn / phi_n - (phi_nn / phi_n) ** 2)
    return {
        "hubble": np.sqrt(potential / (3 - eps1)),
        "eps1": eps1,
        "eps2": eps2,
        "eps2_n": eps2_n,
        "potential": potential,
        "eps_v": log_slope**2 / 2,
        "eta_v": log_curvature,
    }


def curvature_squeeze_rate(eps2):
    """sigma = (z'/z)/(aH) for z = a sqrt(2 eps1): the coefficient of the squeeze generator."""

    return 1 + np.asarray(eps2) / 2


def curvature_pump(eps1, eps2, eps2_n):
    """(z''/z)/(aH)^2 = 2 - e1 + 3e2/2 - e1 e2/2 + e2^2/4 + e2 e3/2, exact."""

    eps1, eps2, eps2_n = (np.asarray(v) for v in (eps1, eps2, eps2_n))
    return 2 - eps1 + 1.5 * eps2 - eps1 * eps2 / 2 + eps2**2 / 4 + eps2_n / 2


def tensor_pump(eps1):
    """(a''/a)/(aH)^2 = 2 - eps1, exact; the tensor and test-field analogue of z''/z."""

    return 2 - np.asarray(eps1)


def constant_index(pump, eps1):
    """nu in z''/z = (nu^2 - 1/4)/eta^2 for frozen eps1 and pump, using (1 - eps1) eta = -1/aH."""

    return np.sqrt(0.25 + np.asarray(pump) / (1 - np.asarray(eps1)) ** 2)


def first_order_index(eps1, eps2):
    """nu = 3/2 + eps1 + eps2/2 to first order (3/2 + 3 eps_V - eta_V in potential parameters)."""

    return 1.5 + np.asarray(eps1) + np.asarray(eps2) / 2


@dataclass
class Background:
    """Dense background trajectory; n_end is where eps1 = 1 (or the end of the span)."""

    model: Model
    solution: object
    n_end: float

    def state(self, n) -> dict:
        phi, phi_n = self.solution.sol(np.asarray(n, dtype=float))
        values = flow_parameters(self.model, phi, phi_n)
        values["phi"] = phi
        values["phi_n"] = phi_n
        return values

    def log_comoving_hubble(self, n) -> np.ndarray:
        """ln(aH) with a = e^N."""

        return np.asarray(n) + np.log(self.state(n)["hubble"])

    def crossing_wavenumber(self, n_cross: float) -> float:
        return float(np.exp(self.log_comoving_hubble(n_cross)))

    def x(self, k: float, n) -> np.ndarray:
        return k * np.exp(-self.log_comoving_hubble(n))

    def time_at(self, k: float, x: float) -> float:
        """The e-fold time when k/(aH) = x; aH grows monotonically while eps1 < 1."""

        return brentq(
            lambda n: self.log_comoving_hubble(n) - math.log(k / x), self.solution.t[0], self.n_end
        )


def solve_background(model: Model) -> Background:
    """Integrate from the slow-roll attractor value phi_N = -V'/V until eps1 = 1."""

    def rhs(_n, y):
        phi, phi_n = y
        eps1 = phi_n * phi_n / 2
        return [phi_n, -(3 - eps1) * (phi_n + model.slope(phi) / model.potential(phi))]

    def end(_n, y):
        return y[1] * y[1] / 2 - 1

    end.terminal = True
    end.direction = 1
    span = POWER_LAW_SPAN if not model.ends else 10 * TOTAL_EFOLDS
    phi0 = model.phi_start
    solution = solve_ivp(
        rhs,
        (0.0, span),
        [phi0, -model.slope(phi0) / model.potential(phi0)],
        method="DOP853",
        rtol=1e-11,
        atol=1e-13,
        dense_output=True,
        events=end,
    )
    n_end = float(solution.t_events[0][0]) if model.ends else float(solution.t[-1])
    return Background(model, solution, n_end)


def hankel_quadratures(y, nu):
    """Constant-nu Bunch–Davies coefficients with y = -k eta:

    F = (sqrt(pi)/2) e^{i pi (nu + 1/2)/2} sqrt(y) H^(1)_nu(y),
    G = -(sqrt(pi)/2) e^{i pi (nu + 1/2)/2} sqrt(y) H^(1)_{nu-1}(y).
    """

    y = np.asarray(y, dtype=float)
    prefactor = math.sqrt(math.pi) / 2 * np.exp(0.5j * math.pi * (nu + 0.5)) * np.sqrt(y)
    return prefactor * hankel1(nu, y), -prefactor * hankel1(nu - 1, y)


def de_sitter_quadratures(x):
    """Massless test field in exact de Sitter (companion article, eq. 69), F = sqrt(k) f_k."""

    x = np.asarray(x, dtype=float)
    phase = np.exp(1j * x)
    return (1 + 1j / x) * phase / math.sqrt(2), -1j * phase / math.sqrt(2)


@dataclass
class ModeSolution:
    k: float
    n: np.ndarray
    x: np.ndarray
    F: np.ndarray
    G: np.ndarray
    state: dict


def solve_mode(
    background: Background,
    n_cross: float,
    *,
    tensor: bool = False,
    x_start: float = 100.0,
    n_eval: np.ndarray | None = None,
    n_stop: float | None = None,
    rtol: float = 1e-10,
) -> ModeSolution:
    """Integrate the background and one mode's quadrature coefficients together.

    The mode starts at x = x_start from the local constant-nu (Hankel) Bunch–Davies solution, which
    is exact for power-law inflation and otherwise differs only at second order in slow roll.
    """

    model = background.model
    k = background.crossing_wavenumber(n_cross)
    log_k = math.log(k)
    n_start = background.time_at(k, x_start)
    start = background.state(n_start)
    eps1 = float(start["eps1"])
    pump = (
        tensor_pump(eps1)
        if tensor
        else curvature_pump(eps1, float(start["eps2"]), float(start["eps2_n"]))
    )
    nu = float(constant_index(pump, eps1))
    f0, g0 = hankel_quadratures(x_start / (1 - eps1), nu)

    def rhs(n, y):
        phi, phi_n, fr, fi, gr, gi = y
        potential = model.potential(phi)
        eps1 = phi_n * phi_n / 2
        phi_nn = -(3 - eps1) * (phi_n + model.slope(phi) / potential)
        x = math.exp(log_k - n) * math.sqrt((3 - eps1) / potential)
        sigma = 1.0 if tensor else 1 + phi_nn / phi_n
        return [
            phi_n,
            phi_nn,
            x * gr + sigma * fr,
            x * gi + sigma * fi,
            -x * fr - sigma * gr,
            -x * fi - sigma * gi,
        ]

    stop = background.n_end if n_stop is None else n_stop
    y0 = [float(start["phi"]), float(start["phi_n"]), f0.real, f0.imag, g0.real, g0.imag]
    result = solve_ivp(
        rhs, (n_start, stop), y0, method="DOP853", rtol=rtol, atol=1e-12, dense_output=True
    )
    n = np.array([stop]) if n_eval is None else np.asarray(n_eval, dtype=float)
    n = np.clip(n, n_start, stop)
    phi, phi_n, fr, fi, gr, gi = result.sol(n)
    state = flow_parameters(model, phi, phi_n)
    x = k * np.exp(-n) / state["hubble"]
    return ModeSolution(k, n, x, fr + 1j * fi, gr + 1j * gi, state)


def bogoliubov(F, G):
    """b(N) = alpha b_in + beta b_in^dagger in the fixed reference basis (companion eq. 48)."""

    return (F + 1j * G) / math.sqrt(2), (np.conj(F) + 1j * np.conj(G)) / math.sqrt(2)


def squeeze_parameters(F, G):
    """Squeezing magnitude r and broad-axis angle phi = arg(alpha beta)/2 from the Q axis."""

    alpha, beta = bogoliubov(F, G)
    return np.arcsinh(np.abs(beta)), 0.5 * np.angle(alpha * beta)


def covariance(F, G) -> np.ndarray:
    """Symmetrized covariance of (Q, P); det = 1/4 for a pure Gaussian state."""

    cross = (F * np.conj(G)).real
    return np.array([[np.abs(F) ** 2, cross], [cross, np.abs(G) ** 2]])


def solution_matrix(F, G) -> np.ndarray:
    """Columns are two real solutions; Sigma = M M^T / 2 and M (cos, sin)/sqrt(2) is the contour."""

    return math.sqrt(2) * np.array([[np.real(F), np.imag(F)], [np.real(G), np.imag(G)]])


def wronskian(F, G):
    """F G* - F* G, equal to i for the canonical normalization."""

    return F * np.conj(G) - np.conj(F) * G


def align_late_phase(F, G, reference: complex):
    """Remove the global phase so the late conserved component is positive imaginary.

    This matches the companion article's de Sitter convention, f_k/a -> i H/sqrt(2k^3).
    """

    phase = np.exp(-1j * (np.angle(reference) - math.pi / 2))
    return F * phase, G * phase


def scalar_power(hubble, eps1, x, F):
    """Dimensionless curvature power k^3 P_zeta/(2 pi^2) = H^2/(8 pi^2 eps1) * 2 x^2 |F|^2."""

    return np.asarray(hubble) ** 2 / (8 * math.pi**2 * np.asarray(eps1)) * 2 * x**2 * np.abs(F) ** 2


def tensor_power(hubble, x, F):
    """Dimensionless tensor power summed over both polarizations: 2H^2/pi^2 * 2 x^2 |F_T|^2."""

    return 2 * np.asarray(hubble) ** 2 / math.pi**2 * 2 * x**2 * np.abs(F) ** 2


def scalar_power_slow_roll(hubble, eps1, eps2, next_order: bool = False):
    """H^2/(8 pi^2 eps1) at k = aH, optionally times 1 - 2(C+1) eps1 - C eps2."""

    leading = np.asarray(hubble) ** 2 / (8 * math.pi**2 * np.asarray(eps1))
    if not next_order:
        return leading
    c = STEWART_LYTH_C
    return leading * (1 - 2 * (c + 1) * np.asarray(eps1) - c * np.asarray(eps2))


def tensor_power_slow_roll(hubble, eps1, next_order: bool = False):
    """2H^2/pi^2 at k = aH, optionally times 1 - 2(C+1) eps1."""

    leading = 2 * np.asarray(hubble) ** 2 / math.pi**2
    if not next_order:
        return leading
    return leading * (1 - 2 * (STEWART_LYTH_C + 1) * np.asarray(eps1))


def relative_power_error(numerical, approximation):
    """Signed fractional residual: positive when the approximation underestimates the power."""

    return np.asarray(numerical) / np.asarray(approximation) - 1


def first_order_observables(eps1, eps2) -> dict:
    """n_s - 1 = -2 eps1 - eps2, r = 16 eps1, n_T = -2 eps1 (so n_T = -r/8)."""

    eps1, eps2 = np.asarray(eps1), np.asarray(eps2)
    return {"ns": 1 - 2 * eps1 - eps2, "r": 16 * eps1, "nt": -2 * eps1}


def slow_roll_estimates(model_key: str, efolds_before_end):
    """Leading large-N estimates of (eps1, eps2) used in the article's model table."""

    n = np.asarray(efolds_before_end, dtype=float)
    if model_key == "starobinsky":
        return 3 / (4 * n**2), 2 / n
    p = {"phi23": 2 / 3, "phi2": 2.0, "phi4": 4.0}[model_key]
    return p / (4 * n + p), 4 / (4 * n + p)


def spectrum(
    background: Background, n_crosses: np.ndarray, *, x_start: float = 50.0, rtol: float = 1e-8
) -> dict:
    """Scalar and tensor powers at the end of the integration for many crossing times.

    The values use a unit potential amplitude; multiply by a normalization factor afterwards.
    The default start and tolerance keep relative errors below 1e-4 at a modest cost.
    """

    rows = {key: [] for key in ("k", "scalar", "tensor", "r_end")}
    for n_cross in n_crosses:
        options = {"x_start": x_start, "rtol": rtol}
        scalar = solve_mode(background, n_cross, **options)
        tensor = solve_mode(background, n_cross, tensor=True, **options)
        s = scalar.state
        rows["k"].append(scalar.k)
        rows["scalar"].append(scalar_power(s["hubble"], s["eps1"], scalar.x, scalar.F)[-1])
        rows["tensor"].append(tensor_power(s["hubble"], tensor.x, tensor.F)[-1])
        rows["r_end"].append(squeeze_parameters(scalar.F, scalar.G)[0][-1])
    crossing = background.state(np.asarray(n_crosses))
    result = {key: np.array(value) for key, value in rows.items()}
    result["crossing"] = crossing
    return result


def normalization(background: Background, n_pivot: float) -> float:
    """Potential amplitude making the late-time scalar power equal to SCALAR_AMPLITUDE at the pivot.

    V -> lambda V rescales H^2 -> lambda H^2 at fixed phi(N), so every power scales with lambda.
    """

    mode = solve_mode(background, n_pivot)
    s = mode.state
    return SCALAR_AMPLITUDE / float(scalar_power(s["hubble"], s["eps1"], mode.x, mode.F)[-1])
