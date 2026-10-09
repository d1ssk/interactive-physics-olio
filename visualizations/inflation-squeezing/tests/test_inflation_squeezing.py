import re
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp


def test_exact_flow_matches_independent_ode_and_preserves_symplectic_form(inflation):
    p = inflation
    times = np.linspace(-np.log(12), -np.log(0.2), 151)
    result = solve_ivp(
        lambda n, s: (p.generator(np.exp(-n)) @ s.reshape(2, 2)).ravel(),
        (times[0], times[-1]),
        np.eye(2).ravel(),
        t_eval=times,
        method="DOP853",
        rtol=1e-11,
        atol=1e-13,
    )
    assert result.success
    for n, numerical in zip(times, result.y.T, strict=True):
        x = np.exp(-n)
        flow = p.solution_basis(x) @ np.linalg.inv(p.solution_basis(12))
        np.testing.assert_allclose(flow, numerical.reshape(2, 2), atol=2e-9)
        np.testing.assert_allclose(flow.T @ p.J @ flow, p.J, atol=2e-13)
        np.testing.assert_allclose(flow @ p.covariance(12) @ flow.T, p.covariance(x), atol=1e-12)


def test_mode_normalization_bogoliubov_and_covariance_agree(inflation):
    p = inflation
    for x in np.geomspace(0.2, 100, 31):
        f, g = p.mode_functions(x, k=3.7)
        np.testing.assert_allclose(f * g.conjugate() - f.conjugate() * g, 1j, atol=1e-14)
        q, momentum = np.sqrt(3.7) * f, g / np.sqrt(3.7)
        sigma = np.array(
            [
                [abs(q) ** 2, (q * momentum.conjugate()).real],
                [(q * momentum.conjugate()).real, abs(momentum) ** 2],
            ]
        )
        np.testing.assert_allclose(sigma, p.covariance(x), atol=1e-14)
        alpha, beta = p.bogoliubov(x)
        np.testing.assert_allclose(abs(alpha) ** 2 - abs(beta) ** 2, 1, atol=1e-14)
        np.testing.assert_allclose(alpha, (q + 1j * momentum) / np.sqrt(2), atol=1e-14)
        np.testing.assert_allclose(
            beta, (q.conjugate() + 1j * momentum.conjugate()) / np.sqrt(2), atol=1e-14
        )
        r, angle = p.squeeze_parameters(x)
        np.testing.assert_allclose(abs(beta), np.sinh(r))
        np.testing.assert_allclose(np.angle(alpha * beta) / 2, angle)
        np.testing.assert_allclose(np.linalg.det(sigma), 0.25, atol=1e-14)
        axes = p.principal_directions(x)
        np.testing.assert_allclose(
            axes.T @ sigma @ axes, np.diag([np.exp(2 * r), np.exp(-2 * r)]) / 2, atol=1e-14
        )


def test_in_annihilator_reconstructs_the_field_and_is_time_independent(inflation):
    """The article's inverse mode expansion defines one fixed, normalized operator."""
    k = 3.7
    times = np.linspace(-np.log(12), -np.log(0.2), 37)
    result = solve_ivp(
        lambda n, matrix: (inflation.generator(np.exp(-n)) @ matrix.reshape(2, 2)).ravel(),
        (times[0], times[-1]),
        np.eye(2).ravel(),
        t_eval=times,
        method="DOP853",
        rtol=1e-11,
        atol=1e-13,
    )
    assert result.success
    initial_annihilator = None
    for n, values in zip(times, result.y.T, strict=True):
        # Rows give the evolved q,p coefficients in the initial canonical Q,P basis.
        flow = values.reshape(2, 2)
        q, momentum = flow[0] / np.sqrt(k), flow[1] * np.sqrt(k)
        f, g = inflation.mode_functions(np.exp(-n), k)
        annihilator = 1j * (f.conjugate() * momentum - g.conjugate() * q)
        if initial_annihilator is None:
            initial_annihilator = annihilator.copy()
        np.testing.assert_allclose(annihilator, initial_annihilator, atol=3e-10)
        np.testing.assert_allclose(
            f * annihilator + f.conjugate() * annihilator.conjugate(), q, atol=2e-14
        )
        np.testing.assert_allclose(
            g * annihilator + g.conjugate() * annihilator.conjugate(), momentum, atol=2e-14
        )
        c_q, c_p = annihilator
        commutator = 1j * (c_q * c_p.conjugate() - c_p * c_q.conjugate())
        np.testing.assert_allclose(commutator, 1, atol=3e-10)


