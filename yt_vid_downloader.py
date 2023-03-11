from pytube import YouTube, Playlist
from sys import argv

link = argv[1] #first command line you give in the program \\\ argv[0] returns name
#link = input("enter video link: ")

####single vid
yt = YouTube(link)

#rint("Title: ", yt.title)
#print("View: ", yt.views)

#yd = yt.streams.get_highest_resolution()

# ADD FOLDER HERE
#yd.download('./YTfolder') #creates folder if it doesnt exist


####playlist
p = Playlist(link)
for video in p.videos:
    video.streams.get_highest_resolution().download('./python tut complete')
    print(video.title)
print("finish")
    