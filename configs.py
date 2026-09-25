"""
configs.py
~~~~~~~~~~~

This file will store all static settings of the project. 
As an example, I can say that - here I will store epoch, 
learning rate, paths and so on.
"""

# path settings
video_data = "./data/raw/video/day_2.avi"
ground_truth = "./data/raw/ground_truth"
frame_names = "./data/raw/frame_names"
path_to_processed_data = "./data/processed"

# reproducibility
seed = 42

# split ratios (must sum to 1.0)
train_split = 0.8
validation_split = 0.1
test_split = 0.1

mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
batch_size = 16
num_workers = 2