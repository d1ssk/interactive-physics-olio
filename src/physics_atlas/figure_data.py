"""Lossless, content-addressed figure chunks for static browser applications."""

from __future__ import annotations

import hashlib
import json
import os
import shutil
from collections import Counter
from pathlib import Path

from .assets import STATIC_DIR


def _json(value: object) -> str:
    return json.dumps(value, ensure_ascii=True, allow_nan=False, separators=(",", ":"))


def pack_figure_data(value: object) -> dict:
    """Intern repeated JSON containers without rounding or changing array order.

    Children precede their parents in the pool. Containers used only once are
    inlined, so unique coordinate arrays do not pay a reference-table penalty.
    Input must already have passed through Plotly's JSON encoder (NaN -> null).
    """
    nodes: list[object] = []
    identifiers: dict[str, int] = {}

    def intern(item):
        if isinstance(item, dict):
            if "$ref" in item:
                raise ValueError("Reserved figure-data key: $ref")
            encoded = {key: intern(child) for key, child in item.items()}
        elif isinstance(item, list):
            encoded = [intern(child) for child in item]
        else:
            return item
        key = _json(encoded)
        if len(key) < 80:
            return encoded
        if key not in identifiers:
            identifiers[key] = len(nodes)
            nodes.append(encoded)
        return {"$ref": identifiers[key]}

    root = intern(value)
    uses: Counter = Counter()

    def count(item):
        if isinstance(item, dict):
            if "$ref" in item:
                uses[item["$ref"]] += 1
            else:
                for child in item.values():
                    count(child)
        elif isinstance(item, list):
            for child in item:
                count(child)

    for item in [root, *nodes]:
        count(item)
    shared = [index for index in range(len(nodes)) if uses[index] > 1]
    remap = {index: new for new, index in enumerate(shared)}

    def inline(item):
        if isinstance(item, dict):
            if "$ref" in item:
                index = item["$ref"]
                return {"$ref": remap[index]} if index in remap else inline(nodes[index])
            return {key: inline(child) for key, child in item.items()}
        if isinstance(item, list):
            return [inline(child) for child in item]
        return item

    return {"format": 1, "pool": [inline(nodes[i]) for i in shared], "root": inline(root)}


def write_figure_chunks(output_dir: Path, metadata: dict, chunks: dict) -> str:
    """Stage independently cacheable families and return a small inline manifest."""
    directory = output_dir / "figure-data"
    directory.mkdir(parents=True, exist_ok=True)
    paths = {}
    for name, value in chunks.items():
        payload = _json(pack_figure_data(value)).encode()
        digest = hashlib.sha256(payload).hexdigest()[:16]
        filename = f"{name}.{digest}.json"
        (directory / filename).write_bytes(payload)
        paths[name] = filename
    loader = (STATIC_DIR / "figure-data.js").read_bytes()
    loader_name = f"figure-data-{hashlib.sha256(loader).hexdigest()[:16]}.js"
    (output_dir / loader_name).write_bytes(loader)
    manifest = _json({**metadata, "chunks": paths, "loader": loader_name})
    return manifest.replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")


def publish_shared_figure_data(site: Path) -> None:
    """Make Japanese pages reuse the byte-identical English figure chunks."""
    for directory in (site / "ja").rglob("figure-data"):
        relative = directory.relative_to(site / "ja")
        shared = site / relative
        local_files = {p.name: p.read_bytes() for p in directory.iterdir()}
        shared_files = {p.name: p.read_bytes() for p in shared.iterdir()}
        if local_files != shared_files:
            raise ValueError(f"Figure data differs between languages: {relative}")
        page = directory.parent / "index.html"
        html = page.read_text(encoding="utf-8")
        marker = 'id="figure-data-manifest" data-base="figure-data/"'
        if html.count(marker) != 1:
            raise ValueError(f"Missing unique figure manifest: {page}")
        base = Path(os.path.relpath(shared, directory.parent)).as_posix() + "/"
        page.write_text(
            html.replace(marker, f'id="figure-data-manifest" data-base="{base}"'), encoding="utf-8"
        )
        shutil.rmtree(directory)
