import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtWidgets import *

WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 1080


class PCPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PC GUI")
        self.viewWidgets()
        self.setGeometry(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setWindowIcon(QIcon(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/Light/icons8-pc-on-desk-96.png"))
        self.show()

    def viewWidgets(self):
        setup_GUI = QHBoxLayout()  # the first layout
        structure_GUI = QVBoxLayout()  # the second layout for the item to view
        button_GUI = QGridLayout()  # the gui for the light and dark modes

        # todo: fix the layout of the left side widget
        # todo: add the dummy data table

        left_side = QGridLayout()  # This layout is for the left side menu

        icon_border = QLabel()

        icon = QPixmap(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/User icon.png")

        icon_border.setPixmap(icon)
        icon_border.setGeometry(0, 0, icon.width(), icon.height())

        username = QLabel("Username")
        username.setAlignment(Qt.AlignRight)

        icon_border.show()

        button_1 = QPushButton("View connected accounts", self)
        button_1.setFixedSize(400, 100)

        button_2 = QPushButton("User information", self)
        button_2.setFixedSize(400, 100)

        button_3 = QPushButton("Settings", self)
        button_3.setFixedSize(400, 100)

        import_User_data = QPushButton("Import user data", self)

        left_side.addWidget(icon_border, 0, 0)
        left_side.addWidget(username, 0, 0)
        left_side.addWidget(button_1, 1, 0)
        left_side.addWidget(button_2, 2, 0)
        left_side.addWidget(button_3, 3, 0)
        left_side.addWidget(import_User_data, 4, 0)

        centre = QGridLayout()
        # insert table with data, replacing the maroon table
        model = QSqlTableModel()
        model.setTable("users")
        model.select()

        table = QTableView()
        table.setModel(model)

        centre.addWidget(table, 1, 2, 2, 2)

        structure_GUI.addLayout(left_side)

        setup_GUI.addLayout(structure_GUI)

        button_GUI.addLayout(centre, 200 - 1, 1)

        light_mode = QPushButton("Light mode", self)
        dark_mode = QPushButton("Dark mode", self)
        import_Data = QPushButton("Import Data", self)

        light_mode.setFixedSize(300, 100)
        dark_mode.setFixedSize(300, 100)

        light_mode.clicked.connect(self.viewLightModeButton)
        dark_mode.clicked.connect(self.viewDarkModeButton)

        button_GUI.addWidget(light_mode, 0, 2)
        button_GUI.addWidget(dark_mode, 0, 3)

        setup_GUI.addLayout(button_GUI)

        left_itemHolder = QWidget()
        left_itemHolder.setLayout(setup_GUI)
        self.setCentralWidget(left_itemHolder)

    def viewLightModeButton(self):
        self.setStyleSheet("background-color: red")
        self.setWindowIcon(QIcon(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/Light/icons8-pc-on-desk-96.png"))

    def viewDarkModeButton(self):
        self.setStyleSheet("background-color: #8d1b12")
        self.setWindowIcon(QIcon(
            "C:/Users/Trina/PycharmProjects/22-23_CE301_roy_trina/Design/images and backgrounds/icons/Dark/icons8-workstation-96.png"))

    def import_Data(self):
        options = QFileDialog.options()
        options |= QFileDialog.DontUseNativeDialog
        file_names, _ = QFileDialog.getOpenFileNames(None, "Select files to import", "",
                                                     "All Files (*);;CSV Files (*.csv)", options=options)
        if file_names:
            for file_name in file_names:
                with open(file_name, 'r') as file:
                    data = file.read()
                print(f"Imported file: {file_name}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    window = PCPage()

    window.show()

    sys.exit(app.exec_())
