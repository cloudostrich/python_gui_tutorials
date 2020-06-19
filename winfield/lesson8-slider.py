import sys
from PyQt5.QtWidgets import QLineEdit, QSlider, QVBoxLayout, QApplication, QPushButton, QWidget
from PyQt5.QtCore import Qt

class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

##        cutshort = QAction("&GET TO THE CHOPPA??", self)
##        cutshort.setShortcut("CTRL+Q")
##        cutshort.triggered.connect(self.close)        

    def init_ui(self):
        # this is home page of window, always activated

        self.le = QLineEdit()
        self.b1 = QPushButton('Clear')
        self.b2 = QPushButton('Print')
        self.s1 = QSlider(Qt.Horizontal)
        self.s1.setMinimum(1)
        self.s1.setMaximum(99)
        self.s1.setValue(25)
        self.s1.setTickInterval(10)
        self.s1.setTickPosition(QSlider.TicksBelow)

        v_box = QVBoxLayout()
        v_box.addWidget(self.le)
        v_box.addWidget(self.b1)
        v_box.addWidget(self.b2)
        v_box.addWidget(self.s1)

        self.setLayout(v_box)
        self.setWindowTitle(' Lesson 8')

        self.b1.clicked.connect(lambda: self.btn_click(self.b1, 'Hello from shit'))
        self.b2.clicked.connect(lambda: self.btn_click(self.b2, 'Hello from crap'))
        self.s1.valueChanged.connect(self.v_change)

        self.show()

    def btn_click(self,b, string):
        if b.text() == 'Print':
            print(self.le.text())
        else:
            self.le.clear()
        print(string)

    def v_change(self):
        my_value = str(self.s1.value())
        self.le.setText(my_value)


app = QApplication(sys.argv)
a_window = Window()
sys.exit(app.exec_())
