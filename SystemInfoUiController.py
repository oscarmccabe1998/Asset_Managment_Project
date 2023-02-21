import sys
from PySide6 import QtWidgets, QtCore
from SystemInfoUi import Ui_MainWindow
from SystemInfo import getInfo, Sysinfo, getSoftware, SoftwareInfo
from addAssets import PrepSQL
from PySide6.QtCore import Slot, Qt, Signal
from findCurrentSystem import run, returnAll, returnSoftware, returnHardwareId, returnLinkData, VulnerableHardwareData, findSoftwareByID, getLog
from dbConnection import create_db_connection, host, uname, pwd, db_name
from Homepage import Ui_HomePageMainWindow
from ViewAssets import Ui_AssetViewWindow
from UpdateSoftware import Ui_UpdateSoftware
from EditAssets import Ui_EditAssets
from CreateUser import Ui_NewUser
from DeleteAsset import execute, DeleteSoftware
from GetSelected import returnItem, returnSelectedSoftware
from UpdateAsset import executeUpdate, executeUpdateSoftware
from loginSystem import AddUser, LogInUser
from apireq import getres
from addSoftwareToDb import AddSoftware, getSoftwareId, linkHwSw, manualLink
import threading
import stopit 
import platform
import ipaddress
import datetime
import signal
from contextlib import contextmanager
from log import AddToLog

class Add_Asset(Sysinfo):
    def __init__(self, sysName, sysMachine, sysMacAddress, sysIP, sysModel, sysManufacturer, ManufactureDate, Note):
        super().__init__(sysName, sysMachine, sysMacAddress, sysIP, sysModel, sysManufacturer)
        self.ManufactureDate = ManufactureDate
        self.Note = Note

class UpdateAsset(Add_Asset):
    def __init__(self, id, sysName, sysMachine, sysMacAddress, sysIP, sysModel, sysManufacturer, ManufactureDate, Note):
        super().__init__(sysName, sysMachine, sysMacAddress, sysIP, sysModel, sysManufacturer, ManufactureDate, Note)
        self.id = id

class SoftwareAssetFromDb(SoftwareInfo):
    def __init__(self, id, Name, Version, BuildVersion, Manufacturer):
        super().__init__(Name, Version, BuildVersion, Manufacturer)
        self.id = id

class Selected:
    def __init__(self, selected = None):
        self.selected = selected
    def getSelected(self):
        return self.selected
    def setSelected(self, x):
        self.selected = x
        #print(self.selected)

class SelectedSoftware:
    def __init__(self, selectedSoftware = None):
        self.selectedSoftware = selectedSoftware
    def getSelectedSoftware(self):
        return self.selectedSoftware
    def setSelectedSoftware(self, x):
        self.selectedSoftware = x

class LoggedIn:
    def __init__(self, LoggedIn = False):
        self.LoggedIn = LoggedIn
    def getLoggedIn(self):
        return self.LoggedIn
    def setLoggedIn(self, x):
        self.LoggedIn = x
class Username:
    def __init__(self, Username = None):
        self.Username = Username
    def getUsername(self):
        return self.Username 
    def setUsername(self, x):
        self.Username = x

def FormatDates(datafetch):
    DataList = []
    for item in datafetch:      #formats the SQL results into a 2d array to make data useable by tableview
        innerlist = []
        for field in item:
            if type(field) == datetime.date:
                strfeild = str(field)
                items = strfeild.split('-')
                innerlist.append((items[2]+'-'+items[1]+'-'+items[0]))      #formats date
            else:
                innerlist.append(str(field))
        DataList.append(innerlist)
    return DataList

def timeoutdatabase():
    with stopit.ThreadingTimeout(10) as context_manager:
        connection = create_db_connection(host, uname, pwd, db_name)
    if context_manager.state == context_manager.EXECUTED:
        return True
    elif context_manager.state == context_manager.TIMED_OUT:
        return False

currentUser = Username()

LoggedIn = LoggedIn()

