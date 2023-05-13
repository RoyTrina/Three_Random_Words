import sys

from PIL import Image
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QPushButton, QWidget


class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout()
        self.setWindowIcon()
        self.setWindowTitle()
        self.show()


class RegisterPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout()
        self.setWindowIcon()
        self.setWindowTitle()
        self.show()


class IPhoneHome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1000, 1100)
        # insert picture of a gif
        pic = Image.open("")

        self.addItems()
        self.show()

    def addItems(self):
        iPhone_layout = QGridLayout()

        iPhone_login_button = QPushButton("Login", self)

        iPhone_register = QPushButton("Register", self)

        light_mode = QPushButton("Light mode", self)

        dark_mode = QPushButton("Dark mode", self)

        iPhone_layout.addWidget(light_mode, 0, 2)
        iPhone_layout.addWidget(dark_mode, 0, 3)
        iPhone_layout.addWidget(iPhone_login_button, 4, 2)
        iPhone_layout.addWidget(iPhone_register, 4, 3)

        iPhone_register.clicked.connect()
        iPhone_login_button.clicked.connect()

        light_mode.clicked.connect()
        dark_mode.clicked.connect()

        iPhone_widget = QWidget()
        iPhone_widget.setLayout(iPhone_layout)
        self.setCentralWidget(iPhone_widget)

    @staticmethod
    def iPhone_login(self):
        if login_button.clicked.connect:
            print("THE LOGIN BUTTON HAS BEEN PRESSED")
        else:
            print("The login button has not been pressed")

    @staticmethod
    def iPhone_register(self):
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

    window = IPhoneHome()
    window.show()

    sys.exit(app.exec_())
