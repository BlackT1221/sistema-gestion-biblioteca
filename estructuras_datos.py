"""
Implementación de estructuras de datos lineales personalizadas
"""

class NodoHistorial:
    """Nodo para lista enlazada del historial detallado"""
    def __init__(self, prestamo):
        self.prestamo = prestamo
        self.siguiente = None

class ListaEnlazadaHistorial:
    """Lista enlazada para historial detallado de préstamos"""
    def __init__(self):
        self.cabeza = None
    
    def agregar(self, prestamo):
        """Agrega un préstamo al historial (operación append)"""
        nuevo_nodo = NodoHistorial(prestamo)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
    
    def mostrar(self):
        """Muestra todos los préstamos en el historial"""
        actual = self.cabeza
        while actual:
            print(f"  - {actual.prestamo}")
            actual = actual.siguiente
    
    def esta_vacia(self):
        """Verifica si la lista está vacía"""
        return self.cabeza is None
    
    def __len__(self):
        """Retorna el número de elementos en la lista"""
        count = 0
        actual = self.cabeza
        while actual:
            count += 1
            actual = actual.siguiente
        return count