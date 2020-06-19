import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QAction, QMessageBox
from PyQt5.QtWidgets import QCheckBox


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
		
		self.show()
		
	def close_application(self):
		# print('whoooo sooo custooom')
		choice = QMessageBox.question(self, 'Extract',
			"Get into the choppa?",
			QMessageBox.Yes | QMessageBox.No)
			
		if choice == QMessageBox.Yes:
			print('Extracting Naaaoooowww!')
			sys.exit()
		else:
			pass
			
	# def closeEvent(self, event):	# actually works in pyqt5 too 
		# event.ignore()
		# self.close_application()
		
	def closeEvent(self, QCloseEvent):
		'''for closing the window from the corner "x" '''
		QCloseEvent.ignore()
		self.close_application()
		
def main():
	app = QApplication(sys.argv)
	gui = window()
	sys.exit(app.exec_())
	
main()