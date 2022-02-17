from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QMouseEvent
from PyQt6.QtCore import Qt

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Mouse Event")
        self.setWindowIcon(QIcon('images/python.png'))

        hbox = QVBoxLayout()
        self.label_press = QLabel("Mouse Press")
        self.label_press.setFont(QFont("Times", 15))
        self.label_release = QLabel("Mouse Release")
        self.label_release.setFont(QFont("Times", 15))
        self.label = QLabel("Mouse Track")
        self.label.setFont(QFont("Times", 15))

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        hbox.addItem(spacerItem)
        hbox.addWidget(self.label_press)
        hbox.addWidget(self.label_release)
        hbox.addWidget(self.label)

        self.setLayout(hbox)

        self.setMouseTracking(True)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.buttons() & Qt.MouseButton.LeftButton:
            x = a0.pos().x()
            y = a0.pos().y()

            text = "X: {0}, Y: {1}".format(x, y)
            self.label_press.setText("Mouse Pressed: " + text)

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        # btns = a0.buttons() # No Buttons
        x = a0.pos().x()
        y = a0.pos().y()

        text = "X: {0}, Y: {1}".format(x, y)
        self.label_release.setText("Mouse Released: " + text)

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        pos = a0.pos()

    # def mouseMoveEvent1(self, event):
    #     event.
    #     x = self.x()
    #     y = self.y()
        x = pos.x()
        y = pos.y()
        text = "X: {0}, y = {1}".format(x, y)
        # print(text)
        self.label.setText(text)

        self.update()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()
    sys.exit(app.exec())
