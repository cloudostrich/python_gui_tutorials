from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
import sys

def run():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('main.qml')

    if not engine.rootObjects():
        print('not working')
        return -1
    
    return app.exec_()


if __name__ == "__main__":
    sys.exit(run())
