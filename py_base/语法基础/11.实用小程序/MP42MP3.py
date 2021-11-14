import os
from moviepy.editor import VideoFileClip
# MP4转MP3程序

def MP42MP3(inputpath):
    listdir = os.listdir(inputpath)

    for file in listdir:
        filepath = os.path.join(inputpath, file)
        video = VideoFileClip(filepath)

        list_filepath = list(filepath)
        if list_filepath[-1] == '4':
            list_filepath[-1] = '3'
            filepath = ''.join(list_filepath)
            print(filepath)
            audio = video.audio
            audio.write_audiofile(filepath)

if __name__ == '__main__':
    # videopath = "G:/children/高立新生物"
    # MP42MP3(videopath)
    pass