import QtQuick
import QtQuick.Controls
import QtCharts

ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"BarChart"

    ChartView {
        anchors.fill:parent
        theme:ChartView.ChartThemeLight
    }

    BarSeries {
        id:myseries
        axisX: BarCategoryAxis {categories : ["2016", "2017", "2018", "2019", "2020","2021"]}
    }
}