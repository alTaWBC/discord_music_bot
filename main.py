from pytube import YouTube
# import playsound

video = YouTube('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

stream = video.streams.filter(only_audio=True)[0]

location = stream.download()

# playsound.playsound(location)
