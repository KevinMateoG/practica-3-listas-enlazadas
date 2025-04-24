from LinkedList import *
from random import randint

def crear_canciones(nombre, artista, duracion):
    return Cancion(str(nombre), artista,duracion)

lista_de_canciones = DoubleLinkedList()
lista_de_canciones.append(crear_canciones(1, "kiss",randint(10, 15)))
lista_de_canciones.append(crear_canciones(2, "luis miguel",randint(10, 15)))
lista_de_canciones.append(crear_canciones(3, "queen",randint(10, 15)))
lista_de_canciones.append(crear_canciones(4, "Ado",randint(10, 15)))
lista_de_canciones.delete_at(2)
lista_de_canciones.append(crear_canciones(1, "kiss",randint(10, 15)))
print(lista_de_canciones)