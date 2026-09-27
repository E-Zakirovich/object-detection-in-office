"""
frame_maker.py
~~~~~~~~~~~~~~~

This method will help me to get frames from video data. Main reason is this.
"""

# import libraries
import cv2 as cv
from pathlib import Path

class FrameMaker:
    def __init__(self):
        self.class_name = "Frame Maker"

    # I need method that can read a video path and will make a frames according to video data
    def make_frames(self, path : str, destination : str, start_number : int):

        video = cv.VideoCapture(path) # open the image

        output_path = Path(destination)  # I need to make a path for destination

        frame_number = start_number # counter for frames

        # need a loop in order to touch each frame
        while True:
            
            success, frame = video.read() # success is status of the frame, if sucess is false -> end of video or there is a problem, frame is just a data

            # following logic will help me to to finish the loop 
            if not success:
                break

            frame_path = output_path / f"frame_{frame_number:06d}.jpg" # process of making path for frame
            cv.imwrite(str(frame_path), frame) # storing process to destination provided by user

            frame_number += 1 # count frames

        video.release() # release will help me to clode the vide.

        # print the result, 
        print(f"Extracted {frame_number} frames.")