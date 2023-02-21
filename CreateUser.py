# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateUser.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_NewUser(object):
    def setupUi(self, NewUser):
        if not NewUser.objectName():
            NewUser.setObjectName(u"NewUser")
        NewUser.resize(800, 600)
        self.centralwidget = QWidget(NewUser)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.UserNamelabel = QLabel(self.centralwidget)
        self.UserNamelabel.setObjectName(u"UserNamelabel")

        self.verticalLayout.addWidget(self.UserNamelabel)

        self.UsernameInput = QLineEdit(self.centralwidget)
        self.UsernameInput.setObjectName(u"UsernameInput")

        self.verticalLayout.addWidget(self.UsernameInput)

        self.Passwordlabel = QLabel(self.centralwidget)
        self.Passwordlabel.setObjectName(u"Passwordlabel")

        self.verticalLayout.addWidget(self.Passwordlabel)

        self.PasswordInput = QLineEdit(self.centralwidget)
        self.PasswordInput.setObjectName(u"PasswordInput")
        self.PasswordInput.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.PasswordInput)

        self.showtext = QCheckBox(self.centralwidget)
        self.showtext.setObjectName(u"showtext")

        self.verticalLayout.addWidget(self.showtext)

        self.Actionlabel = QLabel(self.centralwidget)
        self.Actionlabel.setObjectName(u"Actionlabel")

        self.verticalLayout.addWidget(self.Actionlabel)

        self.CreateUserButton = QPushButton(self.centralwidget)
        self.CreateUserButton.setObjectName(u"CreateUserButton")

        self.verticalLayout.addWidget(self.CreateUserButton)

        self.CancelButton = QPushButton(self.centralwidget)
        self.CancelButton.setObjectName(u"CancelButton")

        self.verticalLayout.addWidget(self.CancelButton)

        NewUser.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(NewUser)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        NewUser.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(NewUser)
        self.statusbar.setObjectName(u"statusbar")
        NewUser.setStatusBar(self.statusbar)

        self.retranslateUi(NewUser)

        QMetaObject.connectSlotsByName(NewUser)
    # setupUi

    def retranslateUi(self, NewUser):
        NewUser.setWindowTitle(QCoreApplication.translate("NewUser", u"Create User", None))
        self.UserNamelabel.setText(QCoreApplication.translate("NewUser", u"Enter User Name for New User", None))
        self.Passwordlabel.setText(QCoreApplication.translate("NewUser", u"Enter Password for New User ", None))
        self.showtext.setText(QCoreApplication.translate("NewUser", u"Show Password", None))
        self.Actionlabel.setText(QCoreApplication.translate("NewUser", u"Click to Create new User ", None))
        self.CreateUserButton.setText(QCoreApplication.translate("NewUser", u"Create New User", None))
        self.CancelButton.setText(QCoreApplication.translate("NewUser", u"Cancel", None))
    # retranslateUi
