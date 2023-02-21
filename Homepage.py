# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomePage.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_HomePageMainWindow(object):
    def setupUi(self, HomePageMainWindow):
        if not HomePageMainWindow.objectName():
            HomePageMainWindow.setObjectName(u"HomePageMainWindow")
        HomePageMainWindow.resize(800, 600)
        self.centralwidget = QWidget(HomePageMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MessageBox = QTextBrowser(self.centralwidget)
        self.MessageBox.setObjectName(u"MessageBox")

        self.verticalLayout.addWidget(self.MessageBox)

        self.dbConnCheckLabel = QLabel(self.centralwidget)
        self.dbConnCheckLabel.setObjectName(u"dbConnCheckLabel")

        self.verticalLayout.addWidget(self.dbConnCheckLabel)

        self.ViewAssetsButton = QPushButton(self.centralwidget)
        self.ViewAssetsButton.setObjectName(u"ViewAssetsButton")

        self.verticalLayout.addWidget(self.ViewAssetsButton)

        self.ViewHardwareSoftwareLink = QPushButton(self.centralwidget)
        self.ViewHardwareSoftwareLink.setObjectName(u"ViewHardwareSoftwareLink")

        self.verticalLayout.addWidget(self.ViewHardwareSoftwareLink)

        self.AddAssetButton = QPushButton(self.centralwidget)
        self.AddAssetButton.setObjectName(u"AddAssetButton")

        self.verticalLayout.addWidget(self.AddAssetButton)

        self.AddUserButton = QPushButton(self.centralwidget)
        self.AddUserButton.setObjectName(u"AddUserButton")

        self.verticalLayout.addWidget(self.AddUserButton)

        self.ViewLog = QPushButton(self.centralwidget)
        self.ViewLog.setObjectName(u"ViewLog")

        self.verticalLayout.addWidget(self.ViewLog)

        self.LogOutButton = QPushButton(self.centralwidget)
        self.LogOutButton.setObjectName(u"LogOutButton")

        self.verticalLayout.addWidget(self.LogOutButton)

        HomePageMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(HomePageMainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        HomePageMainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(HomePageMainWindow)
        self.statusbar.setObjectName(u"statusbar")
        HomePageMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HomePageMainWindow)

        QMetaObject.connectSlotsByName(HomePageMainWindow)
    # setupUi

    def retranslateUi(self, HomePageMainWindow):
        HomePageMainWindow.setWindowTitle(QCoreApplication.translate("HomePageMainWindow", u"Home Page", None))
        self.dbConnCheckLabel.setText(QCoreApplication.translate("HomePageMainWindow", u"TextLabel", None))
        self.ViewAssetsButton.setText(QCoreApplication.translate("HomePageMainWindow", u"View Assets", None))
        self.ViewHardwareSoftwareLink.setText(QCoreApplication.translate("HomePageMainWindow", u"View Link Between Hardware and Software Assets", None))
        self.AddAssetButton.setText(QCoreApplication.translate("HomePageMainWindow", u"Add Asset", None))
        self.AddUserButton.setText(QCoreApplication.translate("HomePageMainWindow", u"Add New User", None))
        self.ViewLog.setText(QCoreApplication.translate("HomePageMainWindow", u"View Change Log", None))
        self.LogOutButton.setText(QCoreApplication.translate("HomePageMainWindow", u"LogOut", None))
    # retranslateUi

