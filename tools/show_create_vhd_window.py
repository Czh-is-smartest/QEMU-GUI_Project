# -*- coding: utf-8 -*-
__version__ = "1.0.0"
import os
import subprocess as s
import sys
import tkinter
from tkinter import filedialog as file_path

from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow

sys.path.append(os.path.abspath(".."))
from modules.Pyinstaller_img import get_resource_path as get

cwd = os.getcwd()
os.chdir("..")

create_vhd_window = uic.loadUiType(get("data\\ui\\create_vhd_window.ui"))[0]
about_window = uic.loadUiType(get("data\\ui\\about_create_vhd_window.ui"))[0]


class CreateVHDWindow(QtWidgets.QMainWindow, create_vhd_window):
    def __init__(self, parent=None):
        sys.path.append(os.path.abspath(".."))
        super(CreateVHDWindow, self).__init__(parent)
        self.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.icon = QtGui.QIcon("img\\qemu.ico")
        self.validator = QRegExpValidator(QRegExp('[^/\:*?"|<>]*'))  # 不允许输入 /\:*?"|<>
        self.name.setValidator(self.validator)
        self.VHD_Path.setText(os.path.dirname(__file__))
        self.VHD_Path.textChanged.connect(self.update)
        self.Path.clicked.connect(self.show_path)
        self.extension.currentTextChanged.connect(self.update)
        self.name.textChanged.connect(self.update)
        self.CancelButton.clicked.connect(self.exit)
        self.CreateButton.clicked.connect(self.create)
        self.tk_init()
        self.format_list = {}
        self.unit_list = {
            "KB": "k",
            "MB": "M",
            "GB": "G",
            "TB": "T",
            "PB": "P",
            "EB": "E",
        }
        self.setWindowIcon(self.icon)

        self.About.triggered.connect(self.show_about_window)
        self.set_combo()
        self.name.setText("vhd")
        self.browse.clicked.connect(self.ask_vhd_path)
        self.update()

    def tk_init(self):
        tk = tkinter.Tk()
        tk.withdraw()
        tk.iconbitmap(f"img\\qemu.ico")

    def show_about_window(self):
        # from ui.about_create_vhd_window import Ui_AboutCreateVHDWindow
        #
        # self.window = QMainWindow(self)
        # ui = Ui_AboutCreateVHDWindow()
        # ui.setupUi(self.window)
        # self.window.show()
        window = AboutWindow(self)
        window.show()

    def show_introduce(self, index):
        self.introduce.setText(list(self.format_list.values())[index])
        self.name.setText(self.name.text().split(".")[0])
        # print(list(self.format_list.values())[index])
        if len(list(self.format_list.values())[index]) > 50:
            self.introduce.setWordWrap(True)
            self.introduce.setFixedWidth(550)
        else:
            self.introduce.setWordWrap(False)

    def set_combo(self):
        with open(f"支持格式.txt", "r", encoding="utf-8") as f:
            for i in f.readlines():
                self.format_list[i.split("：")[0]] = i.split("：")[1]
        self.format.addItems(list(self.format_list.keys()))
        self.format.activated.connect(self.show_introduce)
        self.introduce.setText(self.format_list["qcow2"])
        self.introduce.setWordWrap(True)
        self.introduce.setFixedWidth(550)
        self.unit.addItems(list(self.unit_list.keys()))
        self.extension_list = list(self.format_list.keys())
        self.extension_list.append("img")
        self.extension_list.append("vhd")
        self.extension.addItems(self.extension_list)
        self.extension.setEditable(True)

    def exit(self):
        self.close()

    def ask_vhd_path(self):
        self.vhd_path = file_path.askdirectory()
        if self.vhd_path:
            self.vhd_path = os.sep.join(self.vhd_path.split("/"))
            self.VHD_Path.setText(self.vhd_path)
            self.update()

    def update(self):
        self.Font = QtGui.QFont()
        self.Font.setFamily("微软雅黑")
        self.Font.setPointSize(13)
        self.Font.setUnderline(True)
        self.Path.setFont(self.Font)
        self.path = f"{str(self.VHD_Path.text())}\\{self.name.text()}.{self.extension.currentText()}"
        if not os.path.exists(os.path.dirname(self.path)):
            self.Path.setText("无效路径")
            self.Path.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.Font.setUnderline(False)
            self.Path.setFont(self.Font)
        elif not "." in os.path.basename(os.path.abspath(self.path)):
            self.Path.setText("无效路径")
            self.Path.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
            self.Font.setUnderline(False)
            self.Path.setFont(self.Font)
        else:
            self.Path.setText(os.path.abspath(self.path))
            self.Path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.VHD_Path.setText(str(self.VHD_Path.text()).replace("/", os.sep))

    def create(self):
        from modules.get_disk_FreeSpac import get_disk_FreeSpace as get_free

        if self.Path.text() == "无效路径":
            QMessageBox.warning(self, "警告", "请填入有效的路径！")
            return None
        if os.path.exists(self.Path.text()):
            if not QMessageBox.question(self, "提示", "文件已存在，是否覆盖？"):
                return None
        if (
            self.format.currentText() == "raw"
            and get_free(self.Path.text()[:2], self.unit.currentText(), 5)
            < self.size.value()
        ):
            QMessageBox.warning(self, "警告", f'磁盘"{self.Path.text()[:2]}"空间不足！')
            return None
        os.chdir(cwd)
        os.chdir("..")
        cmd = f'qemu\qemu-img create -f {self.format.currentText()} -o size={self.size.value()}{self.unit_list[self.unit.currentText()]} "{self.Path.text()}"'
        info = s.run(cmd, shell=True, stdout=s.PIPE)  # .read().encode("utf-8").decode()
        if not info.returncode and os.path.exists(self.Path.text()):
            QMessageBox.information(self, "提示", "创建成功！")

        else:
            QMessageBox.warning(self, "错误", "创建失败！%s" % info)

    def show_path(self):
        self.path = self.VHD_Path.text()
        if os.path.exists(self.path):
            os.startfile(self.path)


class AboutWindow(QMainWindow, about_window):
    def __init__(self, parent):
        super(AboutWindow, self).__init__(parent)
        self.setupUi(self)
        self.get_version()

    def get_version(self):
        import os
        import re

        os.chdir(cwd)
        path = f"..\\qemu\\qemu-img.exe --version"
        version = os.popen(path).read()
        version = re.search(r"\d.*", version.split("\n")[0]).group()
        self.qemu_img_version.setText(f"qemu-img 版本：{version}")
        self.version.setText(f"虚拟硬盘工具版本：{__version__}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = CreateVHDWindow()
    ui.show()
    sys.exit(app.exec_())
