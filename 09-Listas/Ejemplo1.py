"""
Listas(Arrays)
son colecciones o conjuntos de deatos/valores, bajo u unico nombre
para acceder a esos valores podemos usar un indice númerico

"""
#definir lista
from typing import List


peliculas=["batman","spiderman","superman","señor de los anillos","alien"]
cantantes=list(("axl","freddy","2pac","alfred"))

peliculas[0]="BATMAN"
cantantes[0]="BATMAN"

print(peliculas)
print(cantantes)


#Crear una lista con un rango numerico o elementos mezclados

años=list(range(2020,2050))
print(años)

#lista variada
variada=["Brandon",24,23.12,True,"texto"]
print(variada)