#Information from pythonguis was used to help create UI with QT
#The guide can be found at https://www.pythonguis.com/tutorials/pyside6-first-steps-qt-designer/

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        this_system = getInfo()
        print(this_system.sysMacAddress)
        SystemSoftware = getSoftware()
        super(MainWindow, self).__init__()
        self.setupUi(self)
        status = LoggedIn.getLoggedIn()
        if status == True:
            self.Instructions.setText("Please fill out the Manufacture Date and Note fields if applicable, The fields are optional")
            self.label.setText(f"System Name : {this_system.sysName}")
            self.label_2.setText(f"System Type : {this_system.sysMachine}")
            self.mac_label.setText(f"Mac Address : {this_system.sysMacAddress}")
            self.label_3.setText(f"IP Address : {this_system.sysIP}")
            self.label_4.setText(f"Model : {this_system.sysModel}")
            self.label_5.setText(f"Manufacturer : {this_system.sysManufacturer}")
            self.OSNameLabel.setText(f"OS Name :  {SystemSoftware.Name}")
            self.OSVersionLabel.setText(f"OS Version : {SystemSoftware.Version}")
            self.OSBuildVersionLabel.setText(f"OS Build Version : {SystemSoftware.BuildVersion}")
            self.OSManufacturerLabel.setText(f"OS Manufacturer : {SystemSoftware.Manufacturer}")
            @Slot()
            def AddAssetToDB():
                date = self.dateEdit.date() #This needs to be within the fucntion to get the correct date and not the default
                newdate = date.__repr__()
                add_date = newdate.split("(")[1][:-1].replace(", ", "-")    #formats the input from the user for database entry
                #print(add_date)
                text_note = self.textEdit.toPlainText() #Check if the user has entered any text in the text box
                if (len(text_note) == 0):
                    sysNote = "NULL"
                else:
                    sysNote = text_note             #Check if the user has entered a date and ignore the default value
                if add_date == "2000-1-1":
                    sysManufactureDate = "NULL"
                else:
                    sysManufactureDate = add_date
                New_Asset = Add_Asset(this_system.sysName, this_system.sysMachine, this_system.sysMacAddress, this_system.sysIP, this_system.sysModel, this_system.sysManufacturer, sysManufactureDate, sysNote)
                PrepSQL(New_Asset)      #call the function responsible with adding data and send the New_Asset object
                uname = currentUser.getUsername()
                action = "Added"
                AssetName = this_system.sysName
                AddToLog(uname, action, AssetName)
                toggle()
            self.pushButton.clicked.connect(AddAssetToDB)
            def AddSoftwareToDatabase():
                AddSoftware(SystemSoftware)
                uname = currentUser.getUsername()
                action = "Added"
                AssetName = SystemSoftware.Name
                AddToLog(uname, action, AssetName)
            self.AddSoftwareToDbButton.clicked.connect(AddSoftwareToDatabase)
            def LinkAssets():                           
                Check = []
                HardwareCheck = []
                def threadforSoftware():
                    uname = currentUser.getUsername()
                    #action = "Added"
                    AssetName = SystemSoftware.Name
                    SoftwareCheckResult = AddSoftware(SystemSoftware, AssetName, uname)
                    Check.append(SoftwareCheckResult)                               #Threading to make checks run faster 
                CheckThread = threading.Thread(target = threadforSoftware)
                def threadforHardware():
                    HardwareCheckResult = run()
                    HardwareCheck.append(HardwareCheckResult)
                HardwareThread = threading.Thread(target = threadforHardware)                   #give both of these functiond a thread each
                CheckThread.start()
                HardwareThread.start()
                CheckThread.join()
                HardwareThread.join()
                Check = Check[0]
                HardwareCheck = HardwareCheck[0]
                if HardwareCheck == 0:
                    AddAssetToDB()                      #thread both of these functions as well
                    addLink()
                elif Check and HardwareCheck == 1:
                    print("Found")
                    addLink()
            def addLink():
                print("test")
                SoftwareID = []
                HardwareID = []
                def SoftwareIDthread():
                    SoftwareIDresult = getSoftwareId(SystemSoftware)
                    SoftwareID.append(SoftwareIDresult)  #thread the first two of these functions to work concurrently as well not the last two as they rely on the
                def HardwareIDthread():
                    HardwareIDresult = returnHardwareId()
                    HardwareID.append(HardwareIDresult)             #first two functions to return values before they run
                executeSoftwareID = threading.Thread(target=SoftwareIDthread)
                executeHardwareID = threading.Thread(target=HardwareIDthread)
                executeSoftwareID.start()
                executeHardwareID.start()
                executeSoftwareID.join()
                executeHardwareID.join()
                SoftwareID = SoftwareID[0]
                HardwareID = HardwareID[0]
                linkHwSw(HardwareID, SoftwareID)
                toggle()
            self.LinkHardwareAndSoftwareButton.clicked.connect(LinkAssets)



            def toggle():
                self.w = HomePage()
                if self.w.isVisible():
                    self.w.hide()

                else:
                    self.w.show()
                self.close()
            self.Go_Back.clicked.connect(self.toggleHome)

        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()



    def toggleHome(self, checked):
        self.w = HomePage()
        if self.w.isVisible():
            self.w.hide()

        else:
            self.w.show()
        self.close()

