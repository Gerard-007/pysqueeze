from PIL import Image
import io
from pathlib import Path

DEFAULT_MAX_SIZE = 1600
DEFAULT_WEBP_QUALITY = 75
DEFAULT_AVIF_QUALITY = 40


def compress_image(
    input_path: str,
    output_path: str,
    *,
    max_size: int = DEFAULT_MAX_SIZE,
    format: str = "webp",
    quality: int | None = None,
) -> None:
    """
    Compress an image using perceptual compression.
    """
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    img = Image.open(input_path)

    # Convert to RGB (removes alpha issues & metadata)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    # Resize while maintaining aspect ratio
    img.thumbnail((max_size, max_size), Image.LANCZOS)

    save_kwargs = {"optimize": True}

    if format.lower() == "webp":
        save_kwargs.update({
            "format": "WEBP",
            "quality": quality or DEFAULT_WEBP_QUALITY,
            "method": 6,
        })

    elif format.lower() == "avif":
        save_kwargs.update({
            "format": "AVIF",
            "quality": quality or DEFAULT_AVIF_QUALITY,
            "speed": 6,
        })

    else:
        raise ValueError("Unsupported format. Use 'webp' or 'avif'.")

    img.save(output_path, **save_kwargs)
