#Capturar excepciones y manejar errores en código susceptibles a fallos/errores
"""
nombre=input("Captura tu nombre: ")
try:
    if len(nombre)>1:
        nombreUsuario=nombre
    print(f"tu nombre es: {nombreUsuario}")
except:
    print("Ha ocurrido un error, mete bien el nombre")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Ha finalizado el try")
"""


#Manejar multiples erorres/excepciones

"""
try:
    numero=int(input("captura un numero para elevarlo al cuadrado: "))

    print("El cuadrado es: ",str(numero*numero))

    #Manera numero 1 para manejar los errores
except TypeError:
    print("Debes convertir tus cadenas a enteros en el código")
except ValueError:
    print("Debes capturar un numero, no una letra")

    #Manera numero 2 para manejar los errores
except Exception as e:
    if type(e)==ValueError:
        print("Debes capturar un numero, no una letra")
        print("Error! : ", type(e).__name__)
    elif type(e)==TypeError:
        print("Debes convertir tus cadenas a enteros en el código")
        print("Error! : ", type(e).__name__)
"""

#Manejo de excepeciones "Personalizadas" o lanzar exepciones
ErrorEdadNoReal=False
ErrorNombreNoReal=False
ErrorNombreNumero=False
try:
    nombre=input("Introduce el nombre: ")
    edad=int(input("Introduce la edad: "))

    if edad<5 and edad>110:
        ErrorEdadNoReal=True
        raise ValueError("La edad inrtoducida no es real")
    elif len(nombre)<=1:
        ErrorNombreNoReal=True
        raise ValueError("El nombre no esta completo")
    elif nombre.isnumeric():
        ErrorNombreNumero=True
        raise ValueError("El nombre no puede ser un numero")
    else:
        print("Bienvenido al master en python")
except ValueError:
    print("Error al capturar los datos")
    # if ErrorEdadNoReal:
    #     print("La edad inrtoducida no es real")
    # elif ErrorNombreNoReal:
    #     print("El nombre no esta completo")
    # elif ErrorNombreNumero:
    #     print("El nombre no puede ser un numero")
except Exception as e:
    print("existe un error",e)










