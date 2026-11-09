#Programa que agregue peliculas a una lista
#Ponerle nombre a mi lista 
peliculas=[]
#Preguntar cuantas pelis quiere
cantPelis=int(input("Cuántas peliculas vas a agregar? "))
i=0
while i<cantPelis:
    peli=input("Ingresa la peli: ")
    peliculas.append(peli)
    print(peliculas)
    i=i+1
peliBuscar=input("Qué pelicula buscas? ")
if peliBuscar in peliculas:
    print("Si esta")
else:
    print("No esta pero dejame la agrego")
    peliculas.append(peliBuscar)
    print(peliculas)
#Trabajo extra
peliBorar=input("Ingresa la pelicula que deseas borrar: ")
peliculas.remove(peliBorar)
print(peliculas)
