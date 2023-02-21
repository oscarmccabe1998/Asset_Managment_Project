from dbConnection import create_db_connection, host, uname, pwd, db_name

def execute(connection, query, data):
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: '{err}'")
    cursor.close()

def LogQuery():
    query = "INSERT INTO ChangeLog (User, Action, Asset) VALUES (%s, %s, %s);"
    return query

def LogData(user, Action, Asset):
    username = {'user' : user }
    actions = {'action' : Action}
    hw = {'asset' : Asset}
    data = (user, Action, Asset)
    print(data)
    return data

def AddToLog(user, Action, Asset):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = LogQuery()
    data = LogData(user, Action, Asset)
    print(data)
    execute(connection, query, data)

