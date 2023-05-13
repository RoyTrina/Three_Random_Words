import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication, QWidget, QGridLayout


# The model of the device is: iPad Pro 12.9"
class TabletPage(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tablet GUI")
        self.attachWidgets()
        self.setFixedSize(1024, 1366)
        self.setStyleSheet("background-color: pink")
        self.setWindowIcon(
            QIcon("/Design/images and backgrounds/icons/Light/"))

    def attachWidgets(self):
        # todo: add left button menu with functionality
        layout = QGridLayout()

        light_mode = QPushButton("Light mode", self)
        dark_mode = QPushButton("Dark mode", self)

        layout.addWidget(light_mode)
        layout.addWidget(dark_mode)

        light_mode.clicked.connect(self.viewLightMode)
        dark_mode.clicked.connect(self.viewDarkMode)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def viewLightMode(self):
        self.setStyleSheet("background-color: #fc4c4e")
        self.setWindowIcon(QIcon(
            "/Design/images and backgrounds/icons/Light/icons8-ipad-pro-96.png"))

    def viewDarkMode(self):
        self.setStyleSheet("background-color: #8d1b12")
        self.setWindowIcon(QIcon(
            "/Design/images and backgrounds/icons/Dark/icons8-ipad-pro-50.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = TabletPage()
    window.show()

    sys.exit(app.exec_())
