
'''
# for desktop
def down(type):
    if type == 1:
        # To get the highest resolution streams
        ys = yt.streams.filter(only_audio=True)
        print("Downloading......")
        ys[0].download(r'C:\Users\thicc\Student Dropbox (Old)\Arihant Debnath\My PC (Thinkpad)\Desktop')
        print("Download completed!!")

    if type == 2:
        # To get the highest resolution streams
        yt.streams.get_highest_resolution().download()
        print("Downloading......")
        ys.download(r'C:\Users\thicc\Student Dropbox (Old)\Arihant Debnath\My PC (Thinkpad)\Desktop')
        print("Download completed!!")
down(type)
# Title of video
print("Title: ", yt.title)

# Number of Views of video
print("Number of views: ", yt.views)

# Description of video
print("Description of the video: ", yt.description)

# Rating
print("Ratings: ", yt.rating)

# printing all the available streams
print(yt.streams.filter(progressive = True))'''
