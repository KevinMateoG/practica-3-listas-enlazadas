class Cancion:
    def __init__(self, nombre: str,artista: str, duracion: int):
        self.nombre = nombre
        self.artista = artista
        self.duracion = duracion
    
    def __repr__(self):
        return str(self.artista)

class Node:
    def __init__(self, value, next = None):
        self.value: Cancion = value
        self.next: Node = next

class Linklist:
    def __init__(self):
        self.__head: Node = None
        self.__tail: Node = None
        self.__size: int = 0
    
    def append(self, value):
        new_node: Node = Node(value)
        if self.__size == 0:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node
        self.__size += 1
    
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
    
    def travers (self):
        current = self.__head
        if self.__size == 0:
            return
        print(current.value)
        while current.next is not None:
            current = current.next
            print(current.value)
    
    def invertir_lista(self):
        anterior = None
        actual = self.__head
        self.__tail = self.__head 
        while actual:
            siguiente = actual.next
            actual.next = anterior
            anterior = actual
            actual = siguiente
        self.__head = anterior

    def __repr__(self):
        rep = ""
        current_node = self.__head
        while current_node is not None:
            rep += str(current_node.value) + "->" + " "
            current_node = current_node.next
        return rep

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

    #Agregar al final de la lista
    def append(self, value):
        new_node = DNode(value) #creo el nuevo nodo
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
        if(pos > self.__size-1):
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

    def __repr__(self):
        return f"{self.__head}"
