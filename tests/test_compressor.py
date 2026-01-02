import os
from PIL import Image
from pysqueeze.compressor import compress_image


def test_webp_compression_reduces_size(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "out.webp"

    compress_image(str(input_path), str(output_path))

    assert output_path.exists()
    assert output_path.stat().st_size < input_path.stat().st_size


def test_resize_respects_max_size(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "resized.webp"

    compress_image(str(input_path), str(output_path), max_size=800)

    with Image.open(output_path) as img:
        assert max(img.size) <= 800


def test_png_to_webp(temp_image_dir, tmp_path):
    input_path = temp_image_dir["logo"]
    output_path = tmp_path / "logo.webp"

    compress_image(str(input_path), str(output_path))

    assert output_path.exists()


def test_invalid_format_raises_error(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "bad.out"

    try:
        compress_image(str(input_path), str(output_path), format="svg")
    except ValueError:
        assert True
    else:
        assert False
