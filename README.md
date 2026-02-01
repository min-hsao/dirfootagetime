# Dir Footage Time

A Python CLI tool to calculate the total duration of all video files in a directory, including subdirectories. Useful for estimating project footage length.

## Features

- ⏱️ Calculate total video duration
- 📁 Recursive subdirectory scanning
- 🔍 Include/exclude file filters
- 📊 Per-subdirectory breakdown
- 🎬 Multiple video format support

## Requirements

- Python 3.6+
- FFmpeg (ffprobe)

## Installation

```bash
# Install FFmpeg (macOS)
brew install ffmpeg
```

No Python dependencies required - uses standard library.

## Usage

```bash
# Basic usage
python dirfootagetime.py /path/to/videos

# Exclude files containing text
python dirfootagetime.py /path/to/videos --exclude "proxy"

# Include only files containing text
python dirfootagetime.py /path/to/videos --include "final"
```

## Arguments

| Argument | Description |
|----------|-------------|
| `directory` | Path to directory containing videos |
| `--exclude` | Exclude files containing this text |
| `--include` | Include only files containing this text |

## Output

```
Calculating total video duration...
Processed clip001.mp4: 125.50 seconds
Processed clip002.mp4: 89.25 seconds
Processed interview/take1.mov: 320.00 seconds

#dirfootagetime
#by Min-Hsao Chen (w/ ChatGPT-4)
#version 0.0005
Subdirectory '.': 214.75 seconds (03:34)
Subdirectory 'interview': 320.00 seconds (05:20)
Total duration of all video files: 534.75 seconds (08:54)
```

## Supported Formats

- MP4
- MOV
- AVI
- MKV
- And any format supported by FFprobe

## License

MIT License - see [LICENSE](LICENSE) for details.
