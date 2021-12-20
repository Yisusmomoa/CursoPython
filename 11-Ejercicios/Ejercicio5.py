"""
    crear una lista con el contenido de esta tabla:
    ACCION     AVENTURA             DEPORTES
    GTA        ASSINS               FIFA 21
    COD        CRASH                PRO
    PUGB       PRINCE OF PERSIA     MOTO GP 21
    una lista con un diccionario que almacenará una categoria y una lista de juegos
"""


from typing import List


ListaGeneros=[
    {
        "Categoria":"Accion",
        "ListaJuegos": ["GTA","COD","PUGB"]
    },
    {
        "Categoria":"Aventura",
        "ListaJuegos": ["ASSINS","CRASH","PRINCE OF PERSIA"]
    },
    {
        "Categoria":"Deportes",
        "ListaJuegos": ["FIFA 21","PRO","MOTO GP 21"]
    }

]
#print(ListaGeneros)


for genero in ListaGeneros:
    print(f"-------Genero:{genero['Categoria']}-------")
    for juego in genero['ListaJuegos']:
        print(f"\t{juego}")