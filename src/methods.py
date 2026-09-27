"""
methods.py
~~~~~~~~~~

I need this file to write all methods that used inside of 
other codebases. I just wanna  avoid to repeat write same
process for different operations.
"""

import os
import configs as get

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