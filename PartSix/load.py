from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication

class Window(QObject):
    def __init__(self):
        super().__init__()






if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    engine = QQmlApplicationEngine(parent=app)
    window = Window()
    engine.rootContext().setContextProperty('window', window)
    engine.load('window.qml')
    ex = app.exec()
    sys.exit(ex)
