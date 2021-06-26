import cowsay
from pytube import YouTube
import os

blacklist=["*", ";", ",", "/", ":"]

mode = input("For mp3 download, hit [0].For mp4 download, hit [1]. For both, hit [2] : ")
link = input ("Insert a link (youtube of course): ")


def mp3():
    video=YouTube(link)
    audio = video.streams.filter(only_audio=True).first()
    if any(ch in blacklist for ch in video.title):
        title = video.title
        NewTitle = title.translate({ord(i): '' for i in blacklist})
        file_name = "[audio] " + NewTitle
    else:
        file_name = "[audio] " + video.title    
    audio.download(filename = file_name)
    filename = file_name + ".mp4"
    Newfilename = file_name + ".mp3"
    os.rename(filename, Newfilename)
    print("mp3 downloaded !")
    
def mp4():
    video=YouTube(link)
    stream=video.streams.get_highest_resolution()
    stream.download()
    print("mp4 downloaded !")
    
    
if mode == '0':
    mp3()
elif mode == '1':
    mp4()
elif mode == '2' :
    mp3()
    mp4()
else:
    print("invalid choice")
cowsay.cow("Done...Enjoy")
