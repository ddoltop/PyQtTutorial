from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont, QMouseEvent, QPaintEvent, QPainter, QPen
from PyQt6.QtCore import Qt, QRect


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Mouse Event")
        self.setWindowIcon(QIcon('images/python.png'))

        self.pos1 = [0, 0]
        self.pos2 = [0, 0]
        self.setMouseTracking(True)
        self.painter = QPainter()
        self.pressed = False

    def paintEvent(self, a0: QPaintEvent) -> None:
        self.draw_circle()

    def draw_line(self):
        painter = self.painter
        painter.begin(self)
        pen = QPen(Qt.GlobalColor.red, 15)
        painter.setPen(pen)
        # painter.drawPoint(self.pos1[0], self.pos1[1])
        painter.drawLine(self.pos1[0], self.pos1[1], self.pos2[0], self.pos2[1])
        painter.end()

    def draw_circle(self):
        painter = self.painter
        painter.begin(self)
        pen = QPen(Qt.GlobalColor.red, 15)
        painter.setPen(pen)
        # painter.drawPoint(self.pos1[0], self.pos1[1])
        # painter.drawEllipse()
        width = self.pos2[0] - self.pos1[0]
        height = self.pos2[1] - self.pos1[1]
        rect = QRect(self.pos1[0], self.pos1[1],width, height)
        startAngle = 0
        arLength = 360 * 16
        painter.drawRect(rect)
        painter.drawArc(rect, startAngle, arLength)
        painter.end()

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.buttons() & Qt.MouseButton.LeftButton:
            self.pos1[0], self.pos1[1] = a0.pos().x(), a0.pos().y()
            self.pos2[0], self.pos2[1] = self.pos1
            self.pressed = True
            self.update()

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        self.pos2[0], self.pos2[1] = a0.pos().x(), a0.pos().y()
        self.update()
        self.pressed = False

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self.pressed:
            self.pos2[0], self.pos2[1] = a0.pos().x(), a0.pos().y()
            self.update()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()
    sys.exit(app.exec())
