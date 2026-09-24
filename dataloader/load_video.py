"""
load_video.py
~~~~~~~~~~~~~~

This file will help me to load the vide data to augmentation process. 
Basically, it will read  video data and  make frames. Then all frames
sent to  augmentations.py file to process. I will also use methods.py 
file to  load some important  methods. All methods  written inside of 
methods, but this file will use combinations of methods that can give 
me desired output.
"""

# import packages 
import cv2 as cv
import os

class LoadVideo:
    def __init__(self, data_path : str, out_dir : str):
        self.path = data_path
        self.out_dir = out_dir

    # lets write a method to load the video and makes frames from images
    def make_frames(self):

        # I need a variable to store vide capturer
        video : cv = cv.VideoCapture(self.path)
        current_frame : int = 0

        # check the availability of the photo
        if not video.isOpened():
            raise FileNotFoundError(f"Cannot open video: {self.path}")

        # need a loop to reach each frames
        while True:
            # status gonna be bool, frame gonna be image data
            status, frame = video.read()

            # if there is no problem, loop will continue. Also, loop will step when video reaches the end status gonna be false
            if not status:
                break

            # need to create name and also path to new data
            name = os.path.join(self.out_dir, f"frame_{current_frame:06d}.jpg")

            # write the data
            cv.imwrite(name, frame)

            current_frame += 1

        video.release()
        return current_frame