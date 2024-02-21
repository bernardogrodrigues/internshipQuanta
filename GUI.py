''' All things PyQt6'''

import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenu, QWidget, QMenuBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.resize(800, 500)
        self.setWindowTitle("Context Menu")

        widget  = QWidget()
        label1 = QLabel("This is a QLabel in the central widget", self)
        label2 = QLabel("This is another one.", self)

        # Set up layout of the main window
        label1.move(30, 20)

        menubar = QMenuBar()
        file_menu = menubar.addMenu("File")
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(sys.exit)
        file_menu.addAction(exit_action)


        self.setCentralWidget(widget)
        self.setMenuBar(menubar)
        self.setWindowTitle("Quanta Falsificado")



app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()