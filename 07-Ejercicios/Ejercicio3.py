'''
Ejercicio3 escribir un programa que muestre los cuadrados 
(un numero multiplicado por si mismo), de los 60 primeros numeros naturales.
resolverlo con while y for
'''

print("for")
contador=0
for contador in range(1,61) :
    print(f"Cuadrado del numemro {contador}: {contador*contador}")
    contador+=1

print("\n")
print("***************************************\n")
print("While")
contador=0
while contador<61 :
    print(f"Cuadrado del numemro {contador}: {contador*contador}")
    contador+=1