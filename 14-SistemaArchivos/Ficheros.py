from io import open
import pathlib
import shutil


#Abrir archivo
#archivo=open("./14-SistemaArchivos/fichero_texto.txt","a+")

# #obtener ruta de archivo
# ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# print(ruta)

# #abrir archivo
# archivo=open(ruta, "a+")
# #Escribir archivo
# archivo.write("*******Soy un texto metido desde python********\n")
# #Cerrar archivo
# archivo.close()


###################Leer contendio ###########################

ruta=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#print(ruta)
#abrir archivo con el permiso r
archivoLectura=open(ruta, "r")

#Leer contenido
# contenido=archivoLectura.read()

# print(contenido)

#leer contendio y guardarlo en una lista
Lista=archivoLectura.readlines()

archivoLectura.close()

#print(Lista)

for elemento in Lista:
    # listaelemento=elemento.split()
    # print(listaelemento)

    #print(f"Elemento: {type (elemento)}")
    print(f"Elemento: {elemento.center(10)}")





#***********Copiar archivo*********
# rutaOriginal=str(pathlib.Path().absolute()) + "/fichero_texto.txt"
# rutaNueva=str(pathlib.Path().absolute()) + "/fichero_textoNuevo.txt"
# shutil.copyfile(rutaOriginal,rutaNueva)



#***********Mover archivo*********

# rutaOriginal=str(pathlib.Path().absolute()) + "/fichero_textoNuevo.txt"
# rutaNueva=str(pathlib.Path().absolute()) + "/fichero_copiadoNUEVO.txt"

# shutil.move(rutaOriginal,rutaNueva)


#***********Eliminar archivo*********

# import os
# os.remove(rutaNueva)



#***********Copmprobar si existe **********

import os.path
#print(os.path.abspath("../"))
rutaComprobar=os.path.abspath("./")+"fichero_texto.txt"
if os.path.isfile(rutaComprobar):
    print("el archivo existe")
else:
    print("el archivo no existe")






