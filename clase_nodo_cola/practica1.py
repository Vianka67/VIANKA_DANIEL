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
    
# Ver el valor del primer elemento (sin eliminarlo)
    def front(self):
        if self.isEmpty():
            raise IndexError("La cola está vacía")
        return self.frente.valor

    # Ver el valor del primer elemento (sin eliminarlo)
    def peek(self):
        return self.front()  # 'peek' es lo mismo que 'front'

    # Comprobar si la cola está vacía
    def isEmpty(self):
        return self.tamaño == 0

    # Obtener el tamaño de la cola
    def size(self):
        return self.tamaño
# Ejemplo de uso
if __name__ == "__main__":
    cola = Cola()

    # Agregar elementos a la cola
    cola.enqueue(10)
    cola.enqueue(20)
    cola.enqueue(30)

    print("Frente de la cola:", cola.front())  # Debería ser 10
    print("Tamaño de la cola:", cola.size())  # Debería ser 3

    # Desencolar un elemento
    print("Desencolando:", cola.dequeue())  # Debería ser 10

    # Ver el frente después de desencolar
    print("Nuevo frente de la cola:", cola.front())  # Debería ser 20
    print("Tamaño de la cola:", cola.size())  # Debería ser 2

    # Verificar si la cola está vacía
    print("¿Está la cola vacía?", cola.isEmpty())  # Debería ser False

    # Desencolar todos los elementos
    print("Desencolando:", cola.dequeue())  # 20
    print("Desencolando:", cola.dequeue())  # 30

    # Verificar si la cola está vacía
    print("¿Está la cola vacía?", cola.isEmpty())  # Debería ser True
