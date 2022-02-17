from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QSlider
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import Qt, QTime, QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QSlider")
        self.setWindowIcon(QIcon('Image/python.png'))

        hbox = QHBoxLayout()
        self.slider = QSlider()
        self.slider.setOrientation(Qt.Orientation.Horizontal)
        self.slider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.slider.setTickInterval(10)

        self.slider.setMinimum(0)
        self.slider.setMaximum(100)

        self.slider.valueChanged.connect(self.changed_slider)

        self.label = QLabel()
        self.label.setFont(QFont("Times", 15))

        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

    def changed_slider(self):
        value = self.slider.value()
        self.label.setText(str(value))


if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()

    sys.exit(app.exec())
