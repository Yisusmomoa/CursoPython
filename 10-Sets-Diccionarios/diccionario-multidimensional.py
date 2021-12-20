
#Lista con diccionarios

contactos=[
    {
        "Nombre":"Brandon",
        "Email":"Brandon@gmail.com"
    },
    {
        "Nombre":"Luis",
        "Email":"Luis@gmail.com"
    },
    {
        "Nombre":"Salvador",
        "Email":"Salvador@gmail.com"
    }
]
#print(type(contactos))
#print(contactos[0]["Nombre"])

#modificar un campo del diccionario
#contactos[0]["Nombre"]="brando"
#print(contactos[0]["Nombre"])

#print("Lista de contactos")

for contacto in contactos:
    print(f"Nombre contacto: {contacto['Nombre']}")
    print(f"Email contacto: {contacto['Email']}")
    print("\n")







