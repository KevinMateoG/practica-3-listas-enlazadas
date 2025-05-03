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
    print("Escribe tu opción y presiona Enter:")

    entrada = input()
    if entrada.lower() == "1":
        nombre = input("ingrese el nombre del artista")
        artista = input("ingrese el artista")
        lista_de_canciones.append(nombre, artista, randint(10,15))

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
#multiprocesing