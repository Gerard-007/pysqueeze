import subprocess
import sys


def test_cli_webp(temp_image_dir, tmp_path):
    input_path = temp_image_dir["large"]
    output_path = tmp_path / "cli.webp"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "pysqueeze.cli",
            str(input_path),
            "-o",
            str(output_path),
            "--mode",
            "standard",
        ],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert output_path.exists()
    assert output_path.stat().st_size > 0
