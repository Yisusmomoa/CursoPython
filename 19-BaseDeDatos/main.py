import mysql.connector

database=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
)

print(database)




