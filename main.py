"""
main.py
~~~~~~~

I need this file in order to run the whole project. 
This file will connect all methods each other.
"""

from src.methods import Methods
from src.data_loader.frame_maker import FrameMaker
from src.data_loader.label_maker import LabelMaker
import configs as get
import os

# I will call all classes that I imported
methods = Methods()
frame_maker = FrameMaker()
label_maker = LabelMaker()

class Main:

    def __init__(self):
        self.information = "Office, employee tracker"

    def run(self):
        
        print(self.information)

        
        
        print("data found, proceeding...")



project = Main()

project.run()