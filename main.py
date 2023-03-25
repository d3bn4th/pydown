from pytube import YouTube
import os
from youtubesearchpython import VideosSearch

# WELCOME MESSAGE
print("\t \t Welcome!!\n")
print("\t To YouTube Downloader\n")

#INPUT LINK
vid_name = input("Link : ")
videosSearch = VideosSearch(vid_name, limit = 1)
videoResult = videosSearch.result();
# print(videoResult)

link = videoResult['result'][0]['link']
print(link)

# link = input("Enter the link \n>>")
yt = YouTube(link)
file_type = input("\tAudio- a or Video- v \n>> ")

# Main Downloading Function
# downloading the file from youtube.com
def down(file_type):
    if file_type == "a":
        # To get the audio format of the file
        ys = yt.streams.filter(only_audio=True)
        print(yt.title)
        print("Downloading......")
        ys[0].download()
        print("Download completed!!")

    if file_type == "v":
        # To get the highest resolution streams
        ys = yt.streams.get_highest_resolution()
        print(yt.title)
        print("Downloading......")
        ys.download()
        print("Download completed!!")

    if file_type == "no":
        return

# To delete the file downloaded
def delete_file_function():

    delete_file = input("\tDo you want to delete the file(yes/no) \n>> ")
    if delete_file == "yes":
        os.remove(file_location)
        print("File :"+file_title+" Deleted")
    if delete_file == "no":
        print("File :" + file_title+ " Saved \n" + "Location: "+file_location)


# Driver code

#download function call
down(file_type)

# getting the title of the video
file_title = yt.title
file_title = file_title.replace(".", "")
file_title = file_title.replace("'", "")
file_title = file_title.replace('"', "")

# getting the current working directory
cwd = os.getcwd()
file_location = cwd +'\\'+file_title+'.mp4'
print(file_location)

#to play the file
os.startfile(file_location)

# to delete the file
delete_file_function()

# Closing the Program
print("\tPress Enter to close the program.")
input()
print("\tThanks for using our app")
