'''
Ejercicio6 mostrar todas las tablas de multiplicar del 1 al 10. mostrando el titulo de la tabla y luego las multiplicaciones del 1 al 10
'''

contador1=0
contador2=0

for contador1 in range(1,11):
    print(f"Tabla del {contador1}")
    for contador2 in range(1,11) :
        print(f"{contador1} x {contador2} = {contador1*contador2}")


