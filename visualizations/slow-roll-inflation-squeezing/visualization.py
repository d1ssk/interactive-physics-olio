"""Precompute every plotted quantity from physics.py and stage a static bilingual application.

The browser only draws: the main page is a dependency-free SVG animation of three modes, and the
supporting views use the site's shared Plotly bundle. Each model or exit-time choice is a separate
JSON file so a page fetches only what it shows.
"""

from __future__ import annotations

import json
import math
import shutil
from pathlib import Path

import numpy as np

from physics_atlas.assets import (
    PLOTLY_GL3D_ASSET_NAME,
    copy_mathjax_assets,
    copy_visualization_theme_assets,
)

from . import physics

SOURCE = Path(__file__).parent
ENDING_MODELS = ("starobinsky", "phi23", "phi2", "phi4")
POWER_LAW_MODELS = ("powerlaw005", "powerlaw015", "powerlaw030")
EXIT_EFOLDS = (55, 25, 10, 5)
# Crossing-time spacing of the three animated modes, in e-folds.
SPACING = 1.5
WINDOW_FRAMES = 161
WINDOW_X_START, WINDOW_X_STOP = 8.0, 0.15
HISTORY_X_START = 20.0
POWER_LAW_PIVOT = 60.0
POWER_LAW_HISTORY = 12.0
LIMIT = 4.4


def _significant(values, digits: int = 5) -> list:
    return [float(f"{value:.{digits}g}") for value in np.asarray(values, dtype=float).ravel()]


def _complex(values, digits: int = 5) -> list:
    values = np.asarray(values)
    return [_significant(part, digits) for part in (values.real, values.imag, np.abs(values))]


def config_keys() -> list[str]:
    keys = [f"{model}-{exit_efolds}" for model in ENDING_MODELS for exit_efolds in EXIT_EFOLDS]
    return keys + list(POWER_LAW_MODELS)


def _pivot_time(background: physics.Background, exit_efolds: float | None) -> float:
    if background.model.ends:
        return background.n_end - (physics.PIVOT_EFOLDS if exit_efolds is None else exit_efolds)
    return POWER_LAW_PIVOT


def _crossing_summary(background: physics.Background, n_cross: float) -> dict:
    s = background.state(n_cross)
    eps1, eps2 = float(s["eps1"]), float(s["eps2"])
    first = physics.first_order_observables(eps1, eps2)
    return {
        "eps1": eps1,
        "eps2": eps2,
        "nu": float(physics.first_order_index(eps1, eps2)),
        "sigma": float(physics.curvature_squeeze_rate(eps2)),
        "ns": float(first["ns"]),
        "r": float(first["r"]),
    }


def config_payload(key: str, background: physics.Background | None = None) -> dict:
    """Three animated modes plus the full history of the middle (pivot) mode."""

    model_key, _, exit_text = key.partition("-")
    exit_efolds = float(exit_text) if exit_text else None
    if background is None:
        background = physics.solve_background(physics.MODELS[model_key])
    n_pivot = _pivot_time(background, exit_efolds)
    n_end = background.n_end if background.model.ends else n_pivot + POWER_LAW_HISTORY
    crossings = [n_pivot + (j - 1) * SPACING for j in range(3)]
    wavenumbers = [background.crossing_wavenumber(n) for n in crossings]
    window_start = background.time_at(wavenumbers[0], WINDOW_X_START)
    window_stop = min(background.time_at(wavenumbers[2], WINDOW_X_STOP), n_end - 0.02)
    window = np.linspace(window_start, window_stop, WINDOW_FRAMES)
    # Every mode must start inside the window at a larger x than it ever displays.
    x_start = max(100.0, 1.5 * float(background.x(wavenumbers[2], window_start)))
    state = background.state(window)
    modes = []
    for n_cross in crossings:
        # The final evaluation point fixes the global phase from the late conserved component.
        mode = physics.solve_mode(
            background, n_cross, n_eval=np.append(window, n_end), n_stop=n_end, x_start=x_start
        )
        F, G = physics.align_late_phase(mode.F[:-1], mode.G[:-1], mode.F[-1])
        x = mode.x[:-1]
        r, angle = physics.squeeze_parameters(F, G)
        F_ds, G_ds = physics.de_sitter_quadratures(x)
        r_ds, angle_ds = physics.squeeze_parameters(F_ds, G_ds)
        matrix = physics.solution_matrix(F, G)
        matrix_ds = physics.solution_matrix(F_ds, G_ds)
        modes.append(
            {
                "crossing": n_cross - n_pivot,
                "x": _significant(x),
                "r": _significant(r),
                "angle": _significant(np.degrees(angle)),
                "rDeSitter": _significant(r_ds),
                "angleDeSitter": _significant(np.degrees(angle_ds)),
                "matrix": [
                    _significant(row, 6) for row in matrix.transpose(2, 0, 1).reshape(-1, 4)
                ],
                "matrixDeSitter": [
                    _significant(row, 6) for row in matrix_ds.transpose(2, 0, 1).reshape(-1, 4)
                ],
            }
        )
    payload = {
        "key": key,
        "model": model_key,
        "exit": exit_efolds,
        "spacing": SPACING,
        "limit": LIMIT,
        "pivot": _crossing_summary(background, n_pivot),
        "end": n_end - n_pivot if background.model.ends else None,
        "window": {
            "n": _significant(window - n_pivot, 6),
            "pump": _significant(
                physics.curvature_pump(state["eps1"], state["eps2"], state["eps2_n"])
            ),
            "tensorPump": _significant(physics.tensor_pump(state["eps1"])),
            "modes": modes,
        },
        "history": history_payload(background, n_pivot, n_end, wavenumbers),
    }
    return payload


