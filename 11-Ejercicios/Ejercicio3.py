"""
Ejercicio 3 Programa que compruebe si una variable está vacia
y si está vacia, rellenarla con texto en minusculas y mostrarlo
en mayusulas
"""

variable="qe"
if len(variable.strip())<=0:
    variable="relleno"
    print(variable.upper())
else:
    print(variable)

