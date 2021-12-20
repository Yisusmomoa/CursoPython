''''
#EJEMPLO 1
color=input("Cuál es mi color favorito?")

if color=="rojo":
    print("El color es rojo")
else:
    print("Color incorecto")
'''

# #EJEMPLO 2
# year=2021
# year=input("En qué año estamos?")
# if int(year)>=2022:
#     print("estamos en el 2022 o adelante")
# else:
#     print("Es un año anterior al 2022")


# #EJEMPLO 3

# nombre="brandon loera"
# ciudad="mty"
# continente="america"
# edad=24
# usuario={
#     "nombre":"brandon loera",
#     "ciudad":"mty",
#     "continente":"america",
#     "edad":24
# }

# mayoria_edad=18

# if usuario.get("edad") >=mayoria_edad :
#     print(f"{usuario.get('nombre')} es mayor de edad")

#     if usuario.get("continente")!="america" :
#         print("no es occidental")
#     else :
#         print(f"Es occidental y de {usuario.get('continente')}")    
# else :
#     print(f"{usuario.get('nombre')} no es mayor de edad")



# #EJEMPLO 4

# dia=1

# if dia==1 :
#     print("es lunes")
# elif dia==2 :
#     print("es martes")
# elif dia==3 :
#     print("es miercoles")
# elif dia==4 :
#     print("es jueves")
# elif dia==5 :
#     print("es viernes")
# else :
#     print("fin de semana")




# #EJEMPLO 5
#operadores logicos
# and Y
# or o
# ! negacion
# not no

# edadminima=18
# edadmaxima=65
# edadoficial=int(input("qué edad tienes?"))

# if edadoficial >=18 and edadoficial <=65 :
#     print("puedes trabajar")
# else :
#     print("no puedes trabajar")


# # #EJEMPLO 6
# pais="Alemania"

# if pais=="mexico" or pais=="españa" or pais=="colombia" :
#     print(f"{pais} es un pais de habla hispana")
# else :
#     print(f"{pais} no es un pais de habla hsipana")




# # #EJEMPLO 7
# pais="españa"

# if not (pais=="mexico" or pais=="españa" or pais=="colombia") :
#     print(f"{pais} es un pais de habla hispana")
# else :
#     print(f"{pais} no es un pais de habla hsipana")

# #EJEMPLO 8
pais="colombia"

if pais!="mexico" and pais!="españa" and pais=="colombia" :
    print(f"{pais} es un pais de habla hispana")
else :
    print(f"{pais} no es un pais de habla hsipana")



