'''
escribir un script que muestre en pantalla todos los numeros pares del 1 al 120
'''

contador=0
for contador in range(1,121) :
    if contador%2==0 :
        print(f"El numero {contador} es par")
    contador+=1
print("fin ciclo")