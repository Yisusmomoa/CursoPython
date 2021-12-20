

variabe="texto prueba"
#funciones generales

#print(variabe)
#print(type(variabe))

#detectar el tipado
comprobar=isinstance(variabe,int)
if comprobar:
    print("Si es un string")
else:
    print("No es un string")


if not isinstance(variabe,float):
    print("la variable no es un float")

