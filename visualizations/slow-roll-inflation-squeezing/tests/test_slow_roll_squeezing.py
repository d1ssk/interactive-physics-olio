"""Physical invariants of slow-roll mode evolution, and the bilingual article contract."""

import json
import math
import re
import shutil
import subprocess
from pathlib import Path

import numpy as np
import pytest

ROOT = Path(__file__).resolve().parents[3]
PAGE = "cosmology/slow-roll-inflation-squeezing/index.md"


def test_power_law_mode_is_the_exact_hankel_solution(slowroll, backgrounds):
    background = backgrounds["powerlaw030"]
    eps1 = 0.3
    nu = 1.5 + eps1 / (1 - eps1)
    n_cross = 60.0
    grid = np.linspace(n_cross - 4, n_cross + 8, 13)
    mode = slowroll.solve_mode(background, n_cross, n_eval=grid)
    np.testing.assert_allclose(mode.state["eps1"], eps1, rtol=1e-9)
    np.testing.assert_allclose(mode.state["eps2"], 0, atol=1e-8)
    F_h, G_h = slowroll.hankel_quadratures(mode.x / (1 - eps1), nu)
    # Solutions agree up to a constant global phase, which no observable depends on.
    phase = F_h[0] / mode.F[0]
    np.testing.assert_allclose(abs(phase), 1, atol=1e-8)
    np.testing.assert_allclose(mode.F * phase, F_h, rtol=1e-7)
    np.testing.assert_allclose(mode.G * phase, G_h, rtol=1e-7, atol=1e-9)
    # The exact constant-nu index equals the frozen-pump formula used for initial data.
    pump = slowroll.curvature_pump(eps1, 0.0, 0.0)
    np.testing.assert_allclose(slowroll.constant_index(pump, eps1), nu, rtol=1e-14)


def test_tiny_slow_roll_reduces_to_the_de_sitter_test_field(slowroll):
    background = slowroll.solve_background(slowroll.power_law(1e-7, "tiny"))
    n_cross = 60.0
    grid = n_cross + np.linspace(-3, 6, 10)
    mode = slowroll.solve_mode(background, n_cross, n_eval=grid)
    F_ds, G_ds = slowroll.de_sitter_quadratures(mode.x)
    phase = F_ds[0] / mode.F[0]
    np.testing.assert_allclose(mode.F * phase, F_ds, rtol=2e-6)
    np.testing.assert_allclose(mode.G * phase, G_ds, rtol=2e-6, atol=1e-8)
    r, angle = slowroll.squeeze_parameters(mode.F, mode.G)
    np.testing.assert_allclose(r, np.arcsinh(1 / (2 * mode.x)), rtol=2e-6)
    np.testing.assert_allclose(angle, -0.5 * np.arctan(2 * mode.x), atol=2e-6)


def test_hankel_solution_limits_and_wronskian(slowroll):
    y = np.array([1e-3, 0.3, 2.0, 40.0])
    for nu in (1.5, 1.52, 1.8):
        F, G = slowroll.hankel_quadratures(y, nu)
        np.testing.assert_allclose(slowroll.wronskian(F, G), 1j, rtol=1e-10)
    F, G = slowroll.hankel_quadratures(y, 1.5)
    F_ds, G_ds = slowroll.de_sitter_quadratures(y)
    np.testing.assert_allclose(F, F_ds, rtol=1e-12)
    np.testing.assert_allclose(G, G_ds, rtol=1e-12)
    # Bunch–Davies: F -> e^{iy}/sqrt(2) and G -> -i e^{iy}/sqrt(2) deep inside the horizon.
    large = np.array([2e3, 5e3])
    F, G = slowroll.hankel_quadratures(large, 1.57)
    np.testing.assert_allclose(F * math.sqrt(2) * np.exp(-1j * large), 1, atol=1e-3)
    np.testing.assert_allclose(G * math.sqrt(2) * np.exp(-1j * large), -1j, atol=1e-3)


