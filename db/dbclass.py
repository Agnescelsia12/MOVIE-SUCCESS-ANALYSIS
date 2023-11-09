import mysql.connector
class dbclass:
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="it052"
    )