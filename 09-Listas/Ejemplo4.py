#Recorrer lista

# peliculas=["batman","spiderman","superman","señor de los anillos","alien"]
# peliculas.append("Deadpool")
# for pelicula in peliculas:
#     #print(pelicula)
#     print(f"{peliculas.index(pelicula)} {pelicula}")

nuevaPelicula=""
PeliculasArray=[]
while nuevaPelicula!="Detener":
    nuevaPelicula=input('Captura una pelicula o escribe "Detener" para dejar de capturar peliculas: ')
    if nuevaPelicula!="Detener":
        PeliculasArray.append(nuevaPelicula)

for pelicula in PeliculasArray:
    print(f"Numero de pelicula: {PeliculasArray.index(pelicula)} - Nombre pelicula: {pelicula}")


