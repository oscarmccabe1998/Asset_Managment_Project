from dbConnection import create_db_connection, host, uname, pwd, db_name

# Articles from free code camp and psycopg were used to implement parts of the query creation and execution
# Free code camp article can be found at https://www.freecodecamp.org/news/connect-python-with-sql/
# psycopg article can be found at https://www.psycopg.org/psycopg3/docs/basic/params.html

def UpdateQuery(connection, query, data):       #Function to bind the parameters from data with the query and execute the query
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: '{err}'")
    cursor.close()

def Setup_query(AssetForDb):        #Sets up the query as prepared statement
    query = "UPDATE Assets SET Sys_Name = %s, Sys_Type = %s, Sys_Ip = %s, Sys_Model = %s, Sys_Manufacturer = %s, Manufacturer_Date = %s, Sys_Note = %s WHERE id = %s;"
    return query

def Setup_data(AssetForDb):     #Takes information from AssetForDb object and binds it to data object
    data = (AssetForDb.sysName, AssetForDb.sysMachine, AssetForDb.sysIP, AssetForDb.sysModel, AssetForDb.sysManufacturer, AssetForDb.ManufactureDate, AssetForDb.Note, AssetForDb.id)
    print(data)
    print (AssetForDb.sysMacAddress)
    return data

def Setup_Software_Query():
    query = "UPDATE SoftwareAssets SET Name = %s, ProductVersion = %s, BuildVersion = %s, Manufacturer = %s WHERE id =%s;"
    return query

def Setup_Software_Data(SoftwareAssetForDb):
    data = (SoftwareAssetForDb.Name, SoftwareAssetForDb.Version, SoftwareAssetForDb.BuildVersion, SoftwareAssetForDb.Manufacturer, SoftwareAssetForDb.id)
    return data

def executeUpdate(AssetForDb):      #asigns results from query and data function to objects and sends them to the Update query function
    connection = create_db_connection(host, uname, pwd, db_name)    #gets connection script from dbConnection.py
    query = Setup_query(AssetForDb)
    data = Setup_data(AssetForDb)
    UpdateQuery(connection, query, data)

def executeUpdateSoftware(SoftwareAssetForDb):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = Setup_Software_Query()
    data = Setup_Software_Data(SoftwareAssetForDb)
    UpdateQuery(connection, query, data)

if __name__ == "__main__":
    executeUpdate(AssetForDb)
