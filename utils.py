from youtube_search import YoutubeSearch
from pytube import YouTube
import os

YOUTUBE_URL = "https://www.youtube.com"

music_queue = []
playing = None

def download(url: str):
    
    if not url.startswith(YOUTUBE_URL):
        url = search(url)

    metadata = YouTube(url)
    # audio_location = metadata.streams.filter(only_audio=True).order_by('resolution').desc().first().download()
    audio_location = metadata.streams.filter(only_audio=True)[0].download()
    return audio_location

def add(url: str):
    location = download(url)
    music_queue.append(location)

def get():
    global playing
    playing = music_queue.pop()
    return playing


def size():
    return len(music_queue)

def has_next_song():
    return len(music_queue) > 0

def clear():
    for file_to_delete in music_queue:
        try:
            os.remove(file_to_delete)
        except:
            print(f'Failed to remove {file_to_delete}')
    music_queue.clear()
    playing = None

def get_queue():
    return f"Currently Playing: {playing.split('/')[-1].split('.')[0]}\n" + "\n - ".join([name.split('/')[-1].split('.')[0] for name in music_queue])

def delete():
    print("Deleting", playing)
    os.remove(playing)

def search(query):
    print(query)
    results = YoutubeSearch(query, max_results=1).to_dict()
    url = results[0]['url_suffix']
    return f'https://www.youtube.com{url}'