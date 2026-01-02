# pysqueeze

High-quality image compression for Python, inspired by TinyPNG and Squoosh.

## Features
- JPG / PNG → WebP / AVIF
- Perceptual compression
- Metadata stripping
- CLI and Python API

## Install
```bash
pip install pysqueeze
```

# Usage
```
from pysqueeze import compress_image
compress_image("input.jpg", "output.webp")
```
```
pysqueeze input.jpg -o output.webp
```


---

### 3.2 `LICENSE` (strongly recommended)

```text
MIT License
```