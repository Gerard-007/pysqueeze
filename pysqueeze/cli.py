import argparse
from .compressor import compress


def main():
    try:
        parser = argparse.ArgumentParser(
            description="TinyPNG-like image compressor"
        )

        parser.add_argument(
            "input",
            help="Input image path or folder"
        )

        parser.add_argument(
            "-o",
            "--output",
            required=True,
            help="Output image path (or folder in batch mode)"
        )

        parser.add_argument(
            "--mode",
            choices=["standard", "target", "auto"],
            default="standard",
            help="Compression mode (default: standard)",
        )

        parser.add_argument(
            "--max-size",
            type=int,
            default=1600,
            help="Maximum width/height in pixels",
        )

        parser.add_argument(
            "--format",
            choices=["webp", "avif"],
            default="webp",
            help="Output format (ignored in auto mode)",
        )

        parser.add_argument(
            "--quality",
            type=int,
            help="Compression quality",
        )

        parser.add_argument(
            "--target-kb",
            type=int,
            help="Target file size in KB (required for target mode)",
        )

        args = parser.parse_args()

        compress(
            input_path=args.input,
            output_path=args.output,
            mode=args.mode,
            max_size=args.max_size,
            format=args.format,
            quality=args.quality,
            target_kb=args.target_kb,
        )

    except Exception as e:
        raise SystemExit(str(e))


if __name__ == "__main__":
    main()
