# Interactive Physics Olio development

The project uses Python 3.12 and [uv](https://docs.astral.sh/uv/) for its development
environment. The essential commands are:

```bash
uv sync --frozen
uv run pytest
uv run ruff check .
uv run ruff format --check .
uv run python scripts/validate_metadata.py
uv run python scripts/build_site.py
uv run zensical serve
```

Published applications are supported over HTTP/HTTPS rather than direct `file://` opening. To
inspect the complete bilingual production build locally, build it and serve `site/` from a
loopback address:

```bash
uv run python scripts/build_site.py
uv run python -m http.server --bind 127.0.0.1 --directory site 8000
```

Then open the English site at `http://127.0.0.1:8000/` or the Japanese site at
`http://127.0.0.1:8000/ja/`. This same-origin HTTP environment is also the local development
contract for module workers and future WebAssembly assets.

The main repository areas are:

```text
workbench/       local exploration
visualizations/  publication-quality visualization source
docs/            public-facing explanations
site/            generated output; never edit or commit
```

Repository-specific development rules live in `AGENTS.md`.
Search metadata policy and Search Console setup are documented in
[`SEARCH_CONSOLE.md`](SEARCH_CONSOLE.md).
Reusable rules for bounded Pyodide/Wasm-style computation runtimes live in
[`visualizations/BROWSER_COMPUTE.md`](visualizations/BROWSER_COMPUTE.md).
