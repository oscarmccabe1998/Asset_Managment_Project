# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateSoftware.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QVBoxLayout, QWidget)

class Ui_UpdateSoftware(object):
    def setupUi(self, UpdateSoftware):
        if not UpdateSoftware.objectName():
            UpdateSoftware.setObjectName(u"UpdateSoftware")
        UpdateSoftware.resize(800, 600)
        self.centralwidget = QWidget(UpdateSoftware)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Instructionlabel = QLabel(self.centralwidget)
        self.Instructionlabel.setObjectName(u"Instructionlabel")

        self.verticalLayout.addWidget(self.Instructionlabel)

        self.NameDescriptionlabel = QLabel(self.centralwidget)
        self.NameDescriptionlabel.setObjectName(u"NameDescriptionlabel")

        self.verticalLayout.addWidget(self.NameDescriptionlabel)

        self.OSNameEdit = QLineEdit(self.centralwidget)
        self.OSNameEdit.setObjectName(u"OSNameEdit")

        self.verticalLayout.addWidget(self.OSNameEdit)

        self.OSProductVersionLabel = QLabel(self.centralwidget)
        self.OSProductVersionLabel.setObjectName(u"OSProductVersionLabel")

        self.verticalLayout.addWidget(self.OSProductVersionLabel)

        self.ProductVersionEdit = QLineEdit(self.centralwidget)
        self.ProductVersionEdit.setObjectName(u"ProductVersionEdit")

        self.verticalLayout.addWidget(self.ProductVersionEdit)

        self.OSBuildVersionlabel = QLabel(self.centralwidget)
        self.OSBuildVersionlabel.setObjectName(u"OSBuildVersionlabel")

        self.verticalLayout.addWidget(self.OSBuildVersionlabel)

        self.OSBuildVersionEdit = QLineEdit(self.centralwidget)
        self.OSBuildVersionEdit.setObjectName(u"OSBuildVersionEdit")

        self.verticalLayout.addWidget(self.OSBuildVersionEdit)

        self.OSManufacturerlabel = QLabel(self.centralwidget)
        self.OSManufacturerlabel.setObjectName(u"OSManufacturerlabel")

        self.verticalLayout.addWidget(self.OSManufacturerlabel)

        self.OSManufacturerEdit = QLineEdit(self.centralwidget)
        self.OSManufacturerEdit.setObjectName(u"OSManufacturerEdit")

        self.verticalLayout.addWidget(self.OSManufacturerEdit)

        self.UpdateSoftwareButton = QPushButton(self.centralwidget)
        self.UpdateSoftwareButton.setObjectName(u"UpdateSoftwareButton")

        self.verticalLayout.addWidget(self.UpdateSoftwareButton)

        self.SoftwareScanButton = QPushButton(self.centralwidget)
        self.SoftwareScanButton.setObjectName(u"SoftwareScanButton")

        self.verticalLayout.addWidget(self.SoftwareScanButton)

        self.GoBackButton = QPushButton(self.centralwidget)
        self.GoBackButton.setObjectName(u"GoBackButton")

        self.verticalLayout.addWidget(self.GoBackButton)

        UpdateSoftware.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(UpdateSoftware)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        UpdateSoftware.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(UpdateSoftware)
        self.statusbar.setObjectName(u"statusbar")
        UpdateSoftware.setStatusBar(self.statusbar)

        self.retranslateUi(UpdateSoftware)

        QMetaObject.connectSlotsByName(UpdateSoftware)
    # setupUi

    def retranslateUi(self, UpdateSoftware):
        UpdateSoftware.setWindowTitle(QCoreApplication.translate("UpdateSoftware", u"Edit Software", None))
        self.Instructionlabel.setText(QCoreApplication.translate("UpdateSoftware", u"Edit the information and click update software to update the database entry or click scan to get the information from this machine", None))
        self.NameDescriptionlabel.setText(QCoreApplication.translate("UpdateSoftware", u"OS Name", None))
        self.OSProductVersionLabel.setText(QCoreApplication.translate("UpdateSoftware", u"Product Version", None))
        self.OSBuildVersionlabel.setText(QCoreApplication.translate("UpdateSoftware", u"Build Version", None))
        self.OSManufacturerlabel.setText(QCoreApplication.translate("UpdateSoftware", u"Manufacturer", None))
        self.UpdateSoftwareButton.setText(QCoreApplication.translate("UpdateSoftware", u"Update Software", None))
        self.SoftwareScanButton.setText(QCoreApplication.translate("UpdateSoftware", u"Scan this machine", None))
        self.GoBackButton.setText(QCoreApplication.translate("UpdateSoftware", u"Go Back", None))
    # retranslateUi
