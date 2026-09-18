# Mirror Tool

A small command-line tool to download YouTube videos, extract audio, or mirror videos horizontally — powered by [yt-dlp](https://github.com/yt-dlp/yt-dlp) and [ffmpeg](https://ffmpeg.org/).

![Status](https://img.shields.io/badge/status-in--development-yellow)

---

## Features

- Download video (best quality, merged MP4)
- Download audio only (converted to MP3 @ 192 kbps)
- Download mirrored video (horizontally flipped) with audio intact
- Friendly error messages instead of raw Python tracebacks
- Installable as a real terminal command — just type `mirror-tool`

---

## Requirements

| Tool | Why | Install |
|---|---|---|
| Python 3.10+ | Runs the tool | [python.org](https://www.python.org/downloads/) |
| ffmpeg | Merges video+audio, converts to MP3, mirrors videos | [ffmpeg.org](https://ffmpeg.org/download.html) |
| yt-dlp | Downloads from YouTube | installed automatically via pip |
| deno *(optional)* | Helps yt-dlp bypass YouTube's bot checks | [deno.land](https://deno.land/) |

### Quick installs by OS

**Windows**

```powershell
winget install ffmpeg
winget install deno
```

**macOS**

```bash
brew install ffmpeg deno
```

**Linux (Debian/Ubuntu)**

```bash
sudo apt update
sudo apt install -y ffmpeg
curl -fsSL https://deno.land/install.sh | sh
```

---

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/novaflareiii/mirror-tool.git
cd mirror-tool
```

**2. Create a virtual environment** *(recommended)*

```bash
python -m venv .venv
```

Activate it — Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

Activate it — macOS / Linux:

```bash
source .venv/bin/activate
```

**3. Install the package**

```bash
pip install -e .
```

The command `mirror-tool` is now available in your terminal.

---

## Usage

```bash
mirror-tool
```

Paste a YouTube URL, then choose an option:

| Choice | Action | Output file |
|---|---|---|
| `1` | Download video + audio (merged MP4) | `downloaded.mp4` |
| `2` | Download audio only (MP3 @ 192 kbps) | `downloaded.mp3` |
| `3` | Download video + audio, then mirror horizontally | `downloaded_mirrored.mp4` |

Files are saved in the folder where you run the command.

---

## Example Session

```
$ mirror-tool

enter your youtube url properly in proper format: https://www.youtube.com/watch?v=dQw4w9WgXcQ
enter your choice '1 = video+audio' , 2 = 'audio only' , 3 = 'mirrored+audio+video' 3

[youtube] Extracting URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
[download] Destination: downloaded.f137.mp4
[download] 100% of 34.85MiB
[Merger] Merging formats into "downloaded.mp4"

Download complete.
Mirroring video...
Mirrored file saved: downloaded_mirrored.mp4
```

---

## Common Issues

**"YouTube thinks you're a bot"**

YouTube rate-limits anonymous requests.

- Wait 10 minutes and try again
- Close your browser and re-run — yt-dlp can then read its cookies
- Get a `cookies.txt` file (browser extension like *Get cookies.txt LOCALLY*) and point yt-dlp to it

**"ffmpeg missing or not on PATH"**

Install ffmpeg — see [Requirements](#requirements).

**"ModuleNotFoundError: No module named 'mirror_tool'"**

You installed the package in one Python but are running it in another.

```bash
python -m pip install -e .
```

**"Permission denied" when reading browser cookies**

Your browser is open and has the cookie DB locked. Fully close it (check the system tray) and try again.

**Work in progress** — core features work, but expect changes and rough edges.

---

## Project Structure

```
mirror-tool/
├── pyproject.toml       # Package config + entry point
├── README.md
├── LICENSE
└── src/
    └── mirror_tool/
        ├── __init__.py
        ├── __main__.py   # Entry point
        ├── banner.py     # ASCII header
        └── downloader.py # Core logic
```

---

## Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you'd like to change.

---

## License

MIT — see [LICENSE](LICENSE).

---

## Credits

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — the downloader engine
- [ffmpeg](https://ffmpeg.org/) — the video processing tool
