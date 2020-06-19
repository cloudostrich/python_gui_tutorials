import sys
from PyQt5 import QtWidgets, QtGui

class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

        cutshort = QtWidgets.QAction("&GET TO THE CHOPPA??", self)
        cutshort.setShortcut("CTRL+Q")
        cutshort.triggered.connect(self.close)        

    def init_ui(self):
        # this is home page of window, always activated

        self.le = QtWidgets.QLineEdit()
        self.b1 = QtWidgets.QPushButton('Clear')
        self.b2 = QtWidgets.QPushButton('Print')
        

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)

        self.setLayout(v_box)
        self.setWindowTitle(' Lesson 6')

        self.b1.clicked.connect(self.btn_click)
        self.b2.clicked.connect(self.btn_click)

        self.show()

    def btn_click(self):
        sender = self.sender()
        if sender.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()

    def close_app(self):
        print('exiting now')
        sys.exit()


app = QtWidgets.QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
