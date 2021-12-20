
nada=None #indica que no tiene nada la variable
cadena="Hola soy una cadena"
entero=99
flotante=4.2
boleano=True
boleano2=False
lista=[10,20,30,100,240,300] #array/matriz
listastring=[44,"treinta",30.5,"cuarenta"]
tupla =("master",4562.2,52)#Lista de datos que no pueden cambiar
diccionario={
    "nombre":cadena,
    "apellido":"Loera",
    "edad":entero,
    "genero":True,
    "listamaterias":{
        "materia1":flotante,
        "materia2":lista,
    },
    "arraymaterias":[80,90],
    "tuplamaterias":(80,90)
} #los diccionarios son como un array asociativo o json, que permite tener una clvae y valor
rango=range(9)
datobyte=b"probando"

print(nada)
print(cadena)
print(entero)
print(flotante)
print(boleano)
print(boleano2)
print(lista)
print(listastring)
print(tupla)
print(diccionario)
print(rango)
print(datobyte)

#mostrar tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(boleano))
print(type(boleano2))
print(type(lista))
print(type(listastring))
print(type(tupla))
print(type(diccionario))
print(type(rango))
print(type(datobyte))



texto="soy un texto"
numero=45
print(type(numero))

print(texto+" "+ str(numero))
print(type(numero))

numero=float(45)
print(type(numero))
print(numero)
