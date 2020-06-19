import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QPolygon
from PyQt5.QtCore import Qt, QPoint

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "QPainter polygon"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 680

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("mongol.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.red, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.red, Qt.VerPattern))

        points=QPolygon([
            QPoint(10,10),
            QPoint(10,100),
            QPoint(100, 10),
            QPoint(100,100)])
        painter.drawPolygon(points)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())