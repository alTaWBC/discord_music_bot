from pytube import YouTube
# # import playsound



# playsound.playsound(location)
from youtube_search import YoutubeSearch


results = YoutubeSearch('search terms', max_results=2).to_dict()

for result in results:
    for key, value in result.items():
        print(key, '->', value)

# print(results)
url = results[0]['url_suffix']
video = YouTube(f'https://www.youtube.com{url}')

stream = video.streams.get_audio_only()

location = stream.download()