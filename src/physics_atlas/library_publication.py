"""Link independently built apps to one versioned copy of each browser library.

This is a production-build step, after both locales have been emitted. Only library
URLs are changed; HTML bodies, figure payloads, kernels, and runtime protocols stay intact.
"""

from __future__ import annotations

import hashlib
import os
import re
import shutil
from html import escape
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from .assets import (
    MATHJAX_ASSET_NAME,
    MATHJAX_LICENSE_PATH,
    MATHJAX_SVG_PATH,
    PLOTLY_GL3D_ASSET_NAME,
    PLOTLY_GL3D_PATH,
    PLOTLY_LICENSE_ASSET_NAME,
    PLOTLY_LICENSE_PATH,
    PYODIDE_RUNTIME_SHA256,
    PYODIDE_VENDOR_DIR,
    PYODIDE_VERSION,
    copy_pyodide_runtime_assets,
)

_PYODIDE_ID = hashlib.sha256(
    "\n".join(
        f"{name}:{digest}" for name, digest in sorted(PYODIDE_RUNTIME_SHA256.items())
    ).encode()
).hexdigest()[:12]
PYODIDE_SHARED_PATH = Path("assets/vendor") / f"pyodide-{PYODIDE_VERSION}-{_PYODIDE_ID}"


def _relative_url(target: Path, source: Path) -> str:
    return Path(os.path.relpath(target, source.parent)).as_posix()


class _LibraryScripts(HTMLParser):
    """Replace script src spans without reserializing equations or inline JavaScript."""

    def __init__(self, html: str, source: Path, aliases: dict[Path, Path]):
        super().__init__(convert_charrefs=False)
        self.html = html
        self.source = source
        self.aliases = aliases
        self.lines = [0, *(match.end() for match in re.finditer("\n", html))]
        self.edits: list[tuple[int, int, str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "script":
            return
        src = dict(attrs).get("src")
        if not src:
            return
        url = urlsplit(src)
        if url.scheme or url.netloc:
            return
        original = (self.source.parent / unquote(url.path)).resolve()
        target = self.aliases.get(original)
        if target is None:
            return
        raw = self.get_starttag_text()
        replacement = re.sub(
            r"(?<![\w-])src\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+)",
            lambda _: f'src="{escape(_relative_url(target, self.source), quote=True)}"',
            raw,
            count=1,
            flags=re.I,
        )
        line, column = self.getpos()
        start = self.lines[line - 1] + column
        self.edits.append((start, start + len(raw), replacement))

    def render(self) -> str:
        self.feed(self.html)
        output = self.html
        for start, end, replacement in reversed(self.edits):
            output = output[:start] + replacement + output[end:]
        return output


def _identical(path: Path, expected: bytes) -> None:
    if path.read_bytes() != expected:
        raise ValueError(f"Refusing to consolidate a different library build: {path}")


def publish_shared_libraries(site: Path) -> None:
    """Consolidate verified library copies and link both locales to the common URLs."""

    site = site.resolve()
    javascript = site / "javascripts"
    javascript.mkdir(parents=True, exist_ok=True)
    aliases: dict[Path, Path] = {}
    obsolete: set[Path] = set()
    for old_name, source, target_name in (
        ("mathjax-tex-svg.js", MATHJAX_SVG_PATH, MATHJAX_ASSET_NAME),
        ("mathjax-LICENSE.txt", MATHJAX_LICENSE_PATH, f"{MATHJAX_ASSET_NAME}.LICENSE.txt"),
        (PLOTLY_GL3D_ASSET_NAME, PLOTLY_GL3D_PATH, PLOTLY_GL3D_ASSET_NAME),
        (PLOTLY_LICENSE_ASSET_NAME, PLOTLY_LICENSE_PATH, PLOTLY_LICENSE_ASSET_NAME),
    ):
        expected = source.read_bytes()
        copies = list(site.rglob(old_name))
        for path in copies:
            _identical(path, expected)
        target = javascript / target_name
        shutil.copy2(source, target)
        for path in copies:
            aliases[path] = target
            if path != target:
                obsolete.add(path)

    # Visit all HTML, including supporting panels and standalone applications.
    for path in site.rglob("*.html"):
        html = path.read_text(encoding="utf-8")
        updated = _LibraryScripts(html, path, aliases).render()
        if updated != html:
            path.write_text(updated, encoding="utf-8")

    shared_runtime = site / PYODIDE_SHARED_PATH
    local_runtimes = [
        path.parent for path in site.rglob("pyodide.mjs") if path.parent != shared_runtime
    ]
    expected_runtime = {
        name: (PYODIDE_VENDOR_DIR / name).read_bytes()
        for name in (*PYODIDE_RUNTIME_SHA256, "LICENSE", "NUMPY-LICENSE.txt")
    }
    for directory in local_runtimes:
        if {path.name for path in directory.iterdir()} != set(expected_runtime):
            raise ValueError(f"Unexpected files in runtime library directory: {directory}")
        for name, contents in expected_runtime.items():
            _identical(directory / name, contents)
        workers = []
        for path in directory.parent.glob("*.mjs"):
            source = path.read_text(encoding="utf-8")
            if '"./pyodide/pyodide.mjs"' not in source:
                continue
            if '"./pyodide/"' not in source:
                raise ValueError(f"Worker must set the shared runtime indexURL: {path}")
            base = _relative_url(shared_runtime, path) + "/"
            updated = source.replace('"./pyodide/pyodide.mjs"', f'"{base}pyodide.mjs"')
            updated = updated.replace('"./pyodide/"', f'"{base}"')
            workers.append((path, updated))
        if not workers:
            raise ValueError(f"No Worker references this runtime library: {directory}")
        for path, updated in workers:
            path.write_text(updated, encoding="utf-8")
    if local_runtimes:
        copy_pyodide_runtime_assets(shared_runtime)
    for directory in local_runtimes:
        shutil.rmtree(directory)
    for path in obsolete:
        path.unlink()
