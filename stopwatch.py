import sys 
from time import sleep

from PyQt5.QtCore import Qt, QThread, pyqtSignal, QTimer
from PyQt5.QtGui import QFont

from PyQt5.QtWidgets import (
    
    QPushButton,
    QApplication,
    QMainWindow,
    QWidget,
    QLabel
)


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stopwatch_thread = StopWatchThread()
        self.stopwatch_thread.progress.connect(self.update_time)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Stopwatch")
        self.resize(350, 200)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setStyleSheet("background-color : black")

        # labels for stopwatch
        self.label = QLabel(self)
        self.label.setGeometry(50, 10, 250, 70)
        self.label.setText(str(self.stopwatch_thread.elapsed_time))  # Use thread's elapsed_time
        self.label.setFont(QFont('Arial', 20))
        self.label.setStyleSheet("color : white")
        self.label.setAlignment(Qt.AlignCenter)

        # stopwatch buttons
        self.startButton = QPushButton("Start",self)
        self.pauseButton = QPushButton("Pause",self)
        self.resetButton = QPushButton("Reset",self)

        # connecting the buttons 
        self.startButton.clicked.connect(self.startButtonFun)
        self.pauseButton.clicked.connect(self.pauseButtonFun)
        self.resetButton.clicked.connect(self.resetButtonFun)

        # button size
        self.startButton.setGeometry(50, 80, 70, 30) 
        self.pauseButton.setGeometry(145, 80, 70, 30) 
        self.resetButton.setGeometry(235, 80, 70, 30) 

        # creating timer object
        timer = QTimer(self)
        timer.start(100)

    # stopwatch start button function
    def startButtonFun(self):
        if not self.stopwatch_thread.isRunning():
            self.stopwatch_thread.running = True
            self.stopwatch_thread.start()

    # stopwatch pause button function
    def pauseButtonFun(self):
        self.stopwatch_thread.running = False

    # stopwatch reset button function
    def resetButtonFun(self):
        self.pauseButtonFun()
        self.stopwatch_thread.elapsed_time = 0
        self.update_time(0)

    # updating time 
    def update_time(self, elapsed_time):
        self.label.setText(str(elapsed_time / 10))

class StopWatchThread(QThread):
    progress = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.running = False
        self.elapsed_time = 0

    def run(self):
        while self.running:
            self.elapsed_time+=1
            self.progress.emit(self.elapsed_time)
            self.msleep(100)


def main():
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
    
if __name__ =="__main__":
    main()