def test_contour_is_material_and_has_the_stated_wigner_level(inflation):
    p = inflation
    angles = np.linspace(0, 2 * np.pi, 31)
    for x in [12, 1, 0.2]:
        ring = p.wigner_contour(x, angles)
        radius_squared = np.einsum("in,ij,jn->n", ring, np.linalg.inv(p.covariance(x)), ring)
        np.testing.assert_allclose(radius_squared, 1, atol=2e-14)
        flow = p.solution_basis(x) @ np.linalg.inv(p.solution_basis(12))
        np.testing.assert_allclose(ring, flow @ p.wigner_contour(12, angles), atol=1e-14)


def test_crossing_shear_and_different_notions_of_direction(inflation):
    p = inflation
    np.testing.assert_allclose(p.generator(1) @ p.generator(1), 0)
    assert np.linalg.norm(p.generator(1)) > 0
    assert p.instantaneous_directions(1) is None
    x = 0.2
    directions = p.instantaneous_directions(x)
    np.testing.assert_allclose(
        p.generator(x) @ directions, directions @ np.diag([np.sqrt(1 - x * x), -np.sqrt(1 - x * x)])
    )
    assert not np.allclose(directions.T @ directions, np.eye(2))
    # At late times the growing solution is horizontal and the decaying solution vertical.
    x = 0.001
    basis = p.solution_basis(x)
    np.testing.assert_allclose(basis[1, 1] / basis[0, 1], -x, rtol=1e-6)
    np.testing.assert_allclose(basis[0, 0] / basis[1, 0], -x / 3, rtol=1e-6)
    np.testing.assert_allclose(p.covariance(1e6), np.eye(2) / 2, atol=1e-6)


def test_traveling_to_standing_pair_term_is_two_identical_squeezes():
    # Congruence of the pair-creation matrix, including the sine-mode phase.
    transform = np.array([[1, 1], [1j, -1j]]) / np.sqrt(2)
    pair = np.array([[0, 1], [1, 0]])
    np.testing.assert_allclose(transform @ pair @ transform.T, np.eye(2), atol=1e-15)
    np.testing.assert_allclose(transform @ transform.conjugate().T, np.eye(2), atol=1e-15)


def test_acoustic_ensembles_have_equal_total_variance(inflation):
    phase = np.linspace(0, 4 * np.pi, 401)
    coherent, incoherent = inflation.acoustic_power(phase)
    np.testing.assert_allclose(coherent[::100], 1)
    np.testing.assert_allclose(coherent[50::100], 0, atol=1e-28)
    np.testing.assert_allclose(incoherent, 0.5)
    np.testing.assert_allclose(np.trapezoid(coherent, phase), np.trapezoid(incoherent, phase))


def test_bilingual_article_equation_parity():
    root = Path(__file__).resolve().parents[3]
    equations = [
        re.findall(
            r"\$\$\s*(.*?)\s*\$\$",
            (root / docs / "cosmology/inflation-squeezing/index.md")
            .read_text()
            .replace(r"\text{ は一定}", r"\text{ constant}"),
            re.S,
        )
        for docs in ["docs", "docs_ja"]
    ]
    assert equations[0] == equations[1]


def test_bilingual_pages_and_shared_animation_payload(builder, tmp_path):
    root = Path(__file__).resolve().parents[3]
    pages = [
        (root / docs / "cosmology/inflation-squeezing/index.md").read_text()
        for docs in ["docs", "docs_ja"]
    ]
    for locale, page in zip(["en", "ja"], pages, strict=True):
        assert f"app/index.html?lang={locale}" in page
        assert 'data-auto-height scrolling="no"' in page
    builder.build(tmp_path)
    assert (tmp_path / "data.json").is_file()
    payload = builder.application_payload()
    assert any(frame["n"] == 0 for frame in payload["frames"])
    np.testing.assert_allclose([payload["frames"][0]["x"], payload["frames"][-1]["x"]], [12, 0.2])
    app = (tmp_path / "app.js").read_text()
    assert "en: {" in app and "ja: {" in app