def _history_grid(background: physics.Background, k: float, n_end: float) -> np.ndarray:
    """Resolve early oscillations with steps of about 0.12/x; use 0.2 e-fold steps later."""

    grid = [background.time_at(k, HISTORY_X_START)]
    while grid[-1] < n_end:
        x = float(background.x(k, grid[-1]))
        grid.append(grid[-1] + min(0.2, 0.12 / x))
    grid[-1] = n_end
    return np.array(grid)


def history_payload(
    background: physics.Background, n_pivot: float, n_end: float, wavenumbers: list[float]
) -> dict:
    """The pivot mode from x = 20 to the end of inflation, with its two analytic comparisons."""

    k = wavenumbers[1]
    grid = _history_grid(background, k, n_end)
    mode = physics.solve_mode(background, n_pivot, n_eval=grid, n_stop=n_end)
    F, G = physics.align_late_phase(mode.F, mode.G, mode.F[-1])
    s = mode.state
    crossing = background.state(n_pivot)
    eps1_c = float(crossing["eps1"])
    nu = float(
        physics.constant_index(
            physics.curvature_pump(eps1_c, float(crossing["eps2"]), float(crossing["eps2_n"])),
            eps1_c,
        )
    )
    F_h, G_h = physics.hankel_quadratures(mode.x / (1 - eps1_c), nu)
    F_h, G_h = physics.align_late_phase(F_h, G_h, F_h[-1])
    F_ds, _ = physics.de_sitter_quadratures(mode.x)
    # zeta_k ∝ x H F/sqrt(eps1); the de Sitter test field phi_k ∝ x F_dS.
    zeta = mode.x * s["hubble"] * F / np.sqrt(s["eps1"])
    zeta = zeta / abs(zeta[-1])
    field = math.sqrt(2) * mode.x * F_ds
    zeta_h = mode.x * F_h
    zeta_h = zeta_h / abs(zeta_h[-1])
    r, _ = physics.squeeze_parameters(F, G)
    r_h, _ = physics.squeeze_parameters(F_h, G_h)
    return {
        "n": _significant(grid - n_pivot, 6),
        "x": [_significant(mode.x * kj / k) for kj in wavenumbers],
        "pump": _significant(physics.curvature_pump(s["eps1"], s["eps2"], s["eps2_n"])),
        "tensorPump": _significant(physics.tensor_pump(s["eps1"])),
        "sigma": _significant(physics.curvature_squeeze_rate(s["eps2"])),
        "eps1": _significant(s["eps1"]),
        "eps2": _significant(s["eps2"]),
        "canonical": _complex(math.sqrt(2) * F),
        "canonicalHankel": _complex(math.sqrt(2) * F_h),
        "canonicalDeSitter": _complex(math.sqrt(2) * F_ds),
        "curvature": _complex(zeta),
        "curvatureHankel": _complex(zeta_h),
        "fieldDeSitter": _complex(field),
        "r": _significant(r),
        "rHankel": _significant(r_h),
        "rDeSitter": _significant(np.arcsinh(1 / (2 * mode.x))),
        "nuCrossing": nu,
    }


