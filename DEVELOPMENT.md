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

Home-page card PNGs in `docs/assets/images/` are retained as editing sources. The production
build converts the 13 images referenced by `FIELDS` to WebP at a maximum width of 600px and
quality 85, then excludes those PNGs from publication. Both languages use the English-root
thumbnail URLs. The first two cards load eagerly; subsequent cards use native lazy loading.

The shared OG/Twitter image is `docs/assets/images/social-card.png`. Its authored layout is
`scripts/assets/social-card.html`, using the existing condensed-matter figure and the site's
self-hosted font. To re-export it, serve the repository root over loopback HTTP, start a separate
Chrome instance with a temporary profile and remote debugging enabled, then run:

```bash
node scripts/render_social_card.mjs http://127.0.0.1:8000 http://127.0.0.1:9222
```

The export script requires Node 22 or later. Inspect the 1200 × 630 output before committing it.
Social titles, descriptions, locales, and image alternative text are generated in
`src/physics_atlas/seo.py` for every public page; embedded applications remain nonindexable.

Search metadata policy and Search Console setup are documented in
[`SEARCH_CONSOLE.md`](SEARCH_CONSOLE.md). Use the host-wide `https://d1ssk.github.io/`
URL-prefix property and submit `https://d1ssk.github.io/sitemap-index.xml` once; this
project continues generating its own child `sitemap.xml`. Keep existing project ownership
verification resources published.
Reusable rules for bounded Pyodide/Wasm-style computation runtimes live in
[`visualizations/BROWSER_COMPUTE.md`](visualizations/BROWSER_COMPUTE.md).
