import sys
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QWidget, QComboBox, QLineEdit, QDateEdit, QPushButton
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Database"
        self.top = 200
        self.left = 500
        self.width = 400
        self.height = 300
        self.init_window()

    def init_window(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        # create a central widget for the window
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # create a grid layout for the central widget
        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        # create labels for each field in the `tbl_clients` table
        last_name_label = QLabel("Last Name")
        first_name_label = QLabel("First Name")
        fathers_name_label = QLabel("Father's Name")
        birth_date_label = QLabel("Birth Date")
        sex_label = QLabel("Sex")
        
        # create line edits for each field in the `tbl_clients` table
        last_name_edit = QLineEdit()
        first_name_edit = QLineEdit()
        fathers_name_edit = QLineEdit()
        birth_date_edit = QDateEdit()
        sex_edit = QComboBox()
        
        # add the available sex descriptions to the sex edit
        sex_edit.addItems(["Male", "Female"])

        # add a save button
        save_button = QPushButton("Save")
        
        # add all the widgets to the grid layout
        grid_layout.addWidget(last_name_label, 0, 0)
        grid_layout.addWidget(first_name_label, 1, 0)
        grid_layout.addWidget(fathers_name_label, 2, 0)
        grid_layout.addWidget(birth_date_label, 3, 0)
        grid_layout.addWidget(sex_label, 4, 0)
        grid_layout.addWidget(last_name_edit, 0, 1)
        grid_layout.addWidget(first_name_edit, 1, 1)
        grid_layout.addWidget(fathers_name_edit, 2, 1)
        grid_layout.addWidget(birth_date_edit, 3, 1)
        grid_layout.addWidget(sex_edit, 4, 1)
        grid_layout.addWidget(save_button, 5, 0, 1, 2)
        
        # show the window
        self.show()
        
# create an instance of the PyQt application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mw = MainWindow()
    sys.exit(app.exec())
