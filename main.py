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
            if os.path.exists("files/data.json") == False: # checks to see if the file is there (returns a bool)
                print(f"data.json not found, creating a new one")
                Initialize_JSON().initialize_json()
            elif os.path.exists("files/data.json") == True:
                print(f"JSON already initialized")
        case 2:
            try:
                if os.path.exists("files/data.json") == False: # checks to see if the file is there (returns a bool)
                    print(f"data.json not found, please Initialize")
                elif os.path.exists("files/data.json") == True:
                    Appending().appending()
            except ValueError:
                print("Please check the values you entered, age can only accept numbers")
        case 3:
            print("I haven't gotten to this point yet")
        case _:
            print("enter a valid number")
print("GOOD BYE")