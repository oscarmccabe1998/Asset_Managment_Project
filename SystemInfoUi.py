# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'systemInfoLayout.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QDateTimeEdit, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Instructions = QLabel(self.centralwidget)
        self.Instructions.setObjectName(u"Instructions")

        self.verticalLayout.addWidget(self.Instructions)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.mac_label = QLabel(self.centralwidget)
        self.mac_label.setObjectName(u"mac_label")

        self.verticalLayout.addWidget(self.mac_label)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCurrentSection(QDateTimeEdit.DaySection)
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateEdit)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")

        self.verticalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.OSNameLabel = QLabel(self.centralwidget)
        self.OSNameLabel.setObjectName(u"OSNameLabel")

        self.verticalLayout.addWidget(self.OSNameLabel)

        self.OSVersionLabel = QLabel(self.centralwidget)
        self.OSVersionLabel.setObjectName(u"OSVersionLabel")

        self.verticalLayout.addWidget(self.OSVersionLabel)

        self.OSBuildVersionLabel = QLabel(self.centralwidget)
        self.OSBuildVersionLabel.setObjectName(u"OSBuildVersionLabel")

        self.verticalLayout.addWidget(self.OSBuildVersionLabel)

        self.OSManufacturerLabel = QLabel(self.centralwidget)
        self.OSManufacturerLabel.setObjectName(u"OSManufacturerLabel")

        self.verticalLayout.addWidget(self.OSManufacturerLabel)

        self.AddSoftwareToDbButton = QPushButton(self.centralwidget)
        self.AddSoftwareToDbButton.setObjectName(u"AddSoftwareToDbButton")

        self.verticalLayout.addWidget(self.AddSoftwareToDbButton)

        self.LinkHardwareAndSoftwareButton = QPushButton(self.centralwidget)
        self.LinkHardwareAndSoftwareButton.setObjectName(u"LinkHardwareAndSoftwareButton")

        self.verticalLayout.addWidget(self.LinkHardwareAndSoftwareButton)

        self.Go_Back = QPushButton(self.centralwidget)
        self.Go_Back.setObjectName(u"Go_Back")

        self.verticalLayout.addWidget(self.Go_Back)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.Instructions.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.mac_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Add Hardware to Database", None))
        self.OSNameLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.OSVersionLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.OSBuildVersionLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.OSManufacturerLabel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.AddSoftwareToDbButton.setText(QCoreApplication.translate("MainWindow", u"Add Software To Database", None))
        self.LinkHardwareAndSoftwareButton.setText(QCoreApplication.translate("MainWindow", u"Link Hardware and Software", None))
        self.Go_Back.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
    # retranslateUi
