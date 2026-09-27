"""
methods.py
~~~~~~~~~~

I need this file to write all methods that used inside of 
other codebases. I just wanna  avoid to repeat write same
process for different operations.
"""

import os
import configs as get
from src.data_loader.frame_maker import FrameMaker
from src.data_loader.label_maker import LabelMaker

# I am gonna load all imported classes here
frame_maker = FrameMaker()
label_maker = LabelMaker()

class Methods:
    def __init__(self):
        self.name = "Office, employee detection"

    # when I upload the code to github, data  folder will be  skipped because of .gitignore
    # thats why, I made a method to make a folder for dataset. Just save time in the future
    def make_folders(self):
        # foder creation part of the project
        os.makedirs(get.processed_train_images, exist_ok=True) # create folder for train images
        os.makedirs(get.processed_train_labels, exist_ok=True) # create folder for train labels
        os.makedirs(get.processed_validation_images, exist_ok=True) # create folder for validation images
        os.makedirs(get.processed_validation_labels, exist_ok=True) # create folder for validation labels
        os.makedirs(get.processed_test_images, exist_ok=True) # create folder for test images
        os.makedirs(get.processed_test_labels, exist_ok=True) # create folder for test labels
        os.makedirs(get.ground_truth, exist_ok=True) # create folder for groud truth
        os.makedirs(get.video_data, exist_ok=True) # create folder for video data

    # following method will help me to get all file names according to given path otherwise empty list
    def get_names(self, path : str) -> list[str]:

        # i need a list to store file names
        file_names = os.listdir(path)

        # there is a trash file inside of folder, so i need to delete it
        if ".DS_Store" in file_names:
            file_names.remove(".DS_Store")

        # return the result 
        return file_names

    # this folder will help me to initialize folders if it is not existed
    def initialize_the_program(self) -> bool:

        folder = os.path.isdir(get.data) # get existance status 

        # checking
        if not folder:
            print("I am creating data folder.")
            self.make_folders()

        # check the existance of files inside of ground truth or videos folder
        ground_truth = len(os.listdir(get.ground_truth))
        videos = len(os.listdir(get.video_data))

        # logic
        if ground_truth != videos:
            print("Unfortantely, you missed some files in ground truth or videos folder. Please check the data.")
            return False

        elif ground_truth == 0:
            print("Please, provide ground truth data.")
            return False

        elif videos == 0:
            print("Please, provide video data.")
            return False

        return True