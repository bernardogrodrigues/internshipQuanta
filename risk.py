import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
from datetime import datetime
import numpy as np

def volatility(data):
  #list of closing prices
  close_data = [candle["close"] for candle in data]
  stdev = np.std(close_data)
  return stdev/close_data[0]
  
def periodic_volatility(data, resolution = 10):
  close_data = [candle["close"] for candle in data]
  moving_stdev = [(np.std(close_data[i*resolution:(i+1)*resolution])/data[i]["close"]*100) for i in range(len(close_data))]
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
        self.periodic_volat = periodic_volatility(self.data)
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

        # for i in range(len(self.data)):
        #     stdev_val = self.periodic_volat[i]
            
        #     p.drawRect(QtCore.QRectF(self.data[i]['date'].timestamp() - 0.5 * width, 0, width, stdev_val))

        # p.end()
        for i in range(len(self.data)-1):
            # (1)
            volume_val, open_val, close_val = self.periodic_volat[i], self.data[i]['open'], self.data[i]['close']
            
            # (2)
            if close_val > open_val:
                p.setPen(pg.mkPen('g'))
                p.setBrush(pg.mkBrush('g'))
            else:
                p.setPen(pg.mkPen('r'))
                p.setBrush(pg.mkBrush('r'))

            # (3)
            p.drawRect(QtCore.QRectF(self.data[i]['date'].timestamp() - 0.5 * width, 0, width, volume_val))

    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)

    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())