class NewUser(QtWidgets.QMainWindow, Ui_NewUser):
    def __init__(self):
        super(NewUser, self).__init__()
        self.setupUi(self)
        status = LoggedIn.getLoggedIn()
        if status == True:
            def stateChange():
                if self.showtext.isChecked():
                    self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
                else:
                    self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.showtext.stateChanged.connect(stateChange)
            def New_User():
                username = self.UsernameInput.text()
                passwd = self.PasswordInput.text()
                newUser = AddUser(username, passwd)
                print(newUser)
                if newUser == True:
                    self.w = HomePage()
                    if self.w.isVisible():
                        self.w.hide()
                    else:
                        self.w.show()
                    self.close()
                elif newUser == False:
                    Alert()
            self.CreateUserButton.clicked.connect(New_User)

            def Alert():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Unable to Log in")
                msg.setText("Unable to create New User. Please ensure the password is atleast 8 characters long and the username isn't already taken")
                #msg.setIcon(QMessageBox.Warning)
                #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                x = msg.exec()

            def Go_Back():
                self.w = HomePage()
                if self.w.isVisible():
                    self.w.hide()
                else:
                    self.w.show()
                self.close()
            self.CancelButton.clicked.connect(Go_Back)
        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()

class LogIn(QtWidgets.QMainWindow, Ui_NewUser):
    def __init__(self):
        super(LogIn, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Login")
        self.UserNamelabel.setText("Enter Username")
        self.Passwordlabel.setText("Enter Password")
        self.Actionlabel.setText("Either click the login button to proceed or cancel to quit the application")
        self.CreateUserButton.setText("Login")
        #code for the timeout function was found at 
        #https://stackoverflow.com/questions/366682/how-to-limit-execution-time-of-a-function-call
        machineuname = platform.uname()
        def connectionattempt():
            connection = create_db_connection(host, uname, pwd, db_name)
        if machineuname.system == "Darwin":
            class TimeoutException(Exception): pass
            
            @contextmanager
            def time_limit(seconds):
                def signal_handler(signum, frame):
                    raise TimeoutException("Timed out!")
                signal.signal(signal.SIGALRM, signal_handler)
                signal.alarm(seconds)
                try:
                    yield
                finally:
                    signal.alarm(0)

            try:
                with time_limit(10):
                    connection = create_db_connection(host, uname, pwd, db_name)
            except TimeoutException as e:
                print("Timed out!")
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Unable to Connect")
                msg.setText("Unable to connect to the database. Please ensure you are connected to the firewall")
                #msg.setIcon(QMessageBox.Warning)
                #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                x = msg.exec()    
                forceExit()
            
        elif machineuname.system == "Windows":
            res = timeoutdatabase()
            if res == False:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Unable to Connect")
                msg.setText("Unable to connect to the database. Please ensure you are connected to the firewall")
                #msg.setIcon(QMessageBox.Warning)
                #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                x = msg.exec()
            
            
        


            
            
            
       
        def stateChange():
            if self.showtext.isChecked():
                self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            else:
                self.PasswordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.showtext.stateChanged.connect(stateChange)


        def Login():
            username = self.UsernameInput.text()
            passwd = self.PasswordInput.text()
            UserLog = LogInUser(username, passwd)
            print (UserLog)
            if UserLog == True:
                print("Logged in")
                LoggedIn.setLoggedIn(UserLog)
                currentUser.setUsername(username)
                self.w = HomePage()
                if self.w.isVisible():
                    self.w.hide()

                else:
                    self.w.show()
                self.close()
            else:
                Alert()
        def Alert():
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Unable to Log in")
            msg.setText("Unable to login. Please check the user name and password are correct")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()


        self.CreateUserButton.clicked.connect(Login)
        self.CancelButton.clicked.connect(self.close)
        def forceExit():
            self.close


class HomePage(QtWidgets.QMainWindow, Ui_HomePageMainWindow):
    def __init__(self):
        super(HomePage, self).__init__()
        self.setupUi(self)
        self.MessageBox.setText("Test")
        uname = currentUser.getUsername()
        print(uname)
        status = LoggedIn.getLoggedIn()
        if status == True:
            SysSearch = run()               #Check to see if the system is already recorded in the database
            if SysSearch >= 1:
                self.dbConnCheckLabel.setText("System found")
                self.MessageBox.setText("It appears that we already have a record of your current machine in our system. Please Select the View Asset Button to Either Update or Delete Asset information and also manually link Hardware and Software Assets\nClick View Link between hardware and Software to View the link between Hardware and Software Assets and view Current vulnerabilities relating to the Assets on the network")
            elif SysSearch == 0:
                self.dbConnCheckLabel.setText("System not found")
                self.MessageBox.setText("We Cannot find any record of your machine in our system. Please press the add asset button to add the system details to the system and quickly link hardware and software on the network.\nPlease Select the View Asset Button to Either Update or Delete Asset information and also manually link Hardware and Software Assets\nClick View Link between hardware and Software to View the link between Hardware and Software Assets and view Current vulnerabilities relating to the Assets on the network")

            self.AddAssetButton.clicked.connect(self.toggle)
            self.ViewAssetsButton.clicked.connect(self.ViewAssetsWindow)
            self.AddUserButton.clicked.connect(self.AddUser)
            self.LogOutButton.clicked.connect(self.logout)
            self.ViewHardwareSoftwareLink.clicked.connect(self.toggleViewRelations)
            self.ViewLog.clicked.connect(self.ViewChanges)
        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()

    def ViewChanges(self, checked):
        self.w = ViewLog()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()

    def toggleViewRelations(self, checked):
        self.w = ViewRelations()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()

    def logout(self, checked):
        LoggedIn.setLoggedIn(False)
        self.w = LogIn()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()

    def AddUser(self, checked):
        self.w = NewUser()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()

    def toggle(self, checked):                  #functions to allow the user to navagate to either the add asset or view assets page
        self.w = MainWindow()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()

    def ViewAssetsWindow(self, checked):
        self.w = ViewAssetsPage()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()

#Some information from pythonguis was used to implement the table view and model
#The information can be found at https://www.pythonguis.com/tutorials/pyside6-qtableview-modelviews-numpy-pandas/

class TableModel(QtCore.QAbstractTableModel):       #sets up the data for the table view in the view assets page
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    headerLabels = ['id', 'Name', 'Type', 'Mac Address', 'IP Adress','Model', 'Manufacturer', 'Manufacture Date', 'System Note']

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headerLabels[section]               #Sets up Headings for columns in table view


    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._data)

    def columnCount(self, index):
        return len(self._data[0])

