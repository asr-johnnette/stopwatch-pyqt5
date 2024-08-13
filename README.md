 stopwatch-pyqt5
for understanding the threading, creating the stopwatch.

This code creates a simple stopwatch application using PyQt5, where the time is tracked in a separate thread to ensure that the user interface remains responsive. Below is an explanation of how each part of the code works.

**Imports and Global Setup**
- sys: Provides access to some system-specific parameters and functions.
- time.sleep: Pauses execution for a specified amount of time.
- PyQt5.QtCore: Contains the core classes for PyQt5, such as threading (QThread), signals (pyqtSignal), and timers (QTimer).
- PyQt5.QtGui: Contains classes for graphics and font (QFont).
- PyQt5.QtWidgets: Provides classes for the user interface elements such as buttons (QPushButton), windows (QMainWindow), labels (QLabel), and the application itself (QApplication).

 **Window Class**

This class defines the main window of the application:

 **Initialization (__init__ method)**
- The __init__ method is the constructor of the Window class. It initializes the stopwatch by creating an instance of the StopWatchThread class, connects the thread's signal to a method (update_time), and sets up the user interface by calling setupUi().

 **User Interface Setup (setupUi method)**
- self.setWindowTitle("Stopwatch"): Sets the window's title to "Stopwatch".
- self.resize(350, 200): Sets the window's size.
- self.centralWidget = QWidget(): Creates a central widget that will hold other UI components.
- self.centralWidget.setStyleSheet("background-color : black"): Sets the background color of the central widget to black.
  
 **Label for Displaying Time**
- self.label: A QLabel that displays the elapsed time. The text is initially set to the thread's elapsed_time.
- self.label.setGeometry(50, 10, 250, 70): Positions the label within the window.
- self.label.setFont(QFont('Arial', 20)): Sets the font of the label to Arial, size 20.
- self.label.setStyleSheet("color : white"): Sets the text color to white.
- self.label.setAlignment(Qt.AlignCenter): Aligns the text to the center of the label.

 **Stopwatch Control Buttons**
- The window has three buttons (Start, Pause, Reset) that control the stopwatch:
  - These buttons are connected to their respective methods (startButtonFun, pauseButtonFun, resetButtonFun) using the clicked.connect method.
  - The geometry and size of the buttons are set using setGeometry.

 **QTimer**
- A QTimer is created but not explicitly used in this version of the code. It is started with an interval of 100 milliseconds but is not connected to any specific functionality.

 **Button Functionality**

- **Start Button (startButtonFun method):**
  - Starts the stopwatch by setting self.stopwatch_thread.running to True and then starting the thread using self.stopwatch_thread.start(). The thread will only start if it is not already running, ensuring multiple threads are not started simultaneously.

- **Pause Button (pauseButtonFun method):**
  - Pauses the stopwatch by setting self.stopwatch_thread.running to False. The thread will continue to run but won't update the elapsed time.

- **Reset Button (resetButtonFun method):**
  - Resets the stopwatch by pausing it and then setting the elapsed time to 0. It updates the display to show the reset time.

- **Update Time (update_time method):**
  - This method is called whenever the thread emits the progress signal. It updates the label with the current elapsed time.

 **StopWatchThread Class**
This class handles the stopwatch's timing functionality in a separate thread:

 **Initialization (__init__ method)**
- self.running: A boolean variable that controls whether the stopwatch is running or paused.
- self.elapsed_time: Tracks the elapsed time in tenths of a second.

 **Run Method (run method)**
- The run method is executed when the thread starts. It continuously increments self.elapsed_time and emits the progress signal with the current time as long as self.running is True.
- The thread sleeps for 100 milliseconds between each increment to simulate real-time tracking.

 **Main Function**
- The main function sets up and starts the PyQt5 application. It creates an instance of the Window class, shows the window, and starts the event loop with sys.exit(app.exec()).
