def holaMundo(_nombre):
    return f"Hola {_nombre}"

def Calculadora(_numero1, _numero2,_basicas=False):
    suma=_numero1+_numero2
    # suma=funcionSuma(_numero1,_numero2)
    resta=_numero1-_numero2
    # resta=funcionResta(_numero1,_numero2)
    multi=_numero1*_numero2
    # multi=funcionMultiplicacion(_numero1,_numero2)
    div=_numero1/_numero2
    # div=funcionDivision(_numero1,_numero2)
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
        cadena+="\n"
    return cadena