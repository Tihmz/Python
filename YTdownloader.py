from __future__ import unicode_literals
import youtube_dl
import cowsay
from pytube import YouTube

#choose format and get the vids link
mode = input("For mp3 download, hit [1]. For mp4 download, hit [2] : ")
link = input ("Insert a link (youtube of course): ")

#convert to mp3
def mp3():
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '320',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    cowsay.cow("Done...Enjoy")

#convert to mp4
def mp4():
    video=YouTube(link)
    stream=video.streams.get_highest_resolution()
    stream.download()
    cowsay.cow("Done...Enjoy")

#download
if mode == '1':
    mp3()
elif mode == '2':
    mp4()
