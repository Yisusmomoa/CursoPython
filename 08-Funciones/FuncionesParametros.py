#Ejemplo2 parametros

#nombre="Brandon Loera"
from main import muestraNombres


nombreint=24
def mostrarTuNombre(_nombre,_edad):
    print(f"Tu nombre es {_nombre}")
    if _edad>=18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

nombre=input("Captura tu nombre: ")
edad=int(input("Captura tu edad: "))


mostrarTuNombre(nombre,edad)
#mostrarTuNombre(nombreint)



