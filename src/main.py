import json
import datetime
import sys
import qdarkstyle
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QTableWidgetItem, QMessageBox
from PySide6.QtCore import QSettings, Qt
from main_ui import Ui_MainWindow as main_ui
from about_ui import Ui_Dialog as about_ui

class MainWindow(QMainWindow, main_ui): # used to display the main user interface
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_manager = SettingsManager(self)  # Initializes SettingsManager
        self.settings_manager.load_settings()  # Load settings when the app starts
        self.all_employees = [] # used to store all employees in the table

        #buttons
        self.button_add.clicked.connect(self.add_info) # write to .json
        self.button_update.clicked.connect(self.update_info) # update .json
        self.button_delete.clicked.connect(self.delete_entry)
        self.button_filter.clicked.connect(self.filter_entry)

        #menu bar
        self.action_new.triggered.connect(self.new_file) # create a new .json file
        self.action_open.triggered.connect(self.open_file) # imports .json file
        self.action_dark_mode.toggled.connect(self.dark_mode)
        self.action_about_qt.triggered.connect(lambda: QApplication.aboutQt())
        self.action_about.triggered.connect(lambda: AboutWindow(dark_mode=self.action_dark_mode.isChecked()).exec())

    def new_file(self): # creates a new .json file
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

    def open_file(self): # open an existing .json file
        self.clear_fields()
        self.filename = QFileDialog.getOpenFileName(self, 'Open a file', '', 'Data File (*.json)')
        if not self.filename[0]:
            return

        self.initialize_table()
        self.setWindowTitle(self.filename[0].split('/')[-1])

        try:
            with open(self.filename[0], "r+") as file:
                data = json.load(file)
                self.all_employees = data['Employees']  # stores the full dataset
                row = 0
                self.current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
                timestamp = self.current_date
            
                for employee in data['Employees']:
                    if not employee.get("Timestamp"):
                        employee["Timestamp"] = timestamp
                    first_name = employee['Name']['First Name']
                    middle_name = employee['Name']['Middle Name']
                    last_name = employee['Name']['Last Name']
                    age = employee['Age']
                    title = employee['Title']
                    address1 = employee['Address']['Address 1']
                    address2 = employee['Address']['Address 2']
                    country = employee['Address']['Country']
                    additional = employee['Misc'][0]
                    self.populate_table(row, employee["Timestamp"], first_name, middle_name, last_name, age, title, address1, address2, country, additional)
                    row += 1
        except FileNotFoundError:
            pass

    def add_info(self): # Add Button pressed
        self.current_date = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
        timestamp = self.current_date
        first_name = self.line_first_name.text()
        middle_name = self.line_middle_name.text()
        last_name = self.line_last_name.text()
        age = self.line_age.text()
        title = self.line_title.text()
        address1 = self.line_address1.text()
        address2 = self.line_address2.text()
        country = self.line_country.text()
        additional = self.line_information.text()

        row = self.table.rowCount()
        self.populate_table(row, timestamp, first_name, middle_name, last_name, age, title, address1, address2, country, additional)

        self.employee = {
            "Timestamp": timestamp,
            "Name": {"First Name": first_name, "Middle Name": middle_name, "Last Name": last_name},
            "Age": age,
            "Title": title,
            "Address": {"Address 1": address1, "Address 2": address2, "Country": country},
            "Misc": [additional]
        }

        try:
            with open(self.filename[0], "r+") as file:
                file_content = json.load(file)
                file_content["Employees"].append(self.employee)
                file.seek(0)
                json.dump(file_content, file, indent=4)
                self.all_employees.append(self.employee)  # update the in-memory full dataset
        except AttributeError:
            self.clear_fields()
            self.table.setRowCount(0)
            QMessageBox.warning(self, "NO FILE TO SUBMIT", "Please select a file or create one")

        self.clear_fields()

    def update_info(self): # Update Button pressed
        selected_row = self.table.currentRow()  # Get the selected row in the table
        if selected_row == -1:  # If no row is selected, show a warning message
            QMessageBox.warning(self, "No Selection", "Please select a row to update.")
            return

        # Get the updated values from the table
        timestamp = self.table.item(selected_row, 0).text()
        first_name = self.table.item(selected_row, 1).text()
        middle_name = self.table.item(selected_row, 2).text()
        last_name = self.table.item(selected_row, 3).text()
        age = self.table.item(selected_row, 4).text()
        title = self.table.item(selected_row, 5).text()
        address1 = self.table.item(selected_row, 6).text()
        address2 = self.table.item(selected_row, 7).text()
        country = self.table.item(selected_row, 8).text()
        additional = self.table.item(selected_row, 9).text()

        # Updated employee data
        updated_employee = {
            "Timestamp": timestamp,
            "Name": {
                "First Name": first_name,
                "Middle Name": middle_name,
                "Last Name": last_name
                },
            "Age": age,
            "Title": title,
            "Address": {
                "Address 1": address1,
                "Address 2": address2,
                "Country": country
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

    def filter_entry(self): # Filter Button pressed
        # Get filter values from the QLineEdit fields
        filter_fname = self.filter_firstname.text().strip().lower()
        filter_lname = self.filter_lastname.text().strip().lower()
        
        # Clear current table display
        self.table.setRowCount(0)
        
        # Iterate through all employees and only show those matching the filter
        row = 0
        for employee in self.all_employees:
            # Use lowercase only for comparison
            first_name_lower = employee['Name']['First Name'].lower()
            last_name_lower = employee['Name']['Last Name'].lower()
            
            # Check if employee matches filter criteria
            matches_fname = filter_fname == "" or filter_fname in first_name_lower
            matches_lname = filter_lname == "" or filter_lname in last_name_lower
            
            # If employee matches both filters, add to table with original case
            if matches_fname and matches_lname:
                timestamp = employee["Timestamp"]
                first_name = employee['Name']['First Name']  # Original case
                middle_name = employee['Name']['Middle Name']
                last_name = employee['Name']['Last Name']    # Original case
                age = employee['Age']
                title = employee['Title']
                address1 = employee['Address']['Address 1']
                address2 = employee['Address']['Address 2']
                country = employee['Address']['Country']
                additional = employee['Misc'][0]
                
                self.populate_table(row, timestamp, first_name, middle_name, last_name, age, title, address1, address2, country, additional)
                row += 1

    def delete_entry(self): # Delete Button pressed
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

        # Remove the entry from the JSON file and update self.all_employees
        try:
            with open(self.filename[0], "r+") as file:
                file_content = json.load(file)

                # Find the employee with the same timestamp and remove it
                file_content["Employees"] = [employee for employee in file_content["Employees"] 
                                        if employee["Timestamp"] != timestamp]
                
                # Update self.all_employees to match the file content
                self.all_employees = file_content["Employees"].copy()  # Use copy() to avoid reference issues
                
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
        self.line_first_name.clear()
        self.line_middle_name.clear()
        self.line_last_name.clear()
        self.line_age.clear()
        self.line_title.clear()
        self.line_address1.clear()
        self.line_address2.clear()
        self.line_country.clear()
        self.line_information.clear()
    
    def initialize_table(self):
        self.table.setRowCount(0)
        self.table.setColumnCount(10)
        self.table.setHorizontalHeaderLabels(['Timestamp', 'First Name', 'Middle Name', 'Last Name', 'Age', 'Title', 'Address 1', 'Address 2','Country', 'Additional Information'])
        self.table.resizeColumnsToContents()

    def populate_table(self, row, timestamp, first_name, middle_name, last_name, age, title, address1, address2, country, additional):
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(timestamp))
        self.table.setItem(row, 1, QTableWidgetItem(first_name))
        self.table.setItem(row, 2, QTableWidgetItem(middle_name))
        self.table.setItem(row, 3, QTableWidgetItem(last_name))
        self.table.setItem(row, 4, QTableWidgetItem(age))
        self.table.setItem(row, 5, QTableWidgetItem(title))
        self.table.setItem(row, 6, QTableWidgetItem(address1))
        self.table.setItem(row, 7, QTableWidgetItem(address2))
        self.table.setItem(row, 8, QTableWidgetItem(country))
        self.table.setItem(row, 9, QTableWidgetItem(additional))

        for col in range(self.table.columnCount()):
            self.table.item(row, col).setFlags(self.table.item(row, col).flags() | Qt.ItemIsEditable)

        self.table.resizeColumnsToContents()

    def dark_mode(self, checked):
        if checked:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        else:
            self.setStyleSheet('')

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

class AboutWindow(QDialog, about_ui): # this is the About Window
    def __init__(self, dark_mode=False):
        super().__init__()
        self.setupUi(self)
        if dark_mode:
            self.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())
        self.button_ok.clicked.connect(self.accept)

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())
