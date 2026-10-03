"""
main.py
~~~~~~~

I need this file in order to run the whole project. 
This file will connect all methods each other.
"""

from src.methods import Methods
from src.data_loader.label_maker import LabelMaker
from src.data_loader.frame_maker import FrameMaker
from src.train.train import Train
import configs as get
import os

# I will call all classes that I imported
methods = Methods()
labels = LabelMaker()
frames = FrameMaker()
train = Train(
    "configurations.yaml",
    "yolo11n.pt"
)

class Main:

    def __init__(self):
        self.information = "Office, employee tracker \n \n"

    def run(self):
        
        print(self.information)

        status = methods.initialize_the_program()

        if not status:
            return
        
        print("data folder is created, raw data is also available.")

        # get labels of files in
        labels_of_videos = methods.get_names(get.video_data)
        labels_of_ground_truth = methods.get_names(get.ground_truth)

        l = len(labels_of_ground_truth)

        for i in range(l):
            if i <= 16:
                path_v = get.processed_train_images + "/" + "day" + str(i + 1)
                path_l = get.processed_train_labels + "/" + "day" + str(i + 1)

            elif i > 16 and i <= 18:
                path_v = get.processed_validation_images + "/" + "day" + str(i + 1)
                path_l = get.processed_validation_labels + "/" + "day" + str(i + 1)
            elif i > 18 and i <= 20:
                path_v = get.processed_test_images + "/" + "day" + str(i + 1)
                path_l = get.processed_test_labels + "/" + "day" + str(i + 1)

            os.makedirs(path_v, exist_ok=True)
            os.makedirs(path_l, exist_ok=True)

            frames.make_frames(
                get.video_data + "/" + labels_of_videos[i],
                path_v,
                1
                )

            labels.make_labels(path_l, path_v, get.ground_truth + "/" + labels_of_ground_truth[i])

        # start training
        
        train.run()

project = Main()

project.run()