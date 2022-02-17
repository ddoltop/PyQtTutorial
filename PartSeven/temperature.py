from typing import Union

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QPieSeries, QBarSet, QStackedBarSeries, QValueAxis,QBarCategoryAxis
from PyQt6.QtCore import QPointF, Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 LineChart")
        self.setWindowIcon(QIcon('images/python.png'))

        low = QBarSet("Min")
        high = QBarSet("Max")

        low.append([-52, -50, -45.3, -37.0, -25.6, -8.0,
                    -6.0, -11.8, -19.7, -32.8, -43.0, -48.0])
        high.append([11.9, 12.8, 18.5, 26.5, 32.0, 34.8,
                     38.2, 34.8, 29.8, 20.4, 15.1, 11.8])

        series = QStackedBarSeries()
        series.append(low)
        series.append(high)
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Temperature Record in Celsius")
        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                      "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        axis_x = QBarCategoryAxis()
        axis_x.append(categories)
        axis_x.setTitleText("Month")

        chart.addAxis(axis_x, Qt.AlignmentFlag.AlignBottom)
        axis_y = QValueAxis()
        axis_y.setRange(-52, 52)
        axis_y.setTitleText("Temperature [&deg;C]")
        chart.addAxis(axis_y, Qt.AlignmentFlag.AlignLeft)

        series.attachAxis(axis_x)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())