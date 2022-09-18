#homework 1

from multiprocessing import connection
import mysql.connector
from mysql.connector import Error

def create_con(hostname, username, userpw, dbname):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = hostname,
            user = username,
            password = userpw,
            database = dbname
        )
        print("success")
    except Error as e:
        print(f'the error {e} occured')
    return connection
conn = create_con('cis3368fall.cbmpmlny9i9n.us-east-1.rds.amazonaws.com', 'admin', 'donnahuynh', 'cis3368')
cursor = conn.cursor(dictionary = True)
sql = 'select * from log'
cursor.execute(sql)
rows = cursor.fetchall()

#values are id,year,comment,revisit


while(True):
    print("Menu")
    print("a- Add travel log")
    print("d- Remove travel log ")
    print("u- Update travel log")
    print("o- Output entire log in console")
    print("s- Save travel log to database")
    print("q-Quit")
    result = input("Where would you like to go, traveler?: \n")
    if 'q' in result:
        exit()
    if 'o' in result:
        cursor.execute(sql)
        rows = cursor.fetchall()
        print(rows)
    if 'd' in result:
        print("which log would you like to delete")
    if 'u' in result:
        print("Update travel log time")
    if 'a' in result:
        inputID = input()
        inputYEAR = input()
        inputCOMMENT = input()
        inputREVISIT = input()
        aresult = (
            "INSERT INTO log (id,years,comments,revisit)"
            "VALUES (%s,%s,%s,%s)"
        )
        data = (inputID,inputYEAR,inputCOMMENT,inputREVISIT)
        try:
            cursor.execute(aresult,data)
            conn.commit()
        except:
            conn.rollback()
        print("Travel Log Inserted")













