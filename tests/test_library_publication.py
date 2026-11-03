"""Verify common URLs, exact library contents, and untouched application data."""

import pytest

from physics_atlas.assets import (
    MATHJAX_ASSET_NAME,
    MATHJAX_SVG_PATH,
    PLOTLY_GL3D_ASSET_NAME,
    PLOTLY_GL3D_PATH,
    PYODIDE_NUMPY_WHEEL,
    PYODIDE_VENDOR_DIR,
    copy_mathjax_assets,
    copy_plotly_assets,
    copy_pyodide_runtime_assets,
)
from physics_atlas.library_publication import (
    PYODIDE_SHARED_PATH,
    _LibraryScripts,
    publish_shared_libraries,
)


def test_publication_shares_libraries_across_locales_panels_and_workers(tmp_path):
    payload = '<script>const DATA = {equation:"a < b", coordinates:[1,2,3]};</script>'
    pages = [
        tmp_path / "index.html",
        tmp_path / "topic/article/app/index.html",
        tmp_path / "ja/topic/article/app/supporting.html",
        tmp_path / "ja/topic/standalone/index.html",
    ]
    for page in pages:
        page.parent.mkdir(parents=True, exist_ok=True)
        copy_mathjax_assets(page.parent)
        copy_plotly_assets(page.parent)
        page.write_text(
            '<head><script defer src="mathjax-tex-svg.js"></script>'
            f'<script src="{PLOTLY_GL3D_ASSET_NAME}"></script></head>'
            + payload
            + "<body><p>Scientific content</p></body>",
            encoding="utf-8",
        )
    workers = []
    for root in (tmp_path / "topic/article/app", tmp_path / "ja/topic/other/app"):
        runtime = root / "runtime"
        copy_pyodide_runtime_assets(runtime / "pyodide")
        (runtime / "kernel.whl").write_bytes(b"unchanged kernel")
        worker = runtime / "compute-worker.mjs"
        worker.write_text(
            'import {loadPyodide} from "./pyodide/pyodide.mjs";\n'
            'const indexURL = new URL("./pyodide/", import.meta.url).href;\n'
            "loadPyodide({indexURL});\n",
            encoding="utf-8",
        )
        workers.append(worker)

    publish_shared_libraries(tmp_path)

    assert not list(tmp_path.rglob("mathjax-tex-svg.js"))
    assert len(list(tmp_path.rglob(MATHJAX_ASSET_NAME))) == 1
    assert len(list(tmp_path.rglob(PLOTLY_GL3D_ASSET_NAME))) == 1
    assert len(list(tmp_path.rglob("pyodide.asm.wasm"))) == 1
    assert len(list(tmp_path.rglob(PYODIDE_NUMPY_WHEEL))) == 1
    assert (tmp_path / "javascripts" / MATHJAX_ASSET_NAME).read_bytes() == (
        MATHJAX_SVG_PATH.read_bytes()
    )
    assert (tmp_path / "javascripts" / PLOTLY_GL3D_ASSET_NAME).read_bytes() == (
        PLOTLY_GL3D_PATH.read_bytes()
    )
    for name in ("pyodide.mjs", "pyodide.asm.wasm", PYODIDE_NUMPY_WHEEL, "LICENSE"):
        assert (tmp_path / PYODIDE_SHARED_PATH / name).read_bytes() == (
            PYODIDE_VENDOR_DIR / name
        ).read_bytes()
    for page in pages:
        html = page.read_text(encoding="utf-8")
        assert payload in html
        assert html.endswith("<body><p>Scientific content</p></body>")
        for name in (MATHJAX_ASSET_NAME, PLOTLY_GL3D_ASSET_NAME):
            relative = html.split('src="', 1)[1].split('"', 1)[0]
            if name == PLOTLY_GL3D_ASSET_NAME:
                relative = html.split('src="', 2)[2].split('"', 1)[0]
            assert (page.parent / relative).resolve() == tmp_path / "javascripts" / name
    for worker in workers:
        source = worker.read_text(encoding="utf-8")
        module = source.split('from "', 1)[1].split('"', 1)[0]
        base = source.split('new URL("', 1)[1].split('"', 1)[0]
        assert (worker.parent / module).resolve() == (
            tmp_path / PYODIDE_SHARED_PATH / "pyodide.mjs"
        )
        assert (worker.parent / base).resolve() == tmp_path / PYODIDE_SHARED_PATH
        assert (worker.parent / "kernel.whl").read_bytes() == b"unchanged kernel"
        assert not (worker.parent / "pyodide").exists()

    before = {p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    publish_shared_libraries(tmp_path)
    after = {p.relative_to(tmp_path): p.read_bytes() for p in tmp_path.rglob("*") if p.is_file()}
    assert before == after


def test_only_script_src_is_relinked(tmp_path):
    source = tmp_path / "index.html"
    old = tmp_path / "mathjax-tex-svg.js"
    new = tmp_path / "javascripts" / MATHJAX_ASSET_NAME
    literal = "<script>const text = '<script src=\"mathjax-tex-svg.js\">';</script>"
    remote = '<script src="https://example.org/mathjax-tex-svg.js"></script>'
    html = (
        "<head>\n<script data-src='leave-this' defer SRC='./mathjax-tex-svg.js'></script>"
        + literal
        + remote
        + "</head>"
    )
    output = _LibraryScripts(html, source, {old: new}).render()
    assert literal in output
    assert remote in output
    assert f"data-src='leave-this' defer src=\"javascripts/{MATHJAX_ASSET_NAME}\"" in output


def test_different_library_build_is_rejected_without_deleting_it(tmp_path):
    library = tmp_path / "mathjax-tex-svg.js"
    library.write_text("a different version", encoding="utf-8")
    with pytest.raises(ValueError, match="different library build"):
        publish_shared_libraries(tmp_path)
    assert library.read_text(encoding="utf-8") == "a different version"


def test_unrecognized_worker_does_not_lose_its_runtime(tmp_path):
    runtime = tmp_path / "app/runtime/pyodide"
    copy_pyodide_runtime_assets(runtime)
    with pytest.raises(ValueError, match="No Worker references"):
        publish_shared_libraries(tmp_path)
    assert (runtime / "pyodide.mjs").is_file()
