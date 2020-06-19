import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "QPainter brush styles"
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
        #painter.setPen(QPen(Qt.blue, 8, Qt.SolidLine))
        painter.setPen(QPen(Qt.blue, 8, Qt.DashLine))
        #painter.setBrush(QBrush(Qt.green, Qt.SolidPattern))
        painter.setBrush(QBrush(Qt.red, Qt.DiagCrossPattern))

        painter.drawRect(10, 100, 150, 100)
        #painter.drawEllipse(100, 100, 400, 200)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense1Pattern))
        painter.drawRect(180, 100, 150, 100)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.HorPattern))
        painter.drawRect(350, 100, 150, 100)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.VerPattern))
        painter.drawRect(520, 100, 150, 100)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.BDiagPattern))
        painter.drawRect(10, 220, 150, 100)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense3Pattern))
        painter.drawRect(350, 220, 150, 100)

        painter.setPen(QPen(Qt.black, 8, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.red, Qt.Dense4Pattern))
        painter.drawRect(180, 220, 150, 100)

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
