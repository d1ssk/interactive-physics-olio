"""Build-time macros for atlas documentation pages."""

from __future__ import annotations

import re
from collections import Counter
from html import escape
from pathlib import Path
from typing import Any

from .fields import FIELDS


def visualization_counts(project_root: Path) -> Counter[str]:
    """Count listings in each field index, including cross-field and external links."""

    counts: Counter[str] = Counter()
    for field in FIELDS:
        index = project_root / "docs" / field.slug / "index.md"
        if index.is_file():
            # Field listings use a bold Markdown title link at the start of a list item.
            counts[field.slug] = len(
                re.findall(
                    r"^[-*] \*\*\[[^\n]+?\]\([^)\n]+\)\*\*", index.read_text(encoding="utf-8"), re.M
                )
            )
    return counts


def render_topic_cards(project_root: Path, locale: str = "en") -> str:
    """Return the home-page topic card grid as static HTML."""

    if locale not in {"en", "ja"}:
        raise ValueError(f"unsupported locale: {locale}")

    counts = visualization_counts(project_root)
    cards: list[str] = ['<div class="topic-grid">']
    for index, field in enumerate(FIELDS):
        count = counts[field.slug]
        noun = "visualization" if count == 1 else "visualizations"
        count_label = f"{count} {noun}" if locale == "en" else f"{count} 件の可視化"
        image = ""
        if field.card_image:
            source = ("../" if locale == "ja" else "") + field.card_image
            loading = "eager" if index < 2 else "lazy"
            image = (
                f'<img src="{escape(source, quote=True)}" alt="" '
                f'loading="{loading}" decoding="async">'
            )
        cards.extend(
            [
                f'<a class="topic-card" href="{escape(field.slug, quote=True)}/">',
                f'  <span class="topic-card__media" aria-hidden="true">{image}</span>',
                '  <span class="topic-card__body">',
                '    <strong class="topic-card__title">'
                f"{escape(field.localized_label(locale))}</strong>",
                f'    <span class="topic-card__count">{count_label}</span>',
                "  </span>",
                "</a>",
            ]
        )
    cards.append("</div>")
    return "\n".join(cards)


def define_env(env: Any) -> None:
    """Register project macros with Zensical."""

    project_root = Path(env.conf["root_dir"])
    env.macro(lambda locale="en": render_topic_cards(project_root, locale), "topic_cards")
