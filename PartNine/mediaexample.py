from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QStyle, QSlider, QLabel, QFileDialog
from PyQt6.QtGui import QIcon
from PyQt6.QtMultimedia import QMediaPlayer, QMediaMetaData
from PyQt6.QtMultimediaWidgets import QVideoWidget
from PyQt6.QtCore import Qt, QUrl


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200, 200, 700, 400)
        self.setWindowTitle("PyQt Media Player")
        self.setWindowIcon(QIcon('player.ico'))

        self.mediaplayer = QMediaPlayer(None)
        videowidget = QVideoWidget()
        # videowidget.resize(400, 300)
        # videowidget.show()

        openBtn = QPushButton("Open Video")
        self.playBtn = QPushButton()
        self.playBtn.setEnabled(False)
        self.playBtn.setIcon(self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay))

        self.slider = QSlider(Qt.Orientation.Horizontal)
        self.slider.setRange(0, 1)
        self.slider.sliderMoved.connect(self.set_position)

        # self.

        hbox = QHBoxLayout()
        hbox.addWidget(openBtn)
        hbox.addWidget(self.playBtn)
        hbox.addWidget(self.slider)

        vbox = QVBoxLayout()
        vbox.addWidget(videowidget)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.mediaplayer.setVideoOutput(videowidget)
        openBtn.clicked.connect(self.open_file)
        self.playBtn.clicked.connect(self.play_video)
        self.mediaplayer.mediaStatusChanged.connect(self.mediastate_changed)
        self.mediaplayer.positionChanged(self.position_change)
        self.mediaplayer.durationChanged.connect(self.duration_changed)


    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(self, "Open Video")
        if filename != '':
            self.mediaplayer.setObjectName(QMediaContent(QUrl.fromLocalFile(filename)))
            self.playBtn.setEnabled(True)

    def play_video(self):
        if self.mediaplayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaplayer.pause()
        else:
            self.mediaplayer.play()

    def mediastate_changed(self):
        if self.mediaplayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPause)
            )
        else:
            self.playBtn.setIcon(
                self.style().standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
            )

    def position_changed(self, position):
        self.slider.setValue(position)

    def duration_changed(self, duration):
        self.slider.setRange(0, duration)

    def set_position(self, position):
        self.mediaplayer.setPosition(position)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('player.ico'))
    window = Window()
    window.show()
    sys.exit(app.exec())
