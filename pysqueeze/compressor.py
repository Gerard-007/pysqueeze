from pathlib import Path
from PIL import Image
import io

DEFAULT_MAX_SIZE = 1600
DEFAULT_WEBP_QUALITY = 75
DEFAULT_AVIF_QUALITY = 40
MIN_QUALITY = 30


def _compress_standard(
    input_path: str,
    output_path: str,
    *,
    max_size: int,
    format: str,
    quality: int | None,
):
    img = Image.open(input_path)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    img.thumbnail((max_size, max_size), Image.LANCZOS)

    if format == "webp":
        img.save(
            output_path,
            "WEBP",
            quality=quality or DEFAULT_WEBP_QUALITY,
            method=6,
            optimize=True,
        )
    elif format == "avif":
        img.save(
            output_path,
            "AVIF",
            quality=quality or DEFAULT_AVIF_QUALITY,
            speed=6,
        )
    else:
        raise ValueError("Unsupported format")


def _compress_target(
    input_path: str,
    output_path: str,
    *,
    max_size: int,
    format: str,
    quality: int | None,
    target_kb: int,
):
    img = Image.open(input_path)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    img.thumbnail((max_size, max_size), Image.LANCZOS)

    def save(q):
        buf = io.BytesIO()
        if format == "webp":
            img.save(buf, "WEBP", quality=q, method=6)
        elif format == "avif":
            img.save(buf, "AVIF", quality=q, speed=6)
        return buf

    q = quality or 80
    while q >= MIN_QUALITY:
        buf = save(q)
        if buf.tell() <= target_kb * 1024:
            Path(output_path).write_bytes(buf.getvalue())
            return
        q -= 5

    Path(output_path).write_bytes(buf.getvalue())


def _compress_auto(
    input_path: str,
    output_path: str,
    *,
    max_size: int,
):
    img = Image.open(input_path)
    if img.mode not in ("RGB", "L"):
        img = img.convert("RGB")

    img.thumbnail((max_size, max_size), Image.LANCZOS)

    results = {}

    for fmt, params in {
        "webp": dict(format="WEBP", quality=75, method=6),
        "avif": dict(format="AVIF", quality=40, speed=6),
    }.items():
        try:
            buf = io.BytesIO()
            img.save(buf, **params)
            results[fmt] = buf
        except Exception:
            pass

    if not results:
        raise RuntimeError("No supported formats available")

    best_fmt = min(results, key=lambda k: results[k].tell())
    output = Path(output_path).with_suffix(f".{best_fmt}")
    output.write_bytes(results[best_fmt].getvalue())


def compress(
    input_path: str,
    output_path: str,
    *,
    mode: str = "standard",
    max_size: int = DEFAULT_MAX_SIZE,
    format: str = "webp",
    quality: int | None = None,
    target_kb: int | None = None,
):
    if not Path(input_path).exists():
        raise FileNotFoundError(f"Input image not found: {input_path}")

    if mode == "standard":
        _compress_standard(
            input_path,
            output_path,
            max_size=max_size,
            format=format,
            quality=quality,
        )

    elif mode == "target":
        if not target_kb:
            raise ValueError("target_kb is required for target mode")

        _compress_target(
            input_path,
            output_path,
            max_size=max_size,
            format=format,
            quality=quality,
            target_kb=target_kb,
        )

    elif mode == "auto":
        _compress_auto(
            input_path,
            output_path,
            max_size=max_size,
        )

    else:
        raise ValueError("Invalid mode: use standard, target, or auto")
