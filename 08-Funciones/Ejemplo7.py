#Ejemplo6 funciones dentro de otras funciones

def funcionSuma(_numero1,_numero2):
    suma=_numero1+_numero2
    return suma
def funcionResta(_numero1,_numero2):
    resta=_numero1-_numero2
    return resta
def funcionMultiplicacion(_numero1,_numero2):
    multi=_numero1*_numero2
    return multi
def funcionDivision(_numero1,_numero2):
    div=_numero1/_numero2
    return div

def Calculadora(_numero1, _numero2,_basicas=False):
    #suma=_numero1+_numero2
    suma=funcionSuma(_numero1,_numero2)
    #resta=_numero1-_numero2
    resta=funcionResta(_numero1,_numero2)
    #multi=_numero1*_numero2
    multi=funcionMultiplicacion(_numero1,_numero2)
    #div=_numero1/_numero2
    div=funcionDivision(_numero1,_numero2)
    cadena=""
    if _basicas!=False:
        cadena+="Suma: "+str(suma)
        cadena+="\n"
        cadena+="Resta: "+str(resta)
        cadena+="\n"
    else:
        cadena+="Multiplicación: "+str(multi)
        cadena+="\n"
        cadena+="División: "+str(div)
    return cadena


print(Calculadora(5,5))



