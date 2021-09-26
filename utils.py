from pytube import YouTube
import os

music_queue = []
playing = None

def download(url: str):
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
    try:
        delete()
    except:
        print(f'Failed to remove {playing}')
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

