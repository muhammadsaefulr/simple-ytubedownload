from pytube import YouTube
from youtubesearchpython import VideosSearch
import os

videoName = input("Cari Video Yang Akan Di Download !:  ")
clean_videoName = videoName.replace(" ", "-")

yt = VideosSearch(videoName, limit=5)

result_array = yt.result().get("result")

i = 1

for value in result_array:
    print(i, ". ", value["title"])

    i += 1

video_chosen_index = input("Pilih Urutan Ke Berapa Video Yang Akan Di Download ! \n")
video_chosen = result_array[int(video_chosen_index) - 1]

print(video_chosen["title"])
print(video_chosen["link"], "\n")

def download_video(url):
    yt = YouTube(url)
    videos = yt.streams.filter(file_extension='mp4')
    video = list(enumerate(videos))
    for i in video:
         print(i)

         print("Masukan Format Yang Akan Di Download:")
         download_format = int(input("Masukan Format/Resolusinya: "))
         videos[download_format].download()
         print("Download Sukses!")

if __name__ == "__main__":
   url = video_chosen["link"]
   download_video(url)
