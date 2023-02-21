import sys
from PySide6 import QtWidgets
from findCurrentSystem import run
from Homepage import Ui_HomePageMainWindow


class HomePage(QtWidgets.QMainWindow, Ui_HomePageMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        self.setupUi(self)
        SysSearch = run()
        if SysSearch >= 1:
            self.dbConnCheckLabel.setText("System found")
        elif SysSearch == 0:
            self.dbConnCheckLabel.setText("System not found")

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = HomePage()
    w.show()
    app.exec()
