"""
Ejercicio 4 Crear un script que tenga 4 variables, una lista,
un string, un entero y un boleano y que imprima un mensaje
según el tipo de dato de cada variable.Usar funciones
"""

VaribaleLista=[1,2,3,4]
VariableString="Hola"
VariableEntero=12
VariableBoleana=True

def traducirtipo(_tipo):
    resultado=""
    if _tipo==list:
        resultado="Lista"
    elif _tipo==str:
        resultado="String"
    elif _tipo==int:
        resultado="Int"
    elif _tipo==bool:
        resultado="Boleano"
    return resultado

def funImprimirTipoDeDato(_Variable,_tipo):
    comprobar=isinstance(_Variable,_tipo)
    resultado=""
    if comprobar:
        tipoaux=traducirtipo(_tipo)
        resultado=f"Este dato es del tipo {tipoaux}"
    else:
        resultado=None
    return resultado


print(funImprimirTipoDeDato(VaribaleLista,type(VaribaleLista)))
print(funImprimirTipoDeDato(VariableString,type(VariableString)))
print(funImprimirTipoDeDato(VariableEntero,type(VariableEntero)))
print(funImprimirTipoDeDato(VariableBoleana,type(VariableBoleana)))