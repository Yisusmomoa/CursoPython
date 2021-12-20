"""
Ejercicio 2 Escribir un programa que añada valores a una lista
mientras que su longitud sea menor a 120 y luego mostrar la lista
plus: usar while y for
"""

Lista=[]

while True:
    auxnumero=int(input("Captura un numero, o ingresa uno cuyo valro sea mayor a 120 para terminar: "))
    if auxnumero>120:
        break
    else:
        Lista.append(auxnumero)
print(Lista)

i=0
while i<120:
    auxnumero=int(input("Captura un numero: "))

    Lista.append(auxnumero)
    i+=1
print(Lista)

i=0
for i in range(0,121):
    auxnumero=int(input(f"Captura el numero que estará en la posición {i+1}: "))

    Lista.append(auxnumero)
print(Lista)
