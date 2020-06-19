import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsScene,
                             QGraphicsView, QGraphicsItem, QPushButton)
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

        self.button1 = QPushButton("Rotate - ", self)
        self.button1.setGeometry(200, 420, 100, 50)
        self.button1.clicked.connect(self.rotateminus)

        self.button2 = QPushButton("Rotate +", self)
        self.button2.setGeometry(320, 420, 100, 50)
        self.button2.clicked.connect(self.rotateplus)
        
        scene = QGraphicsScene() #the scene

        redbrush = QBrush(Qt.red)
        bluebrush = QBrush(Qt.blue)
        blackpen = QPen(Qt.black)
        blackpen.setWidth(7)

        ellipse = scene.addEllipse(10,10, 200, 200, blackpen, redbrush)
        rect = scene.addRect(-100,-100,200,200, blackpen, bluebrush)
        line = scene.addLine(-100,-100,200,200, blackpen)

        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
        line.setFlag(QGraphicsItem.ItemIsMovable)

        self.view = QGraphicsView(scene, self)
        self.view.setGeometry(0,0, 680, 400)
        
        
        self.setWindowIcon(QtGui.QIcon("mongol.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

    def rotateminus(self):
        self.view.rotate(-10)

    def rotateplus(self):
        self.view.rotate(+10)
        

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())
