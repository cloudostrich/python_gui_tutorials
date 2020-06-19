import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton


class window(QMainWindow):

	def __init__(self):
		super(window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle(' lesson 4 liao !')
		self.setWindowIcon(QIcon('icon-smoker.jpg'))
		self.home()
		
	def home(self):
		btn = QPushButton('quit', self)
		btn.clicked.connect(self.close_application)
		btn.resize(btn.sizeHint()) # auto size for btn
		btn.move(0,0)
		self.show()
		
	def close_application(self):
		print('whoooo sooo custooom')
		sys.exit()
		
		
def main():
	app = QApplication(sys.argv)
	gui = window()
	sys.exit(app.exec_())
	
main()