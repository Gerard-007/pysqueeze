# pysqueeze

High-quality image compression for Python, inspired by TinyPNG and Squoosh.
Designed for developers who want small file sizes with minimal visual loss, both from Python code and the command line.

## Features
- JPG / PNG → WebP / AVIF
- Perceptual image compression
- Target file size compression (TinyPNG-like)
- Automatic format selection (WebP vs AVIF)
- Metadata stripping by default
- CLI and Python API
- Cross-platform (Windows, macOS, Linux)

## Install
```bash
pip install pysqueeze
```

### Standard compression (default)
```
from pysqueeze import compress
compress("input.jpg", "output.webp")
```

### Target file size compression
```
from pysqueeze import compress
compress(
    "input.jpg",
    "output.webp",
    mode="target",
    target_kb=200,
)
```

### Automatic format selection (best result)
```
from pysqueeze import compress
compress(
    "input.jpg",
    "output",
    mode="auto",
)
```

### Standard compression
```
pysqueeze input.jpg -o output.webp
```

### Target file size (TinyPNG-style)
```
pysqueeze input.jpg -o output.webp --mode target --target-kb 200
```

### Automatic format selection
```
pysqueeze input.jpg -o output --mode auto
```

### Options
| Option        | Description                                            |
| ------------- | ------------------------------------------------------ |
| `--mode`      | `standard`, `target`, or `auto`                        |
| `--max-size`  | Maximum width/height in pixels (default: 1600)         |
| `--format`    | Output format (`webp` or `avif`, ignored in auto mode) |
| `--quality`   | Compression quality override                           |
| `--target-kb` | Target file size in KB (required for target mode)      |

---

### LICENSE

```text
MIT License
```

### Project Status
`pysqueeze` is actively developed and suitable for production use.
Contributions, issues, and feature requests are welcome.
