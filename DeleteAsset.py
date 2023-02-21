from dbConnection import create_db_connection, host, uname, pwd, db_name
from findCurrentSystem import returnAll, returnSoftware, execute_query

# Articles from free code camp and psycopg were used to implement parts of the query creation and execution
# Free code camp article can be found at https://www.freecodecamp.org/news/connect-python-with-sql/
# psycopg article can be found at https://www.psycopg.org/psycopg3/docs/basic/params.html

def Delete_Query(connection, query, data):      #Sets up query to Delete selected asset
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: '{err}'")
    cursor.close()

def Setup_query():
    query = "DELETE FROM Assets WHERE id = %(id)s;"     #query to delete asset
    return query

def Setup_SoftwareQuery():
    query = "DELETE FROM SoftwareAssets WHERE id = %(id)s;"
    return query

def DeleteSoftwareLinkQuery():
    query = "DELETE FROM AssetLink WHERE Softwareid = %(id)s"
    return query

def CheckHardwareLink():
    query = "SELECT COUNT(*) FROM AssetLink WHERE Softwareid = %(id)s"
    return query

def getSoftwareID():
    query = "SELECT Softwareid FROM AssetLink WHERE Hardwareid = %(id)s"
    return query

def Setup_data(Delete_Item):        #returns id number for the asset getting deleted
    getAllresult = returnAll()
    datafetch = [list(item) for item in getAllresult]
    dataset = []
    for item in datafetch:
        innerlist = []
        for field in item:
            innerlist.append(field)
        dataset.append(innerlist)
    AffetedRow = dataset[Delete_Item]
    data = { 'id' : AffetedRow[0]}      #tuple for sql formatting in module
    return(data)

def Setup_SoftwareData(Delete_Item):
    getAllresult = returnSoftware()
    datafetch = [list(item) for item in getAllresult]
    dataset = []
    for item in datafetch:
        innerlist = []
        for field in item:
            innerlist.append(field)
        dataset.append(innerlist)
    AffetedRow = dataset[Delete_Item]
    data = { 'id' : AffetedRow[0]}      #tuple for sql formatting in module
    return(data)

def execute(Delete_Item):
    connection = create_db_connection(host, uname, pwd, db_name)        #Collects all the parameters and executes delete query
    query = getSoftwareID()
    data = Setup_data(Delete_Item)
    resp = execute_query(connection, query, data)
    if resp:
        for item in range(2):
            resp = resp[0]
        data = { 'id' : resp}
        #data = (resp)
        query = DeleteSoftwareLinkQuery()
        Delete_Query(connection, query, data)
        query = CheckHardwareLink()
        amount = execute_query(connection, query, data)
        for item in range(2):
            amount = amount[0]
        data = Setup_data(Delete_Item)
        query = Setup_query()
        Delete_Query(connection, query, data)
        if amount == 0:
            data = { 'id' : resp}
            query = Setup_SoftwareQuery()
            Delete_Query(connection, query, data)

        print(resp)
        print(amount)
    else:
        print("not linked")
    query = Setup_query()
    Delete_Query(connection, query, data)

def DeleteSoftware(Delete_Item):
    connection = create_db_connection(host, uname, pwd, db_name)
    data = Setup_SoftwareData(Delete_Item)
    query = DeleteSoftwareLinkQuery()
    Delete_Query(connection, query, data)
    query = Setup_SoftwareQuery()
    Delete_Query(connection, query, data)


if __name__ == "__main__":
    Setup_data(Delete_Item)