def test_full_basis_change_is_canonical_and_retains_the_state(inflation):
    p = inflation
    transform = p.standing_to_traveling()
    # Verify the sine convention independently of covariance (the state is invariant
    # under changing both sine quadrature signs, so covariance alone cannot catch it).
    z = np.random.default_rng(21).normal(size=(4, 10))
    traveling_z = transform @ z
    bc, bs = (z[0] + 1j * z[1]) / np.sqrt(2), (z[2] + 1j * z[3]) / np.sqrt(2)
    np.testing.assert_allclose(
        (traveling_z[0] + 1j * traveling_z[1]) / np.sqrt(2), (bc - 1j * bs) / np.sqrt(2)
    )
    np.testing.assert_allclose(
        (traveling_z[2] + 1j * traveling_z[3]) / np.sqrt(2), (bc + 1j * bs) / np.sqrt(2)
    )
    symplectic = np.kron(np.eye(2), p.J)
    np.testing.assert_allclose(transform @ symplectic @ transform.T, symplectic, atol=1e-15)
    for x in [12, 1, 0.2]:
        traveling, standing = p.pair_covariances(x)
        np.testing.assert_allclose(transform.T @ traveling @ transform, standing, atol=1e-14)
        np.testing.assert_allclose(standing[:2, :2], standing[2:, 2:])
        np.testing.assert_allclose(standing[:2, 2:], 0)
        np.testing.assert_allclose(
            traveling[:2, :2], np.eye(2) * (abs(p.bogoliubov(x)[1]) ** 2 + 0.5), atol=1e-14
        )
        np.testing.assert_allclose(np.linalg.det(traveling), 1 / 16, atol=1e-14)
        assert np.linalg.norm(traveling[:2, 2:]) > 0


def test_history_and_frozen_field_limit(inflation):
    p = inflation
    times = np.array([-np.log(12), 0, 4, 9])
    h = p.mode_history(times)
    for i, x in enumerate(h["x"]):
        f, _ = p.mode_functions(x, k=2.3)
        np.testing.assert_allclose(h["rescaled"][i], np.sqrt(2 * 2.3) * f)
        np.testing.assert_allclose(h["field"][i], x * h["rescaled"][i])
    np.testing.assert_allclose(abs(h["field"][-1]), 1, rtol=1e-7)
    np.testing.assert_allclose(h["r"][-1], times[-1], atol=1e-7)
    np.testing.assert_allclose(-h["field"].real[2:], h["field_decaying_asymptote"][2:], rtol=4e-5)
    equal_time = -np.log(2) / 2
    np.testing.assert_allclose(p.mode_history(np.array([equal_time]))["background"], 1)


def test_field_velocity_variance_and_freezing_preserve_quantum_normalization(inflation):
    for k, hubble in [(0.7, 1.3), (3.1, 0.4)]:
        for x in [12.0, 1.0, 0.1, 0.01]:
            a = k / (hubble * x)
            f, g = inflation.mode_functions(x, k)
            field, conformal_velocity, velocity = f / a, g / a, g / a**2
            # Differentiate the field mode independently of its momentum coefficient.
            step = 1e-5
            plus = inflation.mode_functions(x + step, k)[0] * hubble * (x + step) / k
            minus = inflation.mode_functions(x - step, k)[0] * hubble * (x - step) / k
            np.testing.assert_allclose(
                -k * (plus - minus) / (2 * step), conformal_velocity, rtol=2e-7
            )
            np.testing.assert_allclose(abs(conformal_velocity) ** 2, k / (2 * a**2))
            np.testing.assert_allclose(abs(velocity) ** 2, k / (2 * a**4))
            np.testing.assert_allclose(abs(field) ** 2, hubble**2 * (1 + x**2) / (2 * k**3))
            np.testing.assert_allclose(
                abs(velocity) / (hubble * abs(field)), x**2 / np.sqrt(1 + x**2)
            )
            # phi and cosmic-time velocity are not a canonical pair: their commutator
            # is i/a^3, while the pure-state uncertainty determinant is 1/(4 a^6).
            np.testing.assert_allclose(
                (field * velocity.conjugate() - field.conjugate() * velocity) * a**3, 1j
            )
            correlation = (field * velocity.conjugate()).real
            determinant = abs(field) ** 2 * abs(velocity) ** 2 - correlation**2
            np.testing.assert_allclose(determinant * a**6, 0.25, rtol=1e-9)


