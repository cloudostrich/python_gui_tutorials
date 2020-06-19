import sys
from PyQt5.QtWidgets import QLineEdit, QCheckBox, QVBoxLayout, QApplication, QPushButton, QWidget, QLabel
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.lbl = QLabel()
        self.chx = QCheckBox('Do you like dogs?')
        self.btn = QPushButton('Push Me')

        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.chx)
        layout.addWidget(self.btn)
        #layout.setWindowIcon(QtGui.QIcon('icon-mongol.jpg'))

        self.setLayout(layout)
        #self.setWindowIcon(QtGui.QIcon('icon-mongol.jpg'))

        self.btn.clicked.connect(lambda: self.btn_clk(self.chx.isChecked(), self.lbl))

        self.show()

    def btn_clk(self, chk, lbl):
        if chk:
            lbl.setText('I guess you like dogs...')
        else:
            lbl.setText('Dog Hater!!')


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
