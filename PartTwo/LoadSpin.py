from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox
from PyQt6.QtGui import QIcon
from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("DoubleSpinDemo.ui", self)
        self.linePrice = self.findChild(QLineEdit, "lineEdit_price")
        self.doubleSpin = self.findChild(QDoubleSpinBox, "doubleSpinBox")
        self.lineResult = self.findChild(QLineEdit, "lineEdit_total")

        self.doubleSpin.valueChanged.connect(self.spin_selected)

    def spin_selected(self):
        if self.linePrice.text() != 0:
            price = int(self.linePrice.text())
            total_price = self.doubleSpin.value() * price
            self.lineResult.setText(str(total_price))


if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('../Image/python.png'))
    window = UI()
    window.show()

    app.exec(app.exec())
