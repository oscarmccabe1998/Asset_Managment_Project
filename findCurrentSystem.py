from dbConnection import create_db_connection, host, uname, pwd, db_name
from SystemInfo import getIP

# Articles from free code camp and psycopg were used to implement parts of the query creation and execution
# Free code camp article can be found at https://www.freecodecamp.org/news/connect-python-with-sql/
# psycopg article can be found at https://www.psycopg.org/psycopg3/docs/basic/params.html


def execute_query(connection, query, data):         #Executes query and binds paramaeters from data
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query, data)
        result = cursor.fetchall()
        #print(result)
        return result
    except Error as err:
        print(f"Error: '{err}'")
    cursor.close()

def findAll_query(connection):          #Query to return all assets in the database
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute("SELECT * FROM Assets")
        getAllresult = cursor.fetchall()
        #print(getAllresult)
        return getAllresult
    except Err as err:
        print(f"Error: '{err}'")

def getLog(connection):          #Query to return all assets in the database
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute("SELECT * FROM ChangeLog")
        getAllresult = cursor.fetchall()
        #print(getAllresult)
        return getAllresult
    except Err as err:
        print(f"Error: '{err}'")

def findAllSoftware(connection):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute("SELECT * FROM SoftwareAssets")
        getAllresult = cursor.fetchall()
        #print(getAllresult)
        return getAllresult
    except Err as err:
        print(f"Error: '{err}'")

def returnIP():                     #gets ip address from current asset
    interfaceinfo = getIP()
    ip = interfaceinfo[0]
    data = { 'sysIP' : ip }
    return data

def returnMac():
    interfaceinfo = getIP()
    listitem = []
    mac = interfaceinfo[1]
    data = { 'sysMAC ' : mac}
    listitem.append(mac)
    return listitem

def prepQuery():                    #query to find this machine via ip address since ip is static
    ip = getIP()
    query = "SELECT COUNT(*) FROM `Assets` WHERE Sys_MacAddress = %s ;"
    #print(query)
    return query

def findidQuery():
    query = "SELECT id FROM `Assets` WHERE Sys_MacAddress = %s ;"
    return query

def LinkQuery():
    query = "SELECT SoftwareAssets.id, SoftwareAssets.Name, SoftwareAssets.ProductVersion, SoftwareAssets.BuildVersion, SoftwareAssets.Manufacturer FROM (SoftwareAssets INNER JOIN AssetLink ON SoftwareAssets.id = AssetLink.Softwareid) WHERE AssetLink.Hardwareid = %(id)s ;"
    return query

def HardwareLinkQuery():
    query = "SELECT Assets.id, Assets.Sys_Name, Assets.Sys_Type, Assets.Sys_MacAddress, Assets.Sys_Ip, Assets.Sys_Model, Assets.Sys_Manufacturer, Assets.Manufacturer_Date, Assets.Sys_Note FROM (Assets INNER JOIN AssetLink ON Assets.id = AssetLink.Hardwareid) WHERE AssetLink.Softwareid = %(id)s;"
    return query

def findSoftwareByIDQuery():
    query = "SELECT * FROM SoftwareAssets WHERE id = %(id)s;"
    return query

def run():              #Executes query to find the current machine with via the ip address
    connection = create_db_connection(host, uname, pwd, db_name)
    query = prepQuery()
    data = returnMac()
    print(data)
    findAll_query(connection)
    AssetSearch = execute_query(connection, query, data)
    print(AssetSearch)
    SearchResult = AssetSearch[0]           #THIS NEEDS CLEANED UP!!!
    FinalResult = SearchResult[0]
    #print(FinalResult)
    return FinalResult

def returnAll():            #Gets all asset information from the database
    connection = create_db_connection(host, uname, pwd, db_name)
    findAll = findAll_query(connection)
    return findAll

def returnSoftware():
    connection = create_db_connection(host, uname, pwd, db_name)
    software = findAllSoftware(connection)
    return software

def returnHardwareId():
    connection = create_db_connection(host, uname, pwd, db_name)
    query = findidQuery()
    data = returnMac()
    HardwareID = execute_query(connection, query, data)
    print(HardwareID)
    for item in range(2):
        HardwareID = HardwareID[0]
    return HardwareID

def returnLinkData(Asset):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = LinkQuery()
    data = { 'id' : Asset }
    print(data)
    result = execute_query(connection, query, data)
    return result

def VulnerableHardwareData(Softid):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = HardwareLinkQuery()
    data = {'id' : Softid }
    result = execute_query(connection, query, data)
    return result

def findSoftwareByID(ID):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = findSoftwareByIDQuery()
    data = {'id' : ID }
    print("tst")
    result = execute_query(connection, query, data)
    return result

if __name__ == "__main__":
    returnSoftware()
