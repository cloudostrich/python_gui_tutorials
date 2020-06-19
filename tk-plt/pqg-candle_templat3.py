# -*- coding: utf-8 -*-
"""

Description of example


"""
import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui #, QtWidgets
# from PyQt4 import QtCore, QtGui, QtWidgets
import numpy as np
import sys
import numpy as np
import urllib.request


class CandleStick(pg.GraphicsObject):
    def __init__(self, data):
        pg.GraphicsObject.__init__(self)
        self.data = data  ## data must have fields: time, opn, high, low, close
        self.generatePicture()
    
    def generatePicture(self):
        ''' pre-computing a QPicture object allows paint() to run
        much more quickly, rather than re-drawing the shapes every time.'''
        self.picture = QtGui.QPicture()
        p = QtGui.QPainter(self.picture)
        p.setPen(pg.mkPen('w'))
        w = (self.data[1][0] - self.data[0][0]) / 3.
        for (t, opn, high, low, close) in self.data:
            p.drawLine(QtCore.QPointF(t, low), QtCore.QPointF(t, high))
            if opn > close:
                p.setBrush(pg.mkBrush('r'))
            else:
                p.setBrush(pg.mkBrush('g'))
            p.drawRect(QtCore.QRectF(t-w, opn, w*2, close-opn))
        p.end()
    
    def paint(self, p, *args):
        p.drawPicture(0, 0, self.picture)
    
    def boundingRect(self):
        '''boundingRect _must_ indicate the entire area that will be
        drawn on or else we will get artifacts and possibly crashing.
        (in this case, QPicture does all the work of computing the
        bouning rect for us)'''
        return QtCore.QRectF(self.picture.boundingRect())


class Window(QtGui.QWidget):

    def __init__(self):
        super().__init__()
        self.title = "YA YA HEY HEY"
        self.top = 100
        self.left = 100
        self.width = 800
        self.height = 600
        self.init_ui()
        self.plotstuff()

    def init_ui(self):
        self.guiplot = pg.PlotWidget()
        self.setWindowIcon(QtGui.QIcon("icon-mongol.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        layout = QtGui.QGridLayout(self)
        layout.addWidget(self.guiplot, 0,0)
        plotItem = self.guiplot.getPlotItem() # y-axis on left part
        plotItem.showAxis('right')
        plotItem.hideAxis('left')
        plotItem.showGrid(x=True, y=True, alpha=0.8)
        self.show()

    def plotstuff(self):
        mycandle = CandleStick(ohlc)
        self.guiplot.addItem(mycandle)
        

# Starting data
##data = [  ## fields are (time, opn, high, low, close).
##    [1., 10, 15, 5, 13],
##    [2., 13, 20, 9, 17],
##    [3., 17, 23, 11, 14],
##    [4., 14, 19, 5, 15],
##    [5., 15, 22, 8, 9],
##    [6., 9, 16, 8, 15],
##]

def str2int(x, encoding='utf-8'):
    strconverter = int(''.join(x.split('-')))
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter

urlprice = 'https://pythonprogramming.net/yahoo_finance_replacement'
source_code = urllib.request.urlopen(urlprice).read().decode()
stock_data = []
split_source = source_code.split('\n')
for line in split_source:
    split_line = line.split(',')
    if len(split_line) == 7:
        ''.join(split_line[0].split('-'))
        if 'values' not in line and 'Date' not in line:
            stock_data.append(line)
date, closep, highp, lowp, openp,settlep, volume = np.loadtxt(stock_data,
                                                      delimiter=',',
                                                      unpack=True, converters={0: lambda x:  ''.join((x.decode('utf-8')).split('-'))})
                                                      # %Y = full year
                                                      # %y = part year
                                                      # %m = month
                                                      # %d = day
                                                      # %H = hr
                                                      # %M = minute
                                                      # %S = seconds
##                                                      converters={0: bytespdate2num('%Y-%m-%d')})
##                                                      converters={0:np.datetime64})
x = 0
y = len(date)
ohlc = []
##date = str2int(date)

while x < y:
    append_me = date[x], openp[x], highp[x], lowp[x], closep[x] #, volume[x]
    ohlc.append(append_me)
    x += 1
# win.setWindowTitle('pyqtgraph example: ____')
app = QtGui.QApplication(sys.argv)
win = Window()
#win.show()


#sys.exit(app.exec_())
## Start Qt event loop unless running in interactive mode or using pyside.
if __name__ == '__main__':
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        app.instance().exec_()
