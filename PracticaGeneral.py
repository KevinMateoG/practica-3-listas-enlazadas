from LinkedList import *
from random import randint
import sys
import threading

def crear_canciones(nombre, artista, duracion):
    return Cancion(str(nombre), artista,duracion)

lista_de_canciones = DoubleLinkedList()
lista_de_canciones.append(crear_canciones("aishite", "Ado",randint(10, 15)))
lista_de_canciones.append(crear_canciones("Begosip", "Maneskin",randint(10, 15)))
lista_de_canciones.append(crear_canciones("Galileo", "queen",randint(10, 15)))
lista_de_canciones.append(crear_canciones("i want to bracke free", "queen",randint(10, 15)))
lista_de_canciones.append(crear_canciones("hola", "luis miguel",randint(10, 15)))
lista_de_canciones.append(crear_canciones("we will rock you", "queen",randint(10, 15)))
lista_de_canciones.append(crear_canciones("i want your slave", "Maneskin",randint(10, 15)))
lista_de_canciones.append(crear_canciones("crime and punish", "Ado",randint(10, 15)))
lista_de_canciones.append(crear_canciones("show", "Ado",randint(10, 15)))
lista_de_canciones.append(crear_canciones("zitti e buoni", "Maneskin",randint(10, 15)))
lista_de_canciones.append(crear_canciones("bikini azul", "luis miguel",randint(10, 15)))

sub_playlist = None
while True:
    print("ingresa lo que quieres hacer: ")
    print("\n🎵 Bienvenido a tu Playlist Interactiva 🎵")
    print("Selecciona una opción:")
    print("1. Agregar una canción")
    print("2. Adelantar canción (por porcentaje)")
    print("3. Si quieres que se reprodusca automaticamente")
    print("4. Avanzar una canción")
    print("5. Retrocede una cancion")
    print("6. Reproducción aleatoria")
    print("7. Mostrar la playlist")
    print("8. Borrar artista con menos canciones")
    print("9. Crear una sub-playlist")
    print("10. Reproducir sub-playlist")
    print("Escribe tu opción y presiona Enter:")
    
    entrada = input()
    if entrada.lower() == "1":
        nombre = input("ingrese el nombre de la cancion")
        artista = input("ingrese el artista")
        lista_de_canciones.append(crear_canciones(nombre, artista, randint(10,15)))

    elif entrada.lower() == "2":
        adelantar = int(input("cuanto deseas adelantar, elige el tiempo que quieres escuchar(20%, 40%, etc): "))
        lista_de_canciones.adelantar_cancion(adelantar)
        
    elif entrada.lower() == "3":
        lista_de_canciones.avanzar_automatico()
        
    elif entrada.lower() == "4":
        lista_de_canciones.avanzar_de_a_uno()
    
    elif entrada.lower() == "5":
        lista_de_canciones.cancion_de_atras()
    
    elif entrada.lower() == "6":
        lista_de_canciones.aleatorio()
        
    elif entrada.lower() == "7":
        lista_de_canciones.mostrar_playlist()
    
    elif entrada.lower() == "8":
        lista_de_canciones.eliminar_artista_con_menos_canciones()
    
    elif entrada.lower() == "9":
        print("Elige cómo deseas crear la sub-playlist:")
        print("1. Por artista")
        print("2. Por duración mínima")
        print("3. Agregar de a cancion")
        subop = input("Opción: ")

        if subop == "1":
            artista = input("Ingresa el nombre del artista: ")
            sub_playlist = lista_de_canciones.sub_playlist_por_artista(artista)
        
        elif subop == "2":
            duracion = int(input("Duración mínima en segundos: "))
            sub_playlist = lista_de_canciones.sub_playlist_por_duracion(duracion)
        
        elif subop == "3":
            nombre = input("ingrese el nombre de la cancion")
            artista = input("ingrese el artista")
            sub_playlist = DoubleLinkedList()
            sub_playlist.append(crear_canciones(nombre, artista, randint(10,15)))
        
        else:
            print("Opción inválida.")
            continue

        print("\n🎶 Sub-playlist generada:")
        sub_playlist.mostrar_playlist()

    elif entrada.lower() == "10":
        if sub_playlist  is not None:
            sub_playlist.avanzar_automatico()
        else:
            print("No existe Sub-playlist")

#multiprocesing