"""
label_maker.py
~~~~~~~~~~~~~~~

this method will help me to make labels for images. I mean 
I need this one to make my dataset to fit YOLO format.
"""

# load libraries and classes
from pathlib import Path
from scipy.io import loadmat
from src.methods import Methods
import configs as get

# I am gonna call all classes
methods = Methods()

class LabelMaker:
    def __init__(self, path):
        self.labels = methods.get_names(path) # I get all frame names, in order to match image and labels names.
        self.path = path

    def make_labels(self, destination : str) -> None:
        labels = [element.split(".")[0] for element in self.labels]

        ground_truth = loadmat(self.path)

        data = ground_truth["labels"][0]
        l = len(data)


        for i in range(l):

            # get the values of data list
            x = data[i][0]
            y = data[i][1]
            wdth = data[i][2]
            hght = data[i][3]
            identification = data[i][4]

            # make new cordinates, yolo format
            x_center = x + wdth / 2
            y_center = y + hght / 2

            # squeze it 
            x_center /= get.width
            y_center /= get.height

            wdth /= get.width
            hght /= get.height

            annotations = [
                identification, 
                x_center, 
                y_center, 
                wdth, 
                hght, 
            ]

            methods.write(
                annotations, 
                labels[i] + ".txt",
                destination
            )