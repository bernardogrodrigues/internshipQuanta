import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
from datetime import datetime
import numpy as np
import statistics as stat
from PyQt6.QtGui import QColor

def volatility(data):
    #list of closing prices
    close_data = [candle["close"] for candle in data]
    stdev = np.std(close_data)
    return stdev/close_data[0]

def colormap(num, min, max):
    """
    This function returns a color mapped to the given number based on its position between the minimum and maximum values.
    Made for volatility (green = low volatility, red = high volatility)
    
    Params:
        num(int): the number we want to map
        min(int): minimum of origin interval
        max(int): maximum of origin interval

    Returns:
        QColor()
    """
    hue_val = int(120 - (num-min)*120/(max-min))
    return  QColor().fromHsl(hue_val, 128, 128)
  
# def periodic_volatility(data, resolution = 5):
#     close_data = [candle["close"] for candle in data]
#     moving_stdev = [stat.stdev(close_data[i:i+resolution]) for i in range(0, (len(close_data)), resolution)]
#     normalized_stdev = []
#     for val in moving_stdev:
#         normalized_stdev += [val]*resolution
#     return normalized_stdev

def periodic_volatility(data, resolution = 5):
    close_data = [candle["close"] for candle in data]
    moving_stdev = [stat.stdev(close_data[i:i+resolution]) for i in range(len(close_data)-resolution)]
    return moving_stdev

class VolatilityItem(pg.GraphicsObject):
    """
    Class that draws volatility bars in graphs
    """
    def __init__(self, data: list):
        """
        Initializes the VolatItem

        Parameters:
            data (list): List of dictionaries containing OHLC data and timestamps: [{'date': datetime, 'open': float, 'high': float, 'low': float, 'close': float}, ...]

        Returns:
            None
        """
        pg.GraphicsObject.__init__(self)
        
        self.data = data
        self.generatePicture()

    def generatePicture(self):
        """
        Generates a QPicture for rendering the Volat Bar chart.

        Returns:
            None
        """
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        
        if not self.data or len(self.data) < 2:
            print("Error: Insufficient data for volatility bars.")
            return

        # Calculate bin width based on date values
        # Get minimum value from 3 iterations to throw away faulty width values (Friday-Monday, holidays, etc)
        width = float('inf')
        for i in range(2, -1, -1):
            possible_width = (self.data[i]['date'].timestamp() - self.data[i + 1]['date'].timestamp()) * 0.75
            if possible_width < width:
                width = possible_width

        period_volat = periodic_volatility(self.data)
        for i in range(len(period_volat)):
            stdev_val = period_volat[i] * 100

            bar_color = colormap(period_volat[i], min(period_volat), max(period_volat))
            p.setPen(pg.mkPen(bar_color))
            p.setBrush(pg.mkBrush(bar_color))

            p.drawRect(QtCore.QRectF(self.data[i]['date'].timestamp() - 0.5 * width, 0.5, width, stdev_val))
        p.end()

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())