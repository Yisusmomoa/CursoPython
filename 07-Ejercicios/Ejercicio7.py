"""
Ejercicio7 Hacer un programa que muestre todos los numeros impares entre dos numeros que decida el usuario
"""

Numero1=int(input("Captura el primer numero"))
Numero2=int(input("Captura el segundo numero"))
contador=0

if Numero1>Numero2:
    print("El primer numero no puede ser menor que el segundo numero")
else :
    for contador in range(Numero1, Numero2):
        if contador%2!=0 :
            print(f"El numero {contador} es impar")





