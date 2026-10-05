#sistema de recomendacion de peliculas
import pandas as pd

#crea un diccionario llamado 'base_de_datos_peliculas' con 5 peliculas y sus generos
base_de_datos_peliculas = {
    'pelicula': ['Inception', 'The Matrix', 'Interstellar', 'The Godfather', 'Pulp Fiction'],
    'genero': ['Ciencia Ficción', 'Ciencia Ficción', 'Ciencia Ficción', 'Crimen', 'Crimen']
}       
#crea un afuncion llamada 'recomendar_peliculas' que reciba un genero y devuelva una lista de peliculas de ese genero
def recomendar_peliculas(genero):
    #convierte el diccionario en un dataframe de pandas
    df = pd.DataFrame(base_de_datos_peliculas)
    #filtra el dataframe por el genero recibido como parametro
    peliculas_recomendadas = df[df['genero'] == genero]['pelicula'].tolist()
    #devuelve la lista de peliculas recomendadas
    return peliculas_recomendadas   

incluye un ejemplo de uso final imprimiendo las peliculas recomendadas para el genero 'Ciencia Ficción'
#ejemplo de uso 
peliculas = recomendar_peliculas('Ciencia Ficción')
print("Peliculas recomendadas para el genero 'Ciencia Ficción':")
for pelicula in peliculas:
    print(f"- {pelicula}")  

    