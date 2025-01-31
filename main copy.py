# checks to see if the 'PyQT6' module is installed
try: 
    from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
    from PyQt6 import uic
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("PyQT6 module is not installed")
    import subprocess
    required_packages = ['PyQT6']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PyQt6 import uic
import json
import datetime

class UI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self) #load the UI file

        #buttons
        self.create_file_button.clicked.connect(self.create_file) # used to create a new .csv file
        self.select_button.clicked.connect(self.select_file) # used to open a .csv file
        self.submit_button.clicked.connect(self.submit_file) # used to append to a .csv file

        #menu bar
        self.actionAbout.triggered.connect(self.about)

    def about(self):
        self.window = QMainWindow()
        uic.loadUi("about.ui", self.window) #load the UI file
        self.window.show()

    def create_file(self):
        self.table.setRowCount(0)
        self.clear_all()
        self.filename = QFileDialog.getSaveFileName(self, 'create a new file', '', 'Data File (*.json)',)
        self.setWindowTitle(self.filename[0].split('/')[-1])

        json_string = '{"Employees":[]}'
        data = json.loads(json_string)

        try:
            with open(self.filename[0], "w") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
                json.dump(data, file, indent=4) # json.dump converts the dictionary into a json string, 'file' as the second argument and indent to create indentations
        except FileNotFoundError:
            pass

    def select_file(self):
        self.table.setRowCount(0)
        self.clear_all()
        self.filename = QFileDialog.getOpenFileName(self, 'create a new file', '', 'Data File (*.json)',)
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            with open(self.filename[0], "r+") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
                data = json.load(file)
                entry = 0
                for employee in data['Employees']:

                    self.table.insertRow(entry)
                    self.table.setItem(entry, 0, QTableWidgetItem(employee['Timestamp']))
                    self.table.setItem(entry, 1, QTableWidgetItem(employee['Name']))
                    self.table.setItem(entry, 2, QTableWidgetItem(employee['Age']))
                    self.table.setItem(entry, 3, QTableWidgetItem(employee['Title']))
                    self.table.setItem(entry, 4, QTableWidgetItem(employee['Address']['Address 1']))
                    self.table.setItem(entry, 5, QTableWidgetItem(employee['Address']['Address 2']))
                    self.table.setItem(entry, 6, QTableWidgetItem(employee['Misc'][0]))

                    print("")
                    print(f"Entry Number {entry}")
                    print(f"Timestamp: {employee['Timestamp']}")
                    print(f"Name: {employee['Name']}")
                    print(f"Age: {employee['Age']}")
                    print(f"Title: {employee['Title']}")
                    print(f"Address 1: {employee['Address']['Address 1']}")
                    print(f"Address 2: {employee['Address']['Address 2']}")
                    print(f"Misc: {employee['Misc'][0]}")
                    entry += 1
        
        except FileNotFoundError:
            pass

        self.submit_file

    def submit_file(self):
        self.current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
        self.timestamp = self.current_date
        self.name = self.name_edit.text()
        self.age = self.age_edit.text()
        self.title = self.title_edit.text()
        self.address1 = self.address1_edit.text()
        self.address2 = self.address2_edit.text()
        self.additional = self.additional_edit.text()

        row = self.table.rowCount()
        self.populate_table(row)
        

        self.employee = {
                            "Timestamp": self.timestamp,
                            "Name": self.name, 
                            "Age": self.age, 
                            "Title": self.title, 
                            "Address": {
                                        "Address 1": self.address1, 
                                        "Address 2": self.address2
                            },
                            "Misc":[
                                 self.additional
                            ]
                        }
        
        try:
            with open(self.filename[0], "r+") as file:
                file_content = json.load(file)
                file_content["Employees"].append(self.employee)
                file.seek(0)
                json.dump(file_content, file, indent=4)
        except AttributeError:
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")
        
        self.clear_all()
    
    def clear_all(self):
        self.name_edit.clear()
        self.age_edit.clear()
        self.title_edit.clear()
        self.address1_edit.clear()
        self.address2_edit.clear()
        self.additional_edit.clear()
    
    def populate_table(self, row):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(self.timestamp))
        self.table.setItem(row, 1, QTableWidgetItem(self.name))
        self.table.setItem(row, 2, QTableWidgetItem(self.age))
        self.table.setItem(row, 3, QTableWidgetItem(self.title))
        self.table.setItem(row, 4, QTableWidgetItem(self.address1))
        self.table.setItem(row, 5, QTableWidgetItem(self.address2))
        self.table.setItem(row, 6, QTableWidgetItem(self.additional))

# Show/Run app
if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    UIWindow = UI()
    UIWindow.show()
    sys.exit(app.exec())