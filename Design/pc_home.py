import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

from Database.login import LoginSystem
from Database.register import RegisterSystem
from pc_gui import PCPage


class OpenLogin(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(LoginSystem.view_Page)
        self.setWindowTitle(LoginSystem.windowTitle)
        self.setWindowIcon(QIcon(LoginSystem.icon))
        self.show()


class OpenRegister(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(RegisterSystem.view_Widgets)
        self.setWindowTitle(RegisterSystem.windowTitle)
        self.setWindowIcon(QIcon(RegisterSystem.icon))
        self.show()


class OpenPC(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(PCPage.viewWidgets)
        self.setWindowTitle(PCPage.windowTitle)
        self.setWindowIcon(QIcon(PCPage.icon))
        self.show()


WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


class PCHome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.window = None

        self.setWindowTitle("PC page")
        self.setWindowIcon(QIcon("/images and backgrounds/icons/Light/icons8-pc-on-desk-96.png"))
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.showPage()
        self.show()

    def showPage(self):
        PC_layout = QGridLayout()

        login_button = QPushButton("Login", self)

        register_button = QPushButton("Register", self)

        light_mode = QPushButton("Light mode", self)

        dark_mode = QPushButton("Dark mode", self)

        PC_layout.addWidget(light_mode, 0, 2)
        PC_layout.addWidget(dark_mode, 0, 3)
        PC_layout.addWidget(login_button, 4, 2)
        PC_layout.addWidget(register_button, 4, 3)

        login_button.clicked.connect(self.login)
        register_button.clicked.connect(self.register)
        light_mode.clicked.connect(self.viewLightMode)
        dark_mode.clicked.connect(self.viewDarkMode)

        widget = QWidget()
        widget.setLayout(PC_layout)
        self.setCentralWidget(widget)

    def login(self):
        if self.window is None:
            self.window = QMainWindow()
            self.ui = LoginSystem()
            self.ui.view_Page()
            self.window.show()

        else:
            self.window.close()
            self.window = None

    def register(self):
        if self.window is None:
            self.window = QMainWindow()
            self.ui = RegisterSystem()
            self.ui.view_Widgets()
            self.window.show()
        else:
            self.window.close()
            self.window = None

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

    window = PCHome()
    window.show()

    sys.exit(app.exec_())
