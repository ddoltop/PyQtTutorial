from PyQt6 import QtCore

from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle("PyQt6 QComboBox")
        self.setWindowIcon(QIcon('Image/python.png'))


if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()

    sys.exit(app.exec())
