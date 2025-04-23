
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
            rep += str(current_node.value) + "->"
            current_node = current_node.next
        return rep

class Cancion:
    def __init__(self, nombre: str,duracion: int):
        self.nombre = nombre
        self.duracion = duracion
    
    def __repr__(self):
        return str(self.nombre)

