#Diferencia entre variables globales y locales

"""
una variable local que se define dentro de la función y solo se puede usar dentro de la misma, a menos que hagamos un return con esa variable

variables globales son aquellas que se declaran fuera de la función y se pueden suar dentro y fuera de las mismas



"""


#variable global

frase="Algo"
variableglobal=1
print(frase)
print("\n")

def holaMundo():
    frase="hola mundo"
    #variableglobal=10
    global website
    website="uanl.mx"
    print(f"{frase}, el numero es: {variableglobal*10}")
holaMundo()

print("\n")
print(frase)

print(f"{website}")