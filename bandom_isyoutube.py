import pytube
url = input("Enter youtube video URL:\n")
youtube = pytube.YouTube(url)
min = (youtube.length) // 60
sec = (youtube.length) - min*60
print(sec)
print("Title:", ((youtube).title), "\nLenght:",min,":",sec)
print("Are you sure you want to download this video [Y/N]?")
anw = input(":")
if anw == ("Y"):
    print("Downloading the video")
    video = youtube.streams.first()
    video.download()
    print("Done")
else:
    print("Not downloading")     