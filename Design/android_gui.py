import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget, QGridLayout


# The model of the device is: Android Small from Figma
class AndroidPage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Android GUI")
        self.setItems_onWindow()
        self.setGeometry(0, 0, 900, 1100)
        self.setStyleSheet("background-color: pink")
        self.setWindowIcon(QIcon(
            "/Design/images and backgrounds/icons/Light/icons8-android-os-96.png"))
        self.show()

    def setItems_onWindow(self):
        page_layout = QGridLayout()

        light_mode = QPushButton("Light mode", self)
        light_mode.setFixedSize(200, 100)

        dark_mode = QPushButton("Dark mode", self)
        dark_mode.setFixedSize(200, 100)

        light_mode.clicked.connect(self.viewLightMode)
        dark_mode.clicked.connect(self.viewDarkMode)

        page_layout.addWidget(light_mode, 0, 0)
        page_layout.addWidget(dark_mode, 1, 0)

        widget = QWidget()
        widget.setLayout(page_layout)
        self.setCentralWidget(widget)

    def viewLightMode(self):
        self.setStyleSheet("background-color: pink")
        self.setWindowIcon(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/Light/icons8-android-os-96.png")

    def viewDarkMode(self):
        self.setStyleSheet("background-color: #8d1b12")
        self.setWindowIcon(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/Dark/icons8-android-50.png")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = AndroidPage()
    window.show()

    sys.exit(app.exec_())
