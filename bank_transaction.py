
import mysql.connector
from mysql.connector import Error


def connect():
    """ function to connect and fetch rows in a database """

    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            database='bank_transaction',
            user='damilicious',
            password='Atilola0672')

        print("Connected to the database")
    except Error as e:
        print('Not connecting: ', e)
    finally:
        if conn is not None and conn.is_connected():
            return conn