class SoftwareTableModel(QtCore.QAbstractTableModel):
    def __init__(self, SoftwareData):
        super(SoftwareTableModel, self).__init__()
        self._SoftwareData = SoftwareData

    headers = ['id', 'Name', 'Product Version', 'BuildVersion', 'Manufacturer']

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._SoftwareData[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._SoftwareData)

    def columnCount(self, index):
        return len(self._SoftwareData[0])

class VulnTableModel(QtCore.QAbstractTableModel):
    def __init__(self, VulnData):
        super(VulnTableModel, self).__init__()
        self._VulnData = VulnData

    headers = ['Description', 'Status', 'Last Modified', 'Source']

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._VulnData[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._VulnData)

    def columnCount(self, index):
        return len(self._VulnData[0])

class ChangeLogModel(QtCore.QAbstractTableModel):
    def __init__(self, LogData):
        super(ChangeLogModel, self).__init__()
        self._LogData = LogData
    
    headers = ['id', 'User', 'Action', 'Asset', 'Date of Change']

    def headerData(self, section, orientation, role=Qt.DisplayRole):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return self.headers[section]
    
    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self._LogData[index.row()][index.column()]

    def rowCount(self, index):
        return len(self._LogData)
    
    def columnCount(self, index):
        return len(self._LogData[0])


currentSelection = Selected()           #calls to class selected to get and set current selection
currentSelectionSoftware = SelectedSoftware()

class ViewLog(QtWidgets.QMainWindow, Ui_AssetViewWindow):
    def __init__(self):
        super(ViewLog, self).__init__()
        status = LoggedIn.getLoggedIn()
        if status == True:
            self.setupUi(self)
            self.setWindowTitle("Change Log")
            self.GoBackButton.clicked.connect(self.toggle)
            self.DeleteSoftwareButton.hide()
            self.UpdateSoftwareButton.hide()
            self.DeleteAsset.hide()
            self.LinkAssetsButton.hide()
            self.UpdateButton.hide()
            self.SoftwareTableView.hide()
            self.Instruction.setText("Here you can view changes that have been made to the Assets recorded on the System. Click Go Back to return to home page")
            self.Table = self.AssetsTableView
            connection = create_db_connection(host, uname, pwd, db_name)
            Log = getLog(connection)
            datafetch = [list(item) for item in Log]
            DataList = []
            for item in datafetch:
                innerlist = []
                for field in item:
                    if type(field) == datetime:
                        strfeild = str(field)
                        items = strfeild.split(" ")
                        innerlist.append(strfeild)
                    else:
                        innerlist.append(str(field))
                DataList.append(innerlist)
            data = DataList
            self.model = ChangeLogModel(data)
            self.Table.setModel(self.model)             #Sends data and formats table view for user
            self.Table.resizeColumnsToContents()

        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
    def toggle(self, checked):                  #functions to allow the user to navagate to either the add asset or view assets page
        self.w = HomePage()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()

