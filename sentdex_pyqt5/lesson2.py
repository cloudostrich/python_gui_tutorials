import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon

class Window(QMainWindow):
	
	def __init__(self):
		super(Window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle('Lesson 2 baby')
		self.setWindowIcon(QIcon('icon-mongol.jpg'))
		self.show()
		
		
app = QApplication(sys.argv)
gui = Window()
sys.exit(app.exec_())