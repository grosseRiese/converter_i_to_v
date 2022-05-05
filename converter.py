import numpy as np
import os 
from os.path import isfile, join 
from moviepy.editor import *

def my_imgs_to_video():
    frame_array = []
    pathIn = 'myimages/'
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    for i in range(len(files)):
        myImg = ImageClip(pathIn + files[i]).set_duration(4)
        frame_array.append(myImg)

    video_clip = concatenate_videoclips(frame_array, method='compose')
    video_clip.write_videofile("video_outputII.mp4", fps=25, remove_temp=True, codec="libx264", audio_codec="aac")
my_imgs_to_video()
