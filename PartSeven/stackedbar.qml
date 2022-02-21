import QtQuick
import QtQuick.Controls
import QtCharts 2.0

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"BarChart"

    ChartView {
        anchors.fill:parent
        theme:ChartView.ChartThemeLight

        StackedBarSeries {
            id:myseries
            axisX:Bar
        }
    }
}