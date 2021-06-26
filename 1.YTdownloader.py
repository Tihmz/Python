import cowsay
from pytube import YouTube
import os

mode = input("For mp3 download, hit [1]. For mp4 download, hit [2] : ")
link = input ("Insert a link (youtube of course): ")


def mp3():
    sound=YouTube(link)
    stream= sound.streams.filter(only_audio=True).first()
    stream.download()
    filename=sound.title + ".mp4"
    Newfilename=sound.title + ".mp3"
    os.rename(filename, Newfilename)
    cowsay.cow("Done...Enjoy")
    
def mp4():
    video=YouTube(link)
    stream=video.streams.get_highest_resolution()
    stream.download()
    cowsay.cow("Done...Enjoy")
    
if mode == '1':
    mp3()
elif mode == '2':
    mp4()

