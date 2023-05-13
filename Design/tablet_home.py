import sys

from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QPushButton, QWidget


class OpenTabletGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(TabletPage.addWidgets)
        self.setWindowTitle(TabletPage.windowTitle)
        self.setWindowIcon(QIcon(TabletPage.icon))


class TabletHome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1024, 1366)
        self.addWidget()
        self.show()

    def addWidget(self):
        layout = QGridLayout()

        login_button = QPushButton("Login", self)

        register = QPushButton("Register", self)

        light_mode = QPushButton("Light mode", self)

        dark_mode = QPushButton("Dark mode", self)

        layout.addWidget(login_button, 4, 2)
        layout.addWidget(register, 4, 3)

        layout.addWidget(light_mode, 0, 2)
        layout.addWidget(dark_mode, 0, 3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def login(self):
        if login_button.clicked.connect:
            print("THE LOGIN BUTTON HAS BEEN PRESSED")
        else:
            print("The login button has not been pressed")

    def register(self):
        if register.clicked.connect:
            print("THE register button HAS BEEN PRESSED")
        else:
            print("The register button has not been pressed")

    def viewLightMode(self):
        self.setStyleSheet("background-color: red")
        self.setWindowIcon(QIcon(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/Light/icons8-pc-on-desk-96.png"))

    def viewDarkMode(self):
        self.setStyleSheet("background-color: #8d1b12")
        self.setWindowIcon(QIcon(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/Dark/icons8-workstation-96.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = TabletHome()
    window.show()

    sys.exit(app.exec_())
