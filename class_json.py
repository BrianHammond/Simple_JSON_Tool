# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#

import os
import json

class Misc:
    def __init__(self, folder, file, full_path):
        self.folder = folder
        self.file = file
        self.full_path = full_path

class Initialize_JSON(Misc):
    def initialize_json(self):
        json_string = '{"Employees":[]}'
        data = json.loads(json_string)
        with open(self.full_path, "w") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
            json.dump(data, file, indent=4) # json.dump converts the dictionary into a json string, 'file' as the second argument and indent to create indentations

class JSON:
    def __init__(self):
        self.name = input("Enter employee name: ")
        self.age = int(input("Enter employee age: "))
        self.title = input("Enter employee title: ")
        self.address1 = input("Enter Address 1: ")
        self.address2 = input("Enter Address 2: ")
        self.misc = input("Enter any additional information: ")

        self.employee = {
                            "Name": self.name, 
                            "Age": self.age, 
                            "Title": self.title, 
                            "Address": {
                                        "Address 1": self.address1, 
                                        "Address 2": self.address2
                            },
                            "Misc":[
                                 self.misc
                            ]
                        }

class Appending(Misc):
    def appending(self):
        with open(self.full_path, "r+") as file:
            file_content = json.load(file)
            file_content["Employees"].append(JSON().employee)
            file.seek(0)
            json.dump(file_content, file, indent=4)

class Viewing(Misc):
    def viewing(self):
        with open(self.full_path) as file:
            data = json.load(file)
            e = 1
            for employee in data['Employees']:
                print("")
                print(f"Entry Number {e}")
                print(f"Name: {employee['Name']}")
                print(f"Age: {employee['Age']}")
                print(f"Title: {employee['Title']}")
                print(f"Address 1: {employee['Address']['Address 1']}")
                print(f"Address 2: {employee['Address']['Address 2']}")
                print(f"Misc: {employee['Misc'][0]}")
                e += 1
