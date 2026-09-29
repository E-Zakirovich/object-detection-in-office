"""
train.py
~~~~~~~~~

With a help of train.py file, I will train the model with YOLO,
using my handmade data pipeline.
"""

from ultralytics import YOLO
import torch
import configs as get

class Train:

    def __init__(self, data_yaml, model_path):
        self.device = "GPU" if torch.cuda.is_available() else "CPU"
        self.data_yaml = data_yaml
        self.model_path = model_path
        self.model = None

    # following method will help me to load the model according to its model path
    def load_model(self):
        if self.model_path:
            print("YOLO model is loading ...")
            self.model = YOLO(self.model_path)

    def run(self):
        ...