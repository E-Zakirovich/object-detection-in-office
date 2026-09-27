"""
main.py
~~~~~~~

I need this file in order to run the whole project. 
This file will connect all methods each other.
"""

from src.methods import Methods
import configs as get
import os

# I will call all classes that I imported
methods = Methods()

class Main:

    def __init__(self):
        self.information = "Office, employee tracker"

    def run(self):
        print(self.information)
        if not os.path.isdir(get.video_data):
            print("I am making folders for dataset. Please provide data after folder creation part.")
            methods.make_folders()
        elif not os.listdir(get.video_data):
            print("please provide train data to train the model.")
            return
        else:
            print("data found, proceeding...")
        

project = Main()

project.run()