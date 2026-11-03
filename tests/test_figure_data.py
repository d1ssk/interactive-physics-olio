"""Check exact scientific data preservation and bilingual publication."""

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from build_visualizations import _discard_modules, _load_build_function
from plotly.utils import PlotlyJSONEncoder

from physics_atlas.figure_data import pack_figure_data, publish_shared_figure_data

ROOT = Path(__file__).resolve().parents[1]
LOADER = ROOT / "src/physics_atlas/static/figure-data.js"


def test_packing_preserves_distinct_values_and_shares_repeated_containers():
    coordinates = [1.2345678901234567, -0.0, None, 1e-200, 1e200] * 30
    original = {"first": coordinates, "second": coordinates, "third": coordinates + [2]}
    packed = pack_figure_data(original)
    assert packed["pool"]
    assert len(json.dumps(packed)) < len(json.dumps(original))
    assert pack_figure_data(original) == packed
    with pytest.raises(ValueError, match="Reserved"):
        pack_figure_data({"$ref": 0})


@pytest.mark.parametrize("slug", ["conformal-transformations-2d", "ads2-ds2-spacetime-geometry"])
def test_every_published_state_round_trips_through_browser_decoder(tmp_path, monkeypatch, slug):
    build, package = _load_build_function(ROOT / "visualizations" / slug)
    try:
        visualization = sys.modules[f"{package}.visualization"]
        original = json.loads(
            json.dumps(visualization._build_application_data(), cls=PlotlyJSONEncoder)
        )
        metadata, expected = visualization._partition_application_data(original)
        monkeypatch.setattr(visualization, "_build_application_data", lambda: original)
        build(tmp_path)
        html = (tmp_path / "index.html").read_text()
        assert len(html.encode()) < 100_000
        manifest = json.loads(html.split('type="application/json">', 1)[1].split("</script>", 1)[0])
        assert {key: manifest[key] for key in metadata} == metadata
        files = [
            str(tmp_path / "figure-data" / filename) for filename in manifest["chunks"].values()
        ]
        subprocess.run(
            [
                "node",
                "-e",
                """
const fs = require('node:fs');
require(process.argv[1]);
for (const file of process.argv.slice(2)) {
  const restored = PhysicsFigureData.unpack(JSON.parse(fs.readFileSync(file, 'utf8')));
  fs.writeFileSync(file + '.decoded', JSON.stringify(restored));
}
""",
                str(LOADER),
                *files,
            ],
            check=True,
            capture_output=True,
            text=True,
        )
        actual = {
            key: json.loads((tmp_path / "figure-data" / f"{filename}.decoded").read_text())
            for key, filename in manifest["chunks"].items()
        }
        assert actual == expected
        if slug.startswith("conformal"):
            for name, item in original["local"].items():
                assert item == (
                    actual["local-mixed"]["variants"]["0.40"]
                    if name == "mixed"
                    else actual[f"local-{name}"]
                )
            assert actual["mobius-base"] == original["mobiusBase"]
            for name, family in original["mobius"].items():
                assert {**metadata["mobius"][name], "variants": actual[f"mobius-{name}"]} == family
            assert {mode: actual[f"witt-{mode}"] for mode in original["witt"]} == original["witt"]
            assert actual["local-mixed"]["variants"] == original["localVariants"]
            initial = ["local-square", "mobius-base", "mobius-identity", "witt-1"]
        else:
            for kind, charts in original["chartOptions"].items():
                space = actual[f"space-{kind}"]
                assert space == {
                    "surface": original["surfaces"][kind],
                    "layout": original["layouts"][kind],
                    "penrose": original["penrose"][kind],
                }
                for chart in charts:
                    key = f"{kind}|{chart}"
                    chunk = actual[f"chart-{kind}-{chart}"]
                    assert chunk["traces"] == original["charts"][key]
                    assert chunk["controls"] == original["coordinateControls"][key]
                    for boost in original["boostKeys"]:
                        assert chunk["geodesics"][boost] == original["geodesics"][f"{key}|{boost}"]
            initial = ["space-ads", "chart-ads-global"]
        raw = len(json.dumps(original, separators=(",", ":")).encode())
        total = sum(Path(file).stat().st_size for file in files)
        initial_bytes = sum(
            (tmp_path / "figure-data" / manifest["chunks"][key]).stat().st_size for key in initial
        )
        assert total < raw * 0.9
        assert initial_bytes < 2_000_000
    finally:
        _discard_modules(package)


def test_locales_share_figure_urls_and_differing_data_is_rejected(tmp_path):
    en = tmp_path / "topic/article/app"
    ja = tmp_path / "ja/topic/article/app"
    (en / "figure-data").mkdir(parents=True)
    (en / "figure-data/part.abc.json").write_text('{"value":1}')
    (en / "index.html").write_text(
        '<script id="figure-data-manifest" data-base="figure-data/" '
        'type="application/json">{}</script>'
    )
    shutil.copytree(en, ja)
    (ja / "figure-data/part.abc.json").write_text('{"value":2}')
    with pytest.raises(ValueError, match="differs"):
        publish_shared_figure_data(tmp_path)
    assert (ja / "figure-data").exists()
    (ja / "figure-data/part.abc.json").write_text('{"value":1}')
    publish_shared_figure_data(tmp_path)
    assert not (ja / "figure-data").exists()
    assert (
        'data-base="../../../../topic/article/app/figure-data/"' in (ja / "index.html").read_text()
    )
    publish_shared_figure_data(tmp_path)


def test_browser_chunk_cache_retry_and_selection_races():
    subprocess.run(
        ["node", "--test", str(ROOT / "tests/test_figure_data.mjs")],
        check=True,
        capture_output=True,
        text=True,
    )