class ViewVuln(QtWidgets.QMainWindow, Ui_AssetViewWindow):
    def __init__(self):
        super(ViewVuln, self).__init__()
        status = LoggedIn.getLoggedIn()

        if status == True:

            self.setupUi(self)
            self.setWindowTitle("Vulnerability View")
            self.UpdateButton.hide()
            self.DeleteSoftwareButton.hide()
            self.UpdateSoftwareButton.hide()
            self.DeleteAsset.hide()
            self.LinkAssetsButton.hide()
            self.Instruction.setText("You can find a list of vulnerabilities at the top and a list of affected hardware at the bottom. \nScroll to the right to see more information on the table")
            self.Table = self.AssetsTableView
            self.HardwareTable = self.SoftwareTableView
            getSoftware = currentSelectionSoftware.getSelectedSoftware()
            softw = findSoftwareByID(getSoftware)
            softw = softw[0]
            print(softw)
            VulnerableSoft = SoftwareAssetFromDb(softw[0], softw[1], softw[2], softw[3], softw[4])
            print(VulnerableSoft.Name)
            print(softw)
            VulnFetch = getres(VulnerableSoft)
            VulnFetch = [list(item) for item in VulnFetch]
            self.Model = VulnTableModel(VulnFetch)
            self.Table.setModel(self.Model)             #Sends data and formats table view for user
            self.Table.resizeColumnsToContents()
            self.Table.setFixedHeight(250)
            datafetch = VulnerableHardwareData(VulnerableSoft.id)#Need to get hardware data from link table with software id THIS IS WHERE U LEFT OFF!
            HardwareData = FormatDates(datafetch)
            #HardwareData = DataList
            self.Hardmodel = TableModel(HardwareData)
            self.HardwareTable.setModel(self.Hardmodel)             #Sends data and formats table view for user
            self.HardwareTable.resizeColumnsToContents()
            def toggle():              #Returns to the home page
                self.w = ViewRelations()
                if self.w.isVisible():
                    self.w.hide()
                else:
                    self.w.show()
                self.close()
            self.GoBackButton.clicked.connect(toggle)
        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()

class ViewRelations(QtWidgets.QMainWindow, Ui_AssetViewWindow):
    def __init__(self):
        super(ViewRelations, self).__init__()
        status = LoggedIn.getLoggedIn()

        if status == True:

            self.setupUi(self)
            self.setWindowTitle("Asset Link View")
            self.Table = self.AssetsTableView
            self.SoftwareTable = self.SoftwareTableView
            self.Instruction.setText("Select the Hardware Asset you want to view the related Software for, Or you can click view all Software to view all Assets on the Network \nClick View Vulnerabilities to view security risks regarding assets")
            self.UpdateButton.setText("Click to view all software on the network")
            self.DeleteSoftwareButton.hide()
            self.UpdateSoftwareButton.hide()
            self.DeleteAsset.setText("Click to View Software Linked to selected Hardware")
            self.UpdateButton.clicked.connect(self.viewAll)

            #state = 1
            getAllresult = returnAll()
            datafetch = [list(item) for item in getAllresult]   #Gets all the assets recorded on the database
            data = FormatDates(datafetch)
            self.model = TableModel(data)
            self.Table.setModel(self.model)             #Sends data and formats table view for user
            self.Table.resizeColumnsToContents()
            self.LinkAssetsButton.setText("Click to View Current Vulnerabilities Realting to Selected Software")
            def GetRelatedSoftware():
                hardwareindexes = self.Table.selectionModel().selectedRows()
                hardlist = []
                for index in sorted(hardwareindexes):
                    hardlist.append(index.row())
                if len(hardlist) == 1:
                    hardlist = hardlist[0]
                    Asset = returnItem(hardlist)
                    Asset = Asset[0]
                    print(Asset)
                    SoftwareResult = returnLinkData(Asset)
                    if SoftwareResult:
                        print(SoftwareResult)
                        SoftwareFetch = [list(item) for item in SoftwareResult]
                        self.softwareModel = SoftwareTableModel(SoftwareFetch)

                    else:
                        print("No Software Linked to this hadware asset")           
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Not Linked")
                        msg.setText("The selected Hardware Asset is not Linked to a Software Asset")
                        #msg.setIcon(QMessageBox.Warning)
                        #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                        x = msg.exec()
                        self.softwareModel = None
                    self.SoftwareTable.setModel(self.softwareModel)
                    self.SoftwareTable.resizeColumnsToContents()
                    #return SoftwareResult



                else:
                    print("Out of range")
            def getSoft():
                indexes = self.SoftwareTable.selectionModel().selectedRows(column = 0)
                model = self.SoftwareTable.model()
                role = Qt.DisplayRole
                swlist = []
                test = []

                for index in sorted(indexes):
                    swlist.append(index.row())
                    SoftwareId = model.data(index, role)
                    print(f"the id is {SoftwareId}")
                if len(swlist) == 1:
                    swlist = swlist[0]
                    print(f"This is the point {swlist}")
                    return SoftwareId
                else:
                    swlist = "False"
                    return swlist


            def viewvulns():
                try:
                    swlist = getSoft()
                    print(swlist)

                    if swlist != "False":
                        try:
                            print(swlist)
                            currentSelectionSoftware.setSelectedSoftware(swlist)
                            self.w = ViewVuln()
                            if self.w.isVisible():
                                self.w.hide()
                            else:
                                self.w.show()
                            self.close()
                        except:
                            print("unable to call API")
                            Alert()
                    elif swlist == "False":
                        print("inner fail")
                        msg = QtWidgets.QMessageBox()
                        msg.setWindowTitle("Software not selected")
                        msg.setText("Please select a Software asset ")
                        #msg.setIcon(QMessageBox.Warning)
                        #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                        x = msg.exec()
                except:
                    print("Fail")
                    msg = QtWidgets.QMessageBox()
                    msg.setWindowTitle("Software not selected")
                    msg.setText("You need to select a Software Asset. This can be done by either selecting a Hardware Asset and viewing the linked Software Asset or clicking view all Software Assets and Select one of then")
                    #msg.setIcon(QMessageBox.Warning)
                    #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                    x = msg.exec()
                #soft = GetRelatedSoftware()
                #for item in range(2):
                #    soft = soft[0]
                #print(soft)

            self.LinkAssetsButton.clicked.connect(viewvulns)
            def Alert():
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Unable to View Vulnerabilitis")
                msg.setText("Unable to load content, Please wait 30 seconds and try again")
                #msg.setIcon(QMessageBox.Warning)
                #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                x = msg.exec()

            self.DeleteAsset.clicked.connect(GetRelatedSoftware)
            def toggle():              #Returns to the home page
                self.w = HomePage()
                if self.w.isVisible():
                    self.w.hide()
                else:
                    self.w.show()
                self.close()
            self.GoBackButton.clicked.connect(toggle)
        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
    def viewAll(self, checked):
        SoftwareResult = returnSoftware()
        SoftwareFetch = [list(item) for item in SoftwareResult]
        self.softwareModel = SoftwareTableModel(SoftwareFetch)
        self.SoftwareTable.setModel(self.softwareModel)
        self.SoftwareTable.resizeColumnsToContents()



