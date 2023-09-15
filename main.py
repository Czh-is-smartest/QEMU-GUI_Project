__version__ = "0.0.1"

import re
import sys
import tkinter
from subprocess import check_output
from tkinter import filedialog as file_path

from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow

main_window = uic.loadUiType(r"ui\main_window.ui")[0]
about_window = uic.loadUiType(r"ui\about_window.ui")[0]
create_vhd_window = uic.loadUiType(r"ui\create_vhd_window.ui")[0]


def tk_init():
    tk = tkinter.Tk()
    tk.withdraw()
    tk.iconbitmap(r"img\qemu.ico")


class MainWindow(QtWidgets.QMainWindow, main_window):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.window = None
        tk_init()
        self.setupUi(self)
        app_icon = QtGui.QIcon("img\\qemu.ico")
        self.setWindowIcon(app_icon)
        self.open_button.clicked.connect(self.ask_file_path)
        self.about_menu.triggered.connect(self.show_about_window)
        self.open_menu.triggered.connect(self.ask_file_path)
        self.create_menu.triggered.connect(self.show_create_vhd_window)
        self.path = ""

    def ask_file_path(self):
        self.path = file_path.askopenfilename(
            title="打开", filetypes=(("虚拟机配置文件", "*.vmcf"), ("所有文件", "*.*"))
        )

    def show_about_window(self):
        self.window = AboutWindow(self)
        self.window.show()

    def show_create_vhd_window(self):
        self.window = CreateVHDWindow(self)
        self.window.show()


class AboutWindow(QtWidgets.QMainWindow, about_window):
    def __init__(self, parent=main_window):
        super(AboutWindow, self).__init__(parent=parent)
        self.qemu_version_text = None
        self.setupUi(self)
        self.get_version()

    def get_version(self):
        self.qemu_version_text = re.search(
            r"\d.*",
            check_output(".\\qemu\\qemu-system-x86_64 --version")
            .decode()
            .split("\n")[0],
        ).group()
        self.version.setText("QEMU-GUI 版本：" + __version__)
        self.qemu_version.setText("QEMU 版本：" + self.qemu_version_text)


class CreateVHDWindow(QMainWindow, create_vhd_window):
    def __init__(self, parent=main_window):
        super(CreateVHDWindow, self).__init__(parent=parent)
        self.window = None
        self.setupUi(self)
        self.setFixedSize(800, 600)
        self.CancelButton.clicked.connect(self.quit)
        self.About.triggered.connect(self.show_about_window)

    def quit(self):
        self.close()

    def show_about_window(self, parent=create_vhd_window):
        # from PyQt5.QtWidgets import QDialog
        from ui.about_create_vhd_window import Ui_AboutCreateVHDWindow

        self.window = QMainWindow()
        ui = Ui_AboutCreateVHDWindow()
        ui.setupUi(self.window)
        self.window.setWindowIcon(QtGui.QIcon("img\\qemu.ico"))
        self.window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
