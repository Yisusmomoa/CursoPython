# contador=1
# while contador<=100:
#     print(f" estoy en el numero {contador}")
#     contador+=1


# contador=1
# muestrame=str(0)
# while contador<=100:
#     muestrame=muestrame+", "+str(contador)
#     contador+=1
# else:
#     print(muestrame)


numerousuario=int(input("de qué numero quieres ver la tabla: "))
contador=1
if numerousuario<1:
    numerousuario=1
while contador <= 10:
    print(f"{numerousuario} x {contador} = {numerousuario*contador}")
    contador+=1

print("fin bucle")


