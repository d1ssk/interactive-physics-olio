"""Search metadata and sitemaps for the complete static bilingual publication."""

from __future__ import annotations

import re
import tomllib
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from html import escape
from html.parser import HTMLParser
from pathlib import Path, PurePosixPath

import yaml

from .fields import FIELDS
from .metadata import VisualizationMetadata, load_metadata

BRAND = "Interactive Physics Olio"
SITEMAP_NAMESPACE = "http://www.sitemaps.org/schemas/sitemap/0.9"
LOCALES = ("en", "ja")


@dataclass(frozen=True)
class PublicPage:
    """One locale-specific indexable page, shared by head and sitemap generation."""

    path: PurePosixPath
    locale: str
    title: str
    description: str
    standalone: bool = False

    @property
    def relative_url(self) -> str:
        path = self.path.as_posix()
        return "" if path == "." else f"{path}/"


def _markdown_pages(root: Path) -> dict[PurePosixPath, Path]:
    pages = {}
    for source in sorted(root.rglob("*.md")):
        relative = source.relative_to(root)
        if source.name == "AGENTS.md" or relative.parts[0] in {"assets", "app"}:
            continue
        if "app" in relative.parts:
            continue
        path = relative.parent if source.name == "index.md" else relative.with_suffix("")
        if PurePosixPath(path) in pages:
            raise ValueError(f"{source}: multiple prose sources publish the same URL")
        pages[PurePosixPath(path)] = source
    return pages


def collect_public_pages(
    root: Path, visualizations: list[VisualizationMetadata]
) -> list[PublicPage]:
    """Discover bilingual prose and standalone apps; reject missing counterparts."""

    sources = {
        "en": _markdown_pages(root / "docs"),
        "ja": _markdown_pages(root / "docs_ja"),
    }
    if sources["en"].keys() != sources["ja"].keys():
        raise ValueError("Search publication requires matching English and Japanese page trees")
    metadata = {item.page: item for item in visualizations}
    for item in visualizations:
        if item.presentation == "article" and item.page not in sources["en"]:
            raise ValueError(f"{item.page}: visualization is missing its bilingual article")
    fields = {PurePosixPath(field.slug): field for field in FIELDS}
    pages = []
    for locale in LOCALES:
        for path, source in sources[locale].items():
            text = source.read_text(encoding="utf-8")
            frontmatter = {}
            if text.startswith("---\n"):
                _, header, text = text.split("---", 2)
                frontmatter = yaml.safe_load(header) or {}
            heading = re.search(r"^# (.+)$", text, re.M)
            if heading is None:
                raise ValueError(f"{source}: public page needs a title")
            title = frontmatter.get("title", heading.group(1))
            if not isinstance(title, str) or not title.strip():
                raise ValueError(f"{source}: public page needs a nonempty title")
            if path in metadata:
                description = metadata[path].localized_summary(locale)
            elif path in fields:
                description = fields[path].localized_summary(locale)
            elif path == PurePosixPath("."):
                description = (
                    "Explore physical and mathematical concepts through interactive visualizations "
                    "and concise explanations."
                    if locale == "en"
                    else "物理学と数学の概念を、インタラクティブな可視化と簡潔な解説で探索。"
                )
            elif path == PurePosixPath("updates"):
                description = (
                    "New and revised physics and mathematics visualizations and articles, "
                    "listed by update date."
                    if locale == "en"
                    else "物理学と数学の可視化・解説記事の新規公開と改訂を更新日順に掲載。"
                )
            else:
                description = frontmatter.get("description")
            description = frontmatter.get("description", description)
            if not isinstance(description, str) or not description.strip():
                raise ValueError(f"{source}: add a page-specific description to front matter")
            pages.append(PublicPage(path, locale, title, description))
        for item in visualizations:
            if item.presentation == "standalone":
                if item.page in sources[locale]:
                    raise ValueError(f"{item.page}: standalone app collides with a prose page")
                pages.append(
                    PublicPage(
                        item.page,
                        locale,
                        item.localized_title(locale),
                        item.localized_summary(locale),
                        standalone=True,
                    )
                )
    return sorted(pages, key=lambda page: (page.locale, page.relative_url))


def _set_attribute(tag: str, name: str, value: str) -> str:
    attribute = f'{name}="{escape(value, quote=True)}"'
    pattern = rf"\b{re.escape(name)}\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>]+)"
    if re.search(pattern, tag, flags=re.I):
        return re.sub(pattern, lambda _: attribute, tag, count=1, flags=re.I)
    return tag[:-1] + " " + attribute + ">"


