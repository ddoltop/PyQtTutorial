from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QLabel, QVBoxLayout, QTableWidgetItem, QDialog,QMainWindow
from PyQt6.QtGui import QIcon, QFont
from PyQt6.QtCore import QTime, QTimer

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 QTableWidget")
        self.setWindowIcon(QIcon('Image/python.png'))

        # add code
        vbox = QVBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(3)
        table_widget.setColumnCount(3)
        table_widget.setItem(0, 0, QTableWidgetItem("Name"))
        table_widget.setItem(0, 1, QTableWidgetItem("Email"))
        table_widget.setItem(0, 2, QTableWidgetItem("Phone"))

        table_widget.setItem(1, 0, QTableWidgetItem("Parwiz"))
        table_widget.setItem(1, 1, QTableWidgetItem("parwiz@gmail.com"))
        table_widget.setItem(1, 2, QTableWidgetItem("666556"))

        table_widget.setItem(2, 0, QTableWidgetItem("John"))
        table_widget.setItem(2, 1, QTableWidgetItem("john@gmai.com"))
        table_widget.setItem(2, 2, QTableWidgetItem("666555"))

        vbox.addWidget(table_widget)
        self.setLayout(vbox)


if __name__ == "__main__":
    import sys
    app = QApplication([])
    app.setWindowIcon(QIcon('Image/python.png'))
    window = Window()
    window.show()

    sys.exit(app.exec())
