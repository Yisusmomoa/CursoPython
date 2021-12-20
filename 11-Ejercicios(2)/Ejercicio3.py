"""
Ejercicio 3 Progarama que compruebe si una variable está vacia
y si está vacia, rellenarla con texto en minusculas y mostrarlo
en mayusculas
"""
variable=""

if len(variable)>0:
    print(f"{variable}")
else:
    variable="texto de relleno"
    print(f"{variable.upper()}")