def test_samples_are_transport_of_same_initial_draw_and_covariance(inflation):
    p = inflation
    seeds = np.random.default_rng(718).normal(size=(2, 200000))
    for x in [12, 1, 0.2]:
        samples = p.gaussian_samples(x, seeds)
        expected = p.covariance(x)
        np.testing.assert_allclose(np.cov(samples), expected, rtol=0.015, atol=0.004)
        flow = p.solution_basis(x) @ np.linalg.inv(p.solution_basis(12))
        np.testing.assert_allclose(samples, flow @ p.gaussian_samples(12, seeds), atol=1e-13)
        residual = samples[1] - p.conditional_momentum(x, samples[0])
        np.testing.assert_allclose(np.var(residual), x * x / (2 * (1 + x * x)), rtol=0.015)


def test_random_acoustic_realizations_share_zeros_only_when_coherent(inflation):
    p = inflation
    phase = np.array([0, np.pi / 2, np.pi, 3 * np.pi / 2])
    seeds = np.random.default_rng(237).normal(size=(2, 4096))
    coherent = p.acoustic_realizations(phase, seeds, True)
    incoherent = p.acoustic_realizations(phase, seeds, False)
    np.testing.assert_allclose(coherent[:, 1::2], 0, atol=1e-14)
    assert np.std(incoherent[:, 1]) > 0.6
    np.testing.assert_allclose(np.mean(coherent**2, axis=0), p.acoustic_power(phase)[0], atol=0.035)
    np.testing.assert_allclose(
        np.mean(incoherent**2, axis=0), p.acoustic_power(phase)[1], atol=0.035
    )


def test_article_section_order_and_figure_placement(builder, tmp_path):
    root = Path(__file__).resolve().parents[3]
    placements = {"pairs": 6, "background": 8, "squeezing": 8, "basis": 8, "acoustic": 9}
    for docs in ["docs", "docs_ja"]:
        source = (root / docs / "cosmology/inflation-squeezing/index.md").read_text()
        sections = re.split(r"^## ", source, flags=re.M)[1:]
        section_count = 10
        assert [int(s.split(".", 1)[0]) for s in sections[:section_count]] == list(
            range(1, section_count + 1)
        )
        for view, section in placements.items():
            assert f"&amp;view={view}" in sections[section - 1]
        assert "app/index.html?lang=" in sections[7]
        assert "app/teaser.svg" in source.split("## ", 1)[0]
    builder.build(tmp_path)
    assert 'width="720" height="250"' in (tmp_path / "teaser.svg").read_text()
    assert "__PLOTLY_ASSET__" not in (tmp_path / "supporting.html").read_text()
    payload = builder.supporting_payload()
    for locale in ["en", "ja"]:
        assert f"{locale}: {{" in (tmp_path / "supporting.js").read_text()
    assert len(payload["samples"]) == 61
    assert len(payload["acoustic"]["coherent"]["curves"]) == 8


def test_pair_amplitude_kernel_and_number_distributions(inflation):
    p = inflation
    for x in [12.0, 1.0, 0.5, 0.2]:
        r, angle = p.squeeze_parameters(x)
        pair = p.pair_amplitude(x)
        np.testing.assert_allclose(abs(pair), np.tanh(r), atol=1e-14)
        np.testing.assert_allclose(np.angle(pair), 2 * angle, atol=1e-14)
        # The in condition i(f* p - g* q)|psi>=0 gives psi(Q) ∝ exp(-K Q^2/2).
        k = 2.9
        f, g = p.mode_functions(x, k)
        kernel = p.schrodinger_kernel(x)
        np.testing.assert_allclose(kernel, -1j * g.conjugate() / (k * f.conjugate()), atol=1e-14)
        variance = 1 / (2 * kernel.real)
        np.testing.assert_allclose(
            np.array(
                [
                    [variance, -kernel.imag * variance],
                    [-kernel.imag * variance, abs(kernel) ** 2 * variance],
                ]
            ),
            p.covariance(x),
            atol=1e-13,
        )
        traveling = p.two_mode_number_distribution(r, 600)
        standing = p.single_mode_number_distribution(r, 1200)
        np.testing.assert_allclose([traveling.sum(), standing.sum()], 1, atol=1e-12)
        np.testing.assert_allclose(standing[1::2], 0)
        n = np.arange(standing.size)
        np.testing.assert_allclose(n[:601] @ traveling, np.sinh(r) ** 2, rtol=1e-12)
        np.testing.assert_allclose(n @ standing, np.sinh(r) ** 2, rtol=1e-12)
        # n_c + n_s has the distribution of n_k + n_-k = 2n.
        total = np.convolve(standing, standing)[:200]
        np.testing.assert_allclose(total[::2], traveling[:100], atol=1e-15)
        np.testing.assert_allclose(total[1::2], 0, atol=1e-15)
        # A traveling mode alone is Gaussian with symplectic eigenvalue |beta|^2 + 1/2.
        nu = p.pair_covariances(x)[0][0, 0]
        entropy = (nu + 0.5) * np.log(nu + 0.5) - (nu - 0.5) * np.log(nu - 0.5)
        np.testing.assert_allclose(p.pair_entanglement_entropy(r), entropy, rtol=1e-12)
    assert p.pair_entanglement_entropy(0) == 0


