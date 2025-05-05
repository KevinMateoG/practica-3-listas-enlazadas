from LinkedList import *
from random import randint
import sys
import threading

def crear_canciones(nombre, artista, duracion):
    return Cancion(str(nombre), artista,duracion)

play_list_general = DoubleLinkedList()
play_list_general.append(crear_canciones("aishite", "Ado",2))
play_list_general.append(crear_canciones("Begosip", "Maneskin",3))
play_list_general.append(crear_canciones("Galileo", "queen",2))
play_list_general.append(crear_canciones("i want to bracke free", "queen",4))
play_list_general.append(crear_canciones("hola", "luis miguel",3))
play_list_general.append(crear_canciones("we will rock you", "queen",2))
play_list_general.append(crear_canciones("i want your slave", "Maneskin",1))
play_list_general.append(crear_canciones("crime and punish", "Ado",2))
play_list_general.append(crear_canciones("show", "Ado",3))
play_list_general.append(crear_canciones("zitti e buoni", "Maneskin",3))
play_list_general.append(crear_canciones("bikini azul", "luis miguel",4))

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
    print("11. Eliminar una cancion")
    print("12. mostrar la sub playlist")
    print("Escribe tu opción y presiona Enter:")
    
    entrada = input()
    if entrada.lower() == "1":
        nombre = input("ingrese el nombre de la cancion")
        artista = input("ingrese el artista")
        play_list_general.append(crear_canciones(nombre, artista, randint(10,15)))

    elif entrada.lower() == "2":
        adelantar = int(input("cuanto deseas adelantar, elige el tiempo que quieres escuchar(20%, 40%, etc): "))
        play_list_general.adelantar_cancion(adelantar)
        
    elif entrada.lower() == "3":
        play_list_general.avanzar_automatico()
        
    elif entrada.lower() == "4":
        play_list_general.avanzar_de_a_uno()
    
    elif entrada.lower() == "5":
        play_list_general.cancion_de_atras()
    
    elif entrada.lower() == "6":
        play_list_general.aleatorio()
        
    elif entrada.lower() == "7":
        play_list_general.mostrar_playlist()
    
    elif entrada.lower() == "8":
        play_list_general.eliminar_artista_con_menos_canciones()
    
    elif entrada.lower() == "9":
        print("Elige cómo deseas crear la sub-playlist:")
        print("1. Por artista")
        print("2. Por duración mínima")
        print("3. Agregar de a cancion")
        print("4. agregar de la playlista general")
        subop = input("Opción: ")

        if subop == "1":
            artista = input("Ingresa el nombre del artista: ")
            sub_playlist = play_list_general.sub_playlist_por_artista(artista)
        
        elif subop == "2":
            duracion = int(input("Duración mínima en segundos: "))
            sub_playlist = play_list_general.sub_playlist_por_duracion(duracion)
        
        elif subop == "3":
            if sub_playlist is None:
                sub_playlist = DoubleLinkedList()
            nombre = input("ingrese el nombre de la cancion")
            artista = input("ingrese el artista")
            sub_playlist.append(crear_canciones(nombre, artista, randint(10,15)))
        
        elif subop == "4":
            nombre = input("nombre de la cancion")
            sub_playlist = play_list_general.sub_playlist_agregar_de_general(nombre, sub_playlist)
        
        elif subop == "5":
            sub_playlist = play_list_general.sub_playlist_con_duracion_mas_repetida()
        
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
    
    elif entrada.lower() == "11":
        nombre = input("ingrese el nombre de la cancion que desea aliminar")
        play_list_general.borrar_por_titulo(nombre)
    
    elif entrada.lower() == "12":
        sub_playlist.mostrar_playlist()

#multiprocesing
"""
sub_playlist_con_canciones_que-tengan_la_duracion_que_mas_se_repita
"""