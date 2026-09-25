"""
main.py
~~~~~~~~

With this file, I can be able to run the whole project at once.
Basically, it connected to data loader, train and test fodlers
at the same time.
"""

from dataloader.load_video import LoadVideo
from dataloader.load import Load
import configs as get
import os

# I am calling classess
frame_maker = LoadVideo(get.video_data, get.path_to_processed_data)


def main():

    # check, is there any data inside of processed folder, if yes go to pipeline, otherwise make frames and then go to data pipeline
    total_files : int = os.listdir(get.path_to_processed_data)
    if len(total_files) == 0:
        # I am making frames from videos
        print("I am making frames right now")
        n = frame_maker.make_frames()
        print(f"Saved {n} frames")

    

    



if __name__ == "__main__":
    main()