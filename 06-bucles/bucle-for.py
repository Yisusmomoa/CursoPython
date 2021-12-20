
contador=0
suma=0
for contador in range(1,6):
    
    print("voy por el: "+str(contador))
    suma+=contador
print(f"el resultado es: {suma}")


#Ejemplo tablas de multiplicar

numerousuario=int(input("de qué numero quieres ver la tabla"))

if numerousuario<1:
    numerousuario=1
print(f"tabla de multiplicar de {numerousuario}")

for numero_tabla in range(1,11):
    print(f"{numerousuario} x {numero_tabla} = {numerousuario*numero_tabla}")
else:
    print("tabla finalizada")
