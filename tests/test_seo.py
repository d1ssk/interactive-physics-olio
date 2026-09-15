"""Check publication coverage, language correspondence, and untouched scientific payloads."""

import xml.etree.ElementTree as ET
from dataclasses import replace
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath

import pytest

from physics_atlas.metadata import discover_visualizations, load_metadata
from physics_atlas.seo import (
    PublicPage,
    collect_public_pages,
    enrich_html,
    publish_search_metadata,
)

ROOT = Path(__file__).resolve().parents[1]
BASE_URLS = {
    "en": "https://example.org/olio/",
    "ja": "https://example.org/olio/ja/",
}
HTML = """<!doctype html><html lang="en"><head>
<meta charset="utf-8"><meta name="description" content="Generic">
<meta name="robots" content="noindex"><link rel="canonical" href="https://wrong.example/">
<link rel="alternate" hreflang="ja" href="https://wrong.example/ja/">
<title>Original title</title><script>const data = {x: [1, 2], equation: "a < b"};</script>
</head><body><main><a id="brand-home" class="brand" href="../../">Interactive Physics Olio</a>
<a id="locale-link" href="./?lang=ja" lang="ja">日本語</a><h1>Original heading</h1>
<p>\\(f^*(p)=\\sup_x\\{px-f(x)\\}\\)</p></main></body></html>"""


class MetadataParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_head = False
        self.metas = []
        self.links = []
        self.language = None
        self.anchors = {}

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if tag == "head":
            self.in_head = True
        elif tag == "html":
            self.language = attributes.get("lang")
        elif tag == "meta" and self.in_head:
            self.metas.append(attributes)
        elif tag == "link" and self.in_head:
            self.links.append(attributes)
        elif tag == "a":
            self.anchors[attributes.get("id")] = attributes

    def handle_endtag(self, tag):
        if tag == "head":
            self.in_head = False


def parse(html):
    parser = MetadataParser()
    parser.feed(html)
    return parser


def test_inventory_covers_every_article_and_standalone_in_both_languages():
    items = [load_metadata(path) for path in discover_visualizations(ROOT / "visualizations")]
    pages = collect_public_pages(ROOT, items)
    for locale in BASE_URLS:
        paths = {page.path for page in pages if page.locale == locale}
        assert {item.page for item in items} <= paths
        assert PurePosixPath("updates") in paths
        assert PurePosixPath(".") in paths
        assert all("app" not in path.parts for path in paths)
        assert all("assets" not in path.parts for path in paths)
    assert {page.path for page in pages if page.locale == "en"} == {
        page.path for page in pages if page.locale == "ja"
    }


@pytest.mark.parametrize("locale", BASE_URLS)
def test_initial_head_has_one_canonical_and_reciprocal_locales(locale):
    page = PublicPage(PurePosixPath("topic/explorer"), locale, 'Title & "value"', 'A < B & "C"')
    output = enrich_html(HTML, page, BASE_URLS)
    parsed = parse(output)
    assert parsed.language == locale
    assert [link["href"] for link in parsed.links if link["rel"] == "canonical"] == [
        BASE_URLS[locale] + "topic/explorer/"
    ]
    assert {
        link["hreflang"]: link["href"] for link in parsed.links if link["rel"] == "alternate"
    } == {language: base + "topic/explorer/" for language, base in BASE_URLS.items()}
    assert [meta["content"] for meta in parsed.metas if meta.get("name") == "description"] == [
        page.description
    ]
    assert not any(meta.get("name") == "robots" for meta in parsed.metas)
    assert "Title &amp; &quot;value&quot; — Interactive Physics Olio" in output


def test_standalone_heading_and_navigation_exist_before_javascript():
    page = PublicPage(PurePosixPath("topic/explorer"), "ja", "探索アプリ", "概要", standalone=True)
    output = enrich_html(HTML, page, BASE_URLS)
    parsed = parse(output)
    assert "<h1>探索アプリ</h1>" in output
    assert parsed.anchors["brand-home"]["href"] == BASE_URLS["ja"]
    assert parsed.anchors["locale-link"]["href"] == BASE_URLS["en"] + "topic/explorer/"
    assert parsed.anchors["locale-link"]["hreflang"] == "en"
    assert ">English</a>" in output


def test_scientific_payload_and_article_body_are_preserved():
    page = PublicPage(PurePosixPath("topic/article"), "ja", "記事", "概要")
    output = enrich_html(HTML, page, BASE_URLS)
    assert output.split("<body>", 1)[1] == HTML.split("<body>", 1)[1]
    assert '<script>const data = {x: [1, 2], equation: "a < b"};</script>' in output
    assert enrich_html(output, page, BASE_URLS) == output


