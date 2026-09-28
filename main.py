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
        self.information = "Office, employee tracker \n \n"

    def run(self):
        
        print(self.information)

        status = methods.initialize_the_program()

        if not status:
            return
        
        print("data folder is created, raw data is also available.")
        


project = Main()

project.run()