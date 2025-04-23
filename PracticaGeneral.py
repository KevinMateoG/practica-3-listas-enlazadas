from LinkedList import *

def crear_canciones(nombre, duracion):
    return Cancion(str(nombre), duracion)

lista_de_canciones = Linklist()
lista_de_canciones.append(crear_canciones(1,5))
lista_de_canciones.append(crear_canciones(2,5))
lista_de_canciones.append(crear_canciones(3,5))
lista_de_canciones.append(crear_canciones(4,5))
print(lista_de_canciones)