def test_exact_background_terms_match_finite_differences(slowroll, backgrounds):
    background = backgrounds["phi2"]
    n = background.n_end - np.array([30.0, 5.0, 1.0, 0.3])
    step = 1e-3
    s = background.state(n)

    def log_z(times):
        return times + 0.5 * np.log(background.state(times)["eps1"])

    def log_a_hubble(times):
        return background.log_comoving_hubble(times)

    first = (log_z(n + step) - log_z(n - step)) / (2 * step)
    second = (log_z(n + step) - 2 * log_z(n) + log_z(n - step)) / step**2
    np.testing.assert_allclose(first, slowroll.curvature_squeeze_rate(s["eps2"]), atol=1e-6)
    np.testing.assert_allclose(
        (log_a_hubble(n + step) - log_a_hubble(n - step)) / (2 * step), 1 - s["eps1"], atol=1e-6
    )
    # z''/z = (aH)^2 [L_NN + L_N^2 + (1 - eps1) L_N] with L = ln z and d/deta = aH d/dN.
    pump = second + first**2 + (1 - s["eps1"]) * first
    np.testing.assert_allclose(
        pump, slowroll.curvature_pump(s["eps1"], s["eps2"], s["eps2_n"]), atol=1e-5
    )
    np.testing.assert_allclose(slowroll.tensor_pump(s["eps1"]), 2 - s["eps1"])
    # Inflation ends exactly where eps1 reaches one.
    np.testing.assert_allclose(background.state(background.n_end)["eps1"], 1, atol=1e-9)


def test_canonical_normalization_and_pure_state_area(slowroll, backgrounds):
    background = backgrounds["starobinsky"]
    n_cross = background.n_end - 10
    grid = n_cross + np.linspace(-4, 9, 27)
    for tensor in (False, True):
        mode = slowroll.solve_mode(background, n_cross, n_eval=grid, tensor=tensor)
        np.testing.assert_allclose(slowroll.wronskian(mode.F, mode.G), 1j, rtol=1e-8)
        covariance = slowroll.covariance(mode.F, mode.G)
        determinant = covariance[0, 0] * covariance[1, 1] - covariance[0, 1] ** 2
        # Late entries grow like e^{2r}; compare against the size of the cancelling products.
        scale = covariance[0, 0] * covariance[1, 1]
        assert np.all(abs(determinant - 0.25) < 1e-9 * scale + 1e-9)
        matrix = slowroll.solution_matrix(mode.F, mode.G)
        np.testing.assert_allclose(
            np.einsum("ijn,kjn->ikn", matrix, matrix) / 2, covariance, rtol=1e-9, atol=1e-12
        )
        alpha, beta = slowroll.bogoliubov(mode.F, mode.G)
        assert np.all(abs(abs(alpha) ** 2 - abs(beta) ** 2 - 1) < 1e-9 * abs(alpha) ** 2 + 1e-9)


def test_curvature_freezes_and_squeezing_tracks_log_z(slowroll, backgrounds):
    for key in ("starobinsky", "phi2", "phi4"):
        background = backgrounds[key]
        n_cross = background.n_end - 20
        k = background.crossing_wavenumber(n_cross)
        late = np.linspace(background.time_at(k, 1e-2), background.n_end, 9)
        mode = slowroll.solve_mode(background, n_cross, n_eval=late)
        s = mode.state
        zeta = mode.x * s["hubble"] * mode.F / np.sqrt(s["eps1"])
        np.testing.assert_allclose(abs(zeta), abs(zeta[0]), rtol=5e-4)
        r, angle = slowroll.squeeze_parameters(mode.F, mode.G)
        crossing = background.state(n_cross)
        log_z = late + 0.5 * np.log(s["eps1"]) - n_cross - 0.5 * np.log(crossing["eps1"])
        np.testing.assert_allclose(r, log_z, atol=0.1)
        np.testing.assert_allclose(angle, 0, atol=0.02)
        # sigma varies quickly in the final interval, so compare rates before it.
        rate = np.diff(r)[:-1] / np.diff(late)[:-1]
        sigma = slowroll.curvature_squeeze_rate(s["eps2"])[:-1]
        np.testing.assert_allclose(rate, 0.5 * (sigma[1:] + sigma[:-1]), atol=0.02)