def test_two_standing_squeezes_are_the_traveling_pair_state(inflation):
    """Truncated Fock-space check, independent of the closed-form distributions."""
    from math import factorial

    from scipy import sparse

    x, size = 0.6, 90
    r, _ = inflation.squeeze_parameters(x)
    pair = inflation.pair_amplitude(x)
    single = np.zeros(size, complex)
    for m in range(size // 2):
        single[2 * m] = pair**m * np.sqrt(float(factorial(2 * m))) / (2**m * factorial(m))
    single /= np.sqrt(np.cosh(r))
    np.testing.assert_allclose(np.linalg.norm(single), 1, atol=1e-10)
    lower = sparse.diags(np.sqrt(np.arange(1, size)), 1, format="csr")
    # The fixed-basis in condition, (alpha* b - beta b^dagger)|psi> = 0, for one standing mode.
    residual = lower @ single - pair * (lower.T @ single)
    np.testing.assert_allclose(residual[: size - 10], 0, atol=1e-9)
    identity = sparse.identity(size, format="csr")
    b_c, b_s = sparse.kron(lower, identity), sparse.kron(identity, lower)
    plus, minus = (b_c - 1j * b_s) / np.sqrt(2), (b_c + 1j * b_s) / np.sqrt(2)
    state = np.kron(single, single)
    low = np.add.outer(np.arange(size), np.arange(size)).ravel() < size - 10
    np.testing.assert_allclose((plus @ state - pair * (minus.conj().T @ state))[low], 0, atol=1e-9)
    n_plus, n_minus = plus.conj().T @ plus, minus.conj().T @ minus
    difference = (n_plus - n_minus) @ state
    np.testing.assert_allclose(np.vdot(difference, difference).real, 0, atol=1e-9)
    np.testing.assert_allclose(np.vdot(state, n_plus @ state).real, np.sinh(r) ** 2, rtol=1e-8)


def test_pair_payload_shows_identical_total_number(builder):
    pairs = builder.pair_number_payload()
    assert pairs["nMax"] == 24 and len(pairs["frames"]) == 81
    assert pairs["frames"][0]["x"] is None
    for frame in pairs["frames"]:
        np.testing.assert_allclose(frame["standingTotal"], frame["travelingTotal"], rtol=2e-4)
        if frame["x"] is not None:
            np.testing.assert_allclose(np.arcsinh(1 / (2 * frame["x"])), frame["r"], atol=1e-12)


def test_traveling_covariance_has_two_mode_squeezed_form(inflation):
    for x in [12.0, 1.0, 0.2]:
        r, angle = inflation.squeeze_parameters(x)
        reflection = np.array(
            [[np.cos(2 * angle), np.sin(2 * angle)], [np.sin(2 * angle), -np.cos(2 * angle)]]
        )
        expected = 0.5 * np.block(
            [
                [np.cosh(2 * r) * np.eye(2), np.sinh(2 * r) * reflection],
                [np.sinh(2 * r) * reflection, np.cosh(2 * r) * np.eye(2)],
            ]
        )
        np.testing.assert_allclose(inflation.pair_covariances(x)[0], expected, atol=1e-13)
