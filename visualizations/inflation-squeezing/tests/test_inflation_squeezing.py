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
    transform = np.array([[1, 1], [-1j, 1j]]) / np.sqrt(2)
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


def test_bilingual_equations_and_shared_animation_payload(builder, tmp_path):
    root = Path(__file__).resolve().parents[3]
    pages = [
        (root / docs / "cosmology/inflation-squeezing/index.md").read_text()
        for docs in ["docs", "docs_ja"]
    ]
    equations = [re.findall(r"\$\$\s*(.*?)\s*\$\$", page, re.S) for page in pages]
    assert equations[0] == equations[1]
    assert len(equations[0]) >= 20
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
    equal_time = -np.log(2) / 2
    np.testing.assert_allclose(p.mode_history(np.array([equal_time]))["background"], 1)


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


def test_article_follows_ten_section_narrative_and_places_figures(builder, tmp_path):
    root = Path(__file__).resolve().parents[3]
    views = {"background": 4, "squeezing": 5, "basis": 6, "samples": 9, "acoustic": 10}
    for docs in ["docs", "docs_ja"]:
        source = (root / docs / "cosmology/inflation-squeezing/index.md").read_text()
        sections = re.split(r"^## ", source, flags=re.M)[1:]
        assert [int(s.split(".", 1)[0]) for s in sections[:10]] == list(range(1, 11))
        for view, section in views.items():
            assert f"&amp;view={view}" in sections[section - 1]
        assert "app/index.html?lang=" in sections[6]
        assert "app/teaser.svg" in sections[0]
    builder.build(tmp_path)
    assert 'width="720" height="250"' in (tmp_path / "teaser.svg").read_text()
    assert "__PLOTLY_ASSET__" not in (tmp_path / "supporting.html").read_text()
    payload = builder.supporting_payload()
    for locale in ["en", "ja"]:
        assert f"{locale}: {{" in (tmp_path / "supporting.js").read_text()
    assert len(payload["samples"]) == 61
    assert len(payload["acoustic"]["coherent"]["curves"]) == 8
