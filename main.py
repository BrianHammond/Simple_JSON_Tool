import json
import datetime
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QSettings
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui


class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts

        #buttons
        self.button_create.clicked.connect(self.create_file) # used to create a new .csv file
        self.button_import.clicked.connect(self.import_file) # used to open a .csv file
        self.button_submit.clicked.connect(self.submit_file) # used to append to a .csv file

        #menu bar
        self.action_about.triggered.connect(self.show_about)
        self.action_about_qt.triggered.connect(self.about_qt)
        self.action_dark_mode.toggled.connect(self.dark_mode)

        #text fields
        self.name = self.line_name
        self.age = self.line_age
        self.title = self.line_title
        self.address1 = self.line_address1
        self.address2 = self.line_address2
        self.additional = self.line_information

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

    def import_file(self):
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
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

    def show_about(self):  # loads the About window
        self.about_window = AboutWindow(dark_mode=self.action_dark_mode.isChecked())
        self.about_window.show()

    def about_qt(self):
        QApplication.aboutQt()

    def closeEvent(self, event):  # Save settings when closing the app
        self.settings_manager.save_settings()  # Save settings using the manager
        event.accept()



class SettingsManager: # used to load and save settings when opening and closing the app
    def __init__(self, main_window):
        self.main_window = main_window
        self.settings = QSettings('settings.ini', QSettings.IniFormat)

    def load_settings(self):
        size = self.settings.value('window_size', None)
        pos = self.settings.value('window_pos', None)
        dark = self.settings.value('dark_mode')
        
        if size is not None:
            self.main_window.resize(size)
        if pos is not None:
            self.main_window.move(pos)
        if dark == 'true':
            self.main_window.action_dark_mode.setChecked(True)
            self.main_window.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    def save_settings(self):
        self.settings.setValue('window_size', self.main_window.size())
        self.settings.setValue('window_pos', self.main_window.pos())
        self.settings.setValue('dark_mode', self.main_window.action_dark_mode.isChecked())

class AboutWindow(QWidget, about_ui): # Configures the About window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)

        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())




if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
