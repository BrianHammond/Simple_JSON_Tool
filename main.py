import json
import datetime
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_window import AboutWindow

class MainWindow(QMainWindow, main_ui):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = QSettings('settings.ini', QSettings.IniFormat)
        self.loadSettings()

        #buttons
        self.create_file_button.clicked.connect(self.create_file) # used to create a new .csv file
        self.select_button.clicked.connect(self.select_file) # used to open a .csv file
        self.submit_button.clicked.connect(self.submit_file) # used to append to a .csv file

        #menu bar
        self.actionAbout.triggered.connect(self.show_about)
        self.actionAboutQt.triggered.connect(self.about_qt)
        self.actionDarkMode.toggled.connect(self.dark_mode)

        #text fields
        self.name = self.name_edit
        self.age = self.age_edit
        self.title = self.title_edit
        self.address1 = self.address1_edit
        self.address2 = self.address2_edit
        self.additional = self.additional_edit

    def create_file(self):
        self.table.setRowCount(0)
        self.clear_fields()
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
        self.clear_fields()
        self.filename = QFileDialog.getOpenFileName(self, 'create a new file', '', 'Data File (*.json)',)
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            with open(self.filename[0], "r+") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
                data = json.load(file)
                row = 0
                self.current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
                timestamp = self.current_date

                for employee in data['Employees']:
                    name = employee['Name']
                    age = employee['Age']
                    title = employee['Title']
                    address1 = employee['Address']['Address 1']
                    address2 = employee['Address']['Address 2']
                    additional = employee['Misc'][0]

                    self.populate_table(row, timestamp, name, age, title, address1, address2, additional)
        
        except FileNotFoundError:
            pass

        self.submit_file

    def submit_file(self):
        self.current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
        timestamp = self.current_date
        name = self.name.text()
        age = self.age.text()
        title = self.title.text()
        address1 = self.address1.text()
        address2 = self.address2.text()
        additional = self.additional.text()

        row = self.table.rowCount()

        self.populate_table(row, timestamp, name, age, title, address1, address2, additional)
        
        self.employee = {
                            "Timestamp": timestamp,
                            "Name": name, 
                            "Age": age, 
                            "Title": title, 
                            "Address": {
                                        "Address 1": address1, 
                                        "Address 2": address2
                            },
                            "Misc":[
                                 additional
                            ]
                        }
        
        try:
            with open(self.filename[0], "r+") as file:
                file_content = json.load(file)
                file_content["Employees"].append(self.employee)
                file.seek(0)
                json.dump(file_content, file, indent=4)
        except AttributeError:
            self.clear_fields()
            self.table.setRowCount(0)
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")
        
        self.clear_fields()
    
    def clear_fields(self):
        self.name.clear()
        self.age.clear()
        self.title.clear()
        self.address1.clear()
        self.address2.clear()
        self.additional.clear()
    
    def populate_table(self, row, timestamp, name, age, title, address1, address2, additional):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(timestamp))
        self.table.setItem(row, 1, QTableWidgetItem(name))
        self.table.setItem(row, 2, QTableWidgetItem(age))
        self.table.setItem(row, 3, QTableWidgetItem(title))
        self.table.setItem(row, 4, QTableWidgetItem(address1))
        self.table.setItem(row, 5, QTableWidgetItem(address2))
        self.table.setItem(row, 6, QTableWidgetItem(additional))

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self):
        self.about_window = AboutWindow()
        self.about_window.show()

    def about_qt(self):
        QApplication.aboutQt()

    def closeEvent(self, event): #settings will save when closing the app
        self.settings.setValue('window_size', self.size())
        self.settings.setValue('window_pos', self.pos())
        self.settings.setValue('dark_mode', self.actionDarkMode.isChecked())
        event.accept()

    def loadSettings(self): #settings will load when opening the app
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        if size is not None:
            self.resize(size)
        if pos is not None:
            self.move(pos)
        if dark == 'true':
            self.actionDarkMode.setChecked(True)
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
