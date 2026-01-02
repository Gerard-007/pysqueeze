from PIL import Image
from pysqueeze import compress


def test_standard_compression_reduces_size(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "out.webp"

    compress(str(input_path), str(output_path), mode="standard")

    assert output_path.exists()
    assert output_path.stat().st_size < input_path.stat().st_size


def test_resize_respects_max_size(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "resized.webp"

    compress(
        str(input_path),
        str(output_path),
        mode="standard",
        max_size=800,
    )

    with Image.open(output_path) as img:
        assert max(img.size) <= 800


def test_png_to_webp(temp_image_dir, tmp_path):
    input_path = temp_image_dir["logo"]
    output_path = tmp_path / "logo.webp"

    compress(str(input_path), str(output_path), mode="standard")

    assert output_path.exists()


def test_target_kb_compression(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "target.webp"

    compress(
        str(input_path),
        str(output_path),
        mode="target",
        target_kb=200,
    )

    assert output_path.exists()
    assert output_path.stat().st_size <= 200 * 1024


def test_auto_mode_selects_best_format(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_base = tmp_path / "auto"

    compress(
        str(input_path),
        str(output_base),
        mode="auto",
    )

    webp = output_base.with_suffix(".webp")
    avif = output_base.with_suffix(".avif")

    assert webp.exists() or avif.exists()


def test_invalid_mode_raises_error(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "bad.webp"

    try:
        compress(
            str(input_path),
            str(output_path),
            mode="invalid",
        )
    except ValueError:
        assert True
    else:
        assert False
