# -------------------------------------------------------------------------------
# Name:             HyperLabel.py
# Purpose:          Making a text label into a hyperlink
#
# Author:           Jeffreaux
#
# Created:          08Aug24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QLabel, QLineEdit
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("HyperLabel_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")

        self.txtInputLink = self.findChild(QLineEdit, "txtInputLink")
        
        self.lblLink = self.findChild(QLabel, "lblLink")

        self.actExit = self.findChild(QAction, "actExit")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)

        self.txtInputLink.returnPressed.connect(self.move_label)

        self.actExit.triggered.connect(self.closeEvent)

        # Show the app
        self.show()

    def move_label(self):
        link = self.txtInputLink.text()
        print(link)
        tmpString = f"<a href={link}>See Obituary</a>"
        print(tmpString)
        self.lblLink.setText(tmpString)
    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
