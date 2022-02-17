from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QIcon, QPainter, QPen, QBrush, QTextDocument, QLinearGradient, QRadialGradient, QConicalGradient
from PyQt6.QtCore import Qt, QRect, QRectF, QPoint


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 Drawing rectangle")
        self.setWindowIcon(QIcon('images/python.png'))

    def paintEvent(self, event) -> None:
        # self.drawRect()
        # self.drawEllipse()
        # self.drawText()
        # self.draw_lineargradient()
        # self.draw_riaialgradient()
        self.draw_conicalgradient()

    def drawRect(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.DashDotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green,Qt.BrushStyle.BDiagPattern))
        painter.drawRect(100, 15, 300, 100)

    def drawEllipse(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.DashDotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green,Qt.BrushStyle.BDiagPattern))
        painter.drawEllipse(100,100,400,200)

    def drawText(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.red, 5, Qt.PenStyle.DashDotLine))
        painter.setBrush(QBrush(Qt.GlobalColor.green, Qt.BrushStyle.BDiagPattern))
        painter.drawText(100,100,"PyQt6 Course")

        rect = QRect(100, 150, 250, 25)
        painter.drawRect(rect)
        painter.drawText(rect, Qt.AlignmentFlag.AlignCenter, "PyQt6 Course - udemy.com")

        document = QTextDocument()
        rect2 = QRectF(0,0, 250, 250)
        document.setTextWidth(rect2.width())
        document.setHtml("<b>Welcome to PyQt6 Course </b><i>Udemy Course </i> \n <font size = '15' color='red'>Enjoy The Course</font>")
        document.drawContents(painter, rect2)

    def draw_lineargradient(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))
        grad1 = QLinearGradient(25, 100, 150, 175)
        grad1.setColorAt(0.0, Qt.GlobalColor.red)
        grad1.setColorAt(0.5, Qt.GlobalColor.green)
        grad1.setColorAt(1.0, Qt.GlobalColor.yellow)
        painter.setBrush(QBrush(grad1))
        painter.drawRect(10, 10, 200, 200)

    def draw_riaialgradient(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 4, Qt.PenStyle.SolidLine))
        grad = QRadialGradient(100, 100, 100)
        grad.setColorAt(0.2, Qt.GlobalColor.red)
        grad.setColorAt(0.5, Qt.GlobalColor.green)
        grad.setColorAt(0.8, Qt.GlobalColor.yellow)
        painter.setBrush(QBrush(grad))
        # painter.drawEllipse(QPoint(100, 100), 100, 100)
        painter.drawRect(10,10,200,200)

    def draw_conicalgradient(self):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.GlobalColor.black, 5, Qt.PenStyle.SolidLine))

        conicalGradient = QConicalGradient(100,100, 10)
        conicalGradient.setColorAt(0.0, Qt.GlobalColor.red)
        conicalGradient.setColorAt(0.33, Qt.GlobalColor.green)
        conicalGradient.setColorAt(0.66, Qt.GlobalColor.yellow)
        conicalGradient.setColorAt(1.0, Qt.GlobalColor.red)
        painter.setBrush(QBrush(conicalGradient))

        painter.drawRect(10,10, 200, 200)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()
    sys.exit(app.exec())
