import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "QPainter stuff"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("mongol.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def paintEvent(self, e):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        #painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.green, Qt.DiagCrossPattern))

        painter.drawRect(100, 15, 400, 200)
        

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
