# pysqueeze

**pysqueeze** is a high-quality image compression library for Python, inspired by tools like **TinyPNG** and **Squoosh**.
It focuses on achieving **significant file size reduction** while preserving perceptual image quality.

The library is designed for developers who need reliable, automated image optimization for web, mobile, and backend pipelines.


## Key Features
- Convert JPG and PNG images to **WebP** or **AVIF**
- Perceptual compression with sensible defaults
- Target file size compression (TinyPNG-like behavior)
- Automatic format selection (WebP vs AVIF)
- Metadata stripping for smaller output files
- Simple Python API and command-line interface
- Cross-platform support (Windows, macOS, Linux)

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
