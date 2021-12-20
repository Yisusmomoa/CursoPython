#Listas multidimensionales

Contactos=[
    [
        'Antonio',
        'Antonio@gmail.com'
    ],
    [
        'Brandon',
        'Brandon@gmail.com'
    ],
    [
        'Luis',
        'Luis@gmail.com'
    ]
]

#print(Contactos[0][1])
# for contacto in Contactos:
#     print(contacto[0])

for contacto in Contactos:
    for elemento in contacto:
        if contacto.index(elemento)==0:
            print("Nombre: "+elemento)
        else:
            print("Email: "+elemento)
