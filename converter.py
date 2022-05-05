import numpy as np
import os 
from os.path import isfile, join 
from moviepy.editor import *
from PIL import Image

def my_imgs_to_video():
    frame_array = []
    pathIn = 'myimages/'
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    for i in range(len(files)):
        myImg = ImageClip(pathIn + files[i]).set_duration(4)
        frame_array.append(myImg)

    video_clip = concatenate_videoclips(frame_array, method='compose')
    video_clip.write_videofile("myvideos/video_outputII.mp4", fps=25, remove_temp=True, codec="libx264", audio_codec="aac")
#my_imgs_to_video()

def resize_img():
    image = Image.open('myimages/25.jpeg')
    new_image = image.resize((1920, 1920))
    new_image.save('252.jpeg')  
    image = Image.open('myimages/28.jpeg')
    new_image = image.resize((1920, 1920))
    new_image.save('282.jpeg')
#resize_img()

def concat_videos_fls():
    video_array = []
    VpathIn = 'myvideos/'
    Vfiles = [f for f in os.listdir(VpathIn) if isfile(join(VpathIn, f)) ]

    #print(f"V-files: {Vfiles}")

    for i in range(len(Vfiles)):
        myvideo = VideoFileClip(VpathIn + Vfiles[i])
        #print(myvideo)
        video_array.append(myvideo)
    
    final_video= concatenate_videoclips(video_array,method='compose')
    final_video.write_videofile("myvideos/final_video.mp4")
concat_videos_fls()