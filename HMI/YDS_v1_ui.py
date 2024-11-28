# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'YDS_v1.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextBrowser, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1113, 697)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 791, 41))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(100, 50))

        self.horizontalLayout.addWidget(self.label)

        self.pushButton_2d = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2d.setObjectName(u"pushButton_2d")
        self.pushButton_2d.setMaximumSize(QSize(500, 25))

        self.horizontalLayout.addWidget(self.pushButton_2d)

        self.pushButton_3d = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3d.setObjectName(u"pushButton_3d")
        self.pushButton_3d.setMaximumSize(QSize(500, 25))

        self.horizontalLayout.addWidget(self.pushButton_3d)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 60, 791, 591))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.webEngineView = QWebEngineView(self.groupBox)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(-1, 19, 791, 571))
        self.webEngineView.setUrl(QUrl(u"about:blank"))

        self.verticalLayout.addWidget(self.groupBox)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(810, 10, 291, 641))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox_1 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_1.setObjectName(u"groupBox_1")
        self.groupBox_1.setMaximumSize(QSize(500, 200))
        self.gridLayoutWidget = QWidget(self.groupBox_1)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(9, 19, 271, 181))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.textEdit_fc = QTextEdit(self.gridLayoutWidget)
        self.textEdit_fc.setObjectName(u"textEdit_fc")
        self.textEdit_fc.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.textEdit_fc, 3, 1, 1, 1)

        self.pushButton_radar_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_radar_2.setObjectName(u"pushButton_radar_2")
        self.pushButton_radar_2.setMaximumSize(QSize(200, 25))

        self.gridLayout.addWidget(self.pushButton_radar_2, 0, 1, 1, 1)

        self.pushButton_radar_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_radar_1.setObjectName(u"pushButton_radar_1")
        self.pushButton_radar_1.setMaximumSize(QSize(200, 25))

        self.gridLayout.addWidget(self.pushButton_radar_1, 0, 0, 1, 1)

        self.textEdit_B = QTextEdit(self.gridLayoutWidget)
        self.textEdit_B.setObjectName(u"textEdit_B")
        self.textEdit_B.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.textEdit_B, 2, 1, 1, 1)

        self.textEdit_prf = QTextEdit(self.gridLayoutWidget)
        self.textEdit_prf.setObjectName(u"textEdit_prf")
        self.textEdit_prf.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.textEdit_prf, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.textEdit_T = QTextEdit(self.gridLayoutWidget)
        self.textEdit_T.setObjectName(u"textEdit_T")
        self.textEdit_T.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.textEdit_T, 4, 1, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(130, 25))

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.groupBox_1)

        self.groupBox_4 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayoutWidget_3 = QWidget(self.groupBox_4)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(9, 20, 271, 25))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_start = QPushButton(self.horizontalLayoutWidget_3)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setMaximumSize(QSize(300, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_start)


        self.verticalLayout_2.addWidget(self.groupBox_4)

        self.groupBox_2 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMaximumSize(QSize(500, 610))
        self.textBrowser = QTextBrowser(self.groupBox_2)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 20, 271, 281))

        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.verticalLayoutWidget_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMaximumSize(QSize(500, 60))
        self.horizontalLayoutWidget_2 = QWidget(self.groupBox_3)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(9, 19, 271, 31))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_2.addWidget(self.label_6)

        self.textEdit_local = QTextEdit(self.horizontalLayoutWidget_2)
        self.textEdit_local.setObjectName(u"textEdit_local")
        self.textEdit_local.setMaximumSize(QSize(200, 25))

        self.horizontalLayout_2.addWidget(self.textEdit_local)

        self.pushButton_data = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_data.setObjectName(u"pushButton_data")
        self.pushButton_data.setMaximumSize(QSize(100, 25))

        self.horizontalLayout_2.addWidget(self.pushButton_data)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1113, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u5f0f\u9009\u53d6", None))
        self.pushButton_2d.setText(QCoreApplication.translate("MainWindow", u"\u4e8c\u7ef4\u6210\u50cf\u7ed3\u679c", None))
        self.pushButton_3d.setText(QCoreApplication.translate("MainWindow", u"\u4e09\u7ef4\u6210\u50cf\u7ed3\u679c", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6210\u50cf\u7ed3\u679c", None))
        self.groupBox_1.setTitle(QCoreApplication.translate("MainWindow", u"\u96f7\u8fbe\u63a7\u5236", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8f7d\u9891(GHz)", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u5bbd(ms)", None))
        self.pushButton_radar_2.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
        self.pushButton_radar_1.setText(QCoreApplication.translate("MainWindow", u"\u52a0\u8f7d\u9ed8\u8ba4", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5e26\u5bbd(GHz)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u8109\u51b2\u91cd\u590d\u9891\u7387(Hz)", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u542f\u52a8", None))
        self.pushButton_start.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u8f68\u626b\u63cf\u4e0eZYNQ\u7a0b\u5e8f\u8fd0\u884c\u5f00\u59cb", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u4fdd\u5b58\u60c5\u51b5", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u6d4f\u89c8", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u56fe\u50cf\u540d", None))
        self.pushButton_data.setText(QCoreApplication.translate("MainWindow", u"\u786e\u8ba4", None))
    # retranslateUi

