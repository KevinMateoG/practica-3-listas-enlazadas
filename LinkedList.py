import time
import random
import sys

class Cancion:
    def __init__(self, nombre: str,artista: str, duracion: int):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
    
    def __repr__(self):
        return str(self.artista)

class DNode:
    def __init__(self, value, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev


    def __repr__(self):
        return f"{self.value} <-> {self.next}"

class DoubleLinkedList:
    def __init__(self, head = None, tail = None):
        self.__head = head
        self.__tail = tail
        self.__size = 0
        self.__pos = 0

    #Agregar al final de la lista
    def append(self, value):
        new_node = DNode(value) #creo el nuevo nodo
        if self.existe_titulo(value.nombre):
            return
        
        if(self.__size == 0): #está vacía?
            self.__head = new_node
            self.__tail = new_node
        else:
            new_node.prev = self.__tail #el previo del nuevo será el tail actual
            self.__tail.next = new_node #el next del tail actual será el nuevo
            self.__tail = new_node
        self.__size += 1 #actualizo el size

    def insert(self, pos, value):
        current_pos = 0 #posición actual
        current_node = self.__head #nodo inicial
        if(pos > self.__size - 1):
            raise IndexError("índice inválido")

        new_node = DNode(value)
        #insertar al principio
        if(pos == 0):
            new_node.next = self.__head
            self.__head.prev = new_node
            self.__head = new_node
        elif(pos == self.__size - 1): #insertar al final
            new_node.prev = self.__tail
            self.__tail.next = new_node
            self.__tail = new_node
        else: #insertar en cualquier parte del medio
            while(current_node is not None):
                if(pos == current_pos):
                    new_node.prev = current_node.prev
                    new_node.next = current_node
                    current_node.prev = new_node
                    new_node.prev.next = new_node
                    break
                current_node = current_node.next
                current_pos += 1
        self.__size += 1

    def delete_at(self, pos):
        if self.__size == 0:
            raise IndexError("Lista vacía")
        
        if pos < 0 or pos >= self.__size:
            raise IndexError("Índice fuera de rango")

        if pos == 0:
            self.delete_first()
        
        elif pos == self.__size - 1:
            self.delete_last()
        
        else:
            current_pos = 0
            current_node = self.__head
            while current_node is not None:
                if current_pos == pos:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                    self.__size -= 1
                    return
                current_node = current_node.next
                current_pos += 1
    
    def deleat_end(self):
        current = self.__head
        if self.__size == 0:
            return "no hay nada"
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.__tail = current
        self.__size -= 1
    
    def delete_first(self):
        if self.__size == 0:
            return
        elif self.__size == 1:
            self.__head = None
            self.__tail = None
        else:
            self.__head = self.__head.next
            self.__head.prev = None
        self.__size -= 1

    def traverse(self):
        current_node = self.__head #punto de partida
        while(current_node is not None):
            print(current_node.value)
            current_node = current_node.next

    def invtraverse(self):
        current_node = self.__tail #punto de partida
        while(current_node is not None):
            print(current_node.value)
            current_node = current_node.prev

    def existe_titulo(self, titulo):
        current = self.__head
        while current:
            if current.value.nombre == titulo:
                return True
            current = current.next
        return False

    def avanzar_de_a_uno(self):
        self.ejecutar_por_posicion(self.__pos, flag=True)
        

    def avanzar_automatico(self):
        current = self.__head
        if self.__size == 0:
            print("No hay canciones en la playlist.")
            return
        
        while current is not None:
            print(f"\nReproduciendo: {current.value.nombre} - {current.value.artista} ({current.value.duracion} segundos)")
            self.reproducir_con_barra(current.value)
            current = current.next
        self.__pos = 0

    def borrar_por_titulo(self, titulo):
        current = self.__head
        pos = 0
        if self.__size == 0:
            return
        if self.__size == 1 or current.value.nombre == titulo:
            self.delete_first()
        else:
            while current is not None:
                
                if current.value.nombre == titulo:
                    if self.__size == pos+1:
                        self.deleat_end()
                        return
                    
                    else:
                        current.prev.next = current.next
                        current.next.prev = current.prev
                        self.__size -= 1
                        return
                pos += 1
                current = current.next
    
    def mostrar_playlist(self):
        current = self.__head
        mostrar = 0
        if self.__size == 0:
            return
        
        else:
            while current:
                mostrar+=1
                print(mostrar,"." ,current.value.nombre)
                print("------------------")
                current = current.next

    def adelantar_cancion(self):
        current = self.__head
        if self.__size == 0:
            return
        else:
            current_pos = 0
            adelanto = int(input("ingrese cuanto desea adelanatar: "))
            adelanto = adelanto * 100
            print(adelanto)
            while current is not None:
                if self.__pos == current_pos:
                    self.reproducir_con_barra(current.value, flag=True, adelatar=adelanto)
                current = current.next
                current_pos += 1
    
    def aleatorio(self):
        cont = 0
        lista_aleatoria = []
        while self.__size != len(lista_aleatoria):
            num_aleatorio = random.randint(0, self.__size-1)
            if num_aleatorio in lista_aleatoria:
                cont -= 1
            else:
                lista_aleatoria.append(num_aleatorio)
                cont += 1
            
        for i in lista_aleatoria:
            self.ejecutar_por_posicion(i)

    
    def ejecutar_por_posicion(self, pos, flag=False):
        print(self.__pos)
        current_pos = 0
        current= self.__head
        if self.__size == 0:
            return
        else:
            while current is not None:
                if current_pos == pos:
                    print(f"\nReproduciendo: {current.value.nombre} - {current.value.artista} ({current.value.duracion} segundos)")
                    self.reproducir_con_barra(current.value)
                current = current.next
                current_pos += 1
        if flag == True:
            self.__pos += 1
        print(self.__pos)

    def reproducir_con_barra(self, cancion, flag=False, adelatar = None):
        duracion = cancion.duracion
        if flag is True:
            duracion *= adelatar
        for segundos in range(duracion + 1):
            barra = ('█' * segundos) + ('-' * (duracion - segundos))
            sys.stdout.write(f"\r[{barra}] {segundos}/{duracion}s")
            sys.stdout.flush()
            time.sleep(1)
        print() 
    
    def __repr__(self):
        return f"{self.__head}"