def _spectrum_grid(background: physics.Background) -> tuple[np.ndarray, int]:
    if background.model.ends:
        before_end = np.concatenate([np.arange(65.0, 4.0, -2.0), np.arange(4.0, 0.4, -0.5)])
        pivot = int(np.flatnonzero(before_end == physics.PIVOT_EFOLDS)[0])
        return background.n_end - before_end, pivot
    offsets = np.arange(-12.0, 52.1, 4.0)
    return POWER_LAW_PIVOT + offsets, int(np.flatnonzero(offsets == 0)[0])


def spectrum_payload(key: str, background: physics.Background | None = None) -> dict:
    """Scalar and tensor spectra at the end of inflation, against slow-roll formulas."""

    if background is None:
        background = physics.solve_background(physics.MODELS[key])
    crossings, pivot = _spectrum_grid(background)
    spec = physics.spectrum(background, crossings)
    scale = physics.SCALAR_AMPLITUDE / spec["scalar"][pivot]
    c = spec["crossing"]
    ln_k = np.log(spec["k"] / spec["k"][pivot])
    scalar, tensor = scale * spec["scalar"], scale * spec["tensor"]
    hubble = math.sqrt(scale) * c["hubble"]
    first = physics.first_order_observables(c["eps1"], c["eps2"])
    tilt = 1 + np.gradient(np.log(scalar), ln_k)
    tensor_tilt = np.gradient(np.log(tensor), ln_k)
    ratio = tensor / scalar
    pivot_potential = scale * float(c["potential"][pivot])
    approximations = {
        "scalarLeading": physics.scalar_power_slow_roll(hubble, c["eps1"], c["eps2"]),
        "scalarNext": physics.scalar_power_slow_roll(hubble, c["eps1"], c["eps2"], True),
        "tensorLeading": physics.tensor_power_slow_roll(hubble, c["eps1"]),
        "tensorNext": physics.tensor_power_slow_roll(hubble, c["eps1"], True),
    }
    return {
        "key": key,
        "lnk": _significant(ln_k, 6),
        "cmbWindow": {
            "pivotMpc": physics.PIVOT_WAVENUMBER_MPC_INV,
            "kMpc": list(physics.CMB_WAVENUMBER_RANGE_MPC_INV),
            "lnk": physics.log_wavenumber_ratio(physics.CMB_WAVENUMBER_RANGE_MPC_INV).tolist(),
        },
        "beforeEnd": _significant(background.n_end - crossings, 4)
        if background.model.ends
        else None,
        "scalar": _significant(scalar),
        "tensor": _significant(tensor),
        **{name: _significant(values) for name, values in approximations.items()},
        "relativeErrors": {
            name: _significant(
                physics.relative_power_error(
                    scalar if name.startswith("scalar") else tensor, values
                )
            )
            for name, values in approximations.items()
        },
        "ns": _significant(tilt),
        "nsFirst": _significant(first["ns"]),
        "r": _significant(ratio),
        "rFirst": _significant(first["r"]),
        "nt": _significant(tensor_tilt),
        "ntFirst": _significant(first["nt"]),
        "consistency": _significant(-ratio / 8),
        "squeezingEnd": _significant(spec["r_end"], 4),
        "pivot": {
            "index": pivot,
            "ns": float(tilt[pivot]),
            "r": float(ratio[pivot]),
            "nt": float(tensor_tilt[pivot]),
            "hubbleGeV": float(hubble[pivot]) * physics.REDUCED_PLANCK_MASS_GEV,
            "energyGeV": pivot_potential**0.25 * physics.REDUCED_PLANCK_MASS_GEV,
            "squeezing": float(spec["r_end"][pivot]),
        },
    }


