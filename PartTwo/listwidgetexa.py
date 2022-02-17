from PyQt6.QtWidgets import QApplication, QWidget, QListWidget, QLabel, QVBoxLayout, QListWidgetItem
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QListWidget")
        self.setWindowIcon(QIcon('Image/python.png'))

        # add code
        vbox = QVBoxLayout()
        self.list_widget = QListWidget()
        self.list_widget.insertItem(0, "Python")
        self.list_widget.insertItem(1, "Java")
        self.list_widget.insertItem(2, "C++")
        self.list_widget.insertItem(3, "C#")
        self.list_widget.insertItem(4, "Kotlin")

        self.list_widget.setFont(QFont("Times", 15))
        self.list_widget.setStyleSheet('background-color:gray')

        self.list_widget.clicked.connect(self.item_clicked)

        self.label = QLabel("")
        self.label.setFont(QFont("Times", 15))

        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def item_clicked(self):
        item: QListWidgetItem = self.list_widget.currentItem()
        self.label.setText("You have selected: " + str(self.list_widget.row(item)) + " text: " + str(item.text()))

if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()

    sys.exit(app.exec())
