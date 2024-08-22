import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, 
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt5.QtCore import QTimer, QTime, Qt

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00", self)
        self.start_button = QPushButton("Começar", self)
        self.stop_button = QPushButton("Parar", self)
        self.reset_button = QPushButton("Recomeçar", self)
        self.timer = QTimer(self)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("Cronômetro")

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
            QPushButton, QLabel{font-weight: bold}
            QPushButton{font-size: 20px}
            QLabel{font-size: 50px}
        """)

        self.start_button.clicked.connect(self.startT)
        self.stop_button.clicked.connect(self.stopT)
        self.reset_button.clicked.connect(self.resetT)
        self.timer.timeout.connect(self.updateDisplay)

    def startT(self):
        self.timer.start(10)

    def stopT(self):
        self.timer.stop()

    def resetT(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.formatT(self.time))

    def formatT(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}:{milliseconds:02}"

    def updateDisplay(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.formatT(self.time))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    stopwatch = Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())