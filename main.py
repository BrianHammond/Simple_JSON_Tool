# checks to see if the 'PyQT6' module is installed
try: 
    from PyQt6.QtWidgets import QApplication
except ModuleNotFoundError: # if it's not then it will automatically be installed
    print("PyQt6 module is not installed")
    import subprocess
    required_packages = ['PyQt6']
    for package in required_packages:
        subprocess.call(['pip', 'install', package])

import sys
from PyQt6.QtWidgets import QApplication
from main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv) # needs to run first
    MainWindow = MainWindow()
    MainWindow.show()
    sys.exit(app.exec())