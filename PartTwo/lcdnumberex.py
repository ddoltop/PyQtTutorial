from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLCDNumber
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QTime, QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QLCDNumber")
        self.setWindowIcon(QIcon('../Image/python.png'))

        timer = QTimer()
        timer.timeout.connect(self.show_lcd)
        timer.start(1000)

        self.show_lcd()

    def show_lcd(self):
        vbox = QVBoxLayout()
        lcd = QLCDNumber()
        lcd.setStyleSheet('background:red')

        vbox.addWidget(lcd)
        time = QTime.currentTime()
        text = time.toString('mm:ss')

        lcd.display(text)

        self.setLayout(vbox)
        print(text)

if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('../Image/python.png'))
    window = Window()
    window.show()

    app.exec(app.exec())