def test_spectra_agree_with_next_order_slow_roll(slowroll, backgrounds):
    for key in ("starobinsky", "phi23", "phi2", "phi4"):
        background = backgrounds[key]
        n_pivot = background.n_end - slowroll.PIVOT_EFOLDS
        crossings = n_pivot + np.array([-0.5, 0.0, 0.5])
        spec = slowroll.spectrum(background, crossings)
        c = spec["crossing"]
        leading = slowroll.scalar_power_slow_roll(c["hubble"], c["eps1"], c["eps2"])
        nxt = slowroll.scalar_power_slow_roll(c["hubble"], c["eps1"], c["eps2"], next_order=True)
        eps1, eps2 = c["eps1"][1], c["eps2"][1]
        np.testing.assert_allclose(spec["scalar"], nxt, rtol=1e-3)
        assert np.all(abs(spec["scalar"] / leading - 1) < 2 * (abs(eps1) + abs(eps2)))
        tensor_next = slowroll.tensor_power_slow_roll(c["hubble"], c["eps1"], next_order=True)
        np.testing.assert_allclose(spec["tensor"], tensor_next, rtol=1e-3)
        # The plotted residual must retain sign and resolve the next-order improvement.
        for actual, lowest, corrected in (
            (spec["scalar"], leading, nxt),
            (
                spec["tensor"],
                slowroll.tensor_power_slow_roll(c["hubble"], c["eps1"]),
                tensor_next,
            ),
        ):
            error = slowroll.relative_power_error(actual, corrected)
            assert np.all(abs(error) < 1e-3)
            assert np.all(abs(error) < abs(slowroll.relative_power_error(actual, lowest)))
            np.testing.assert_allclose(corrected * (1 + error), actual)
        ln_k = np.log(spec["k"])
        tilt = 1 + (np.log(spec["scalar"][2]) - np.log(spec["scalar"][0])) / (ln_k[2] - ln_k[0])
        tensor_tilt = (np.log(spec["tensor"][2]) - np.log(spec["tensor"][0])) / (ln_k[2] - ln_k[0])
        ratio = spec["tensor"][1] / spec["scalar"][1]
        first = slowroll.first_order_observables(eps1, eps2)
        second_order = 3 * (eps1 + eps2) ** 2
        assert abs(tilt - first["ns"]) < second_order
        assert abs(ratio / first["r"] - 1) < 3 * (eps1 + eps2)
        assert abs(tensor_tilt + ratio / 8) < second_order


def test_slow_roll_estimates_describe_the_numerical_backgrounds(slowroll, backgrounds):
    for key in ("starobinsky", "phi23", "phi2", "phi4"):
        background = backgrounds[key]
        before_end = np.array([55.0, 25.0])
        s = background.state(background.n_end - before_end)
        eps1, eps2 = slowroll.slow_roll_estimates(key, before_end)
        np.testing.assert_allclose(s["eps1"], eps1, rtol=0.2)
        np.testing.assert_allclose(s["eps2"], eps2, rtol=0.1)
        np.testing.assert_allclose(s["eps_v"], s["eps1"], rtol=0.05)


def test_config_payload_windows_and_history(builder, backgrounds):
    for key in ("starobinsky-55", "phi4-5", "powerlaw030"):
        payload = builder.config_payload(key, backgrounds[key.partition("-")[0]])
        window = payload["window"]
        n = np.array(window["n"])
        assert len(n) == builder.WINDOW_FRAMES and np.all(np.diff(n) > 0)
        xs = [np.array(mode["x"]) for mode in window["modes"]]
        np.testing.assert_allclose(xs[0][0], builder.WINDOW_X_START, rtol=1e-4)
        for x in xs:
            # Strictly decreasing x shows no mode was clipped to its start time.
            assert np.all(np.diff(x) < 0)
        assert xs[2][0] > xs[1][0] > xs[0][0]
        np.testing.assert_allclose([m["crossing"] for m in window["modes"]], [-1.5, 0, 1.5])
        for mode in window["modes"]:
            matrix = np.array(mode["matrix"])
            np.testing.assert_allclose(
                matrix[:, 0] * matrix[:, 3] - matrix[:, 1] * matrix[:, 2], -1, atol=2e-4
            )
        history = payload["history"]
        curvature = np.array(history["curvature"])
        np.testing.assert_allclose(curvature[:, -1], [0, 1, 1], atol=1e-4)
        assert history["n"][0] < -2 and history["x"][1][0] == pytest.approx(20, rel=1e-3)


def test_spectrum_payload_is_normalized_at_the_pivot(builder, slowroll, backgrounds):
    payload = builder.spectrum_payload("phi2", backgrounds["phi2"])
    pivot = payload["pivot"]["index"]
    assert payload["lnk"][pivot] == 0
    np.testing.assert_allclose(payload["scalar"][pivot], slowroll.SCALAR_AMPLITUDE, rtol=1e-4)
    assert payload["beforeEnd"][pivot] == slowroll.PIVOT_EFOLDS
    cmb = payload["cmbWindow"]
    # The band is a physical wavenumber interval on a natural-log axis, with the pivot inside.
    assert cmb["lnk"][0] < 0 < cmb["lnk"][1]
    assert payload["lnk"][0] < cmb["lnk"][0] < cmb["lnk"][1] < payload["lnk"][-1]
    np.testing.assert_allclose(np.exp(cmb["lnk"]) * cmb["pivotMpc"], cmb["kMpc"])
    np.testing.assert_allclose(
        slowroll.log_wavenumber_ratio(np.array(cmb["kMpc"]) * 1000, cmb["pivotMpc"] * 1000),
        cmb["lnk"],
    )
    np.testing.assert_allclose(payload["pivot"]["ns"], 0.9634, atol=5e-4)
    np.testing.assert_allclose(payload["pivot"]["r"], 0.144, rtol=1e-2)
    for name, errors in payload["relativeErrors"].items():
        numerical = payload["scalar" if name.startswith("scalar") else "tensor"]
        # Residuals are computed before JSON rounding so small errors remain resolvable.
        np.testing.assert_allclose(
            np.array(payload[name]) * (1 + np.array(errors)), numerical, rtol=1e-4
        )


