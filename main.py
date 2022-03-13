from ast import Return
from pytube import YouTube
import os

link = input("Enter the link: ")
yt = YouTube(link)
type = int(input("Audio - 1 or Audio/Video - 2 : "))

# for desktop
def down(type):
    if type == 1:
        # To get the highest resolution streams
        ys = yt.streams.filter(only_audio=True)
        print("Downloading......")
        ys[0].download()
        print("Download completed!!")

    if type == 2:
        # To get the highest resolution streams
        ys = yt.streams.get_highest_resolution()
        print("Downloading......")
        ys.download()
        print("Download completed!!")
    if type == 3:
        return

down(type)

file_title = yt.title
print(file_title)

# getting the current working directory
cwd = os.getcwd()
file_location = cwd +'\\'+file_title+'.mp4'
print(file_location)
os.startfile(file_location)

delete_file = input("Do you want to delete the file(YES) \n>> ")
if delete_file == "YES":
    os.remove(file_location)
    print("File "+file_title+" Deleted")
if delete_file == "NO":
    print("File" + file_title+ "Saved \n" + "Location: "+file_location)

