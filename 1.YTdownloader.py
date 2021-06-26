import cowsay
from pytube import YouTube
import os

blacklist=["*", ";", ",", "/", ":"] #blacklisted characters from YT titles, maybe incomplete

#getting file extension and YT link
mode = input("For mp3 download, hit [0].For mp4 download, hit [1]. For both, hit [2] : ")
link = input ("Insert a link (youtube of course): ")

#convert video to mp3 file
def mp3():
    video=YouTube(link)
    audio = video.streams.filter(only_audio=True).first() #pytube only download .mp4, so I use OS to rename the file in .mp3
    if any(ch in blacklist for ch in video.title):        #but some characters from YT titles (the blacklist) aren't in the downloaded file name
        title = video.title                               #so i need to remove them
        NewTitle = title.translate({ord(i): '' for i in blacklist})
        file_name = "[audio] " + NewTitle
    else:
        file_name = "[audio] " + video.title    
    audio.download(filename = file_name)
    filename = file_name + ".mp4"
    Newfilename = file_name + ".mp3"
    os.rename(filename, Newfilename) #with the blacklisted characteres removed, I can rename the file witouth any problem in .mp3 
    print("mp3 downloaded !")

#convert video to mp4 file
def mp4():
    video=YouTube(link)
    stream=video.streams.get_highest_resolution()
    stream.download()
    print("mp4 downloaded !")
    
#test to download the right format   
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
