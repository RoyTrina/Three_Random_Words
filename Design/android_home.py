import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QApplication, QGridLayout, QPushButton, QWidget


class OpenRegister(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout()
        self.setWindowTitle("")
        self.setWindowIcon(QIcon(""))


class OpenLogin(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout("")
        self.setWindowTitle("")
        self.setWindowIcon(QIcon(""))


class OpenAndroidPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(AndroidPage.setItems_onWindow)
        self.setWindowTitle(AndroidPage.windowTitle)
        self.setWindowIcon(QIcon(AndroidPage.icon))


class AndroidHome(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = ""
        self.window = QMainWindow()
        self.ui = ""
        self.window = QMainWindow()
        self.setFixedSize(900, 1100)
        self.addWidget()
        self.show()

    def addWidget(self):
        layout = QGridLayout()

        login_button = QPushButton("Login", self)

        register = QPushButton("Register", self)

        light_mode = QPushButton("Light mode", self)

        dark_mode = QPushButton("Dark mode", self)

        login_button.clicked.connect(self.login_Android)
        register.clicked.connect(self.register)

        light_mode.clicked.connect(self.light_view_mode)
        dark_mode.clicked.connect(self.dark_view_mode)

        layout.addWidget(login_button, 4, 2)
        layout.addWidget(register, 4, 3)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def login_Android(self):
        if login_button.clicked.connect:
            if self.window is None:
                pass

        else:
            print("The login button has not been pressed")

    def register(self):
        if register.clicked.connect:
            if self.window is None:
                pass
        else:
            print("The register button has not been pressed")

    def light_view_mode(self):
        self.setStyleSheet("background-color: red")
        self.setWindowIcon(QIcon(
            "/Design/images and backgrounds/icons/Light/icons8-pc-on-desk-96.png"))

    def dark_view_mode(self):
        self.setStyleSheet("background-color: #8d1b12")
        self.setWindowIcon(QIcon(
            "/Design/images and backgrounds/icons/Dark/icons8-workstation-96.png"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = AndroidHome()
    window.show()

    sys.exit(app.exec_())
