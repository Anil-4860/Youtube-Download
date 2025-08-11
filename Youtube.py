#YouTube Video  Downloader

#To print YouTube title
from pytube import YouTube
link="https://youtu.be/N4hRNe8zneE?si=BFTDqqwRQQSXkv8a"
youtube_1=YouTube(link)
print(youtube_1.title)


#To print thumbnail
from pytube import YouTube
link="https://youtu.be/N4hRNe8zneE?si=BFTDqqwRQQSXkv8a"
youtube_1=YouTube(link)
print(youtube_1.thumbnail_url)


#Video Download From Youtube
from pytube import YouTube
link = "https://youtu.be/bTkq3495kPw?si=A6GL4oTHwbO9M-87"
youtube_1 = YouTube(link)
video = youtube_1.streams.all()
vid = list(enumerate(video))
for i in vid:
   print(i)
print() 
strm = int(input("enter: "))
video[strm].download()
print("Download successfilly")

# from pytube import YouTube

link = "https://youtu.be/bTkq3495kPw?si=A6GL4oTHwbO9M-87"
youtube_1 = YouTube(link)
video = youtube_1.streams.all()

# Print the available streams
for i, stream in enumerate(video):
    print(f"{i+1}: {stream}")

# Get user input
strm = int(input("Enter the stream number to download: ")) - 1

# Download the selected stream
video[strm].download()


#Only Audio download from youtube
from pytube import YouTube
link = "https://youtu.be/N4hRNe8zneE?si=BFTDqqwRQQSXkv8a"
youtube_1 = YouTube(link)
video = youtube_1.streams.filter(only_audio=True)
vid = list(enumerate(video))
for i in vid:
   print(i)
print()  
strm = int(input("enter: "))
video[strm].download()
print("Download successfilly")


#Complete playlist download from youtube
from pytube import Playlist
py = Playlist(input("enter url"))
print(f"Downloading: {py.title}")

for video in py.videos:
   video.streams.first().download()





from plyer import notification
import time
if __name__=='__main__':
     while True:
         notification.notify(title="***Take Rest***",message="	Rest is vital for better mental health.",
         app_icon="C:/Users/ANIL KUMAR SAHOO/Desktop/Anil/file1",timeout=5)
         time.sleep(10)
