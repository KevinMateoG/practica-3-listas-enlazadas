from LinkedList import *
from random import randint
import sys
import threading

def crear_canciones(nombre, artista, duracion):
    return Cancion(str(nombre), artista,duracion)

lista_de_canciones = DoubleLinkedList()
lista_de_canciones.append(crear_canciones("Begosip", "Maneskin",randint(10, 15)))
lista_de_canciones.append(crear_canciones("bikini azul", "luis miguel",randint(10, 15)))
lista_de_canciones.append(crear_canciones("Galileo", "queen",randint(10, 15)))
lista_de_canciones.append(crear_canciones("crime and punish", "Ado",randint(10, 15)))

print("ingresa lo que quieres hacer: ")
while True:
    for line in sys.stdin:
        entrada = line.strip()
        if entrada.lower() == "agregar":
            nombre = input("ingrese el nombre del artista")
            artista = input("ingrese el artista")
            lista_de_canciones.append(nombre, artista, randint(10,15))
        
        elif entrada.lower() == "adelantar":
            lista_de_canciones.adelantar_cancion()
        
        elif entrada.lower() == "reproducir":
            t = threading.Thread(target=lista_de_canciones.avanzar_siguiente_cancion)
            t.start()
        
        elif entrada.lower() == "mostrar":
            lista_de_canciones.mostrar_playlist()