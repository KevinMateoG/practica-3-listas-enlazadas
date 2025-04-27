from LinkedList import *
from random import randint
import sys
import threading

def crear_canciones(nombre, artista, duracion):
    return Cancion(str(nombre), artista,duracion)

lista_de_canciones = DoubleLinkedList()
lista_de_canciones.append(crear_canciones("Begosip", "Maneskin",2))
lista_de_canciones.append(crear_canciones("bikini azul", "luis miguel",2))
lista_de_canciones.append(crear_canciones("Galileo", "queen",2))
lista_de_canciones.append(crear_canciones("crime and punish", "Ado",2))

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
            t = threading.Thread(target=lista_de_canciones.avanzar_automatico)
            t.start()
        elif entrada.lower() == "avanzar":
            lista_de_canciones.avanzar_de_a_uno()
        elif entrada.lower() == "aleatorio":
            lista_de_canciones.aleatorio()
        
        elif entrada.lower() == "mostrar":
            lista_de_canciones.mostrar_playlist()

"""    def avanzar_siguiente_cancion(self):
        current = self.__head
        current_post = 0
        if self.__size == 0:
            return
        if self.__pos == 0:
            print(f"nombre de la cancion: {current.value.nombre}, artista: {current.value.artista}, duracion: {current.value.duracion} Seg")
            self.reproducir_con_barra(current.value)
        else:
            while current.next is not None:
                if self.__pos == current_post:
                    print(f"nombre de la cancion: {current.value.nombre}, artista: {current.value.artista}, duracion: {current.value.duracion} Seg")
                    self.reproducir_con_barra(current.value)
                else:
                    self.__pos += 1
                current_post += 1
                current = current.next"""