class ViewAssetsPage(QtWidgets.QMainWindow, Ui_AssetViewWindow):
    def __init__(self):
        super(ViewAssetsPage, self).__init__()
        status = LoggedIn.getLoggedIn()
        if status == True:
            self.setupUi(self)
            self.Table = self.AssetsTableView
            self.SoftwareTable = self.SoftwareTableView
            self.Instruction.setText("Selecet the row Containng the Asset information you want to manipulate. Select Update or Delete Asset to carry out the desired action\nSelect one fo each row for linking assets. Select Assets by clicking on the column on the table")
            getAllresult = returnAll()
            datafetch = [list(item) for item in getAllresult]   #Gets all the assets recorded on the database
            data = FormatDates(datafetch)
            SoftwareResult = returnSoftware()
            SoftwareFetch = [list(item) for item in SoftwareResult]
            self.model = TableModel(data)
            self.Table.setModel(self.model)             #Sends data and formats table view for user
            self.Table.resizeColumnsToContents()
            self.softwareModel = SoftwareTableModel(SoftwareFetch)
            self.SoftwareTable.setModel(self.softwareModel)
            self.SoftwareTable.resizeColumnsToContents()
            self.GoBackButton.clicked.connect(self.toggle)
            self.DeleteAsset.clicked.connect(self.checkSelection)
            self.UpdateButton.clicked.connect(self.toggle_Update)
            self.DeleteSoftwareButton.clicked.connect(self.DeleteSoftware)
            self.UpdateSoftwareButton.clicked.connect(self.UpdateSoftware)
            self.LinkAssetsButton.clicked.connect(self.Link)
            
        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()

    def Link(self, checked):
        print("test")
        softwareindexes = self.SoftwareTable.selectionModel().selectedRows()
        softlist = []
        for index in sorted(softwareindexes):
            softlist.append(index.row())
        #print(softlist)
        hardwareindexes = self.Table.selectionModel().selectedRows()
        hardlist = []
        for index in sorted(hardwareindexes):
            hardlist.append(index.row())
        #print(hardlist)
        if len(softlist) and len(hardlist) == 1:
            HWselection = hardlist[0]
            SWselection = softlist[0]
            result = manualLink(HWselection, SWselection)
            if result == False:
                msg = QtWidgets.QMessageBox()
                msg.setWindowTitle("Already Linked")
                msg.setText("The Hadware Asset you are trying to link is already asigned to a Software Asset")
                #msg.setIcon(QMessageBox.Warning)
                #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
                x = msg.exec()
        else:
            print("Out of range")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()

    def UpdateSoftware(self, checked):
        indexes = self.SoftwareTable.selectionModel().selectedRows()
        datalist = []
        for index in sorted(indexes):
            datalist.append(index.row())
        if len(datalist) == 0:
            print("You need to select an asset")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()
        elif len(datalist) == 1:
            SoftwareSelection = datalist[0]
            currentSelectionSoftware.setSelectedSoftware(SoftwareSelection)
            self.w = UpdateSoftware()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
        else:
            print("You can only select one")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()

    def toggle_Update(self, checked):           #Gets currently selected row and sends it to the Edit asset menu

        indexes = self.Table.selectionModel().selectedRows()
        dataList = []
        for index in sorted(indexes):
            dataList.append(index.row())
        if len(dataList) == 0:
            print("You need to select atleast 1 option")            #Error handling to ensure that the user only selects on value at a time to edit
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()
        elif len(dataList) == 1:
            def setSelectedAsset(self):
                tempval = dataList[0]
                EditAsset = tempval
                print(f"the asset is{EditAsset}")
                currentSelection.setSelected(EditAsset)
            setSelectedAsset(self)
            self.w = EditAssets()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
        else:
            print("You can only select one asset")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()

    def DeleteSoftware(self, chceked):
        indexes = self.SoftwareTable.selectionModel().selectedRows()
        swlist = []
        for index in sorted(indexes):
            swlist.append(index.row())
        if len(swlist) == 0:
            print("You need to select atleast one")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()
        elif len(swlist) == 1:
            Delete_Item = index.row()
            DeleteSoftware(Delete_Item)
            uname = currentUser.getUsername()
            action = "Deleted"
            newindex = self.SoftwareTable.selectionModel().selectedRows(column=1)
            model = self.SoftwareTable.model()
            role = Qt.DisplayRole
            poslist = []
            for item in sorted(newindex):
                #poslist.append(item.row())
                AssetName = model.data(item, role)
            AddToLog(uname, action, AssetName)
            self.w = ViewAssetsPage()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
        else:
            print("You can only select one")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()

        




    def checkSelection(self, checked):                          #Checks the user selection again and deletes the selected asset
        #today = datetime.date.today()
        indexes = self.Table.selectionModel().selectedRows()
        checklist = []
        datalist = []
        for index in sorted(indexes):           #More error handling to check the selection again
            tempval = str(index)
            checklist.append(index.row)
        if len(checklist) == 0:
            print(len(checklist))
            print("You Need to select one Asset")
        #    Alert()
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()
        elif len(checklist) == 1:
            
            Delete_Item = index.row()
            uname = currentUser.getUsername()
            Todaysdate = datetime.date.today()
            Todaysdate = str(Todaysdate)
            action = "Deleted"
            newindex = self.Table.selectionModel().selectedRows(column=1)
            model = self.Table.model()
            role = Qt.DisplayRole
            poslist = []
            for item in sorted(newindex):
                #poslist.append(item.row())
                AssetName = model.data(item, role)
            #AssetName = poslist[0]
            print(uname)
            print(action) 
            print(Todaysdate) 
            print(AssetName)
            #action = action.text()
            AddToLog(uname, action, AssetName)
            execute(Delete_Item)
            self.w = ViewAssetsPage()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
            return Delete_Item
        else:
            print("You can only select one Asset")
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Incorrect Selection")
            msg.setText("You need to select one asset from the desired table. You can select a maximum of one asset")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()
            #Alert()

    


    def toggle(self, checked):              #Returns to the home page
        self.w = HomePage()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()
    
    #def Alert():
        

