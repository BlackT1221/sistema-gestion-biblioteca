"""
Definición de clases de datos del sistema
"""

import datetime

class Libro:
    """Clase que representa un libro en el sistema"""
    def __init__(self, id, titulo, autor, isbn, año, categoria, estado="disponible"):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año = año
        self.categoria = categoria
        self.estado = estado  # disponible, prestado, reservado
    
    def __str__(self):
        return f"ID: {self.id} | {self.titulo} - {self.autor} ({self.estado})"

class Usuario:
    """Clase que representa un usuario del sistema"""
    def __init__(self, id, nombre, email, telefono, tipo="regular"):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.tipo = tipo  # regular, premium, administrador
        self.historial_prestamos = []  # Lista para historial de préstamos
        self.libros_prestados = []     # Lista para libros actualmente prestados
    
    def __str__(self):
        return f"ID: {self.id} | {self.nombre} | {self.email}"

class Prestamo:
    """Clase que representa un préstamo de libro"""
    def __init__(self, id_libro, id_usuario, fecha_prestamo, fecha_devolucion_prevista):
        self.id_libro = id_libro
        self.id_usuario = id_usuario
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion_prevista = fecha_devolucion_prevista
        self.fecha_devolucion_real = None
        self.estado = "activo"  # activo, devuelto, vencido
    
    def __str__(self):
        return f"Libro: {self.id_libro} | Usuario: {self.id_usuario} | Estado: {self.estado}"