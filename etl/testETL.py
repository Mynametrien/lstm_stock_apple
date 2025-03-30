import pymssql as sql


import pyodbc


string_connect =("DRIVER={ODBC Driver 17 for SQL Server};"
            "SERVER=172.23.16.1,1433;"
            "DATABASE=my_database;"
            "UID=trien;"
            "PWD=123456")
def connect_with_sqlserver(string_connect):
    try:
        conn = pyodbc.connect(
            string_connect
        )
        print('success')
        return conn
    except pyodbc.Error as e :
        print(e)
connection = connect_with_sqlserver(string_connect)






import pandas as pd
connection.cursor().commit()
def truncate_data():
    connection.cursor().execute("truncate table deparments").commit()
def create_table():
        connection.cursor().execute("""create table deparments
        (dep_id int, 
        dep_name nvarchar(50))""").commit()



b =pd.read_csv('test.csv')



















connection.cursor().close()
connection.close()