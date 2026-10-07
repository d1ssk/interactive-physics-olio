"""One real standing mode of a massless scalar in exact de Sitter, hbar=1.

Q=sqrt(k) a phi, P=(q' - a'/a q)/sqrt(k), x=-k eta=exp(-N).
The curvature-perturbation interpretation requires a separate slow-roll approximation.
"""

import numpy as np

J = np.array([[0.0, 1.0], [-1.0, 0.0]])
D = np.diag([1.0, -1.0])
FREQUENCY_BALANCE_N = float(-np.log(2) / 2)


def generator(x: float) -> np.ndarray:
    """Hamiltonian generator per e-fold, not per conformal time."""
    return D + x * J


def solution_basis(x: float) -> np.ndarray:
    """Exact real solutions: decaying column, then growing column as x -> 0."""
    c, s = np.cos(x), np.sin(x)
    return np.array([[c - s / x, s + c / x], [s, -c]])


def covariance(x: float) -> np.ndarray:
    """Symmetrized Bunch–Davies covariance in the fixed Q,P quadratures."""
    return 0.5 * np.array([[1 + x**-2, -1 / x], [-1 / x, 1.0]])


def mode_functions(x: float, k: float = 1.0) -> tuple[complex, complex]:
    """Positive-frequency q and p coefficients multiplying the in annihilator."""
    phase = np.exp(1j * x)
    return (1 + 1j / x) * phase / np.sqrt(2 * k), -1j * np.sqrt(k / 2) * phase


def bogoliubov(x: float) -> tuple[complex, complex]:
    """b(N)=alpha b_in + beta b_in^dagger, b=(Q+iP)/sqrt(2)."""
    return (1 + 1j / (2 * x)) * np.exp(1j * x), -1j / (2 * x) * np.exp(-1j * x)


def squeeze_parameters(x: float) -> tuple[float, float]:
    """Magnitude r and major-axis angle phi in radians, -pi/4 < phi < 0."""
    return float(np.arcsinh(1 / (2 * x))), float(-0.5 * np.arctan(2 * x))


def principal_directions(x: float) -> np.ndarray:
    """Columns: broad axis, narrow axis; orthogonal in the chosen quadratures."""
    _, angle = squeeze_parameters(x)
    c, s = np.cos(angle), np.sin(angle)
    return np.array([[c, -s], [s, c]])


def instantaneous_directions(x: float) -> np.ndarray | None:
    """Stretch/contract eigenvectors; exist only in the hyperbolic regime."""
    if x >= 1:
        return None
    eigenvalue = np.sqrt(1 - x * x)
    vectors = np.array([[1.0, -x / (1 + eigenvalue)], [-x / (1 + eigenvalue), 1.0]])
    return vectors / np.linalg.norm(vectors, axis=0)


def wigner_contour(x: float, angles: np.ndarray) -> np.ndarray:
    """Advected unit-Mahalanobis contour; markers at fixed angles are material points."""
    return solution_basis(x) @ np.array([np.cos(angles), np.sin(angles)]) / np.sqrt(2)


def hamiltonian_fields(x: float, points: np.ndarray) -> list[np.ndarray]:
    """Rotation, squeeze, and total velocities, all per e-fold (unscaled)."""
    return [matrix @ points for matrix in (x * J, D, generator(x))]


def acoustic_power(phase: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Toy oscillator with equal total initial variance in the two ensembles."""
    return np.cos(phase) ** 2, np.full_like(phase, 0.5)


def standing_to_traveling() -> np.ndarray:
    """Map (Q_R,P_R,Q_I,P_I) to (Q_+,P_+,Q_-,P_-), a_+=(b_R+i b_I)/sqrt(2)."""
    return np.array([[1, 0, 0, -1], [0, 1, 1, 0], [1, 0, 0, 1], [0, 1, -1, 0]]) / np.sqrt(2)


def pair_covariances(x: float) -> tuple[np.ndarray, np.ndarray]:
    """Full covariance in traveling and standing bases, with no mode traced out."""
    standing = np.kron(np.eye(2), covariance(x))
    transform = standing_to_traveling()
    return transform @ standing @ transform.T, standing


def mode_history(times: np.ndarray) -> dict[str, np.ndarray]:
    """Dimensionless exact de Sitter functions; q-mode and physical field-mode differ by a.

    rescaled = sqrt(2k) f; field = sqrt(2 k^3) f/a/H = x sqrt(2k) f.
    """
    x = np.exp(-times)
    rescaled = (1 + 1j / x) * np.exp(1j * x)
    return {
        "x": x,
        "r": np.arcsinh(1 / (2 * x)),
        "angle": -0.5 * np.arctan(2 * x),
        "background": 2 / x**2,
        "rescaled": rescaled,
        "field": x * rescaled,
    }


def gaussian_samples(x: float, seeds: np.ndarray) -> np.ndarray:
    """Advect fixed standard normal seeds to a Gaussian with covariance Sigma(x)."""
    return solution_basis(x) @ seeds / np.sqrt(2)


def conditional_momentum(x: float, q: np.ndarray) -> np.ndarray:
    """Mean P given Q in the positive Gaussian Wigner density."""
    return -x / (1 + x * x) * q


def acoustic_realizations(phase: np.ndarray, amplitudes: np.ndarray, coherent: bool) -> np.ndarray:
    """Rows are real oscillator histories; unit total initial variance in expectation.

    Independent rows of amplitudes are standard normals. A coherent ensemble uses
    A~N(0,1), B=0; an incoherent one uses A,B~N(0,1/2). No spatial phase is aligned.
    """
    a, b = amplitudes
    if coherent:
        return a[:, None] * np.cos(phase)
    return (a[:, None] * np.cos(phase) + b[:, None] * np.sin(phase)) / np.sqrt(2)
