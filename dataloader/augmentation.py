"""
augmentation.py
~~~~~~~~~~~~~~~~

This file is also important as other files. With a help of this file, 
I can make a tensors and normalization operation for video frames to 
train artificial intelligence model.
"""

# load packages
from torchvision import transforms
import configs


class Augmentation:
    # I need a static method, no need to return any data or something, just a method to use in augmentation part
    @staticmethod
    def transformation():

        # transformation code for validation and test data
        result = transforms.Compose([

            # change the size of the image
            transforms.Resize(

                (
                    configs.image_size, # amount
                    configs.image_size # amount
                )
            ),

            # make a tensor from imported image
            transforms.ToTensor(),

            # normalization part
            transforms.Normalize(
                mean = configs.mean, # mean
                std = configs.std # std
            )
        ])

        # returning the result
        return result