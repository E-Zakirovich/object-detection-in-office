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
        self.device = self._pick_device()
        self.data_yaml = data_yaml
        self.model_path = model_path
        self.model = None

    @staticmethod
    def _pick_device():
        if torch.cuda.is_available():
            return 0
        if torch.backends.mps.is_available():
            return "mps"
        return "cpu"

    # following method will help me to load the model according to its model path
    def load_model(self):

        if not self.model_path:
            raise ValueError("model_path is empty, e.g. 'yolo26n.pt'")

        print(f"Loading {self.model_path} ...")
        self.model = YOLO(self.model_path)

    def run(self):
        if self.model is None:
            self.load_model()

        self.model.train(
            data = self.data_yaml,
            epochs = get.epochs,
            batch = get.batch,
            device = self.device,
            patience = get.patience,
            workers = get.num_workers,
            imgsz = get.width
        )