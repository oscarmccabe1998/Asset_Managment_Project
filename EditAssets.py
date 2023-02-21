# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditAssets.ui'
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
from PySide6.QtWidgets import (QApplication, QDateEdit, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextEdit, QVBoxLayout, QWidget)

class Ui_EditAssets(object):
    def setupUi(self, EditAssets):
        if not EditAssets.objectName():
            EditAssets.setObjectName(u"EditAssets")
        EditAssets.resize(800, 667)
        self.centralwidget = QWidget(EditAssets)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Instructions = QLabel(self.centralwidget)
        self.Instructions.setObjectName(u"Instructions")

        self.verticalLayout.addWidget(self.Instructions)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.SysNameEdit = QLineEdit(self.centralwidget)
        self.SysNameEdit.setObjectName(u"SysNameEdit")

        self.verticalLayout.addWidget(self.SysNameEdit)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.SysTypeEdit = QLineEdit(self.centralwidget)
        self.SysTypeEdit.setObjectName(u"SysTypeEdit")

        self.verticalLayout.addWidget(self.SysTypeEdit)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.macaddressLabel = QLabel(self.centralwidget)
        self.macaddressLabel.setObjectName(u"macaddressLabel")

        self.verticalLayout.addWidget(self.macaddressLabel)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.ipEdit = QLineEdit(self.centralwidget)
        self.ipEdit.setObjectName(u"ipEdit")

        self.verticalLayout.addWidget(self.ipEdit)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.ModelEdit = QLineEdit(self.centralwidget)
        self.ModelEdit.setObjectName(u"ModelEdit")

        self.verticalLayout.addWidget(self.ModelEdit)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.ManufacturerEdit = QLineEdit(self.centralwidget)
        self.ManufacturerEdit.setObjectName(u"ManufacturerEdit")

        self.verticalLayout.addWidget(self.ManufacturerEdit)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout.addWidget(self.label_7)

        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateEdit)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout.addWidget(self.label_8)

        self.NoteEdit = QTextEdit(self.centralwidget)
        self.NoteEdit.setObjectName(u"NoteEdit")

        self.verticalLayout.addWidget(self.NoteEdit)

        self.Scan = QPushButton(self.centralwidget)
        self.Scan.setObjectName(u"Scan")

        self.verticalLayout.addWidget(self.Scan)

        self.UpdateAssetButton = QPushButton(self.centralwidget)
        self.UpdateAssetButton.setObjectName(u"UpdateAssetButton")

        self.verticalLayout.addWidget(self.UpdateAssetButton)

        self.CancelButton = QPushButton(self.centralwidget)
        self.CancelButton.setObjectName(u"CancelButton")

        self.verticalLayout.addWidget(self.CancelButton)

        EditAssets.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(EditAssets)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        EditAssets.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(EditAssets)
        self.statusbar.setObjectName(u"statusbar")
        EditAssets.setStatusBar(self.statusbar)

        self.retranslateUi(EditAssets)

        QMetaObject.connectSlotsByName(EditAssets)
    # setupUi

    def retranslateUi(self, EditAssets):
        EditAssets.setWindowTitle(QCoreApplication.translate("EditAssets", u"Update Assets", None))
        self.Instructions.setText(QCoreApplication.translate("EditAssets", u"TextLabel", None))
        self.label_2.setText(QCoreApplication.translate("EditAssets", u"System Name", None))
        self.label_3.setText(QCoreApplication.translate("EditAssets", u"System Type", None))
        self.label.setText(QCoreApplication.translate("EditAssets", u"MAC Address", None))
        self.macaddressLabel.setText(QCoreApplication.translate("EditAssets", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("EditAssets", u"IP Address", None))
        self.label_5.setText(QCoreApplication.translate("EditAssets", u"Model", None))
        self.label_6.setText(QCoreApplication.translate("EditAssets", u"Manufacturer", None))
        self.label_7.setText(QCoreApplication.translate("EditAssets", u"Date found on sticker", None))
        self.label_8.setText(QCoreApplication.translate("EditAssets", u"Note", None))
        self.Scan.setText(QCoreApplication.translate("EditAssets", u"Quick Scan", None))
        self.UpdateAssetButton.setText(QCoreApplication.translate("EditAssets", u"Update Asset", None))
        self.CancelButton.setText(QCoreApplication.translate("EditAssets", u"Cancel", None))
    # retranslateUi

