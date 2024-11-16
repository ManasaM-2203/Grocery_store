# import mysql.connector

# __cnx = None

# def get_sql_connection():
#     global __cnx
#     if __cnx is None:
#         __cnx = mysql.connector.connect(user='root',password='Wealthy@1456',
#                                 host='127.0.0.1',
#                                 database='grocery_store')
    
#     return __cnx

import mysql.connector

def get_sql_connection():
    connection = mysql.connector.connect(
        host='127.0.0.1',  # Replace with your MySQL server's host, e.g., '127.0.0.1'
        user='root',  # Replace with your MySQL username
        password='Wealthy@1456',  # Replace with your MySQL password
        database='grocery_store'  # Replace with your database name
    )
    return connection
