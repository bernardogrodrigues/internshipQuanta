import sys, os

import pyqtgraph as pg
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton,
    QToolBar, QLabel, QListWidget, QSplitter, QSizePolicy, QComboBox, QMenu, QToolTip,
    QDockWidget, QDialog, QMenuBar
)
from PyQt6.QtGui import QIcon, QPixmap, QPalette, QColor, QAction, QPen
from PyQt6.QtCore import Qt, QSize
import pyqtgraph as pqtg
from datetime import datetime
import numpy as np
from cs import CandlestickItem

BG_COLOR = "#151820" # dark background's color

LIGHT_COLOR = "#8c4ee9" # lighter color of theme

class GUI(QWidget):
    '''
    Quanta da Wish Risk Analysis GUI application.

    Attributes:
        main_widgets (dict): Dictionary containing main widgets.
        buttons (dict): Dictionary containing the buttons.
    '''
    def __init__(self):
        super().__init__()
        
        # Set Main widgets
        self.main_widgets = {"main_window": QMainWindow(),
                             "ohlc_chart": pg.PlotWidget(),
                             "risk_chart": pg.PlotWidget(),
                             "tool_bar": QToolBar()}

        # Set title label
        self.title_label = QLabel("Quanta da Wish Risk Analysis")
        self.setStyleSheet(f"color: {LIGHT_COLOR}; \
                            padding-left: 0px; \
                            padding-right: 60px;")

        # Buttons for plotting charts
        self.buttons = {"plot_ohlc": QPushButton("Plot OHLC"),
                        "plot_risk": QPushButton("Plot Risk"),
                        "EUR/USD": QPushButton("EUR/USD"),
                        "GBP/USD": QPushButton("GBP/JPY"),
                        "EUR/JPY": QPushButton("EUR/JPY")}
        
        # Initialize layout and add elements to it
        self.setupGUI()

    def setupGUI(self):
        """
        Set up the GUI
        """
        # Styling window
        self.setStyleSheet(f"background: {BG_COLOR};")
        self.main_widgets["main_window"].setStyleSheet(f"background: {BG_COLOR};")

        # Styling charts
        graphs = [self.main_widgets["ohlc_chart"],
                  self.main_widgets["risk_chart"]]
        
        # Customize axis labels and colors
        label_style = {'color': 'purple', 'font-size': '12px', 'font-weight': 'bold'}
        axis_color = LIGHT_COLOR
        
        for graph in graphs:
            graph.setBackground(BG_COLOR)
            graph.showGrid(x=True, y=True, alpha=0.5)

            # Set y axis label and pen
            y_axis = graph.getAxis('left')
            y_axis.setLabel("Currency pair price" if graph is self.main_widgets["ohlc_chart"] else "Volatilty Periods", **label_style)
            y_axis.setPen(LIGHT_COLOR)

            # Set x axis as a date axis item, set label, set pen, but hide x axis if it is the top graph
            if graph is self.main_widgets["ohlc_chart"]:
                graph.getAxis("bottom").hide()
            else:
                graph.setAxisItems({'bottom':pqtg.DateAxisItem()})
                x_axis = graph.getAxis('bottom')
                x_axis.setLabel('Date', **label_style)
                x_axis.setPen(axis_color)
            
            # Set the height of the volume graph
            self.main_widgets["risk_chart"].setFixedHeight(100)


if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setApplicationName('Quanta (da Wish)')

    # Define your custom color palette
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.WindowText, QColor(255, 255, 255))  # Text color
    # Apply the custom color palette to the application
    app.setPalette(palette)

    ui = GUI()
    ui.show()

    sys.exit(app.exec())