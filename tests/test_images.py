"""Keep publication images lightweight without changing their aspect ratios."""

from pathlib import Path

import build_site
from PIL import Image

from physics_atlas.fields import FIELDS
from physics_atlas.seo import SOCIAL_IMAGE

ROOT = Path(__file__).resolve().parents[1]


def test_staged_card_images_are_small_shared_and_preserve_source_aspect(tmp_path, monkeypatch):
    english = tmp_path / "en"
    japanese = tmp_path / "ja"
    monkeypatch.setattr(build_site, "ENGLISH_BUILD_DOCS_DIR", english)
    monkeypatch.setattr(build_site, "JAPANESE_BUILD_DOCS_DIR", japanese)
    build_site.stage_english_docs()
    build_site.stage_japanese_docs()
    total_size = 0
    for field in FIELDS:
        if not field.image:
            continue
        target = english / field.card_image
        total_size += target.stat().st_size
        with Image.open(ROOT / "docs" / field.image) as source, Image.open(target) as thumbnail:
            assert thumbnail.format == "WEBP"
            assert thumbnail.width <= 600
            assert abs(thumbnail.height - source.height * thumbnail.width / source.width) <= 1
        assert not (english / field.image).exists()
        assert not (japanese / field.image).exists()
        assert not (japanese / field.card_image).exists()
    assert total_size < 1_000_000
    assert not (english / "assets/images/string-theory_old.png").exists()
    assert not (japanese / SOCIAL_IMAGE).exists()
    with Image.open(english / SOCIAL_IMAGE) as image:
        assert image.format == "PNG"
        assert image.size == (1200, 630)
