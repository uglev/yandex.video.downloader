import yt_dlp
import csv

def download_video(url):
    ydl_opts = {}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

with open('videos.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        url = row[0]
        download_video(url)