import sys
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction


class window(QMainWindow):

	def __init__(self):
		super(window, self).__init__()
		self.setGeometry(50, 50, 500, 300)
		self.setWindowTitle(' lesson 5 liao !')
		self.setWindowIcon(QIcon('icon-mongol.jpg'))
		
		extractAction = QAction(' Get to the choppa', self)
		extractAction.setShortcut('Ctrl+Q')
		extractAction.setStatusTip('leave the app')
		extractAction.triggered.connect(self.close_application)
		
		self.statusBar()
		
		mainMenu = self.menuBar()
		fileMenu = mainMenu.addMenu('&File')
		fileMenu.addAction(extractAction)
		
		self.home()
		
	def home(self):
		btn = QPushButton('quit', self)
		btn.clicked.connect(self.close_application)
		# btn.resize(btn.sizeHint()) # auto size for btn
		btn.resize(btn.minimumSizeHint())
		btn.move(0,100)
		
		extractAction = QAction(QIcon('icon-smoker.jpg'), 'Flee the scene', self)
		extractAction.triggered.connect(self.close_application)
		
		self.toolBar = self.addToolBar('Extraction')
		self.toolBar.addAction(extractAction)
		
		bsAction = QAction(QIcon('icon-me.jpg'), 'bullshit time', self)
		bsAction.triggered.connect(self.bullshit)
		self.toolBar.addAction(bsAction)
		
		self.show()
		
	def close_application(self):
		print('whoooo sooo custooom')
		sys.exit()
		
	def bullshit(self):
		print('I am the greatest!!!')
		
def main():
	app = QApplication(sys.argv)
	gui = window()
	sys.exit(app.exec_())
	
main()