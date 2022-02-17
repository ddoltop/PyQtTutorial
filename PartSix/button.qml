import QtQuick 2.5
import QtQuick.Controls 2.5


ApplicationWindow {
    visible:true
    width:600
    height:400
    title:"Button Example"

    Button {
        text:"Click ME"
        id:mybutton
//        y:70
//        x:70
        anchors.centerIn:parent
        background:Rectangle {
            implicitWidth:100
            implicitHeight:40
            color:button.down ? "#d6d6d6" : "#f6f6f6"
            border.color:"#26282a"
            border.width:1
            radius:4
        }
    }

    onClicked: {
        window.hellow()
    }
}