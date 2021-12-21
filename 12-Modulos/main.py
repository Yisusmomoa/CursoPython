"""
los modulos son funcionalidades ya hechas para reutilizar.
podemos conseguir modulos que ya vienen en el lenguaje, que vienen en internet o crear nuestros propios modulos
Crear un modulo
se crea una archivo externo al .main
"""
#importar modulo propio, te importa todas las funcionss que tenga ese modulo
#import MiModulo
# print(MiModulo.holaMundo("Brandon"))
# print(MiModulo.Calculadora(10,5))

#importar solo una función del modulo
#from MiModulo import holaMundo
#print(holaMundo("Brandon"))

#Importar todas las funcionalidades, pero sin la necesidad de usar "Mimodulo.nombrefuncion"
# from MiModulo import *
# print(holaMundo("Brandon"))

#**********************Modulo de fechas**********************
#**********************Modulo de fechas**********************
#**********************Modulo de fechas**********************
#**********************Modulo de fechas**********************

import datetime

# print(datetime.date.today())

# fechacompleta=datetime.datetime.now()
# print(fechacompleta)
# print(fechacompleta.year)
# print(fechacompleta.month)
# print(fechacompleta.day)
# print(fechacompleta.hour)
# print(fechacompleta.second)

# fechaPersonalizada=fechacompleta.strftime("%d/%m/%Y\t %I:%M %p")
# print(fechaPersonalizada)


# print(datetime.datetime.now().time())


#**********************Modulo de Matematicas**********************
#**********************Modulo de Matematicas**********************
#**********************Modulo de Matematicas**********************
#**********************Modulo de Matematicas**********************

import math
# print("La raíz cuadrada de 10 es: ",math.sqrt(10) )
# print("Numero pi:", math.pi)
# print("Numero pi:", math.pi)
# print("Redondear: ", math.ceil(math.pi))#redondea hacia arriba
# print("Redondear: ", math.floor(math.pi))#redondea hacia abajo

#**********************Modulo de Random**********************
#**********************Modulo de Random**********************
#**********************Modulo de Random**********************
#**********************Modulo de Random**********************

import random
print("Numero aleatorio entre 15 y 67: ",random.randint(15,67) )
