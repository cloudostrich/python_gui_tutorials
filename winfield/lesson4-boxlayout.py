import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    b = QtWidgets.QPushButton(w)
    l = QtWidgets.QLabel(w)

    b.setText('Push Me')
    l.setText('Look at Me')

    h_box = QtWidgets.QHBoxLayout()
    h_box.addStretch()
    h_box.addWidget(l)
    h_box.addStretch()
    
    v_box = QtWidgets.QVBoxLayout()
    v_box.addWidget(b)
    v_box.addLayout(h_box)
    
    w.setLayout(v_box)
    
    w.setWindowTitle('lesson 3')

##    w.setGeometry(100, 100, 300, 200)
##    b.move(100, 50)
##    l.move(110, 100)

    w.show()
    sys.exit(app.exec_())

window()
