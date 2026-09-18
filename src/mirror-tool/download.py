## test video link : https://www.youtube.com/watch?v=YKsQJVzr3a8
from yt_dlp import YoutubeDL
import subprocess


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
            "format" : "bestaudio/best",
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
        print("invalid choice choose between either 1 or 2 ")
        exit()


with YoutubeDL(opts) as ydl:
    ydl.download([url])

if choice == 3:
    subprocess.run([
        "ffmpeg", "-y",
        "-i", "downloaded.mp4",
        "-vf", "hflip",
        "-c:a", "copy",
        "downloaded_mirrored.mp4",
    ])