def background_payload(key: str, background: physics.Background | None = None) -> dict:
    """Trajectory against e-folds before the end, and V(phi) with marked exit times."""

    if background is None:
        background = physics.solve_background(physics.MODELS[key])
    before_end = np.concatenate([np.linspace(70, 2, 137), np.linspace(2, 0, 81)[1:]])
    s = background.state(background.n_end - before_end)
    pivot_potential = float(background.state(background.n_end - physics.PIVOT_EFOLDS)["potential"])
    marks = np.array([55.0, 25.0, 10.0, 5.0, 0.0])
    marked = background.state(background.n_end - marks)
    phi = np.linspace(0, float(s["phi"][0]) * 1.04, 241)
    potential = np.vectorize(background.model.potential)(phi)
    return {
        "key": key,
        "n": _significant(-before_end, 6),
        "eps1": _significant(s["eps1"]),
        "eps2": _significant(s["eps2"]),
        "epsV": _significant(s["eps_v"]),
        "eps2V": _significant(4 * s["eps_v"] - 2 * s["eta_v"]),
        "phi": _significant(phi),
        "potential": _significant(potential / pivot_potential),
        "marks": {
            "beforeEnd": marks.tolist(),
            "phi": _significant(marked["phi"]),
            "potential": _significant(marked["potential"] / pivot_potential),
        },
    }


def build(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    copy_mathjax_assets(output_dir)
    copy_visualization_theme_assets(output_dir)
    for source in (SOURCE / "static").iterdir():
        shutil.copy2(source, output_dir / source.name)
    supporting = output_dir / "supporting.html"
    supporting.write_text(
        supporting.read_text(encoding="utf-8").replace("__PLOTLY_ASSET__", PLOTLY_GL3D_ASSET_NAME),
        encoding="utf-8",
    )
    data = output_dir / "data"
    data.mkdir(exist_ok=True)
    backgrounds = {key: physics.solve_background(model) for key, model in physics.MODELS.items()}

    def write(name: str, payload: dict) -> None:
        (data / f"{name}.json").write_text(
            json.dumps(payload, separators=(",", ":")), encoding="utf-8"
        )

    teaser = None
    for key in config_keys():
        payload = config_payload(key, backgrounds[key.partition("-")[0]])
        write(f"config-{key}", payload)
        if key == "starobinsky-55":
            teaser = payload
    for key in physics.MODELS:
        write(f"spectrum-{key}", spectrum_payload(key, backgrounds[key]))
    for key in ENDING_MODELS:
        write(f"background-{key}", background_payload(key, backgrounds[key]))
    (output_dir / "teaser.svg").write_text(teaser_svg(teaser), encoding="utf-8")


def teaser_svg(payload: dict) -> str:
    """The three modes' Wigner contours at the pivot crossing, on identical fixed axes."""

    window = payload["window"]
    frame = int(np.argmin(np.abs(np.array(window["n"]))))
    titles = ("Earliest crossing", "Pivot crossing", "Latest crossing")
    colors = ("#397da9", "#d26541", "#569d88")
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="250" viewBox="0 0 720 250">',
        "<style>text{font:13px system-ui,sans-serif;fill:#28333d}</style>",
    ]
    angles = np.linspace(0, 2 * np.pi, 161)
    circle = np.array([np.cos(angles), np.sin(angles)]) / math.sqrt(2)
    for i, mode in enumerate(window["modes"]):
        cx, cy, scale = 135 + i * 230, 125, 20
        x = mode["x"][frame]
        parts.append(f'<text x="{cx}" y="20" text-anchor="middle">{titles[i]} · x = {x:.2g}</text>')
        parts.append(f'<clipPath id="c{i}"><rect x="{cx - 88}" y="37" width="176" height="176"/>')
        parts.append("</clipPath>")
        for tick in (-4, -2, 0, 2, 4):
            xp, yp = cx + scale * tick, cy - scale * tick
            parts.extend(
                [
                    f'<path d="M{xp},37V213 M{cx - 88},{yp}H{cx + 88}" '
                    'stroke="#ded6cc" fill="none"/>',
                    f'<text x="{xp}" y="231" text-anchor="middle">{tick}</text>',
                    f'<text x="{cx - 95}" y="{yp + 4}" text-anchor="end">{tick}</text>',
                ]
            )
        ring = np.array(mode["matrix"][frame]).reshape(2, 2) @ circle
        points = " ".join(f"{cx + scale * q:.2f},{cy - scale * p:.2f}" for q, p in ring.T)
        parts.append(
            f'<polygon clip-path="url(#c{i})" points="{points}" fill="{colors[i]}" '
            f'fill-opacity="0.16" stroke="{colors[i]}" stroke-width="1.8"/>'
        )
    parts.append('<text x="360" y="249" text-anchor="middle">Field quadrature Q</text>')
    parts.append(
        '<text transform="translate(13 125) rotate(-90)" text-anchor="middle">'
        "Momentum quadrature P</text></svg>"
    )
    return "".join(parts)
