"""Build a static SVG animation from one shared, precomputed physics payload.

SVG keeps dense quiver arrows and three equal-aspect panels legible during playback
without a plotting runtime. Only drawing and playback run in the browser.
"""

import json
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
LIMIT = 4.4


def _rounded(values: np.ndarray) -> list:
    return np.round(values, 7).tolist()


def _directions(vectors: np.ndarray | None) -> list:
    if vectors is None:
        return []
    unit = vectors / np.linalg.norm(vectors, axis=0)
    return _rounded((unit * LIMIT * 1.5).T)


def application_payload() -> dict:
    """Precompute every plotted physical quantity; the UI does no evolution."""
    times = np.unique(np.append(np.linspace(-np.log(12), -np.log(0.2), 181), 0.0))
    grid = np.linspace(-3.6, 3.6, 7)
    points = np.array(np.meshgrid(grid, grid)).reshape(2, -1)
    frames = []
    for n in times:
        x = float(np.exp(-n))
        r, angle = physics.squeeze_parameters(x)
        frames.append(
            {
                "n": float(n),
                "x": x,
                "r": r,
                "angle": float(np.degrees(angle)),
                "fields": [
                    _rounded((field / np.sqrt(1 + x * x)).T)
                    for field in physics.hamiltonian_fields(x, points)
                ],
                "ring": _rounded(physics.wigner_contour(x, np.linspace(0, 2 * np.pi, 161)).T),
                "markers": _rounded(
                    physics.wigner_contour(x, np.linspace(0, 2 * np.pi, 12, endpoint=False)).T
                ),
                "principal": _directions(physics.principal_directions(x)),
                "flow": _directions(physics.instantaneous_directions(x)),
                "solutions": _directions(physics.solution_basis(x)[:, ::-1]),
            }
        )
    return {
        "limit": LIMIT,
        "points": _rounded(points.T),
        "frames": frames,
    }


def build(output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "teaser.svg").write_text(teaser_svg(), encoding="utf-8")
    copy_mathjax_assets(output_dir)
    copy_visualization_theme_assets(output_dir)
    for source in (SOURCE / "static").iterdir():
        shutil.copy2(source, output_dir / source.name)
    supporting = output_dir / "supporting.html"
    supporting.write_text(
        supporting.read_text(encoding="utf-8").replace("__PLOTLY_ASSET__", PLOTLY_GL3D_ASSET_NAME),
        encoding="utf-8",
    )
    (output_dir / "supporting.json").write_text(
        json.dumps(supporting_payload(), separators=(",", ":")), encoding="utf-8"
    )
    (output_dir / "data.json").write_text(
        json.dumps(application_payload(), separators=(",", ":")), encoding="utf-8"
    )


def supporting_payload() -> dict:
    """Shared figures for the background, basis, squeezing, stochastic, and acoustic views."""
    times = np.linspace(-np.log(12), 4, 321)
    history = physics.mode_history(times)
    evolution = {
        "n": _rounded(times),
        "equalTerms": physics.FREQUENCY_BALANCE_N,
        "r": _rounded(history["r"]),
        "angle": _rounded(np.degrees(history["angle"])),
        "background": _rounded(history["background"]),
        "reference": _rounded(np.ones_like(times)),
        "asymptote": _rounded(np.maximum(times, 0)),
        # Keep small decaying amplitudes resolved on the logarithmic late-time plot.
        "decayingAsymptote": history["field_decaying_asymptote"].tolist(),
    }
    for name in ("rescaled", "field"):
        mode = history[name]
        evolution[name] = [component.tolist() for component in (mode.real, mode.imag, np.abs(mode))]
    basis = []
    for x in (12.0, 1.0, 0.2):
        traveling, standing = physics.pair_covariances(x)
        basis.append({"x": x, "traveling": _rounded(traveling), "standing": _rounded(standing)})
    seeds = np.random.default_rng(718).normal(size=(2, 256))
    sample_frames = []
    for n in np.linspace(-np.log(12), -np.log(0.2), 61):
        x = float(np.exp(-n))
        sample_frames.append(
            {
                "n": float(n),
                "x": x,
                "points": _rounded(physics.gaussian_samples(x, seeds)),
                "ring": _rounded(physics.wigner_contour(x, np.linspace(0, 2 * np.pi, 161))),
                "relation": _rounded(physics.conditional_momentum(x, np.array([-12, 12]))),
            }
        )
    phase = np.linspace(0, 4 * np.pi, 241)
    amplitudes = np.random.default_rng(237).normal(size=(2, 4096))
    exact = physics.acoustic_power(phase)
    acoustic = {"u": _rounded(phase / np.pi)}
    for i, coherent in enumerate((True, False)):
        values = physics.acoustic_realizations(phase, amplitudes, coherent)
        acoustic["coherent" if coherent else "incoherent"] = {
            "curves": _rounded(values[:8]),
            "power": _rounded(np.mean(values**2, axis=0)),
            "exact": _rounded(exact[i]),
        }
    return {"evolution": evolution, "basis": basis, "samples": sample_frames, "acoustic": acoustic}


def teaser_svg() -> str:
    """Three actual Wigner contours with equal, fixed Q/P scales (article preview)."""
    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="720" height="250" viewBox="0 0 720 250">',
        "<style>text{font:13px system-ui,sans-serif;fill:#28333d}</style>",
    ]
    for i, (x, title) in enumerate(zip((12, 1, 0.2), ("Early", "Crossing", "Late"), strict=True)):
        cx, cy, scale = 135 + i * 230, 125, 20
        parts.append(f'<text x="{cx}" y="20" text-anchor="middle">{title}</text>')
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
        ring = physics.wigner_contour(x, np.linspace(0, 2 * np.pi, 161)).T
        points = " ".join(f"{cx + scale * q:.2f},{cy - scale * p:.2f}" for q, p in ring)
        parts.append(
            f'<polygon points="{points}" fill="#397da9" fill-opacity="0.14" '
            'stroke="#28333d" stroke-width="1.7"/>'
        )
    parts.append('<text x="360" y="249" text-anchor="middle">Field quadrature</text>')
    parts.append(
        '<text transform="translate(13 125) rotate(-90)" text-anchor="middle">'
        "Momentum quadrature</text></svg>"
    )
    return "".join(parts)
