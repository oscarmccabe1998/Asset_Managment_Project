from dbConnection import create_db_connection, host, uname, pwd, db_name
import bcrypt
import hashlib
import hmac
import unittest
from base64 import b64encode

BCRYPT_ID     = '2a'
BCRYPT_COST   = 13
BCRYPT_PEPPER = 'hmac_bcrypt'


#information from https://www.geeksforgeeks.org/hashing-passwords-in-python-with-bcrypt/
#was used to implement this system

def hmac_bcrypt_hash(password: str, settings: str, pepper=BCRYPT_PEPPER) -> str:
    cost = BCRYPT_COST
    salt = ''

    if settings:
        (_, _, cost, salt) = settings.split('$')
        cost = int(cost)
    if not cost:
        cost = BCRYPT_COST

    if not salt:
        settings = bcrypt.gensalt(cost)\
                .decode("utf-8")\
                .replace("$2b$", "$2a$")
    else:
        settings = settings[0:29]

    pre_hash = b64encode(
        hmac.new(
            bytes(pepper,   encoding='utf-8'),
            bytes(password, encoding='utf-8'),
            hashlib.sha512
            ).digest()
        ).decode()

    mid_hash = bcrypt.hashpw(
            bytes(pre_hash, encoding='utf-8'),
            bytes(settings, encoding='utf-8')
            )

    post_hash = b64encode(
            hmac.new(
                bytes(pepper, encoding='utf-8'),
                mid_hash,
                hashlib.sha512
                ).digest()
            ).decode().replace('=', '')
    print(post_hash)
    return settings + post_hash

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
                                                    #the first execute fucntion returns a value. the second one just ecexutes a query
def execute_insert(connection, query, data):         #Function to bind parameters and execute query
    cursor = connection.cursor()
    try:
        cursor.execute(query, data)
        connection.commit()
        print("Query sucessful")
    except Error as err:
        print(f"Error: '{err}'")
    cursor.close()

def AddUser(username, passwd):
    if username != "":
        if len(passwd) >= 8:
            connection = create_db_connection(host, uname, pwd, db_name)    #Checks if the username and password provided are valid
            query = checkquery()
            data = CheckUsers(username)
            UserSearch = execute_query(connection, query, data)
            for item in range(2):
                UserSearch = UserSearch[0]
            if UserSearch == 0:
                #bytes = passwd.encode('utf8')       #Encrypts password and adds username and encrypted password to the database
                #salt = bcrypt.gensalt()
                #hash = bcrypt.hashpw(bytes, salt)
                settings =""
                hashed = hmac_bcrypt_hash(passwd, settings)
                connection = create_db_connection(host, uname, pwd, db_name)
                query = InsertQuery()
                data = InsertData(username, hashed)
                execute_insert(connection, query, data)
                return True
            else:
                print("Password is not long enough")
                return False
        else:
            print("Username already taken")
            return False
    else:
        print("You need to enter a username")       #Errors for what might go wrong
        return False

def hmac_bcrypt_verify(password: str, expected: str, pepper=BCRYPT_PEPPER) -> bool:
    return hmac.compare_digest(
            hmac_bcrypt_hash(password, expected, pepper),
            expected
            )

def CheckUsers(username):           #functions to set up apropraiate query and bind the data to them
    data = { 'username' : username }
    return data

def checkquery():
    query = "SELECT COUNT(*) FROM `AssetManagmentUsers` WHERE uname = %(username)s;"
    return query

def InsertQuery():
    query = "INSERT INTO AssetManagmentUsers (uname, pwd) VALUES (%s, %s);"
    return query

def InsertData(username, hash):
    data = (username, hash)
    print(data)
    return data

def LogInUser(username, passwd):
    connection = create_db_connection(host, uname, pwd, db_name)
    query = loginquery()
    data = CheckUsers(username)
    UserSearch = execute_query(connection, query, data) #Gets username and encrypted password from database
    if not UserSearch:
        result = False          #Error checking incase incorrect username or non exsisting username is entered
    else:
        UserSearch = UserSearch[0]
        hash = UserSearch[1]
        #hash = hash.encode('utf8')      #Encodes encryped password and user enteders password for check
        #userBytes = passwd.encode('utf8')
        #userBytes = passwd.encode('utf8')
        result = hmac_bcrypt_verify(passwd, hash)
        #result = bcrypt.checkpw(userBytes, hash)        #checks the password against the encrypted password from the database
    return result



def loginquery():
    query = "SELECT uname, pwd FROM `AssetManagmentUsers` WHERE uname = %(username)s;"
    return query

class TestLogin(unittest.TestCase):
    def test(self):
        expected = True
        actual = LogInUser('admin', 'Password-1')
        self.assertEqual(actual, expected)
    def testincorrectLogin(self):
        self.assertFalse(LogInUser('incorrectUser', 'IncorrectPassword'))
if __name__ == "__main__":
    unittest.main()
