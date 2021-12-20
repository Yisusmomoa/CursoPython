"""
Ejercicio 2 Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 120 y luego mostrar la lista
hacerlo con for y while
"""

from typing import List


Lista=[]

# for i in range(0,120):
#     #Primera manera
#     #NumeroGuardar=int(input("Captura un numero: "))
#     #Lista.append(NumeroGuardar)

#     #Segunda manera
#     #Lista.append(i)

#     #Tercera manera
#     Lista.append(f"Elemento: {i}")

# for elemento in Lista:
#     print(f"Indice: {Lista.index(elemento)} - {elemento}")

#Con while

# i=0
# while i<121:
#     Lista.append(f"Elemento: {i}")
#     i+=1

# i=0
# while i<121:
#     print(f"La lista es: {Lista[i]}")
#     i+=1

# peliculas=["batman","spiderman","superman","señor de los anillos","alien"]

# i=0
# while i<len(peliculas):
#     print(f"Nombre pelicula: {peliculas[i]}")
#     i+=1
# print("***********************")
# for i in enumerate(peliculas):
#     print(f"Pelicula es: {peliculas}")
# #se repite el indice
Lista2=[1,2,3,56,65,56,2]

# # for elemento in Lista2:
# #     print(f"Indice: {Lista2.index(elemento)} - {elemento}")

# print(f"posición numero 3 {Lista2[3]}")
# print(f"Posición numero 5 {Lista2[5]}")

for indice, nombre in enumerate(Lista2):
    print(f"En {indice} tenemos a {nombre}")

peliculas=["batman","spiderman","superman","señor de los anillos","alien"]

print("***********************")
for indice,NombrePelicula in enumerate(peliculas):
    print(f"Indice de la pelicula: {indice}, y el nombre de la pelicula es: {NombrePelicula}")