from yt_dlp import YoutubeDL
import subprocess


def print_box(message, symbol="!"):
    border = "=" * 64
    print()
    print(border)
    print(f"  {symbol}  {message}")
    print(border)
    print()


def run_downloader():
    url = input("enter your youtube url properly in proper format: ")
    choice = int(input("enter your choice '1 = video+audio' , 2 = 'audio only' , 3 = 'mirrored+audio+video' "))

    if choice == 1:
        opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "cookiefile": None,
            "cookiesfrombrowser": None,
            "outtmpl": "downloaded.%(ext)s",
        }
    elif choice == 2:
        opts = {
            "format": "bestaudio/best",
            "cookiefile": None,
            "cookiesfrombrowser": None,
            "outtmpl": "downloaded.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }
    elif choice == 3:
        opts = {
            "format": "bestvideo+bestaudio/best",
            "merge_output_format": "mp4",
            "cookiefile": None,
            "cookiesfrombrowser": None,
            "outtmpl": "downloaded.%(ext)s",
        }
    else:
        print_box("Invalid choice. Please choose 1, 2, or 3.", "!")
        return

    try:
        with YoutubeDL(opts) as ydl:
            ydl.download([url])
    except Exception as e:
        msg = str(e)
        if "Sign in to confirm" in msg:
            print_box("YouTube thinks you're a bot. Try again in ~10 minutes.", "!")
        elif "Too Many Requests" in msg or "429" in msg:
            print_box("YouTube rate-limited you. Wait ~10 minutes and retry.", "!")
        elif "ffmpeg" in msg.lower():
            print_box("ffmpeg missing or not on PATH. Install it and try again.", "!")
        else:
            print_box(f"Download failed: {msg}, might be a bug from our end", "!")
        return

    print_box("Download complete.", "+")

    if choice == 3:
        print_box("Mirroring video...", "*")
        try:
            subprocess.run([
                "ffmpeg", "-y",
                "-i", "downloaded.mp4",
                "-vf", "hflip",
                "-c:a", "aac",
                "downloaded_mirrored.mp4",
            ], check=True)
            print_box("Mirrored file saved: downloaded_mirrored.mp4", "+")
        except subprocess.CalledProcessError as e:
            print_box(f"Mirror failed: {e}", "!")


if __name__ == "__main__":
    run_downloader()