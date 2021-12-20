Numero1=int(input("Captura el numero1: "))
Numero2=int(input("Captura el numero2: "))

contador=0
print(f"Numeros impares desde el {Numero1} hasta el {Numero2}")
for contador in range(Numero1, Numero2+1):
    if contador%2!=0:
        print(f"Numero impar: {contador}")
else:
    print("Fin ciclo")