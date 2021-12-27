import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python", #es como un use
    port="3308"
)

#print(database)


cursor=database.cursor(buffered=True)
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

# cursor.execute("SHOW DATABASES")

# for bd in cursor:
#     print(bd)

#Crear tablas

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Vehiculos(
        Id int(10) auto_increment not null,
        Marca varchar(40) not null,
        Modelo varchar(40) not null,
        precio float(10,2) not null,
        CONSTRAINT pk_vehiculo PRIMARY KEY (Id)
    );
""")
# cursor.execute("Show tables")
# for tabla in cursor:
#     print(tabla)

#insertar 1 registro en tabla
# cursor.execute("""
#     INSERT INTO Vehiculos(Marca,Modelo,precio) VALUES("Ford", "challenger",9999.99)
# """)


#insertar datos de una manera más "masiva"
# coches=[
#     ("Porche","911",4589.02),
#     ("Audi","modeloaudi",3999),
#     ("lamborghini","murcielago",9999.99),
#     ("renault","clío",1099)
# ]
# cursor.executemany(""" INSERT INTO Vehiculos(Marca,Modelo,precio) 
#     VALUES(%s,%s,%s) """,coches)
# database.commit()

#consultar tabla 


# cursor.execute("SELECT * FROM Vehiculos")
# result=cursor.fetchall()

# #Muestra toda la info de los coches
# for row in result:
#     print(row)

# #Muestra un dato en concreto
# for row in result:
#     print(row[0])

# cursor.execute("SELECT Marca,Precio FROM Vehiculos where precio<=5000")
# result=cursor.fetchall()
# for row in result:
#     print(row)


# cursor.execute("SELECT * FROM Vehiculos")
# #obtener el primer elemento de la lista que trae
# result=cursor.fetchone()
# print(result)

#Eliminar 

# cursor.execute("Delete from vehiculos where precio<4000")

# database.commit()

# print(cursor.rowcount,"borrados")

#modificar

cursor.execute('UPDATE vehiculos set modelo="cayman" where Id=3')

database.commit()
