import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QGridLayout, QWidget


# The model of the device is: iPhone 14
class IPhonePage(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("iPhone GUI")
        self.viewWidgetsOnPage()
        self.setGeometry(0, 0, 1000, 1100)
        self.setStyleSheet("background-color: pink")
        self.setWindowIcon(
            QIcon(
                "/Design/images and backgrounds/icons/Light/icons8-iphone-14-96.png"))

    def viewWidgetsOnPage(self):
        # todo: add left button menu with functionality
        layout = QGridLayout()

        light_mode = QPushButton("Light mode", self)
        dark_mode = QPushButton("Dark mode", self)

        light_mode.clicked.connect(self.viewLightMode)
        dark_mode.clicked.connect(self.viewDarkMode)

        layout.addWidget(light_mode, 0, 0)
        layout.addWidget(dark_mode, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def viewLightMode(self):
        self.setStyleSheet("background-color: pink")
        self.setWindowIcon(QIcon(
            "/Design/images and backgrounds/icons/Light/icons8-iphone-14-96.png"))

    def viewDarkMode(self):
        self.setStyleSheet("background-color: #8d1b12")
        self.setWindowIcon(QIcon(
            "/Design/images and backgrounds/icons/Dark/icons8-iphone-14-50.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = IPhonePage()
    window.show()

    sys.exit(app.exec_())
