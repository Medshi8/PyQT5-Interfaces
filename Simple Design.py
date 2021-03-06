# -*- coding: utf-8 -*-
# Created by: Medshi8 using PyQt5 UI code generator 5.15.1



from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 516)
        MainWindow.setStyleSheet("*{\n"
"background-color: qlineargradient(spread:pad, x1:0.733, y1:0.023, x2:0.569, y2:0.505, stop:0.1875 rgba(254, 109, 74, 255), stop:0.289773 rgba(254, 109, 74, 255), stop:0.545455 rgba(255, 255, 255, 255), stop:0.613636 rgba(255, 255, 255, 255));\n"
"}\n"
"QLabel{\n"
"    background:transparent;\n"
"    color: rgb(229, 96, 66);\n"
"    font:20px Arial;\n"
"}\n"
"\n"
"#userFrame\n"
"{\n"
"    border: 2px solid #d1d0d0;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(229, 227, 228);\n"
"    margin-right: 5px;\n"
"    margin-top:5px;\n"
"    margin-left:40;\n"
"    margin-right:30;\n"
"    \n"
"}\n"
"\n"
"#usrin{\n"
"background: transparent;\n"
"\n"
"\n"
"}\n"
"QLineEdit{\n"
"font: 12px Arial;\n"
"padding:3px;\n"
"background:transparent;\n"
"}\n"
"\n"
"#PassFrame\n"
"{\n"
"    border: 2px solid #d1d0d0;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(229, 227, 228);\n"
"    margin-right: 5px;\n"
"    margin-top:5px;\n"
"    margin-left:40;\n"
"    margin-right:30;\n"
"    \n"
"}\n"
"\n"
"#wid{\n"
"background:transparent;\n"
"}\n"
"QPushButton{\n"
"    background: rgb(236, 99, 68);\n"
"    border:1px solid  rgb(225, 94, 64);\n"
"    border-radius: 10px;\n"
"    color:white;\n"
"    font: 19px Tahoma;\n"
"    padding:5px;\n"
"    margin-left:25;\n"
"    margin-right:25;\n"
"    tansition: 0.8s;\n"
"}\n"
"QPushButton:hover{\n"
"    \n"
"    background-color: rgb(203, 0, 61);\n"
"    \n"
"    border-color: rgb(10, 247, 231);\n"
"    \n"
"    \n"
"    color: rgb(194, 255, 255);\n"
"\n"
"}\n"
"\n"
"#title{\n"
"    color: rgb(214, 0, 61);\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.wid = QtWidgets.QWidget(self.centralwidget)
        self.wid.setMinimumSize(QtCore.QSize(1, 50))
        self.wid.setMaximumSize(QtCore.QSize(16777215, 50))
        self.wid.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.wid.setObjectName("wid")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.wid)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.title = QtWidgets.QLabel(self.wid)
        self.title.setMinimumSize(QtCore.QSize(121, 41))
        self.title.setMaximumSize(QtCore.QSize(121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.title.setFont(font)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")
        self.horizontalLayout_3.addWidget(self.title)
        self.gridLayout.addWidget(self.wid, 0, 0, 1, 1)
        self.userFrame = QtWidgets.QFrame(self.centralwidget)
        self.userFrame.setMinimumSize(QtCore.QSize(230, 51))
        self.userFrame.setMaximumSize(QtCore.QSize(291, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(10)
        self.userFrame.setFont(font)
        self.userFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.userFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.userFrame.setLineWidth(2)
        self.userFrame.setObjectName("userFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.userFrame)
        self.horizontalLayout_2.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.userFrame)
        self.label_2.setMinimumSize(QtCore.QSize(31, 21))
        self.label_2.setMaximumSize(QtCore.QSize(31, 21))
        self.label_2.setStyleSheet("image: url(:/newPrefix/user-login-icon-14.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.usrin = QtWidgets.QLineEdit(self.userFrame)
        self.usrin.setMinimumSize(QtCore.QSize(147, 24))
        self.usrin.setDragEnabled(True)
        self.usrin.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.usrin.setClearButtonEnabled(True)
        self.usrin.setObjectName("usrin")
        self.horizontalLayout_2.addWidget(self.usrin)
        self.gridLayout.addWidget(self.userFrame, 1, 0, 1, 1)
        self.PassFrame = QtWidgets.QFrame(self.centralwidget)
        self.PassFrame.setMinimumSize(QtCore.QSize(230, 51))
        self.PassFrame.setMaximumSize(QtCore.QSize(291, 51))
        self.PassFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.PassFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.PassFrame.setObjectName("PassFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.PassFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.PassFrame)
        self.label_3.setMinimumSize(QtCore.QSize(31, 21))
        self.label_3.setMaximumSize(QtCore.QSize(31, 21))
        self.label_3.setStyleSheet("image: url(:/newPrefix/lck2.png);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.usrin_2 = QtWidgets.QLineEdit(self.PassFrame)
        self.usrin_2.setMinimumSize(QtCore.QSize(147, 24))
        self.usrin_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.usrin_2.setWhatsThis("")
        self.usrin_2.setAccessibleDescription("")
        self.usrin_2.setAutoFillBackground(False)
        self.usrin_2.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.usrin_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.usrin_2.setDragEnabled(True)
        self.usrin_2.setClearButtonEnabled(True)
        self.usrin_2.setObjectName("usrin_2")
        self.horizontalLayout.addWidget(self.usrin_2)
        self.gridLayout.addWidget(self.PassFrame, 2, 0, 1, 1)
        self.LogButt = QtWidgets.QPushButton(self.centralwidget)
        self.LogButt.setMaximumSize(QtCore.QSize(320, 16777215))
        self.LogButt.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.LogButt.setObjectName("LogButt")
        self.gridLayout.addWidget(self.LogButt, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "USER LOGIN"))
        self.usrin.setPlaceholderText(_translate("MainWindow", "USER NAME"))
        self.usrin_2.setPlaceholderText(_translate("MainWindow", "PASSWORD"))
        self.LogButt.setText(_translate("MainWindow", "Login"))
import source_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
