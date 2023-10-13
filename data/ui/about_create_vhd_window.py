# -*- coding: utf-8 -*-
import sys

__version__ = "0.0.1"

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AboutCreateVHDWindow(object):
    def setupUi(self, AboutCreateVHDWindow):
        AboutCreateVHDWindow.setObjectName("AboutCreateVHDWindow")
        AboutCreateVHDWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(AboutCreateVHDWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            343, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored
        )
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            106, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            106, 94, QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem2, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            37, 94, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
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
        self.qemu_img_version = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.qemu_img_version.sizePolicy().hasHeightForWidth()
        )
        self.qemu_img_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.qemu_img_version.setFont(font)
        self.qemu_img_version.setTextFormat(QtCore.Qt.AutoText)
        self.qemu_img_version.setObjectName("qemu_img_version")
        self.verticalLayout.addWidget(self.qemu_img_version)
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
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.verticalLayout.addWidget(self.update_button)
        self.gridLayout.addLayout(self.verticalLayout, 1, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            106, 37, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed
        )
        self.gridLayout.addItem(spacerItem4, 1, 3, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored
        )
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            106, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem6, 3, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            106, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem7, 4, 3, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(
            106, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem8, 5, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(
            106, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem9, 6, 3, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(
            106, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem10, 7, 3, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(
            106, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem11, 8, 3, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(
            106, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem12, 9, 3, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(
            106, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred
        )
        self.gridLayout.addItem(spacerItem13, 10, 3, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(
            106, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem14, 11, 3, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(
            106, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum
        )
        self.gridLayout.addItem(spacerItem15, 12, 3, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(
            106, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem16, 13, 3, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(
            106, 9, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem17, 14, 3, 1, 1)
        spacerItem18 = QtWidgets.QSpacerItem(
            106, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum
        )
        self.gridLayout.addItem(spacerItem18, 15, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 16, 2, 1, 1)
        AboutCreateVHDWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutCreateVHDWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 23))
        self.menubar.setObjectName("menubar")
        AboutCreateVHDWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutCreateVHDWindow)
        self.statusbar.setObjectName("statusbar")
        AboutCreateVHDWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutCreateVHDWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutCreateVHDWindow)

    def retranslateUi(self, AboutCreateVHDWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutCreateVHDWindow.setWindowTitle(
            _translate("AboutCreateVHDWindow", "关于 QEMU-GUI 创建虚拟硬盘")
        )
        self.version.setText(_translate("AboutCreateVHDWindow", "虚拟硬盘工具版本："))
        self.qemu_img_version.setText(
            _translate("AboutCreateVHDWindow", "qemu-img 版本：")
        )
        self.update_button.setText(_translate("AboutCreateVHDWindow", "检测更新"))
        self.label.setText(
            _translate(
                "AboutCreateVHDWindow",
                "Powered By Czh-is-smartest\n"
                "https://github.com/Czh-is-smartest/QEMU-GUI_Project",
            )
        )
        self.get_version()

    def get_version(self):
        import os
        import re

        path = f"{os.path.dirname(__file__)}\\..\\qemu\\qemu-img --version"
        version = os.popen(path).read()
        version = re.search(r"\d.*", version.split("\n")[0]).group()
        self.qemu_img_version.setText(f"qemu-img 版本：{version}")
        self.version.setText(f"虚拟硬盘工具版本：{__version__}")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_AboutCreateVHDWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
