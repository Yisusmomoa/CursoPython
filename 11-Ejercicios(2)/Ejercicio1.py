"""
Ejercicio 1 Hacer un programa que tenga una lista de 8 numeros enteros y haga lo siguiente
    -recorrer la lista y mostrarla (función) LISTO
    -hacer función que recorra la lista de numeros y devuelva un string LISTO
    -ordenarla y mostrarla (función) LISTO
    -mostrar su longitud (función lambda) LISTO
    -buscar algún numero que el usuario pida en la lista(función)
"""
from typing import List


Lista=[1,9,30,126,0,2,4,5]

#-recorrer la lista y mostrarla (función) LISTO
def funcRecorreMuestraListaFor(_ListaAux):
    for indice,numero in enumerate( _ListaAux):
        print(f"Numero de la lista: {numero} y con indice: {indice}")

#-hacer función que recorra la lista de numeros y devuelva un string LISTO
def funcRecorreListaString(_ListaAux):
    cadena=""
    for numero in _ListaAux:
        cadena+=f"{numero}, "
    return cadena

# -buscar algún numero que el usuario pida en la lista(función)
def funcBuscarNumeroLista(_Numeroaux):
    position=-1
    for i in range(len(Lista)):
        if Lista[i]==_Numeroaux:
            position=i
            return position
    return position

# #-hacer función que recorra la lista de numeros y devuelva un string LISTO
# print(funcRecorreListaString(Lista))

# #-ordenarla y mostrarla (función) LISTO
# funcRecorreMuestraListaFor(Lista)
# print("**********")
# Lista.sort()        
# funcRecorreMuestraListaFor(Lista)

# #-mostrar su longitud (función lambda) LISTO
# LongitudLista=lambda _lista:print(f"La lonngitud de la lista es: {len(_lista)}")
# LongitudLista(Lista)

# # -buscar algún numero que el usuario pida en la lista(función)
numero=int(input("Busca un numero: "))

auxposition=funcBuscarNumeroLista(numero)
if auxposition>-1:
    print(f"El numero que buscaste es: {Lista[auxposition]} y se encuentra en la posición: {auxposition}")
else :
    print(f"El numero que buscaste no se encuentra en la lista")
