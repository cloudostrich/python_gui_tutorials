import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen, QLinearGradient
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
        painter.setPen(QPen(Qt.black, 4, Qt.SolidLine))

        grad1 = QLinearGradient(25, 100, 150, 175)
        grad1.setColorAt(0.0, Qt.darkGray)
        grad1.setColorAt(0.5, Qt.green)
        grad1.setColorAt(1.0, Qt.yellow)
        painter.setBrush(QBrush(grad1))

        painter.drawRect(10,10, 200, 200)
        

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
