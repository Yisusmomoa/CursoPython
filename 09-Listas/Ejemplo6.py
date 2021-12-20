#Funciones predefinidas

peliculas=["batman","spiderman","superman","señor de los anillos","alien"]

numeros=[1,2,5,8,4,3,12,8]


#ordenar una lista
# print(numeros)
# numeros.sort()
# print(numeros)
# peliculas.sort()
# print(peliculas)

#agregar elementos a una lista
# peliculas.append("pelicula")
# peliculas.insert(0,"primer pelicula")#le tengo que indicar en que indice se va a colocar
# print(peliculas)

#Eliminar elemento en base a su posición/indice
# print(numeros)
# numeros.pop(3)
# print(numeros)

#Eliminar un elemento en base a su contenido
# print(peliculas)
# peliculas.remove("superman")
# print(peliculas)

#Dar la vuelta a una lista
# print(numeros)
# numeros.reverse()
# print(numeros)

#Buscar dentro de una lista, con el in puedo buscar un elemento dentro de una lista, es como un operador
#print("batman" in peliculas)

#Contar elementos
#print(len(numeros))

#Cuantas veces aparece un elemento en la lista
# numeros.append(8)
# print(numeros.count(8))

#Conseguir un indice
#print(peliculas.index("batman"))

#Unir dos listas

peliculas.extend(numeros)
print(peliculas)

#recorrer una lista y mostrar su "posicion/indice"
# for indice, nombre in enumerate(lista):
#     if indice==4:
#         print(f"Estoy en la posición numero {indice}")
#     #print("En " + str(indice) + " tenemos a " + nombre)
#     # O con f strings
#     print(f"En {indice} tenemos a {nombre}")
