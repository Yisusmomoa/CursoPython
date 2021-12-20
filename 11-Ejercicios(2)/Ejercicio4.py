"""
Ejercicio 4 Crear un script que tenga 4 variables,una lista,
un string, un entero y un booleano y que imprima un mensaje
según el tipo de dato de cada variable. Usar funciones
"""

def funcMuestraTipoDeDato(_variable):
    cadena=""
    if type(_variable)==bool:
        cadena="la variable es de tipo booleana"
    elif type(_variable)==int:
        cadena="la variable es de tipo int"
    elif type(_variable)==list:
        cadena="La variable es de tipo lista"
    elif type(_variable)==str:
        cadena="La variable es de tipo string"
    return cadena

variableLista=["Hola mundo",24]
variableString="Hola"
variableEnteri=129
variableBoolean=True


print(funcMuestraTipoDeDato(variableBoolean))