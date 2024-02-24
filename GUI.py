''' All things PyQt6'''

import sys, os

import pyqtgraph as pg
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QToolBar, QLabel, QListWidget, QSplitter, QSizePolicy, QComboBox, QMenu, QToolTip,
    QDockWidget, QDialog, QMenuBar
)
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QColor, QAction
from PyQt6.QtCore import Qt, QSize
import pyqtgraph as pqtg
from datetime import datetime
import numpy as np


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main window style
        self.setWindowTitle("Quanta Falsificado")
        self.resize(800, 500)

        # Menu bar
        menubar = QMenuBar()
        menubar.setStyleSheet('background-color:#2F234C;')
        # File menu in menubar
        file_menu = menubar.addMenu(QIcon("SP_TrashIcon"), "File")

        # Exit action with shortcut "Space" for temporary convenience
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Space")
        exit_action.triggered.connect(sys.exit)
        file_menu.addAction(exit_action)

        pw = pg.plot(xVals, yVals, pen='r')  # plot x vs y in red
        pw.plot(xVals, yVals2, pen='b')

        win = pg.GraphicsLayoutWidget()  # Automatically generates grids with multiple items
        win.addPlot(data1, row=0, col=0)
        win.addPlot(data2, row=0, col=1)
        win.addPlot(data3, row=1, col=0, colspan=2)

        pg.show(imageData)  # imageData must be a numpy array with 2 to 4 dimensions

        # Set menubar as such
        self.setMenuBar(menubar)

app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()