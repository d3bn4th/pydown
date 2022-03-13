from pytube import YouTube
import os

link = input("Enter the link /n>>")
yt = YouTube(link)
file_type = input("Audio- a or Video- v \n>> ")

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

# delete the file
def delete_file_function():
    # delete file
    delete_file = input("Do you want to delete the file(y/n) \n>> ")
    if delete_file == "y":
        os.remove(file_location)
        print("File :"+file_title+" Deleted")
    if delete_file == "n":
        print("File :" + file_title+ " Saved \n" + "Location: "+file_location)


# Driver code

#downloading the file
down(type)

# getting the title of the video
file_title = yt.title

# getting the current working directory
cwd = os.getcwd()
file_location = cwd +'\\'+file_title+'.mp4'
print(file_location)

#to play the file
os.startfile(file_location)

# to delete the file
delete_file_function()