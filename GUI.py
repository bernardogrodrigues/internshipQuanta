''' All things PyQt6'''

import sys
from PyQt6.QtCharts import QChart, QCandlestickSeries, QValueAxis, QBarCategoryAxis
from PyQt6.QtCore import QDateTime,  Qt
from PyQt6.QtGui import QAction, QIcon, QColor
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow, QMenuBar, QMenu, QPushButton, QStyle, QScrollBar


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


        btn = QPushButton("Button")
        pixmapi = QStyle.StandardPixmap.SP_TrashIcon
        icon = self.style().standardIcon(pixmapi)
        btn.setIcon(icon)

        # EUR/USD chart (kind of)
        acmeSeries = QCandlestickSeries()
        acmeSeries.setName("Acme Ltd")
        acmeSeries.setIncreasingColor(QColor("green"))
        acmeSeries.setDecreasingColor(QColor("red"))   

        # chart instance
        chart = QChart()
        chart.addSeries(acmeSeries)
        chart.setTitle("Acme Ltd. Historical Data (July 2015)")
        chart.createDefaultAxes()
        axisX = QValueAxis()
        axisY = QValueAxis()
        axisY.setMax(axisY.max() * 1.01)
        axisY.setMin(axisY.min() * 0.99)
        

        # Set menubar as such
        self.setMenuBar(menubar)

app = QApplication(sys.argv)


window = MainWindow()
window.show()

app.exec()