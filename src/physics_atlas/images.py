"""Build lightweight card images from the retained publication sources."""

from pathlib import Path

from PIL import Image

from .fields import FIELDS


def build_card_images(source_docs: Path, output_docs: Path) -> None:
    """Publish 600px WebP thumbnails, excluding their full-resolution PNG sources."""

    for field in FIELDS:
        if not field.image or not field.card_image:
            continue
        target = output_docs / field.card_image
        target.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source_docs / field.image) as source:
            width = min(600, source.width)
            height = round(source.height * width / source.width)
            thumbnail = source.resize((width, height), Image.Resampling.LANCZOS)
            thumbnail.save(target, "WEBP", quality=85, method=6)
        (output_docs / field.image).unlink(missing_ok=True)