class UpdateSoftware(QtWidgets.QMainWindow, Ui_UpdateSoftware):
    def __init__(self):
        super(UpdateSoftware, self).__init__()
        self.setupUi(self)
        status = LoggedIn.getLoggedIn()
        if status == True:
            SelectedSoftware = currentSelectionSoftware.getSelectedSoftware()
            data = returnSelectedSoftware(SelectedSoftware)
            SoftwareFromDb = SoftwareAssetFromDb(data[0], data[1], data[2], data[3], data[4])
            self.OSNameEdit.setText(SoftwareFromDb.Name)
            self.ProductVersionEdit.setText(SoftwareFromDb.Version)
            self.OSBuildVersionEdit.setText(SoftwareFromDb.BuildVersion)
            self.OSManufacturerEdit.setText(SoftwareFromDb.Manufacturer)
            constantID = SoftwareFromDb.id
            self.SoftwareScanButton.clicked.connect(self.overwrite)
            self.GoBackButton.clicked.connect(self.goBack)
            self.UpdateSoftwareButton.clicked.connect(lambda x: self.UpdateSoftwareAsset(self, constantID))
        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
    def overwrite(self, checked):
        scan = getSoftware()
        self.OSNameEdit.setText(scan.Name)
        self.ProductVersionEdit.setText(scan.Version)
        self.OSBuildVersionEdit.setText(scan.BuildVersion)
        self.OSManufacturerEdit.setText(scan.Manufacturer)
    def goBack(self, checked):
        self.w = ViewAssetsPage()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()
    def UpdateSoftwareAsset(self, checked, constantID):
        OSName =  self.OSNameEdit.text()
        OSVersion = self.ProductVersionEdit.text()
        OSBuildVersion = self.OSBuildVersionEdit.text()
        OSManufacturer = self.OSManufacturerEdit.text()
        print(constantID)
        SoftwareAssetForDb = SoftwareAssetFromDb(constantID, OSName, OSVersion, OSBuildVersion, OSManufacturer)
        executeUpdateSoftware(SoftwareAssetForDb)
        uname = currentUser.getUsername()
        action = "Updated"
        AssetName = OSName+OSVersion
        AddToLog(uname, action, AssetName)
        self.w = ViewAssetsPage()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()



