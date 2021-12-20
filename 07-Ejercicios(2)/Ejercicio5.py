Numero1=int(input("Captura el primer numero: "))
Numero2=int(input("Captura el segundo numero: "))


contador=0

if Numero1>Numero2:
    print("EL primer numero no puede ser mayor que el segundo numero")
else:
    for contador in range(Numero1,Numero2+1):
        print(f"Numero {contador}")

