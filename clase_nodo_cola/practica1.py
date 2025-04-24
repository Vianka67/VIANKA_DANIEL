class Nodo:
    def __init__(self, valor):
        self.valor = valor  # El valor que almacena el nodo
        self.siguiente = None  # Apunta al siguiente nodo en la cola

class Cola:
    def __init__(self):
        self.frente = None  # El primer nodo (frente de la cola)
        self.final = None  # El último nodo (final de la cola)
        self.tamaño = 0  # El tamaño de la cola

    # Encolar (agregar un elemento al final de la cola)
    def enqueue(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.final is None:
            self.frente = self.final = nuevo_nodo  # Si la cola está vacía
        else:
            self.final.siguiente = nuevo_nodo  # Conectamos el nodo al final
            self.final = nuevo_nodo  # Ahora el nuevo nodo es el final de la cola
        self.tamaño += 1
        
# Desencolar (eliminar el elemento del frente de la cola)
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("La cola está vacía")
        valor = self.frente.valor  # Guardamos el valor del nodo al frente
        self.frente = self.frente.siguiente  # El frente se mueve al siguiente nodo
        if self.frente is None:
            self.final = None  # Si la cola quedó vacía, final también es None
        self.tamaño -= 1
        return valor