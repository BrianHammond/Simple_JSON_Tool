# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#

import json

class Files:
    def __init__(self):
        self.folder = "files"
        self.file = "data.json"
        self.full_path = self.folder + "/" + self.file

class Initialize_JSON():
    def initialize_json(self):
        json_string = '{"employees":[]}'
        data = json.loads(json_string)
        with open(Files().full_path, "w") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
            json.dump(data, file, indent=4) # json.dump converts the dictionary into a json string, 'file' as the second argument and indent to create indentations
            print(f"json file was created")

class JSON:
    def __init__(self):
        self.name = input("Enter employee name: ")
        self.age = int(input("Enter employee age: "))
        self.title = input("Enter employee title: ")
        self.misc = input("Enter miscellaneous information: ")

        self.employee = {
                            "name": self.name, 
                            "age": self.age, 
                            "title": self.title, 
                            "misc": [self.misc]
                        }

class Appending():
    def appending(self):
        with open(Files().full_path, "r+") as file:
            file_content = json.load(file)
            file_content["employees"].append(JSON().employee)
            file.seek(0)
            json.dump(file_content, file, indent=4)

class Reading():
    def reading(self):
        with open(Files().full_path) as file:
            data = json.load(file)
        for employee in data['employees']:
            print(employee)