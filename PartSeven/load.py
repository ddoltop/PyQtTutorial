from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtCore import QObject
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCharts import *
import sys

class Window(QObject):
    def __init__(self):
        super(Window, self).__init__()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    
    window = Window()
    engine.rootContext().setContextProperty("window", window)
    engine.load('linechart.qml')

    # window.show()
    sys.exit(app.exec())
