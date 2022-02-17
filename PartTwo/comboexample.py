from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QLabel, QHBoxLayout
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle("PyQt6 QComboBox")
        self.setWindowIcon(QIcon('Image/python.png'))

        self.create_combo()

    def create_combo(self):
        hbox = QHBoxLayout()

        label = QLabel("Select Account Type: ")
        label.setFont(QFont("Times", 15))

        self.combo = QComboBox()
        self.combo.addItem("Deposit Account")
        self.combo.addItem("Current Account")
        self.combo.addItem("Saving Account")

        self.combo.currentIndexChanged.connect(self.combo_changed)

        vbox = QVBoxLayout()
        self.label_result = QLabel("Hello")
        self.label_result.setFont(QFont("Times", 15))

        vbox.addWidget(self.label_result)
        vbox.addLayout(hbox)

        hbox.addWidget(label)
        hbox.addWidget(self.combo)

        self.setLayout(vbox)

    def combo_changed(self):
        item = self.combo.currentText()
        self.label_result.setText("Your Account Type Is : " + item)

if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()

    sys.exit(app.exec())
