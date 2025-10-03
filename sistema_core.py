"""
Clase principal del sistema con la lógica de negocio
"""

import datetime
from collections import deque
from modelos import Libro, Usuario, Prestamo
from estructuras_datos import ListaEnlazadaHistorial

class SistemaGestionBiblioteca:
    """Clase principal del sistema de gestión"""
    
    def __init__(self):
        # Arreglos para almacenamiento principal
        self.libros = []  # Arreglo de libros
        self.usuarios = []  # Arreglo de usuarios
        self.prestamos_activos = []  # Arreglo de préstamos activos
        
        # Estructuras especializadas
        self.reservas = {}  # Diccionario con pilas para reservas
        self.cola_prestamos = deque()  # Cola para solicitudes de préstamo
        self.historial_completo = ListaEnlazadaHistorial()  # Lista enlazada para historial
        
        # Contadores para IDs
        self.contador_libros = 1
        self.contador_usuarios = 1
        self.contador_prestamos = 1
    
    # ==============================
    # MÉTODOS PARA GESTIÓN DE LIBROS
    # ==============================
    
    def agregar_libro(self, titulo, autor, isbn, año, categoria):
        """Agrega un nuevo libro al sistema"""
        libro = Libro(self.contador_libros, titulo, autor, isbn, año, categoria)
        self.libros.append(libro)
        self.contador_libros += 1
        print(f"✓ Libro '{titulo}' agregado exitosamente (ID: {libro.id})")
        return libro
    
    def buscar_libro(self, criterio, valor):
        """Busca libros por diferentes criterios"""
        resultados = []
        for libro in self.libros:
            if criterio == "id" and str(libro.id) == valor:
                resultados.append(libro)
            elif criterio == "titulo" and valor.lower() in libro.titulo.lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.autor.lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados
    
    def mostrar_libros(self):
        """Muestra todos los libros del sistema"""
        if not self.libros:
            print("No hay libros registrados en el sistema.")
            return
        
        print("\n=== CATÁLOGO DE LIBROS ===")
        for libro in self.libros:
            print(libro)
    
    # ==============================
    # MÉTODOS PARA GESTIÓN DE USUARIOS
    # ==============================
    
    def registrar_usuario(self, nombre, email, telefono, tipo="regular"):
        """Registra un nuevo usuario en el sistema"""
        # Validar email único
        for usuario in self.usuarios:
            if usuario.email == email:
                print("✗ Error: Ya existe un usuario con ese email.")
                return None
        
        usuario = Usuario(self.contador_usuarios, nombre, email, telefono, tipo)
        self.usuarios.append(usuario)
        self.contador_usuarios += 1
        print(f"✓ Usuario '{nombre}' registrado exitosamente (ID: {usuario.id})")
        return usuario
    
    def buscar_usuario(self, criterio, valor):
        """Busca usuarios por diferentes criterios"""
        resultados = []
        for usuario in self.usuarios:
            if criterio == "id" and str(usuario.id) == valor:
                resultados.append(usuario)
            elif criterio == "nombre" and valor.lower() in usuario.nombre.lower():
                resultados.append(usuario)
            elif criterio == "email" and valor.lower() in usuario.email.lower():
                resultados.append(usuario)
        return resultados
    
    def mostrar_usuarios(self):
        """Muestra todos los usuarios del sistema"""
        if not self.usuarios:
            print("No hay usuarios registrados en el sistema.")
            return
        
        print("\n=== USUARIOS REGISTRADOS ===")
        for usuario in self.usuarios:
            print(usuario)
    
    # ==============================
    # MÉTODOS PARA PRÉSTAMOS
    # ==============================
    
    def prestar_libro(self, id_libro, id_usuario):
        """Realiza el préstamo de un libro a un usuario"""
        # Buscar libro y usuario
        libro = next((l for l in self.libros if l.id == id_libro), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        
        if not libro:
            print("✗ Error: Libro no encontrado.")
            return False
        
        if not usuario:
            print("✗ Error: Usuario no encontrado.")
            return False
        
        # Verificar disponibilidad
        if libro.estado != "disponible":
            print(f"✗ Error: El libro no está disponible. Estado: {libro.estado}")
            return False
        
        # Verificar límite de préstamos (máximo 3 libros)
        if len(usuario.libros_prestados) >= 3:
            print("✗ Error: El usuario ha alcanzado el límite de préstamos (3 libros).")
            return False
        
        # Realizar préstamo
        fecha_prestamo = datetime.datetime.now()
        fecha_devolucion = fecha_prestamo + datetime.timedelta(days=14)  # 2 semanas
        
        prestamo = Prestamo(id_libro, id_usuario, fecha_prestamo, fecha_devolucion)
        self.prestamos_activos.append(prestamo)
        self.historial_completo.agregar(prestamo)
        
        # Actualizar estados
        libro.estado = "prestado"
        usuario.libros_prestados.append(id_libro)
        usuario.historial_prestamos.append(prestamo)
        
        print(f"✓ Préstamo realizado exitosamente.")
        print(f"  Libro: {libro.titulo}")
        print(f"  Usuario: {usuario.nombre}")
        print(f"  Fecha de devolución: {fecha_devolucion.strftime('%Y-%m-%d')}")
        return True
    
    def devolver_libro(self, id_libro, id_usuario):
        """Procesa la devolución de un libro"""
        # Buscar préstamo activo
        prestamo = next((p for p in self.prestamos_activos 
                        if p.id_libro == id_libro and p.id_usuario == id_usuario), None)
        
        if not prestamo:
            print("✗ Error: No se encontró un préstamo activo con esos datos.")
            return False
        
        # Buscar libro y usuario
        libro = next((l for l in self.libros if l.id == id_libro), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        
        if libro and usuario:
            # Actualizar estados
            libro.estado = "disponible"
            if id_libro in usuario.libros_prestados:
                usuario.libros_prestados.remove(id_libro)
            
            # Marcar préstamo como devuelto
            prestamo.fecha_devolucion_real = datetime.datetime.now()
            prestamo.estado = "devuelto"
            self.prestamos_activos.remove(prestamo)
            
            print(f"✓ Devolución procesada exitosamente.")
            print(f"  Libro: {libro.titulo}")
            print(f"  Usuario: {usuario.nombre}")
            
            # Verificar si hay reservas para este libro
            if id_libro in self.reservas and self.reservas[id_libro]:
                siguiente_usuario = self.reservas[id_libro].pop()
                print(f"  Nota: El libro tiene reservas pendientes.")
                return self.prestar_libro(id_libro, siguiente_usuario)
            
            return True
        
        return False
    
    # ==============================
    # MÉTODOS PARA RESERVAS (PILAS)
    # ==============================
    
    def reservar_libro(self, id_libro, id_usuario):
        """Agrega una reserva para un libro (sistema de pilas)"""
        libro = next((l for l in self.libros if l.id == id_libro), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        
        if not libro:
            print("✗ Error: Libro no encontrado.")
            return False
        
        if not usuario:
            print("✗ Error: Usuario no encontrado.")
            return False
        
        # Inicializar pila de reservas si no existe
        if id_libro not in self.reservas:
            self.reservas[id_libro] = []
        
        # Verificar si el usuario ya tiene una reserva para este libro
        if id_usuario in self.reservas[id_libro]:
            print("✗ Error: El usuario ya tiene una reserva para este libro.")
            return False
        
        # Agregar reserva (operación push en la pila)
        self.reservas[id_libro].append(id_usuario)
        libro.estado = "reservado"
        
        print(f"✓ Reserva realizada exitosamente.")
        print(f"  Libro: {libro.titulo}")
        print(f"  Usuario: {usuario.nombre}")
        print(f"  Posición en cola de reservas: {len(self.reservas[id_libro])}")
        return True
    
    def mostrar_reservas(self, id_libro):
        """Muestra las reservas pendientes para un libro"""
        if id_libro not in self.reservas or not self.reservas[id_libro]:
            print("No hay reservas pendientes para este libro.")
            return
        
        libro = next((l for l in self.libros if l.id == id_libro), None)
        if libro:
            print(f"\n=== RESERVAS PARA: {libro.titulo} ===")
            for i, id_usuario in enumerate(reversed(self.reservas[id_libro]), 1):
                usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
                if usuario:
                    print(f"{i}. {usuario.nombre} ({usuario.email})")
    
    # ==============================
    # MÉTODOS PARA COLA DE PRÉSTAMOS
    # ==============================
    
    def agregar_solicitud_prestamo(self, id_libro, id_usuario):
        """Agrega una solicitud de préstamo a la cola"""
        libro = next((l for l in self.libros if l.id == id_libro), None)
        usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
        
        if libro and usuario:
            solicitud = (id_libro, id_usuario)
            self.cola_prestamos.append(solicitud)
            print(f"✓ Solicitud de préstamo agregada a la cola.")
            print(f"  Posición en cola: {len(self.cola_prestamos)}")
            return True
        return False
    
    def procesar_solicitud_prestamo(self):
        """Procesa la siguiente solicitud en la cola"""
        if not self.cola_prestamos:
            print("No hay solicitudes de préstamo pendientes.")
            return False
        
        id_libro, id_usuario = self.cola_prestamos.popleft()
        print(f"Procesando solicitud: Libro ID {id_libro}, Usuario ID {id_usuario}")
        return self.prestar_libro(id_libro, id_usuario)
    
    def mostrar_cola_prestamos(self):
        """Muestra las solicitudes pendientes en la cola"""
        if not self.cola_prestamos:
            print("No hay solicitudes de préstamo en la cola.")
            return
        
        print("\n=== COLA DE SOLICITUDES DE PRÉSTAMO ===")
        for i, (id_libro, id_usuario) in enumerate(self.cola_prestamos, 1):
            libro = next((l for l in self.libros if l.id == id_libro), None)
            usuario = next((u for u in self.usuarios if u.id == id_usuario), None)
            if libro and usuario:
                print(f"{i}. {usuario.nombre} -> {libro.titulo}")
    
    # ==============================
    # MÉTODOS DE REPORTES
    # ==============================
    
    def generar_reporte_libros(self):
        """Genera reporte de estadísticas de libros"""
        total_libros = len(self.libros)
        disponibles = sum(1 for l in self.libros if l.estado == "disponible")
        prestados = sum(1 for l in self.libros if l.estado == "prestado")
        reservados = sum(1 for l in self.libros if l.estado == "reservado")
        
        print("\n=== REPORTE DE LIBROS ===")
        print(f"Total de libros: {total_libros}")
        print(f"Disponibles: {disponibles}")
        print(f"Prestados: {prestados}")
        print(f"Reservados: {reservados}")
        
        # Libros más populares (con más reservas)
        libros_populares = []
        for id_libro, reservas in self.reservas.items():
            if reservas:
                libro = next((l for l in self.libros if l.id == id_libro), None)
                if libro:
                    libros_populares.append((libro, len(reservas)))
        
        if libros_populares:
            print("\n--- Libros más populares (por reservas) ---")
            libros_populares.sort(key=lambda x: x[1], reverse=True)
            for libro, num_reservas in libros_populares[:5]:
                print(f"  {libro.titulo}: {num_reservas} reservas")
    
    def generar_reporte_usuarios(self):
        """Genera reporte de estadísticas de usuarios"""
        total_usuarios = len(self.usuarios)
        usuarios_con_prestamos = sum(1 for u in self.usuarios if u.libros_prestados)
        
        print("\n=== REPORTE DE USUARIOS ===")
        print(f"Total de usuarios: {total_usuarios}")
        print(f"Usuarios con préstamos activos: {usuarios_con_prestamos}")
        
        # Usuarios más activos
        usuarios_activos = []
        for usuario in self.usuarios:
            if usuario.historial_prestamos:
                usuarios_activos.append((usuario, len(usuario.historial_prestamos)))
        
        if usuarios_activos:
            print("\n--- Usuarios más activos ---")
            usuarios_activos.sort(key=lambda x: x[1], reverse=True)
            for usuario, num_prestamos in usuarios_activos[:5]:
                print(f"  {usuario.nombre}: {num_prestamos} préstamos en historial")
    
    def mostrar_historial_completo(self):
        """Muestra el historial completo de préstamos"""
        print("\n=== HISTORIAL COMPLETO DE PRÉSTAMOS ===")
        self.historial_completo.mostrar()