def test_hankel_reference_is_local_but_exact_for_power_law(builder, backgrounds):
    payload = builder.config_payload("starobinsky-55", backgrounds["starobinsky"])
    h = payload["history"]
    ratio = np.array(h["canonical"][2]) / np.array(h["canonicalHankel"][2])
    near_crossing = np.argmin(abs(np.array(h["n"]) - 5))
    assert ratio[near_crossing] == pytest.approx(1, abs=0.01)
    assert ratio[-1] == pytest.approx(51.3, rel=0.01)
    exact = builder.config_payload("powerlaw030", backgrounds["powerlaw030"])["history"]
    np.testing.assert_allclose(exact["canonical"][2], exact["canonicalHankel"][2], rtol=2e-5)


@pytest.mark.skipif(
    shutil.which("node") is None, reason="Node.js is needed for UI concurrency tests"
)
def test_supporting_ui_keeps_the_latest_selection():
    subprocess.run(
        [shutil.which("node"), "--test", str(Path(__file__).with_name("supporting_ui.test.cjs"))],
        check=True,
        capture_output=True,
        text=True,
    )


def test_build_stages_bilingual_static_application(builder, tmp_path, monkeypatch):
    monkeypatch.setattr(builder, "config_keys", lambda: ["starobinsky-55"])
    monkeypatch.setattr(
        builder.physics, "MODELS", {"starobinsky": builder.physics.MODELS["starobinsky"]}
    )
    monkeypatch.setattr(builder, "ENDING_MODELS", ("starobinsky",))
    builder.build(tmp_path)
    for name in ("index.html", "supporting.html", "teaser.svg", "data/config-starobinsky-55.json"):
        assert (tmp_path / name).is_file()
    assert "__PLOTLY_ASSET__" not in (tmp_path / "supporting.html").read_text()
    assert 'width="720" height="250"' in (tmp_path / "teaser.svg").read_text()
    json.loads((tmp_path / "data/spectrum-starobinsky.json").read_text())
    for script in ("app.js", "supporting.js", "common.js"):
        source = (tmp_path / script).read_text()
        assert "en: {" in source and "ja: {" in source


def test_bilingual_articles_share_equations_embeds_and_structure():
    pages = {docs: (ROOT / docs / PAGE).read_text(encoding="utf-8") for docs in ("docs", "docs_ja")}
    equations = [re.findall(r"\$\$\s*(.*?)\s*\$\$", page, re.S) for page in pages.values()]
    assert equations[0] == equations[1] and len(equations[0]) == 33
    numbered = [equation for equation in equations[0] if r"\tag{" in equation]
    assert len(numbered) == 30
    for index, equation in enumerate(numbered, start=1):
        assert rf"\tag{{{index}}}\label{{eq:slowroll-{index}}}" in equation
    for locale, docs in (("en", "docs"), ("ja", "docs_ja")):
        page = pages[docs]
        sections = re.split(r"^## ", page, flags=re.M)[1:]
        assert [s.split(".", 1)[0] for s in sections[:8]] == [str(i) for i in range(1, 9)]
        for view, section in (("background", 1), ("frequencies", 2), ("modes", 5), ("spectrum", 7)):
            assert f"supporting.html?lang={locale}&amp;view={view}" in sections[section - 1]
        assert f"app/index.html?lang={locale}" in sections[5]
        assert "../inflation-squeezing/" in page.split("## 1.", 1)[0]
        assert page.count('data-auto-height scrolling="no"') == 5
        assert "app/teaser.svg" in page.split("## 1.", 1)[0]


def test_article_is_listed_in_both_cosmology_indexes():
    for docs, title in (
        ("docs", "Quantum Fluctuations in Single-Field Slow-Roll Inflation"),
        ("docs_ja", "単一場 slow-roll インフレーションの量子揺らぎ"),
    ):
        index = (ROOT / docs / "cosmology/index.md").read_text(encoding="utf-8")
        assert f"- **[{title}](slow-roll-inflation-squeezing/)**<br>" in index
