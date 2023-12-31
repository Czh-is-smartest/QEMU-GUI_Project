# -*- coding: utf-8 -*-
import re
import sys

# Form implementation generated from reading ui file 'about_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import check_output
import os

sys.path.append("G:\\QEMU-GUI_Project")

from main import __version__


class Ui_about_window(object):
    def __init__(self, parent):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, about_window):
        about_window.setObjectName("about_window")
        about_window.resize(640, 480)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        about_window.setFont(font)
        self.centralwidget = QtWidgets.QWidget(about_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem, 9, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.gridLayout.addItem(spacerItem1, 10, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem3, 1, 5, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem4, 0, 5, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem5, 1, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem6, 5, 5, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem7, 16, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem8, 16, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem9, 13, 5, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored
        )
        self.gridLayout.addItem(spacerItem10, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 16, 5, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem11, 3, 5, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum
        )
        self.gridLayout.addItem(spacerItem12, 12, 5, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored
        )
        self.gridLayout.addItem(spacerItem13, 2, 2, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem14, 4, 5, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.version = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.version.setFont(font)
        self.version.setObjectName("version")
        self.verticalLayout.addWidget(self.version)
        self.qemu_version = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.qemu_version.sizePolicy().hasHeightForWidth())
        self.qemu_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.qemu_version.setFont(font)
        self.qemu_version.setTextFormat(QtCore.Qt.AutoText)
        self.qemu_version.setObjectName("qemu_version")
        self.verticalLayout.addWidget(self.qemu_version)
        self.update_button = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.update_button.sizePolicy().hasHeightForWidth()
        )
        self.update_button.setSizePolicy(sizePolicy)
        self.update_button.setObjectName("update_button")
        self.verticalLayout.addWidget(self.update_button)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem15, 8, 5, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum
        )
        self.gridLayout.addItem(spacerItem16, 15, 5, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem17, 11, 5, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem18, 7, 5, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem19, 6, 5, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem20, 14, 5, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem21, 16, 3, 1, 1)
        about_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(about_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 25))
        self.menubar.setObjectName("menubar")
        about_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(about_window)
        self.statusbar.setObjectName("statusbar")
        about_window.setStatusBar(self.statusbar)

        self.retranslateUi(about_window)
        QtCore.QMetaObject.connectSlotsByName(about_window)
        self.get_version()

    def retranslateUi(self, about_window):
        _translate = QtCore.QCoreApplication.translate
        about_window.setWindowTitle(_translate("about_window", "关于 QEMU-GUI"))
        self.label.setText(_translate("about_window", "Powered By Czh-is-smartest"))
        self.version.setText(_translate("about_window", "QEMU-GUI 版本："))
        self.qemu_version.setText(_translate("about_window", "QEMU 版本："))
        self.update_button.setText(_translate("about_window", "检测更新"))

    def get_version(self):
        self.qemu_version_text = re.search(
            r"\d.*",
            check_output("..\qemu\qemu-system-x86_64 --version")
            .decode()
            .split("\n")[0],
        ).group()
        self.version.setText("QEMU-GUO 版本：" + __version__)
        self.qemu_version.setText("QEMU 版本：" + self.qemu_version_text)


def show(self, parent):
    self.app = QtWidgets.QApplication(sys.argv)
    self.w = QtWidgets.QMainWindow()
    self.window = Ui_about_window(parent)
    self.window.setupUi(self.w)
    self.w.show()
    sys.exit(self.app.exec_())


if __name__ == "__main__":
    show(Ui_about_window, None)
