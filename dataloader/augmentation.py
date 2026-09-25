"""
augmentation.py
~~~~~~~~~~~~~~~~

This file is also important as other files. With a help of this file, 
I can make a tensors and normalization operation for video frames to 
train artificial intelligence model.
"""

# load packages
from torchvision import transforms
import configs as get


class Augmentation:
    # I need a static method, no need to return any data or something, just a method to use in augmentation part
    @staticmethod
    def transformation():

        # transformation code for validation and test data
        result = transforms.Compose([


            # make a tensor from imported image
            transforms.ToTensor(),

            # normalization part
            transforms.Normalize(
                mean = get.mean, # mean
                std = get.std # std
            )
        ])

        # returning the result
        return result