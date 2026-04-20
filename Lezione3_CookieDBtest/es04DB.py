# pip install mysql-connector-python
import mysql.connector as sql

connection = sql.connect(
    host="127.0.0.1",
    port=3306,
    user="root",
    password="root",
    database="pythondb"
)
print(connection)

cursor = connection.cursor()
# result = cursor.execute(
#     """
#     CREATE TABLE user (
#     username varchar(256) primary key,
#     password varchar(256)
#     );
#     """)

cursor.execute("SELECT * FROM user")
#result = cursor.fetchone() # ritorna una riga di osservazione
result = cursor.fetchall()  # ritorna tutte le righe in una lista

username = input("username: ")
password = input("password: ")

query = f"""INSERT INTO user VALUES ('{username}','{password}')"""
print (query)
cursor.execute(query)
connection.commit()


print (result)