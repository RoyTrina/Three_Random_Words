import random
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html

class User:
    def __init__(self, ID_number, user, passphrase):
        """

        :type passphrase: str
        :type ID_number: int
        :type user: str
        """
        self.ID = ID_number
        self.username = user
        self.password = passphrase

    def username_Generator(self):
        characters = "!£$%^&*()_+~@?¬|"
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        username = "".format()
        return username

    def password_Generator(self):
        characters = "!£$%^&*()_+~@?¬|"
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        numbers = "0123456789"
        password = "".format()
        return password

    def ID_generator(self):
        ID = random.randint(0, 10000)
        ID_string = "{:3d}".format(ID)
        print(ID_string)

    def PIN_generator(self):
        PIN = random.randint(1, 19999)
        PIN_string = "{:5d}".format(PIN)
        return PIN_string


class RegisterSystem(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register")
        self.viewWidgets()
        self.show()

    def view_Widgets(self):
        page_Layout = QHBoxLayout()

        page_Layout.setAlignment(Qt.AlignVCenter)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def register_Form(self):
        layout = QFormLayout()

        userLabel = QLabel("Username: ")
        userTextLabel = QLineEdit()

        emaiLabel = QLabel("Email: ")
        emailTextLabel = QLineEdit()

        passLabel = QLabel("Password: ")
        passTextLabel = QLineEdit().Password

        layout.addRow(userLabel, userTextLabel)
        layout.addRow(emaiLabel, emailTextLabel)
        layout.addRow(passLabel, passTextLabel)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def PIN(self):
        layout = QHBoxLayout()

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def store_Info_In_Database(self):
        ID = self.ID_generator().text
        username = self.username_Generator().text
        password = self.password_Generator()

        query = "INSERT INTO users VALUES()"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = RegisterSystem()
    window.show()

    sys.exit(app.exec_())
