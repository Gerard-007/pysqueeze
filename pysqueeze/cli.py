import argparse
from .compressor import compress_image


def main():
    try:
        parser = argparse.ArgumentParser(description="TinyPNG-like image compressor")
        parser.add_argument("input", help="Input image path")
        parser.add_argument("-o", "--output", required=True, help="Output image path")
        parser.add_argument("--max-size", type=int, default=1600)
        parser.add_argument("--format", choices=["webp", "avif"], default="webp")
        parser.add_argument("--quality", type=int)

        args = parser.parse_args()

        compress_image(
            args.input,
            args.output,
            max_size=args.max_size,
            format=args.format,
            quality=args.quality,
        )
    except Exception as e:
        raise SystemExit(str(e))


if __name__ == "__main__":
    main()
