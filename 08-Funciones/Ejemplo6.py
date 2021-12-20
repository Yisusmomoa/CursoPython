#Ejemplo 6 Calculadora con parametros, parametros opcionales, y return



def Calculadora(_numero1, _numero2,_basicas=False):
    suma=_numero1+_numero2
    resta=_numero1-_numero2
    multi=_numero1*_numero2
    div=_numero1/_numero2
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


print(Calculadora(5,5,1))



