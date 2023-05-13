import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from pc_gui import PCPage

from android_gui import AndroidPage
from iphone_gui import IPhonePage
from tablet_gui import TabletPage


class OpenPCGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(PCPage.viewWidgets)
        self.setWindowTitle(PCPage.windowTitle)
        self.setWindowIcon(QIcon(PCPage.icon))
        self.show()


class OpenAndroidGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(AndroidPage.setItems_onWindow)
        self.setWindowTitle(AndroidPage.windowTitle)
        self.setWindowIcon(QIcon(AndroidPage.icon))
        self.show()


class OpenIPhoneGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(IPhonePage.viewWidgetsOnPage)
        self.setWindowTitle(IPhonePage.windowTitle)
        self.setWindowIcon(QIcon(IPhonePage.icon))
        self.show()


class OpenTabletGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setLayout(TabletPage.addWidgets)
        self.setWindowTitle(TabletPage.windowTitle)
        self.setWindowIcon(QIcon(TabletPage.icon))
        self.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.window = None

        # Setting the look of the master GUI
        self.setWindowTitle("Master GUI page")
        self.setItemsOnPage()
        self.setWindowIcon(
            QIcon(
                "images and backgrounds/icons/Light/icons8-devices-64.png"))
        self.setGeometry(600, 200, 1200, 800)
        self.show()

    def setItemsOnPage(self):
        horizontal_layout = QVBoxLayout()

        pc_label = QLabel("PC GUI place")
        pc_gui_button = QPushButton("pc_gui_button", self)
        pc_gui_button.clicked.connect(self.openPCGUI)

        android_label = QLabel("Android GUI place")
        android_gui_button = QPushButton("android_gui_button", self)
        android_gui_button.clicked.connect(self.openAndroidGUI)

        iphone_label = QLabel("iPhone GUI place")
        i_phone_gui_button = QPushButton("i_phone_gui_button", self)
        i_phone_gui_button.clicked.connect(self.open_iPhoneGUI)

        tablet_label = QLabel("Tablet GUI place")
        tablet_gui_button = QPushButton("tablet_gui_button")
        tablet_gui_button.clicked.connect(self.openTabletGUI)

        horizontal_layout.setSpacing(30)

        horizontal_layout.addWidget(pc_label)
        horizontal_layout.addWidget(pc_gui_button)

        horizontal_layout.addWidget(android_label)
        horizontal_layout.addWidget(android_gui_button)

        horizontal_layout.addWidget(iphone_label)
        horizontal_layout.addWidget(i_phone_gui_button)

        horizontal_layout.addWidget(tablet_label)
        horizontal_layout.addWidget(tablet_gui_button)

        widget_container = QWidget()
        widget_container.setLayout(horizontal_layout)
        self.setCentralWidget(widget_container)

    def openPCGUI(self):
        if self.window is None:
            self.window = QMainWindow()
            self.ui = PCPage()
            self.ui.viewWidgets()
            self.window.show()

        else:
            self.window.close()
            self.window = None

    def openAndroidGUI(self):
        if self.window is None:
            self.window = QMainWindow()
            self.ui = AndroidPage()
            self.ui.setItems_onWindow()
            self.window.show()

        else:
            self.window.close()
            self.window = None

    def openTabletGUI(self):
        if self.window is None:
            self.window = QMainWindow()
            self.ui = TabletPage()
            self.ui.attachWidgets()
            self.window.show()

        else:
            self.window.close()
            self.window = None

    def open_iPhoneGUI(self):
        if self.window is None:
            self.window = QMainWindow()
            self.ui = IPhonePage()
            self.ui.viewWidgetsOnPage()
            self.window.show()
        else:
            self.window.close()
            self.window = None


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
