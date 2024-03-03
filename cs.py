import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui
from datetime import datetime
from api import getTimeSeries

class CandlestickItem(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  # data: list[dict[datetime, ohlc data]]
        self.generatePicture()
    
    def generatePicture(self):
        ## pre-computing a QPicture object
        self.picture = QtGui.QPicture()

        # Calculate width
        width = 1

        p = QtGui.QPainter(self.picture)
        for entry in self.data:
          open_val, close_val, min_val, max_val = entry['open'], entry['close'], entry['low'], entry['high']
          
          # set green pen for bullish candle and red pen for bearish candle 
          if open_val > close_val:
            p.setPen(pg.mkPen("r"))
            p.setBrush(pg.mkBrush("r"))
          else:
            p.setPen(pg.mkPen("g"))
            p.setBrush(pg.mkBrush("g"))

            # Draw the candlestick rectangle
            p.drawRect(QtCore.QRectF(entry['date'].timestamp() - 0.5 * width, open_val, width, close_val - open_val))
            
            # Draw the wick (vertical line)
            p.drawLine(QtCore.QPointF(entry['date'].timestamp(), min_val), QtCore.QPointF(entry['date'].timestamp(), max_val))

        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        return QtCore.QRectF(self.picture.boundingRect())
  