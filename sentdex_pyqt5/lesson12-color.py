import sys
from PyQt5.QtCore import QCoreApplication, Qt
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QPushButton, 
	QAction, QMessageBox, QCheckBox, QProgressBar, QComboBox, QLabel, QStyleFactory, 
	QFontDialog, QColorDialog, QCalendarWidget)


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
		
		fontChoice = QAction('font', self)
		fontChoice.triggered.connect(self.font_choice)
		self.toolBar.addAction(fontChoice)
		
		color = QColor(0, 0, 0)
		fontColor = QAction('Font bg Color', self)
		fontColor.triggered.connect(self.color_picker)
		self.toolBar.addAction(fontColor)
		
		cal = QCalendarWidget(self)
		cal.move(500, 200)
		cal.resize(200, 200)
		
		checkBox = QCheckBox('window size', self)
		checkBox.move(300, 25)
		# checkBox.toggle()
		checkBox.stateChanged.connect(self.enlargeWindow)
		
		self.progress = QProgressBar(self)
		self.progress.setGeometry(200, 80, 250, 20)
		
		self.btn = QPushButton('download', self)
		self.btn.move(200, 120)
		self.btn.clicked.connect(self.download)
		
		# print(self.style().objectName())
		self.styleChoice = QLabel('Windows', self)
		
		comboBox = QComboBox(self)
		# comboBox.addItem('motif')
		# comboBox.addItem('Windows')
		# comboBox.addItem('cde')
		# comboBox.addItem('Plastique')
		# comboBox.addItem('Cleanlooks')
		# comboBox.addItem('windowsvista')
		comboBox.addItems(QStyleFactory.keys())
		
		comboBox.move(25, 250)
		self.styleChoice.move(50,150)
		comboBox.activated[str].connect(self.style_choice)
		
		self.show()
		
	def color_picker(self):
		color = QColorDialog.getColor()
		self.styleChoice.setStyleSheet("QWidget {background-color: %s}" % color.name())
		
	def font_choice(self):
		font, valid = QFontDialog.getFont()
		if valid:
			self.styleChoice.setFont(font)
		
	def style_choice(self, text):
		self.styleChoice.setText(text)
		self.styleChoice.resize(self.styleChoice.sizeHint()) # change font size on render
		QApplication.setStyle(QStyleFactory.create(text))
		
	def download(self):
		self.completed = 0
		while self.completed < 100:
			self.completed += 0.0001
			self.progress.setValue(self.completed)
		
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
		
	def bullshit(self):
		print('I am the greatest!!!')
		
	def enlargeWindow(self, state):
		if state == Qt.Checked:
			self.setGeometry(50, 50, 1000, 600)
		else:
			self.setGeometry(50, 50, 500, 300)
			
			
def main():
	app = QApplication(sys.argv)
	gui = window()
	sys.exit(app.exec_())
	
main()