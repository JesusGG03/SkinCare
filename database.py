import mysql.connector
from config import Credentials

class connection:
    connector = mysql.connector
    credentails = Credentials.credentials

    cnx = connector.connect(**credentails)

    print("Database successfully connected")