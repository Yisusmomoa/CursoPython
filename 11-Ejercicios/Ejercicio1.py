"""
Ejercicio1. Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
Recorrer la lista y mostrarla
Hacer función que recorra lista de numeros y devuelva un string
ordenarla y mostrarla
mostrar su longitud usanod una función lambda
buscar algún elemento (que el usuario pida por el teclado) en función
"""
listaNumeros=[8,3,1,5,2,6,7,4]
#recorrer lista y ordenarla
def funcRecorrerLista(_listanumeros=[]):
    cadena=""
    for numero in _listanumeros:
        cadena+=str(numero)
        cadena+=", "
    return cadena

listaNumeros.sort()
print(funcRecorrerLista(listaNumeros))
#recorrer lista y ordenarla

#longitud array
LongitudLista=lambda longitud:print(f"La longitud de la lista es: {longitud}")
LongitudLista(len(listaNumeros))
#longitud array

#buscar numero y ver si esta en la lista
NumeroBusqueda=int(input("Que numero quieres buscar?: "))
ComprobarInt=isinstance(NumeroBusqueda,int)

while not ComprobarInt or NumeroBusqueda<=0:
    NumeroBusqueda=int(input("Que numero quieres buscar?: "))
else:
    search=listaNumeros.index(NumeroBusqueda)
    print(f"EL indice del numero que esta buscando es: {search}") 
#buscar numero y ver si esta en la lista
