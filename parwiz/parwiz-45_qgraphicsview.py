
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPainter, QBrush, QPen, QLinearGradient
from PyQt5.QtCore import Qt, QPoint

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "QPainter polygon"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        scene = QGraphicsScene() #the scene

        redbrush = QBrush(Qt.red)
        bluebrush = QBrush(Qt.blue)
        blackpen = QPen(Qt.black)
        blackpen.setWidth(7)

        ellipse = scene.addEllipse(10,10, 200, 200, blackpen, redbrush)
        rect = scene.addRect(-100,-100,200,200, blackpen, bluebrush)

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)

        view = QGraphicsView(scene, self)
        view.setGeometry(0,0, 680, 500)
        
        
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
