# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewAssets.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QHeaderView,
    QLabel, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTableView, QVBoxLayout,
    QWidget)

class Ui_AssetViewWindow(object):
    def setupUi(self, AssetViewWindow):
        if not AssetViewWindow.objectName():
            AssetViewWindow.setObjectName(u"AssetViewWindow")
        AssetViewWindow.resize(800, 600)
        self.centralwidget = QWidget(AssetViewWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Instruction = QLabel(self.centralwidget)
        self.Instruction.setObjectName(u"Instruction")

        self.verticalLayout.addWidget(self.Instruction)

        self.AssetsTableView = QTableView(self.centralwidget)
        self.AssetsTableView.setObjectName(u"AssetsTableView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AssetsTableView.sizePolicy().hasHeightForWidth())
        self.AssetsTableView.setSizePolicy(sizePolicy)
        self.AssetsTableView.setBaseSize(QSize(8, 1))
        self.AssetsTableView.setAutoFillBackground(False)
        self.AssetsTableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.AssetsTableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.AssetsTableView.horizontalHeader().setCascadingSectionResizes(True)

        self.verticalLayout.addWidget(self.AssetsTableView)

        self.UpdateButton = QPushButton(self.centralwidget)
        self.UpdateButton.setObjectName(u"UpdateButton")

        self.verticalLayout.addWidget(self.UpdateButton)

        self.DeleteAsset = QPushButton(self.centralwidget)
        self.DeleteAsset.setObjectName(u"DeleteAsset")

        self.verticalLayout.addWidget(self.DeleteAsset)

        self.SoftwareTableView = QTableView(self.centralwidget)
        self.SoftwareTableView.setObjectName(u"SoftwareTableView")
        self.SoftwareTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout.addWidget(self.SoftwareTableView)

        self.UpdateSoftwareButton = QPushButton(self.centralwidget)
        self.UpdateSoftwareButton.setObjectName(u"UpdateSoftwareButton")

        self.verticalLayout.addWidget(self.UpdateSoftwareButton)

        self.DeleteSoftwareButton = QPushButton(self.centralwidget)
        self.DeleteSoftwareButton.setObjectName(u"DeleteSoftwareButton")

        self.verticalLayout.addWidget(self.DeleteSoftwareButton)

        self.LinkAssetsButton = QPushButton(self.centralwidget)
        self.LinkAssetsButton.setObjectName(u"LinkAssetsButton")

        self.verticalLayout.addWidget(self.LinkAssetsButton)

        self.GoBackButton = QPushButton(self.centralwidget)
        self.GoBackButton.setObjectName(u"GoBackButton")

        self.verticalLayout.addWidget(self.GoBackButton)

        AssetViewWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(AssetViewWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        AssetViewWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(AssetViewWindow)
        self.statusbar.setObjectName(u"statusbar")
        AssetViewWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AssetViewWindow)

        QMetaObject.connectSlotsByName(AssetViewWindow)
    # setupUi

    def retranslateUi(self, AssetViewWindow):
        AssetViewWindow.setWindowTitle(QCoreApplication.translate("AssetViewWindow", u"Asset View", None))
        self.Instruction.setText(QCoreApplication.translate("AssetViewWindow", u"TextLabel", None))
        self.UpdateButton.setText(QCoreApplication.translate("AssetViewWindow", u"Update Hardware", None))
        self.DeleteAsset.setText(QCoreApplication.translate("AssetViewWindow", u"Delete Hardware Asset", None))
        self.UpdateSoftwareButton.setText(QCoreApplication.translate("AssetViewWindow", u"Update Software", None))
        self.DeleteSoftwareButton.setText(QCoreApplication.translate("AssetViewWindow", u"Delete Software Asset", None))
        self.LinkAssetsButton.setText(QCoreApplication.translate("AssetViewWindow", u"Link Hardware and Software", None))
        self.GoBackButton.setText(QCoreApplication.translate("AssetViewWindow", u"Go Back", None))
    # retranslateUi
