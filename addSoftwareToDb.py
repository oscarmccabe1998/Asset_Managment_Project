from dbConnection import create_db_connection, host, uname, pwd, db_name
from GetSelected import SoftwareData, Setup_data, returnItem
from log import AddToLog

def execute_query(connection, query, data):         #Function to bind parameters and execute query
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: '{err}'")
    cursor.close()

def check_query(connection, query, data):         #Executes query and binds paramaeters from data
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

def SetUpCheckQuery():
    query = "SELECT COUNT(*) FROM SoftwareAssets WHERE Name = %s AND ProductVersion = %s AND BuildVersion = %s AND Manufacturer = %s"
    return query

def Setup_query():
     query = "INSERT INTO SoftwareAssets (Name, ProductVersion, BuildVersion, Manufacturer) VALUES (%s, %s, %s, %s);"
     return query

def Setup_data(SystemSoftware):
    data = (SystemSoftware.Name, SystemSoftware.Version, SystemSoftware.BuildVersion, SystemSoftware.Manufacturer)
    return data

def AddSoftware(SystemSoftware, AssetName, user):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = SetUpCheckQuery()
    data = Setup_data(SystemSoftware)
    Check = check_query(connection, query, data)
    for item in range(2):
        Check = Check[0]
    if Check == 0:
        connection = create_db_connection(host, uname, pwd, db_name)
        query = Setup_query()
        execute_query(connection, query, data)
        Check = 1
        action = "Added"
        AddToLog(user, action, AssetName)

    return Check

def ID_query():
    query = "SELECT id FROM SoftwareAssets WHERE Name = %s AND ProductVersion = %s AND BuildVersion = %s AND Manufacturer = %s"
    return query

def getSoftwareId(SystemSoftware):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = ID_query()
    data = Setup_data(SystemSoftware)
    Check = check_query(connection, query, data)
    for item in range(2):
        Check = Check[0]
    return Check

def linkQuery():
    query = "INSERT INTO AssetLink (Hardwareid, Softwareid) VALUES (%s, %s);"
    return query

def linkdata(HardwareID, SoftwareID):
    data = (HardwareID, SoftwareID)
    return data

def CheckForLinkquery():
    query = "SELECT COUNT(*) FROM AssetLink WHERE Hardwareid = %s AND Softwareid = %s;"
    return query

def linkHwSw(HardwareID, SoftwareID):
    connection = create_db_connection(host, uname, pwd, db_name)
    #query = linkQuery()
    data = linkdata(HardwareID, SoftwareID)
    query = CheckForLinkquery()
    CheckLink = check_query(connection, query, data)
    for item in range(2):
        CheckLink = CheckLink[0]
    if CheckLink == 0:
        query = linkQuery()
        execute_query(connection, query, data)
        return True
    else:
        print("Assets Already Linked")
        return False


def manualLink(HWselection, SWselection):
    print (HWselection, SWselection)
    softwareid = SoftwareData(SWselection)
    softwareid = softwareid[0]
    print(softwareid)
    hardwareid = returnItem(HWselection)
    hardwareid = hardwareid[0]
    print(hardwareid)
    result = linkHwSw(hardwareid, softwareid)
    return result