class EditAssets(QtWidgets.QMainWindow, Ui_EditAssets):
    def __init__(self):
        super(EditAssets, self).__init__()
        SelectedAsset = currentSelection.getSelected()          #Gets the selected user asset from the table view and asigns it a new object
        print(f"The selected index is {SelectedAsset}")
        data = returnItem(SelectedAsset)
        print(data)
        AssetFromDb = UpdateAsset(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8])
        constantID = AssetFromDb.id
        self.setupUi(self)
        status = LoggedIn.getLoggedIn()
        if status == True:
            self.Instructions.setText("Replace the text in the text boxes and click the update button to correct any parts of the assets information")
            self.SysNameEdit.setText(AssetFromDb.sysName)
            self.SysTypeEdit.setText(AssetFromDb.sysMachine)            #Auto fills the inputs with data from selected asset
            self.macaddressLabel.setText(AssetFromDb.sysMacAddress)
            self.ipEdit.setText(AssetFromDb.sysIP)
            self.ModelEdit.setText(AssetFromDb.sysModel)
            self.ManufacturerEdit.setText(AssetFromDb.sysManufacturer)
            self.dateEdit.setDate(AssetFromDb.ManufactureDate)
            self.NoteEdit.setText(AssetFromDb.Note)
            self.CancelButton.clicked.connect(self.go_back)
            self.Scan.clicked.connect(self.overwrite)

       
            self.UpdateAssetButton.clicked.connect(lambda x: self.UpdateAssetToDb(self, constantID, AssetFromDb)) #Lambda function to send extra information to the update function
            print(constantID)
        else:
            self.w = LogIn()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()

    def overwrite(self, checked):
        scan = getInfo()
        self.SysNameEdit.setText(scan.sysName)
        self.SysTypeEdit.setText(scan.sysMachine)
        self.ipEdit.setText(scan.sysIP)
        self.ModelEdit.setText(scan.sysModel)
        self.ManufacturerEdit.setText(scan.sysManufacturer)

    def UpdateAssetToDb(self, checked, constantID, AssetFromDb):
        print(constantID)
        tempDate = self.dateEdit.text()
        items = tempDate.split("/")
        newdate = (items[2]+'-'+items[1]+'-'+items[0])      #Formating date from selected asset
        if newdate == "2000-01-01":
            newdate = None
        TextNoteData = self.NoteEdit.toPlainText()
        if (len(TextNoteData) == 0):            #Checking if the date and text are empty
            TextNoteData = None
        UpdatedSysName = self.SysNameEdit.text()#Collecting the information from the text boxes in the edit asset class
        UpdatedSysType = self.SysTypeEdit.text()
        UpdatedSysip = self.ipEdit.text()
        UpdatedSysModel = self.ModelEdit.text()
        UpdatedSysManufacturer = self.ManufacturerEdit.text()
        UpdatedSysDate = newdate
        UpdatedSysNote =  TextNoteData
        returnedip = UpdatedSysip
        try: 
            ip = ipaddress.ip_address(returnedip)
            result = True
        except ValueError:
            result = False
        if result == False:    
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Invalid IP")
            msg.setText("The IP address you have entered is incorrect")
            #msg.setIcon(QMessageBox.Warning)
            #msg.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
            x = msg.exec()
        elif result == True:
            AssetForDb = UpdateAsset(constantID, UpdatedSysName, UpdatedSysType, AssetFromDb.sysMacAddress, UpdatedSysip, UpdatedSysModel, UpdatedSysManufacturer, UpdatedSysDate, UpdatedSysNote)
            uname = currentUser.getUsername()
            action = "Updated"
            AssetName = UpdatedSysName
            AddToLog(uname, action, AssetName)
            executeUpdate(AssetForDb)       #Asign updated values into new object and send it to UpdateAsset to update the values in the database
            self.w = ViewAssetsPage()
            if self.w.isVisible():
                self.w.hide()
            else:
                self.w.show()
            self.close()
                                    #methods to go to different pages within the application
    def go_back(self, checked):
        self.w = ViewAssetsPage()
        if self.w.isVisible():
            self.w.hide()
        else:
            self.w.show()
        self.close()
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    w = LogIn()
    w.show()
    app.exec()
