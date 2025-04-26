from LinkedList import *
from random import randint
import sys

def crear_canciones(nombre, artista, duracion):
    return Cancion(str(nombre), artista,duracion)

lista_de_canciones = DoubleLinkedList()
lista_de_canciones.append(crear_canciones("Begosip", "Maneskin",randint(10, 15)))
lista_de_canciones.append(crear_canciones("bikini azul", "luis miguel",randint(10, 15)))
lista_de_canciones.append(crear_canciones("Galileo", "queen",randint(10, 15)))
lista_de_canciones.append(crear_canciones("crime and punish", "Ado",randint(10, 15)))

#lista_de_canciones.avanzar_siguiente_cancion()
lista_de_canciones.ejecutar_por_posicion(2)
lista_de_canciones.mostrar_playlist()
lista_de_canciones.aleatorio()
print(lista_de_canciones)