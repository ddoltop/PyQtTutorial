from typing import Union

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QPieSeries, QBarSet, QBarSeries
from PyQt6.QtCore import QPointF, Qt
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt6 LineChart")
        self.setWindowIcon(QIcon('images/python.png'))

        series = QPieSeries()
        series.setHoleSize(0.40)

        series.append('Protein 4.3 %', 4.3)

        my_slice = series.append('Fat 15.6 %', 15.6)
        my_slice.setExploded(True)
        my_slice.setLabelVisible(True)
        series.append('Other 30 %', 30)
        series.append("Carbs 57 %", 57)

        chart = QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QChart.AnimationOption.SeriesAnimations)
        chart.setTitle("Donut Chart")
        chart.setTheme(QChart.ChartTheme.ChartThemeDark)
        chart.createDefaultAxes()

        chart_view = QChartView(chart)

        self.setCentralWidget(chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
