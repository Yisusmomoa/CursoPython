"""
    crear una lista con el contenido de esta tabla:
    ACCION     AVENTURA             DEPORTES
    GTA        ASSINS               FIFA 21
    COD        CRASH                PRO
    PUGB       PRINCE OF PERSIA     MOTO GP 21
    una lista con un diccionario que almacenará una categoria y una lista de juegos
"""

Lista=[
    {
        "Genero":"Accion",
        "ListaJuegos":["GTA","COD","PUBG"]
    },
    {
        "Genero":"Aventura",
        "ListaJuegos":["ASSINS","CRASH","PRINCE OF PERSIA"]
    },
    {
        "Genero":"Deportes",
        "ListaJuegos":["FIFA 21","PRO","MOTO GP 21"]
    }
]

for genero in Lista:
    print(f"{genero['Genero']}")
    for Videojuego in genero['ListaJuegos']:
        print(f"Videojuego: {Videojuego}")
    print("\n")

