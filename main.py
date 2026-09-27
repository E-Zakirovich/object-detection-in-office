"""
main.py
~~~~~~~

I need this file in order to run the whole project. 
This file will connect all methods each other.
"""

class Main:

    def __init__(self):
        self.information = "Office, employee tracker"

    def run(self):
        print(self.information)

project = Main()

project.run()