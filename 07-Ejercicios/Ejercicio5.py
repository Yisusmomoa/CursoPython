"""
Ejercicio5 Hacer un programa que muestre todos lso numeros entre dos numeros que diga el usuario
y validar que el numero uno sea menor que el numero 2
"""

numero1=int(input("Captura el primer numero: "))
numero2=int(input("Captura el segundo numero: "))
contador=0
if numero1>numero2:
    print("Error el numero 1 debe ser meno que el numero 2")
else:
     for contador in range(numero1,numero2+1):
        print(f"{contador}")



