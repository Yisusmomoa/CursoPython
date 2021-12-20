#Ejemplo4 parametros opcionales


def getEmpleados(_NombreEmpleado, _dni=None):
    print(f"Nombre del empleado: {_NombreEmpleado}")
    if _dni!=None:
        print(f"DNI: {_dni}")


getEmpleados("Brandon", 23456)
getEmpleados("Brandon2")


