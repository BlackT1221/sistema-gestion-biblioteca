"""
Módulo para datos de prueba y utilidades de carga
"""

def cargar_datos_prueba(sistema):
    """Carga datos de prueba para demostrar el sistema"""
    # Agregar algunos libros de prueba
    libros_prueba = [
        ("Cien años de soledad", "Gabriel García Márquez", "9788437604947", 1967, "Novela"),
        ("1984", "George Orwell", "9788499890944", 1949, "Ciencia Ficción"),
        ("El Quijote", "Miguel de Cervantes", "9788467031250", 1605, "Clásico"),
        ("Crimen y castigo", "Fiódor Dostoyevski", "9788491051258", 1866, "Novela"),
        ("Orgullo y prejuicio", "Jane Austen", "9788491051289", 1813, "Romance")
    ]
    
    for titulo, autor, isbn, año, categoria in libros_prueba:
        sistema.agregar_libro(titulo, autor, isbn, año, categoria)
    
    # Registrar algunos usuarios de prueba
    usuarios_prueba = [
        ("Ana García", "ana.garcia@email.com", "555-0101", "regular"),
        ("Carlos López", "carlos.lopez@email.com", "555-0102", "premium"),
        ("María Rodríguez", "maria.rodriguez@email.com", "555-0103", "regular")
    ]
    
    for nombre, email, telefono, tipo in usuarios_prueba:
        sistema.registrar_usuario(nombre, email, telefono, tipo)
    
    print("✓ Datos de prueba cargados exitosamente")

def crear_ejemplo_prestamos(sistema):
    """Crea algunos préstamos de ejemplo para demostración"""
    # Ejemplo de préstamos entre los datos de prueba
    if len(sistema.libros) >= 2 and len(sistema.usuarios) >= 2:
        sistema.prestar_libro(1, 1)  # Libro 1 a Usuario 1
        sistema.prestar_libro(2, 2)  # Libro 2 a Usuario 2
        print("✓ Préstamos de ejemplo creados")