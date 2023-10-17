# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_vhd_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateVHDWindow(object):
    def setupUi(self, CreateVHDWindow):
        CreateVHDWindow.setObjectName("CreateVHDWindow")
        CreateVHDWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CreateVHDWindow.sizePolicy().hasHeightForWidth())
        CreateVHDWindow.setSizePolicy(sizePolicy)
        CreateVHDWindow.setMinimumSize(QtCore.QSize(800, 600))
        CreateVHDWindow.setMaximumSize(QtCore.QSize(800, 600))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        CreateVHDWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CreateVHDWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.introduce = QtWidgets.QLabel(self.centralwidget)
        self.introduce.setEnabled(True)
        self.introduce.setGeometry(QtCore.QRect(190, 95, 101, 71))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.introduce.sizePolicy().hasHeightForWidth())
        self.introduce.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.introduce.setFont(font)
        self.introduce.setObjectName("introduce")
        self.format = QtWidgets.QComboBox(self.centralwidget)
        self.format.setGeometry(QtCore.QRect(100, 105, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.format.sizePolicy().hasHeightForWidth())
        self.format.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.format.setFont(font)
        self.format.setStyleSheet("/*border-radius: 10px;\n"
"border: 1px solid;*/\n"
"")
        self.format.setObjectName("format")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 105, 85, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 60, 85, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.VHD_Path = QtWidgets.QLineEdit(self.centralwidget)
        self.VHD_Path.setGeometry(QtCore.QRect(100, 60, 450, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.VHD_Path.setFont(font)
        self.VHD_Path.setStyleSheet("border-radius: 10px;\n"
"border: 1px solid;\n"
"")
        self.VHD_Path.setObjectName("VHD_Path")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(560, 60, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.browse.sizePolicy().hasHeightForWidth())
        self.browse.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        self.browse.setFont(font)
        self.browse.setObjectName("browse")
        self.CreateButton = QtWidgets.QPushButton(self.centralwidget)
        self.CreateButton.setGeometry(QtCore.QRect(639, 540, 75, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CreateButton.sizePolicy().hasHeightForWidth())
        self.CreateButton.setSizePolicy(sizePolicy)
        self.CreateButton.setObjectName("CreateButton")
        self.CancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.CancelButton.setGeometry(QtCore.QRect(720, 540, 75, 27))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CancelButton.sizePolicy().hasHeightForWidth())
        self.CancelButton.setSizePolicy(sizePolicy)
        self.CancelButton.setObjectName("CancelButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(316, 10, 168, 36))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.title.sizePolicy().hasHeightForWidth())
        self.title.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(21)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.title.setFont(font)
        self.title.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.title.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.title.setAutoFillBackground(False)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 85, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.size = QtWidgets.QSpinBox(self.centralwidget)
        self.size.setGeometry(QtCore.QRect(100, 150, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.size.setFont(font)
        self.size.setStyleSheet("/*border-radius: 10px;\n"
"border: 1px solid;*/")
        self.size.setMinimum(1)
        self.size.setMaximum(999999999)
        self.size.setObjectName("size")
        self.unit = QtWidgets.QComboBox(self.centralwidget)
        self.unit.setGeometry(QtCore.QRect(190, 150, 60, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.unit.setFont(font)
        self.unit.setStyleSheet("/*border-radius: 10px;\n"
"border: 1px solid;*/")
        self.unit.setObjectName("unit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 195, 85, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(100, 195, 160, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.name.setFont(font)
        self.name.setStyleSheet("border-radius: 10px;\n"
"border: 1px solid;\n"
"")
        self.name.setObjectName("name")
        self.extension = QtWidgets.QComboBox(self.centralwidget)
        self.extension.setGeometry(QtCore.QRect(290, 195, 80, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.extension.setFont(font)
        self.extension.setObjectName("extension")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(270, 180, 20, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(23)
        font.setUnderline(False)
        self.label_5.setFont(font)
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 120, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.Path = QtWidgets.QPushButton(self.centralwidget)
        self.Path.setGeometry(QtCore.QRect(0, 270, 801, 51))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        font.setUnderline(True)
        self.Path.setFont(font)
        self.Path.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Path.setStyleSheet("background-color: transparent;")
        self.Path.setText("")
        self.Path.setObjectName("Path")
        CreateVHDWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CreateVHDWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        CreateVHDWindow.setMenuBar(self.menubar)
        self.About = QtWidgets.QAction(CreateVHDWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../img/qemu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.About.setIcon(icon)
        self.About.setObjectName("About")
        self.menu_Help.addAction(self.About)
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(CreateVHDWindow)
        QtCore.QMetaObject.connectSlotsByName(CreateVHDWindow)

    def retranslateUi(self, CreateVHDWindow):
        _translate = QtCore.QCoreApplication.translate
        CreateVHDWindow.setWindowTitle(_translate("CreateVHDWindow", "新建虚拟硬盘"))
        self.introduce.setText(_translate("CreateVHDWindow", "无"))
        self.label_2.setText(_translate("CreateVHDWindow", "硬盘格式："))
        self.label.setText(_translate("CreateVHDWindow", "存放路径："))
        self.browse.setText(_translate("CreateVHDWindow", "浏览"))
        self.CreateButton.setText(_translate("CreateVHDWindow", "创建"))
        self.CancelButton.setText(_translate("CreateVHDWindow", "取消"))
        self.title.setText(_translate("CreateVHDWindow", "创建虚拟硬盘"))
        self.label_3.setText(_translate("CreateVHDWindow", "硬盘大小："))
        self.label_4.setText(_translate("CreateVHDWindow", "硬盘名称："))
        self.label_5.setText(_translate("CreateVHDWindow", "."))
        self.label_6.setText(_translate("CreateVHDWindow", "最终生成路径："))
        self.menu_Help.setTitle(_translate("CreateVHDWindow", "帮助(&H)"))
        self.About.setText(_translate("CreateVHDWindow", "关于 QEMU-GUI 创建虚拟硬盘(&A)"))