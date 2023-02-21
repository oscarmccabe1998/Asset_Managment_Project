from dbConnection import create_db_connection, host, uname, pwd, db_name
from findCurrentSystem import run

# Articles from free code camp and psycopg were used to implement parts of the query creation and execution
# Free code camp article can be found at https://www.freecodecamp.org/news/connect-python-with-sql/
# psycopg article can be found at https://www.psycopg.org/psycopg3/docs/basic/params.html

def execute_query(connection, query, data):         #Function to bind parameters and execute query
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: '{err}'")
    cursor.close()

def Setup_query(New_Asset):             #Function to return correct query
    if New_Asset.ManufactureDate != "NULL" and New_Asset.Note != "NULL":        #Checks for NULL values and removes them from the query
        query = "INSERT INTO Assets (Sys_Name, Sys_Type, Sys_MacAddress, Sys_Ip, Sys_Model, Sys_Manufacturer, Manufacturer_Date, Sys_Note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    elif New_Asset.Note == "NULL" and New_Asset.ManufactureDate == "NULL":
        query = "INSERT INTO Assets (Sys_Name, Sys_Type, Sys_MacAddress, Sys_Ip, Sys_Model, Sys_Manufacturer) VALUES (%s, %s, %s, %s, %s, %s);"
    elif New_Asset.ManufactureDate == "NULL":
        query = "INSERT INTO Assets (Sys_Name, Sys_Type, Sys_MacAddress, Sys_Ip, Sys_Model, Sys_Manufacturer, Sys_Note) VALUES (%s, %s, %s, %s, %s, %s, %s);"
    elif New_Asset.Note == "NULL":
        query = "INSERT INTO Assets (Sys_Name, Sys_Type, Sys_MacAddress, Sys_Ip, Sys_Model, Sys_Manufacturer, Manufacturer_Date) VALUES (%s, %s, %s, %s, %s, %s, %s);"

    return query

def Setup_data(New_Asset):      #Function to return the correct data for the query
    if New_Asset.ManufactureDate != "NULL" and New_Asset.Note != "NULL":        #Checks for NULL values and removes them from the data used in the query
        data = (New_Asset.sysName, New_Asset.sysMachine, New_Asset.sysMacAddress, New_Asset.sysIP, New_Asset.sysModel, New_Asset.sysManufacturer, New_Asset.ManufactureDate, New_Asset.Note)
    elif New_Asset.Note == "NULL" and New_Asset.ManufactureDate == "NULL":
        data = (New_Asset.sysName, New_Asset.sysMachine, New_Asset.sysMacAddress, New_Asset.sysIP, New_Asset.sysModel, New_Asset.sysManufacturer)
    elif New_Asset.ManufactureDate == "NULL":
        data = (New_Asset.sysName, New_Asset.sysMachine, New_Asset.sysMacAddress, New_Asset.sysIP, New_Asset.sysModel, New_Asset.sysManufacturer, New_Asset.Note)
    elif New_Asset.Note == "NULL":
        data = (New_Asset.sysName, New_Asset.sysMachine, New_Asset.sysMacAddress, New_Asset.sysIP, New_Asset.sysModel, New_Asset.sysManufacturer, New_Asset.ManufactureDate)

    return data

def PrepSQL(New_Asset):     #Checks if the system is recorded in the database and if not executes query to add asset to database
    SysSearch = run()
    if SysSearch == 0:
        connection = create_db_connection(host, uname, pwd, db_name)
        query = Setup_query(New_Asset)
        data = Setup_data(New_Asset)
        execute_query(connection, query, data)
    else:
        print("System already recorded in database")

if __name__ == "__main__":
    PrepSQL(New_Asset)
