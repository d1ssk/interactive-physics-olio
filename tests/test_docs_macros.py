from pathlib import Path

from physics_atlas.docs_macros import render_topic_cards, visualization_counts
from physics_atlas.fields import FIELDS


def test_topic_cards_count_field_listings(tmp_path: Path) -> None:
    directory = tmp_path / "docs" / "mathematics-for-physics"
    directory.mkdir(parents=True)
    (directory / "index.md").write_text(
        "# Mathematics for Physics\n\n- **[Example](example/)**<br>\n  Summary.\n",
        encoding="utf-8",
    )

    counts = visualization_counts(tmp_path)
    cards = render_topic_cards(tmp_path)
    japanese_cards = render_topic_cards(tmp_path, "ja")

    assert counts["mathematics-for-physics"] == 1
    assert 'href="mathematics-for-physics/"' in cards
    for field in FIELDS:
        if field.card_image:
            assert f'src="{field.card_image}"' in cards
            assert f'src="../{field.card_image}"' in japanese_cards
    assert cards.count("<img ") == japanese_cards.count("<img ") == 13
    assert cards.count('loading="eager"') == 2
    assert cards.count('loading="lazy"') == 11
    assert "background-image" not in cards
    assert "1 visualization" in cards
    assert "0 visualizations" in cards
    assert cards.count('class="topic-card"') == 14
    assert 'class="topic-card__summary"' not in cards
    assert 'class="topic-card__summary"' not in japanese_cards
    assert "An example visualization." not in cards
    assert "物理数学" in japanese_cards
    assert "1 件の可視化" in japanese_cards


def test_counts_include_cross_field_and_external_listings(tmp_path: Path) -> None:
    directory = tmp_path / "docs" / "cosmology"
    directory.mkdir(parents=True)
    (directory / "index.md").write_text(
        "# Cosmology\n\n"
        "- **[Local](local/)**<br>\n  A local application.\n"
        "- **[External](https://example.com/app/?lang=en)**<br>\n  An external app.\n"
        "- **[Cross-field](../particle-physics/example/?lang=en)**<br>\n"
        "  Related reading [source](https://example.com/source).\n",
        encoding="utf-8",
    )

    assert visualization_counts(tmp_path)["cosmology"] == 3
    assert "3 visualizations" in render_topic_cards(tmp_path, "en")
    assert "3 件の可視化" in render_topic_cards(tmp_path, "ja")


def test_published_field_counts_include_all_listings() -> None:
    root = Path(__file__).resolve().parents[1]
    counts = visualization_counts(root)
    assert counts["cosmology"] == 5
    assert counts["thermodynamics"] == 2
    assert counts["string-theory"] == 2
