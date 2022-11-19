# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'base.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QFrame, QGroupBox,
    QLCDNumber, QLabel, QPushButton, QRadioButton,
    QSizePolicy, QSpinBox, QWidget)

class Ui_applicationUi(object):
    def setupUi(self, applicationUi):
        if not applicationUi.objectName():
            applicationUi.setObjectName(u"applicationUi")
        applicationUi.resize(460, 300)
        applicationUi.setMinimumSize(QSize(460, 300))
        applicationUi.setMaximumSize(QSize(460, 300))
        applicationUi.setCursor(QCursor(Qt.PointingHandCursor))
        applicationUi.setContextMenuPolicy(Qt.DefaultContextMenu)
        icon = QIcon()
        icon.addFile(u"./perspective.ico", QSize(), QIcon.Normal, QIcon.Off)
        applicationUi.setWindowIcon(icon)
        applicationUi.setStyleSheet(u"background-color: rgb(15, 15, 15);\n"
"font: 14pt \"Segoe UI Variable Display\";\n"
"color: rgb(240, 240, 240);")
        self.pushButton = QPushButton(applicationUi)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(140, 230, 181, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI Variable Display"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.frame = QFrame(applicationUi)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 20, 421, 201))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 71, 16))
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 81, 16))
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 130, 191, 20))
        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 170, 191, 20))
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(10, 90, 191, 20))
        self.groupBox = QGroupBox(self.frame)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(230, 0, 181, 80))
        self.lcdNumber = QLCDNumber(self.groupBox)
        self.lcdNumber.setObjectName(u"lcdNumber")
        self.lcdNumber.setGeometry(QRect(10, 30, 161, 31))
        self.lcdNumber.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.lcdNumber.setSmallDecimalPoint(True)
        self.lcdNumber.setDigitCount(10)
        self.lcdNumber.setProperty("value", 0.000000000000000)
        self.groupBox_2 = QGroupBox(self.frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(230, 100, 181, 80))
        self.lcdNumber_2 = QLCDNumber(self.groupBox_2)
        self.lcdNumber_2.setObjectName(u"lcdNumber_2")
        self.lcdNumber_2.setGeometry(QRect(10, 30, 161, 31))
        self.lcdNumber_2.setStyleSheet(u"background-color: rgb(34, 34, 34);")
        self.lcdNumber_2.setSmallDecimalPoint(True)
        self.lcdNumber_2.setDigitCount(10)
        self.lcdNumber_2.setProperty("value", 0.000000000000000)
        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(80, 10, 131, 22))
        self.spinBox.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.spinBox.setFrame(False)
        self.spinBox.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox.setKeyboardTracking(True)
        self.spinBox.setProperty("showGroupSeparator", True)
        self.spinBox.setMinimum(-999999999)
        self.spinBox.setMaximum(999999999)
        self.spinBox_2 = QSpinBox(self.frame)
        self.spinBox_2.setObjectName(u"spinBox_2")
        self.spinBox_2.setGeometry(QRect(80, 50, 131, 22))
        self.spinBox_2.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.spinBox_2.setFrame(False)
        self.spinBox_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.spinBox_2.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinBox_2.setKeyboardTracking(True)
        self.spinBox_2.setProperty("showGroupSeparator", True)
        self.spinBox_2.setMinimum(-999999999)
        self.spinBox_2.setMaximum(999999999)

        self.retranslateUi(applicationUi)

        QMetaObject.connectSlotsByName(applicationUi)
    # setupUi

    def retranslateUi(self, applicationUi):
        applicationUi.setWindowTitle(QCoreApplication.translate("applicationUi", u"Generador Random", None))
        self.pushButton.setText(QCoreApplication.translate("applicationUi", u"Generate", None))
        self.label.setText(QCoreApplication.translate("applicationUi", u"Desde : ", None))
        self.label_2.setText(QCoreApplication.translate("applicationUi", u"Hasta :", None))
        self.radioButton.setText(QCoreApplication.translate("applicationUi", u"Solo Pares", None))
        self.radioButton_2.setText(QCoreApplication.translate("applicationUi", u"Solo Impares", None))
        self.radioButton_3.setText(QCoreApplication.translate("applicationUi", u"Todos", None))
        self.groupBox.setTitle(QCoreApplication.translate("applicationUi", u"Generador X", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("applicationUi", u"Generador Y", None))
    # retranslateUi

