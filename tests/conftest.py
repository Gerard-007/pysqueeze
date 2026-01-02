import pytest
from PIL import Image


@pytest.fixture
def temp_image_dir(tmp_path):
    """
    Creates temporary test images dynamically.
    """
    assets = tmp_path / "assets"
    assets.mkdir()

    # Large JPG (simulates camera photo)
    large_path = assets / "large.jpg"
    with Image.new("RGB", (4000, 3000), color="red") as img:
        img.save(large_path, "JPEG", quality=95)

    # PNG with transparency
    logo_path = assets / "logo.png"
    with Image.new("RGBA", (512, 512), color=(0, 255, 0, 128)) as img:
        img.save(logo_path, "PNG")

    return {
        "dir": assets,
        "large": large_path,
        "logo": logo_path,
    }