def test_embedded_pages_are_noindex_without_blocking_link_discovery():
    output = enrich_html(HTML, None, BASE_URLS)
    parsed = parse(output)
    assert [meta["content"] for meta in parsed.metas if meta.get("name") == "robots"] == ["noindex"]
    assert not parsed.links
    assert output.split("<body>", 1)[1] == HTML.split("<body>", 1)[1]


def test_verification_is_only_emitted_on_property_homepage():
    home = PublicPage(PurePosixPath("."), "en", "Interactive Physics Olio", "Overview")
    for page, expected in (
        (home, True),
        (replace(home, locale="ja"), False),
        (replace(home, path=PurePosixPath("updates")), False),
    ):
        parsed = parse(enrich_html(HTML, page, BASE_URLS, verification='token & "value"'))
        tokens = [
            meta["content"]
            for meta in parsed.metas
            if meta.get("name") == "google-site-verification"
        ]
        assert tokens == (['token & "value"'] if expected else [])
    assert "<title>Interactive Physics Olio</title>" in enrich_html(HTML, home, BASE_URLS)
    assert "google-site-verification" not in enrich_html(HTML, home, BASE_URLS)


def test_build_publishes_complete_sitemap_and_excludes_embeds(tmp_path):
    source = ROOT / "visualizations" / "complex-functions" / "metadata.yml"
    standalone = tmp_path / "visualizations" / "complex-functions"
    standalone.mkdir(parents=True)
    standalone.joinpath("metadata.yml").write_text(
        source.read_text(encoding="utf-8"), encoding="utf-8"
    )
    article = tmp_path / "visualizations" / "lorentz-transformation"
    article.mkdir()
    article.joinpath("metadata.yml").write_text(
        (ROOT / "visualizations" / "lorentz-transformation" / "metadata.yml").read_text(
            encoding="utf-8"
        ),
        encoding="utf-8",
    )
    items = [load_metadata(standalone), load_metadata(article)]
    for locale, docs_name in (("en", "docs"), ("ja", "docs_ja")):
        docs = tmp_path / docs_name
        docs.mkdir()
        (docs / "index.md").write_text("# Interactive Physics Olio\n", encoding="utf-8")
        prose = docs / "relativity" / "lorentz-transformation" / "index.md"
        prose.parent.mkdir(parents=True)
        prose.write_text("# Lorentz transformation\n", encoding="utf-8")
        site = tmp_path / "site"
        if locale == "ja":
            site /= "ja"
        for relative in (
            "index.html",
            "404.html",
            "sitemap.xml",
            "sitemap.xml.gz",
            "relativity/lorentz-transformation/index.html",
            "relativity/lorentz-transformation/app/index.html",
            "mathematics-for-physics/complex-functions/index.html",
        ):
            target = site / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(HTML, encoding="utf-8")
        name = "zensical.toml" if locale == "en" else "zensical.ja.toml"
        (tmp_path / name).write_text(
            f'[project]\nsite_url = "{BASE_URLS[locale]}"\n', encoding="utf-8"
        )
    publish_search_metadata(tmp_path, [standalone, article])
    locations = [
        element.text
        for element in ET.parse(tmp_path / "site/sitemap.xml").iter()
        if element.tag.endswith("loc")
    ]
    expected = [
        BASE_URLS[page.locale] + page.relative_url for page in collect_public_pages(tmp_path, items)
    ]
    assert locations == expected
    assert len(locations) == len(set(locations)) == 6
    assert not (tmp_path / "site/ja/sitemap.xml").exists()
    assert not list((tmp_path / "site").rglob("sitemap.xml.gz"))
    for locale in BASE_URLS:
        site = tmp_path / "site" / "ja" if locale == "ja" else tmp_path / "site"
        for relative in ("404.html", "relativity/lorentz-transformation/app/index.html"):
            assert any(
                meta.get("content") == "noindex"
                for meta in parse((site / relative).read_text(encoding="utf-8")).metas
            )


def test_missing_translation_stops_publication(tmp_path):
    (tmp_path / "docs/topic").mkdir(parents=True)
    (tmp_path / "docs/topic/index.md").write_text("# Topic\n", encoding="utf-8")
    (tmp_path / "docs_ja").mkdir()
    with pytest.raises(ValueError, match="matching English and Japanese"):
        collect_public_pages(tmp_path, [])


def test_new_prose_page_uses_authored_description(tmp_path):
    for name in ("docs", "docs_ja"):
        (tmp_path / name).mkdir()
        (tmp_path / name / "new.md").write_text(
            '---\ndescription: "Authored explanation"\n---\n# New page\n', encoding="utf-8"
        )
    pages = collect_public_pages(tmp_path, [])
    assert len(pages) == 2
    assert all(page.relative_url == "new/" for page in pages)
    assert all(page.description == "Authored explanation" for page in pages)
