# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#

import os
from class_json import *

menu = ("""
1. Initialize JSON
2. Writing JSON     
3. Reading JSON
0. Exit  
""")

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0:
            break
        case 1:
            if not os.path.isdir(Files().folder):
                print(f"{Files().folder} not found, creating folder")
                os.makedirs(Files().folder)

            if not os.path.exists(Files().full_path): # checks to see if the file is there (returns a bool)
                print(f"data.json not found, creating a new one")
                Initialize_JSON().initialize_json()
            elif os.path.exists(Files().full_path):
                print(f"JSON already initialized")
        case 2:
            try:
                if not os.path.exists(Files().full_path): # checks to see if the file is there (returns a bool)
                    print(f"data.json not found, please Initialize")
                elif os.path.exists(Files().full_path):
                    Appending().appending()
            except ValueError:
                print("Please check the values you entered, age can only accept numbers")
        case 3:
            if not os.path.exists(Files().full_path):
                print(".json doesn't exist, please check or initialize a new one")
            elif os.path.exists(Files().full_path):
                Reading().reading()
        case _:
            print("enter a valid number")
print("GOOD BYE")