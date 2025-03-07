import json
import datetime
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QSettings, Qt
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Form as about_ui

class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts

        #buttons
        self.button_add.clicked.connect(self.add_info) # write to .json
        self.button_update.clicked.connect(self.update_info) # update .json
        self.button_delete.clicked.connect(self.delete_entry)

        #menu bar
        self.action_new.triggered.connect(self.new_file)
        self.action_open.triggered.connect(self.open_file)
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

    def new_file(self):
        self.filename = QFileDialog.getSaveFileName(self, 'create a new file', '', 'Data File (*.json)',)
        
        if not self.filename[0]:
            return  # Do nothing if no file is selected
            
        self.initialize_table()

        self.setWindowTitle(self.filename[0].split('/')[-1])

        json_string = '{"Employees":[]}'
        data = json.loads(json_string)

        try:
            with open(self.filename[0], "w") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
                json.dump(data, file, indent=4) # json.dump converts the dictionary into a json string, 'file' as the second argument and indent to create indentations
        except FileNotFoundError:
            pass

    def open_file(self):
        self.clear_fields()
        
        self.filename = QFileDialog.getOpenFileName(self, 'create a new file', '', 'Data File (*.json)',)

        if not self.filename[0]:
            return  # Do nothing if no file is selected
            
        self.initialize_table()
            
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            with open(self.filename[0], "r+") as file: # this will write the txt_data and create a new file, or overwrite the txt_data if file already available 
                data = json.load(file)
                row = 0
                self.current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
                timestamp = self.current_date

                for employee in data['Employees']:

                    if not employee.get("Timestamp"): # If the timestamp is missing or blank, generate a new one
                        employee["Timestamp"] = timestamp  # Set it to the current timestamp if it's missing

                    name = employee['Name']
                    age = employee['Age']
                    title = employee['Title']
                    address1 = employee['Address']['Address 1']
                    address2 = employee['Address']['Address 2']
                    additional = employee['Misc'][0]

                    self.populate_table(row, employee["Timestamp"], name, age, title, address1, address2, additional)
                    row += 1
        
        except FileNotFoundError:
            pass

    def add_info(self):
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

    def update_info(self):
        selected_row = self.table.currentRow()  # Get the selected row in the table
        if selected_row == -1:  # If no row is selected, show a warning message
            QMessageBox.warning(self, "No Selection", "Please select a row to update.")
            return

        # Get the updated values from the table
        timestamp = self.table.item(selected_row, 0).text()  # Timestamp (no change)
        name = self.table.item(selected_row, 1).text()
        age = self.table.item(selected_row, 2).text()
        title = self.table.item(selected_row, 3).text()
        address1 = self.table.item(selected_row, 4).text()
        address2 = self.table.item(selected_row, 5).text()
        additional = self.table.item(selected_row, 6).text()

        # Updated employee data
        updated_employee = {
            "Timestamp": timestamp,
            "Name": name,
            "Age": age,
            "Title": title,
            "Address": {
                "Address 1": address1,
                "Address 2": address2
            },
            "Misc": [additional]
        }

        # Now let's check if we're really updating the file content.
        try:
            with open(self.filename[0], "r+") as file:
                file_content = json.load(file)
                print("File content before update:", file_content)  # Debugging: Log before update

                # Find the employee with the same timestamp (assuming Timestamp is unique)
                for idx, employee in enumerate(file_content["Employees"]):
                    if employee["Timestamp"] == timestamp:
                        print(f"Found matching employee: {employee}")  # Debugging: Log found employee
                        file_content["Employees"][idx] = updated_employee  # Update the employee data
                        print(f"Updated employee: {updated_employee}")  # Debugging: Log updated employee
                
                # If no matching employee was found
                if not any(employee["Timestamp"] == timestamp for employee in file_content["Employees"]):
                    print(f"No employee with Timestamp {timestamp} found.")  # Debugging: Log if no match

                # Overwrite the file with updated data
                file.seek(0)  # Move to the beginning of the file
                file.truncate(0)  # Truncate the file content
                json.dump(file_content, file, indent=4)
                print("File content after update:", file_content)  # Debugging: Log after update
            
            QMessageBox.information(self, "Success", "Employee data updated successfully.")
        except Exception as e:
            print(f"Error updating file: {str(e)}")  # Debugging: Log any error
            QMessageBox.warning(self, "Error", f"Failed to update file: {str(e)}")

        self.clear_fields()

        self.table.resizeColumnsToContents()

    def delete_entry(self):
        # Get the selected row in the table
        selected_row = self.table.currentRow()
        
        # If no row is selected, show a warning message
        if selected_row == -1:
            QMessageBox.warning(self, "No Selection", "Please select a row to delete.")
            return

        # Get the timestamp of the selected row (it's in the first column)
        timestamp = self.table.item(selected_row, 0).text()

        # Confirm the deletion
        confirm = QMessageBox.question(self, "Confirm Deletion", 
                                    f"Are you sure you want to delete the entry with Timestamp: {timestamp}?",
                                    QMessageBox.Yes | QMessageBox.No)
        if confirm == QMessageBox.No:
            return

        # Remove the entry from the JSON file
        try:
            with open(self.filename[0], "r+") as file:
                file_content = json.load(file)

                # Find the employee with the same timestamp and remove it
                file_content["Employees"] = [employee for employee in file_content["Employees"] 
                                            if employee["Timestamp"] != timestamp]
                
                # Overwrite the file with the updated data
                file.seek(0)
                file.truncate(0)  # Clear the file content before writing
                json.dump(file_content, file, indent=4)

            # Remove the selected row from the table
            self.table.removeRow(selected_row)

            # Show a success message
            QMessageBox.information(self, "Success", "Employee data deleted successfully.")
            
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Failed to delete entry: {str(e)}")

    def clear_fields(self):
        self.name.clear()
        self.age.clear()
        self.title.clear()
        self.address1.clear()
        self.address2.clear()
        self.additional.clear()
    
    def initialize_table(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['Timestamp','Name','Age','Title','Address 1','Address 2','Additional Information'])
        self.table.resizeColumnsToContents()

    def populate_table(self, row, timestamp, name, age, title, address1, address2, additional):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(timestamp))
        self.table.setItem(row, 1, QTableWidgetItem(name))
        self.table.setItem(row, 2, QTableWidgetItem(age))
        self.table.setItem(row, 3, QTableWidgetItem(title))
        self.table.setItem(row, 4, QTableWidgetItem(address1))
        self.table.setItem(row, 5, QTableWidgetItem(address2))
        self.table.setItem(row, 6, QTableWidgetItem(additional))

        for col in range(self.table.columnCount()):
            self.table.item(row, col).setFlags(self.table.item(row, col).flags() | Qt.ItemIsEditable)

        self.table.resizeColumnsToContents()

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
