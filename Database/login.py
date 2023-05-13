import sys

from PyQt5.QtWidgets import *


class LoginSystem(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login Page")
        self.view_Page()
        self.show()

    def view_Page(self):
        label_layout = QGridLayout()  # layout for the label
        buttonLayout = QGridLayout()  # layout for the buttons
        displayLayout = QGridLayout()  # the encompassing layout

        text = QLabel("Hello, how would you like to log in?")

        font = text.font()
        font.setPointSize(28)
        text.setFont(font)

        cameraButton = QPushButton("Camera", self)
        cameraButton.setFixedSize(300, 100)

        login_form = QPushButton("Login form", self)
        login_form.setFixedSize(300, 100)

        pin = QPushButton("PIN", self)
        pin.setFixedSize(300, 100)

        voiceButton = QPushButton("Voice", self)
        voiceButton.setFixedSize(300, 100)

        cameraButton.clicked.connect(self.faceDetection)
        login_form.clicked.connect(self.login_Form)
        pin.clicked.connect(self.PIN)
        voiceButton.clicked.connect(self.voiceDetection)

        label_layout.addWidget(text)

        buttonLayout.addWidget(cameraButton)
        buttonLayout.addWidget(login_form)
        buttonLayout.addWidget(pin)
        buttonLayout.addWidget(voiceButton)
        displayLayout.addWidget(label_layout)
        displayLayout.addWidget(buttonLayout)

        widget = QWidget()
        widget.setLayout(displayLayout)
        self.setCentralWidget(widget)

    def login_Form(self):
        formLayout = QVBoxLayout()

        username_form = QLabel()
        userLabel = QLineEdit()

        email = QLabel()
        email_Label = QLineEdit()

        password_Label = QLabel()
        password = QLineEdit().Password
        password.setEchoMode(True)

        formLayout.addWidget(userLabel, 2)
        formLayout.addWidget(username_form)
        formLayout.addWidget(email_Label)
        formLayout.addWidget(email)
        formLayout.addWidget(password_Label)
        formLayout.addWidget(password)

        formHolder = QWidget()
        formHolder.setLayout(formLayout)
        self.setCentralWidget(formHolder)

    def PIN(self):
        pin_Layout = QHBoxLayout()

        widget = QWidget()
        self.setCentralWidget(widget)

    def faceDetection(self):
        face

    def voiceDetection(self):

        widget = QWidget()
        self.setCentralWidget(widget)

    def verify_Info(self):
        if self.cameraButton.clicked.connect() is True:
            verifyFace()
        else:
            if self.login_form.clicked.connect() is True:
                login_Form()

    # get the info

    # Look up in the login table in the database
    ID = 00000
    username = "admin"
    password = "123456789"

    def verifyFace(self):
        faceDetection()


# if face has been stored in the database

# look for it


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = LoginSystem()
    window.show()

    sys.exit(app.exec_())
