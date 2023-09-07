import yt_dlp
import requests
from bs4 import BeautifulSoup

# Function to download a song from YouTube
def download_song(url, output_path):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as e:
        print(f"Failed to download {url}: {str(e)}")

# Function to search for a song on YouTube using the YouTube Data API
def search_song(title):
    try:
        api_key = "AIzaSyBsjEut9or5HdBM5c3zz47iwijZiwn5Yn4"  # Replace with your YouTube Data API key
        search_url = f"https://www.googleapis.com/youtube/v3/search?key={api_key}&q={title}&type=video&maxResults=1"
        response = requests.get(search_url)
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            video_id = data["items"][0]["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"
    except Exception as e:
        print(f"Failed to search for {title}: {str(e)}")
    return None

# Output directory where downloaded songs will be saved
output_directory = 'E:/downloaded_songs'


# Create the output directory if it doesn't exist
import os
os.makedirs(output_directory, exist_ok=True)

# Web scraping to get song titles
url = "https://www.popxo.com/article/latest-bollywood-songs-that-will-help-you-update-your-playlist/"
res = requests.get(url)
h = res.status_code
print(h, "success, you can access")
soup = BeautifulSoup(res.text, "lxml")
s_name = soup.find_all("div", {"class": "storyContent relative font-openSans md:px-12 px-4 transition-all ease-in w-full fixed"})

# List to store song titles
song_titles = []

with open("songsss.txt", "w", encoding="utf-8") as output_file:
    for songs in s_name:
        t = songs.find_all("h3")
     
        
        for song in t:
            song_name = song.text
            print(song_name)
            output_file.write(song_name + "\n")
            song_titles.append(song_name)

        

# Download each song in the list
for title in song_titles:
    video_url = search_song(title)
    if video_url:
        download_song(video_url, output_directory)
    else:
        print(f"No results found for {title}")
