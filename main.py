# Python file detection
# Python writing files (.txt, .json, .csv)

# writing modes = 'w' will write the txt_data and create a new file, or overwrite the txt_data if file already available  )
#                 'x' will fail to write if a file already exists
#                 'a' will append new text data
#

import os
from class_json import *

menu = ("""
1. Write new JSON
2. Appending to existing JSON     
3. Viewing JSON
0. Exit  
""")

folder = input("folder: ")
file = input("file: ") + ".json"
full_path = folder + "/" + file

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0:
            break
        
        case 1:
            if not os.path.isdir(folder):
                os.makedirs(folder)
            
            if not os.path.exists(full_path): # checks to see if the file is there (returns a bool)
                print(f"{file} not found, creating a new one")
            else:
                print(f"{full_path} already exists, will end to prevent accidental overwrite")
                break
                      
            Initialize_JSON(folder, file, full_path).initialize_json()
            try:
                Appending(folder, file, full_path).appending()
            except ValueError:
                print("Please check the values you entered, age can only accept numbers")
                
        case 2:
            if not os.path.exists(full_path): # checks to see if the file is there (returns a bool)
                print(f"{full_path} not found, please Initialize")
 
            try:    
                Appending(folder, file, full_path).appending()
            except ValueError:
                print("Please check the values you entered, age can only accept numbers")
        
        case 3:
            if not os.path.exists(full_path):
                print(f"{full_path} doesn't exist, please check or initialize a new one")
            elif os.path.exists(full_path):
                Viewing(folder, file, full_path).viewing()
        case _:
            print("enter a valid number")

print("GOOD BYE")