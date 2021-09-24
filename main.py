from pytube import YouTube
import playsound

video = YouTube('http://youtube.com/watch?v=2lAe1cqCOXo')

stream = video.streams.filter(only_audio=True)[0]

location = stream.download()

playsound.playsound(location)