class _MetadataEditor(HTMLParser):
    """Edit selected HTML spans without serializing scripts, equations, or plot data."""

    def __init__(
        self,
        html: str,
        metadata: str,
        page: PublicPage | None,
        urls: dict[str, str],
        home_url: str,
    ) -> None:
        super().__init__(convert_charrefs=False)
        self.html = html
        self.metadata = metadata
        self.page = page
        self.urls = urls
        self.home_url = home_url
        self.in_head = False
        self.found_head = False
        self.edits: list[tuple[int, int, str]] = []
        self.content: tuple[str, int, str] | None = None
        self.lines = [0]
        self.lines.extend(match.end() for match in re.finditer("\n", html))

    def position(self) -> int:
        line, column = self.getpos()
        return self.lines[line - 1] + column

    def remove_metadata(self, start: int, end: int) -> None:
        # Include a following newline so repeated enrichment is stable.
        if self.html[end : end + 1] == "\n":
            end += 1
        self.edits.append((start, end, ""))

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        raw = self.get_starttag_text()
        start = self.position()
        end = start + len(raw)
        if tag == "head":
            self.in_head = True
            self.found_head = True
        elif tag == "html" and self.page:
            self.edits.append((start, end, _set_attribute(raw, "lang", self.page.locale)))
        elif self.in_head and tag == "meta":
            if (attributes.get("name") or "").lower() in {
                "description",
                "robots",
                "google-site-verification",
            }:
                self.remove_metadata(start, end)
        elif self.in_head and tag == "link":
            relations = (attributes.get("rel") or "").lower().split()
            if "canonical" in relations or ("alternate" in relations and "hreflang" in attributes):
                self.remove_metadata(start, end)
        elif self.in_head and tag == "title" and self.page:
            title = self.page.title
            if title != BRAND:
                title += f" — {BRAND}"
            self.content = (tag, end, escape(title))
        elif self.page and self.page.standalone:
            if tag == "h1":
                self.content = (tag, end, escape(self.page.title))
            elif tag == "a":
                if attributes.get("id") == "brand-home":
                    self.edits.append((start, end, _set_attribute(raw, "href", self.home_url)))
                elif attributes.get("id") == "locale-link":
                    alternate = "ja" if self.page.locale == "en" else "en"
                    raw = _set_attribute(raw, "href", self.urls[alternate])
                    raw = _set_attribute(raw, "lang", alternate)
                    raw = _set_attribute(raw, "hreflang", alternate)
                    self.edits.append((start, end, raw))
                    self.content = (tag, end, "日本語" if alternate == "ja" else "English")
                elif attributes.get("data-language") in LOCALES:
                    locale = attributes["data-language"]
                    self.edits.append((start, end, _set_attribute(raw, "href", self.urls[locale])))

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)

    def handle_endtag(self, tag: str) -> None:
        if self.content and self.content[0] == tag:
            _, start, value = self.content
            self.edits.append((start, self.position(), value))
            self.content = None
        if tag == "head":
            self.edits.append((self.position(), self.position(), self.metadata))
            self.in_head = False

    def render(self) -> str:
        self.feed(self.html)
        if not self.found_head:
            raise ValueError("Published HTML must contain a head element")
        output = self.html
        for start, end, replacement in sorted(self.edits, reverse=True):
            output = output[:start] + replacement + output[end:]
        return output


def enrich_html(
    html: str,
    page: PublicPage | None,
    base_urls: dict[str, str],
    *,
    verification: str = "",
) -> str:
    """Render metadata in initial HTML; a missing page denotes a nonindexable URL."""

    urls = {}
    if page is None:
        metadata = '<meta name="robots" content="noindex">\n'
        home_url = ""
    else:
        urls = {locale: base_urls[locale] + page.relative_url for locale in LOCALES}
        home_url = base_urls[page.locale]
        metadata = (
            f'<meta name="description" content="{escape(page.description, quote=True)}">\n'
            f'<link rel="canonical" href="{escape(urls[page.locale], quote=True)}">\n'
        )
        for locale in LOCALES:
            metadata += (
                f'<link rel="alternate" hreflang="{locale}" '
                f'href="{escape(urls[locale], quote=True)}">\n'
            )
        if verification and page.path == PurePosixPath(".") and page.locale == "en":
            metadata += (
                '<meta name="google-site-verification" '
                f'content="{escape(verification, quote=True)}">\n'
            )
    return _MetadataEditor(html, metadata, page, urls, home_url).render()


def publish_search_metadata(root: Path, directories: list[Path]) -> None:
    """Finish the production build with one sitemap and consistent bilingual heads."""

    visualizations = [load_metadata(directory) for directory in directories]
    pages = collect_public_pages(root, visualizations)
    configs = {}
    for locale, name in (("en", "zensical.toml"), ("ja", "zensical.ja.toml")):
        with (root / name).open("rb") as file:
            configs[locale] = tomllib.load(file)["project"]
    base_urls = {locale: configs[locale]["site_url"] for locale in LOCALES}
    verification = configs["en"].get("extra", {}).get("search_console_verification", "")
    site = root / "site"
    for page in pages:
        locale_root = site / "ja" if page.locale == "ja" else site
        target = locale_root.joinpath(*page.path.parts, "index.html")
        html = target.read_text(encoding="utf-8")
        target.write_text(
            enrich_html(html, page, base_urls, verification=verification), encoding="utf-8"
        )
    for locale in LOCALES:
        locale_root = site / "ja" if locale == "ja" else site
        excluded = [locale_root / "404.html"]
        excluded.extend(
            locale_root.joinpath(*item.application_path.parts, "index.html")
            for item in visualizations
            if item.presentation == "article"
        )
        for target in excluded:
            html = target.read_text(encoding="utf-8")
            target.write_text(enrich_html(html, None, base_urls), encoding="utf-8")

    ET.register_namespace("", SITEMAP_NAMESPACE)
    sitemap = ET.Element(f"{{{SITEMAP_NAMESPACE}}}urlset")
    for page in pages:
        url = ET.SubElement(sitemap, f"{{{SITEMAP_NAMESPACE}}}url")
        ET.SubElement(url, f"{{{SITEMAP_NAMESPACE}}}loc").text = (
            base_urls[page.locale] + page.relative_url
        )
    ET.indent(sitemap, space="  ")
    ET.ElementTree(sitemap).write(site / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    # Zensical's locale sitemaps only include navigation pages. Publish one complete inventory.
    (site / "ja" / "sitemap.xml").unlink(missing_ok=True)
    for target in (site / "sitemap.xml.gz", site / "ja" / "sitemap.xml.gz"):
        target.unlink(missing_ok=True)
