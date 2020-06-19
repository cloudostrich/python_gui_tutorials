import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()

    w.setWindowTitle('Simple')
    w.setWindowIcon(QtGui.QIcon('icon-mongol.jpg'))
    
    w.setGeometry(100, 100, 300, 200)
    w.show()

    sys.exit(app.exec_())

window()
