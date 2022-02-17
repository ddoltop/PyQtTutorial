from typing import Union

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QPieSeries, QBarSet , QPercentBarSeries
from PyQt6.QtCore import QPointF, Qt
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 LineChart")
        self.setWindowIcon(QIcon('images/python.png'))

        self.bar_chart()

    def bar_chart(self):
        set0 = QBarSet("Parwiz")
        set1 = QBarSet("John")
        set2 = QBarSet("Bob")
        set3 = QBarSet("Nawiz")

        set0 << 1 << 2 << 3 << 4 << 5 << 6
        set1 << 5 << 7 << 0 << 10 << 1 << 3
        set2 << 3 << 2 << 1 << 4 << 5 << 6
        set3 << 4 << 5 << 6 << 2 << 1 << 0

        series = QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)

        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        chart.setTitle("BarChart Example")

        chartview = QChartView(chart)
        self.setCentralWidget(chartview)


    def pie_chart(self):
        series = QPieSeries()
        series.append("Python", 90)
        series.append("C++", 80)
        series.append("Java", 60)
        series.append("C#", 30)

        #add slice
        my_slice = series.slices()[2]
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)
        chart.setTitle("Pie Chart Example")
        chart.setTheme(QChart.ChartTheme.ChartThemeBrownSand)
        # chart.legend().setVisible(False)
        chart.legend().setAlignment(Qt.AlignmentFlag.AlignBottom)

        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)

    def line_chart(self):
        series = QLineSeries()
        series.append([
            QPointF(1.0, 1.8), QPointF(2.0, 73.0), QPointF(3.0, 268.0),
            QPointF(4.0, 17.0), QPointF(5.0, 120.0), QPointF(6.0, 210.0)
        ])
        chart = QChart()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setTitle("LineChart Example")
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setTheme(QChart.ChartTheme.ChartThemeBlueIcy)

        chartview = QChartView(chart)
        self.setCentralWidget(chartview)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())