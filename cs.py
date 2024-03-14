import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
from datetime import datetime
from api import getTimeSeries

class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data: list):
        pg.GraphicsObject.__init__(self)
        self.data = data  # data: list[dict[datetime, ohlc data]]
        self.generatePicture()
    
    def generatePicture(self):
        ## pre-computing a QPicture object
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)

        # Calculate rectangle width based on date values
        # Get minimum value from 3 iterations to throw away faulty width values (Friday-Monday, holidays, etc)
        width = float('inf')
        for i in range(2,-1, -1):
            possible_width = (self.data[i]['date'].timestamp() - self.data[i+1]['date'].timestamp()) * 0.75 # avoids adjacent candlesticks
            if possible_width < width:
                width = possible_width
        
        for entry in self.data:
          open_val, close_val, min_val, max_val = entry['open'], entry['close'], entry['low'], entry['high']
          
          # set green pen for bearish candle (1) and red pen for bullish candle (2)
          if open_val > close_val: #1
            p.setPen(pg.mkPen("r"))
            p.setBrush(pg.mkBrush("r"))
          else: #2
            p.setPen(pg.mkPen("g"))
            p.setBrush(pg.mkBrush("g"))

          # Draw the wick (vertical line)
          p.drawLine(QtCore.QPointF(entry['date'].timestamp(), min_val), QtCore.QPointF(entry['date'].timestamp(), max_val))

          # Draw the candlestick rectangle
          p.drawRect(QtCore.QRectF(entry['date'].timestamp() - 0.5 * width, open_val, width, close_val - open_val))
            
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())