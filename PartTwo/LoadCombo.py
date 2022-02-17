from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QDoubleSpinBox, QLabel, QComboBox
from PyQt6.QtGui import QIcon
from PyQt6 import uic

class UI(QWidget):
    def __init__(self):
        super().__init__()

        uic.loadUi("ComboDemo.ui", self)

        self.label_result: QLabel = self.findChild(QLabel, "label_result")
        self.combo: QComboBox = self.findChild(QComboBox, "comboBox")
        self.combo.currentTextChanged.connect(self.combo_changed)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText("Your Favorite Language: " + item)


if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('Image/python.png'))
    window = UI()
    window.show()

    sys.exit(app.exec())
