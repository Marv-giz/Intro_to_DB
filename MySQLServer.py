
import mysql.connector
from mysql.connector import Error

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Joel@20199",
    database="alx_book_store"
)
    if mydb.is_connected():
        cursor = mydb.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database created successfully")

except mysql.connector.Error as err:
    print("Error while connecting to MySQL", err)

finally:
    if cursor is not None:
        cursor.close()
    if mydb is not None and mydb.is_connected():
        mydb.close()
