"""
load.py
~~~~~~~~

load.py  file is  foindation of my  project, basically  this 
file is connected to other three files inside of data-loader
folder. Also, this  folder will receive the data from ./data
folder and sends it to YOLO.
"""

# load packages
import torch
from torch.utils.data import random_split
from .augmentation import Augmentation
from .methods import Methods
import configs as get

# I am importing Augmentation
augmentation = Augmentation()

# I am importing methods
methods = Methods()


class Load:

    @staticmethod
    def __load_data():

        # load train images
        train_images = methods.load_images(
            path = get.path_to_processed_data, # location for train dataset
            transform = augmentation.transformation() # transformation method for import images
        )

        # load validation images
        validation_images = methods.load_images(
            path=get.path_to_processed_data,  # location for validation dataset
            transform=augmentation.transformation() # transformation method for import images
        )

        # load test images
        test_images = methods.load_images(
            path=get.path_to_processed_data,  # location for test dataset
            transform=augmentation.transformation() # transformation method for import images
        )

        # generate seed
        just_seed = torch.Generator().manual_seed(
            get.seed
        )

        # splitting them according to their indices
        train_indices, validation_indices, test_indices = random_split(
            train_images, # images
            lengths = [
                get.train_split, # 0.9
                get.validation_split, # 0.1
                get.test_split
            ],
            generator = just_seed # seed = 42
        )

        # make a subset for train data
        train_subset = methods.make_subset(
            train_images,  # src for subset
            indices=train_indices.indices,  # indices
        )

        # make a subset for validation data
        validation_subset = methods.make_subset(
            validation_images,  # src for subset
            indices=validation_indices.indices,  # indices
        )

        test_subset = methods.make_subset(
            test_images,  # src for subset
            indices=test_indices.indices,  # indices
        )
        

        # load the train dataset
        train_data = methods.load_dataset(
            train_subset,
            shuffle=True
        )

        # load the validation dataset
        validation_data = methods.load_dataset(
            validation_subset,
            shuffle=False
        )

        # load the test dataset
        test_data = methods.load_dataset(
            test_subset,
            shuffle=False
        )

        return train_data, validation_data, test_data

    @staticmethod
    def data_pipeline():

        train_data, validation_data, test_data = Load.__load_data()

        return train_data, validation_data, test_data