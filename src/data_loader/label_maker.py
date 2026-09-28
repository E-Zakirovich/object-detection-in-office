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
    def __init__(self):
        self.name_of_the_file = "Label maker"

    def make_labels(self, destination : str, frame_path : str, src : str,) -> None:
        labels = methods.get_names(frame_path)
        labels = [e for e in labels if e != ".DS_Store"]        # remove ds store
        labels = sorted(e.split(".")[0] for e in labels) 

        ground_truth = loadmat(src) # ground truth data

        data = ground_truth["labels"][0]
        l = len(data)


        for i in range(l):

            annotations = []                       # [[], [], []] for this frame

            for person in data[i]:                 # loop over the 3 slots
                x, y, wdth, hght, identification = person.astype(float)

                # empty padding slot, skip it
                if wdth == 0 and hght == 0:
                    continue

                # yolo format
                x_center = x + wdth / 2
                y_center = y + hght / 2

                # squeeze to 0..1
                x_center /= get.width
                y_center /= get.height
                wdth /= get.width
                hght /= get.height

                annotations.append([
                    int(identification),
                    x_center,
                    y_center,
                    wdth,
                    hght,
                ])

            methods.write(
                annotations,
                labels[i] + ".txt",
                destination
            )
        # for i in range(l):

        #     # get the values of data list
        #     x = data[i][0]
        #     y = data[i][1]
        #     wdth = data[i][2]
        #     hght = data[i][3]
        #     identification = data[i][4]

        #     # make new cordinates, yolo format
        #     x_center = x + wdth / 2
        #     y_center = y + hght / 2

        #     # squeze it 
        #     x_center /= get.width
        #     y_center /= get.height

        #     wdth /= get.width
        #     hght /= get.height

        #     annotations = [
        #         identification, 
        #         x_center, 
        #         y_center, 
        #         wdth, 
        #         hght, 
        #     ]

            # methods.write(
            #     annotations, 
            #     labels[i] + ".txt",
            #     destination
            # )