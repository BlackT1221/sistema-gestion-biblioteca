"""
Módulo de interfaz de usuario - Menús y navegación
"""

def mostrar_menu_principal():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("      SISTEMA DE GESTIÓN DE BIBLIOTECA")
    print("="*50)
    print("1. Gestión de Libros")
    print("2. Gestión de Usuarios")
    print("3. Préstamos y Devoluciones")
    print("4. Sistema de Reservas")
    print("5. Cola de Préstamos")
    print("6. Reportes y Estadísticas")
    print("7. Salir")
    print("-"*50)

def mostrar_menu_libros():
    """Muestra el menú de gestión de libros"""
    print("\n--- GESTIÓN DE LIBROS ---")
    print("1. Agregar nuevo libro")
    print("2. Buscar libro")
    print("3. Mostrar todos los libros")
    print("4. Volver al menú principal")

def mostrar_menu_usuarios():
    """Muestra el menú de gestión de usuarios"""
    print("\n--- GESTIÓN DE USUARIOS ---")
    print("1. Registrar nuevo usuario")
    print("2. Buscar usuario")
    print("3. Mostrar todos los usuarios")
    print("4. Volver al menú principal")

def mostrar_menu_prestamos():
    """Muestra el menú de préstamos y devoluciones"""
    print("\n--- PRÉSTAMOS Y DEVOLUCIONES ---")
    print("1. Realizar préstamo")
    print("2. Devolver libro")
    print("3. Mostrar préstamos activos")
    print("4. Volver al menú principal")

def mostrar_menu_reservas():
    """Muestra el menú del sistema de reservas"""
    print("\n--- SISTEMA DE RESERVAS ---")
    print("1. Hacer reserva")
    print("2. Ver reservas de un libro")
    print("3. Volver al menú principal")

def mostrar_menu_cola():
    """Muestra el menú de la cola de préstamos"""
    print("\n--- COLA DE PRÉSTAMOS ---")
    print("1. Agregar solicitud a la cola")
    print("2. Procesar siguiente solicitud")
    print("3. Mostrar cola de solicitudes")
    print("4. Volver al menú principal")

def mostrar_menu_reportes():
    """Muestra el menú de reportes"""
    print("\n--- REPORTES Y ESTADÍSTICAS ---")
    print("1. Reporte de libros")
    print("2. Reporte de usuarios")
    print("3. Historial completo")
    print("4. Volver al menú principal")

# Las funciones de gestión (gestionar_libros, gestionar_usuarios, etc.)
# se mantienen igual que en tu código original, pero ahora reciben 'sistema' como parámetro

def gestionar_libros(sistema):
    """Maneja la interfaz de gestión de libros"""
    while True:
        mostrar_menu_libros()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- AGREGAR NUEVO LIBRO ---")
            titulo = input("Título: ").strip()
            autor = input("Autor: ").strip()
            isbn = input("ISBN: ").strip()
            año = input("Año de publicación: ").strip()
            categoria = input("Categoría: ").strip()
            
            if titulo and autor and isbn and año and categoria:
                sistema.agregar_libro(titulo, autor, isbn, int(año), categoria)
            else:
                print("✗ Error: Todos los campos son obligatorios.")
        
        elif opcion == "2":
            print("\n--- BUSCAR LIBRO ---")
            print("Criterios de búsqueda: id, titulo, autor, categoria")
            criterio = input("Criterio de búsqueda: ").strip().lower()
            valor = input("Valor a buscar: ").strip()
            
            if criterio in ["id", "titulo", "autor", "categoria"]:
                resultados = sistema.buscar_libro(criterio, valor)
                if resultados:
                    print(f"\nSe encontraron {len(resultados)} resultados:")
                    for libro in resultados:
                        print(f"  - {libro}")
                else:
                    print("No se encontraron libros con esos criterios.")
            else:
                print("Criterio de búsqueda no válido.")
        
        elif opcion == "3":
            sistema.mostrar_libros()
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def gestionar_usuarios(sistema):
    """Maneja la interfaz de gestión de usuarios"""
    while True:
        mostrar_menu_usuarios()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- REGISTRAR NUEVO USUARIO ---")
            nombre = input("Nombre completo: ").strip()
            email = input("Email: ").strip()
            telefono = input("Teléfono: ").strip()
            tipo = input("Tipo (regular/premium): ").strip().lower() or "regular"
            
            if nombre and email and telefono:
                sistema.registrar_usuario(nombre, email, telefono, tipo)
            else:
                print("✗ Error: Nombre, email y teléfono son obligatorios.")
        
        elif opcion == "2":
            print("\n--- BUSCAR USUARIO ---")
            print("Criterios de búsqueda: id, nombre, email")
            criterio = input("Criterio de búsqueda: ").strip().lower()
            valor = input("Valor a buscar: ").strip()
            
            if criterio in ["id", "nombre", "email"]:
                resultados = sistema.buscar_usuario(criterio, valor)
                if resultados:
                    print(f"\nSe encontraron {len(resultados)} resultados:")
                    for usuario in resultados:
                        print(f"  - {usuario}")
                        if usuario.libros_prestados:
                            print(f"    Libros prestados: {len(usuario.libros_prestados)}")
                else:
                    print("No se encontraron usuarios con esos criterios.")
            else:
                print("Criterio de búsqueda no válido.")
        
        elif opcion == "3":
            sistema.mostrar_usuarios()
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def gestionar_prestamos(sistema):
    """Maneja la interfaz de préstamos y devoluciones"""
    while True:
        mostrar_menu_prestamos()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- REALIZAR PRÉSTAMO ---")
            try:
                id_libro = int(input("ID del libro: ").strip())
                id_usuario = int(input("ID del usuario: ").strip())
                sistema.prestar_libro(id_libro, id_usuario)
            except ValueError:
                print("✗ Error: Los IDs deben ser números enteros.")
        
        elif opcion == "2":
            print("\n--- DEVOLVER LIBRO ---")
            try:
                id_libro = int(input("ID del libro: ").strip())
                id_usuario = int(input("ID del usuario: ").strip())
                sistema.devolver_libro(id_libro, id_usuario)
            except ValueError:
                print("✗ Error: Los IDs deben ser números enteros.")
        
        elif opcion == "3":
            print("\n--- PRÉSTAMOS ACTIVOS ---")
            if sistema.prestamos_activos:
                for prestamo in sistema.prestamos_activos:
                    libro = next((l for l in sistema.libros if l.id == prestamo.id_libro), None)
                    usuario = next((u for u in sistema.usuarios if u.id == prestamo.id_usuario), None)
                    if libro and usuario:
                        print(f"  - {usuario.nombre} -> {libro.titulo} (Hasta: {prestamo.fecha_devolucion_prevista.strftime('%Y-%m-%d')})")
            else:
                print("No hay préstamos activos en este momento.")
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def gestionar_reservas(sistema):
    """Maneja la interfaz del sistema de reservas"""
    while True:
        mostrar_menu_reservas()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- HACER RESERVA ---")
            try:
                id_libro = int(input("ID del libro: ").strip())
                id_usuario = int(input("ID del usuario: ").strip())
                sistema.reservar_libro(id_libro, id_usuario)
            except ValueError:
                print("✗ Error: Los IDs deben ser números enteros.")
        
        elif opcion == "2":
            print("\n--- VER RESERVAS ---")
            try:
                id_libro = int(input("ID del libro: ").strip())
                sistema.mostrar_reservas(id_libro)
            except ValueError:
                print("✗ Error: El ID debe ser un número entero.")
        
        elif opcion == "3":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def gestionar_cola(sistema):
    """Maneja la interfaz de la cola de préstamos"""
    while True:
        mostrar_menu_cola()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            print("\n--- AGREGAR SOLICITUD A COLA ---")
            try:
                id_libro = int(input("ID del libro: ").strip())
                id_usuario = int(input("ID del usuario: ").strip())
                sistema.agregar_solicitud_prestamo(id_libro, id_usuario)
            except ValueError:
                print("✗ Error: Los IDs deben ser números enteros.")
        
        elif opcion == "2":
            print("\n--- PROCESAR SIGUIENTE SOLICITUD ---")
            sistema.procesar_solicitud_prestamo()
        
        elif opcion == "3":
            sistema.mostrar_cola_prestamos()
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def gestionar_reportes(sistema):
    """Maneja la interfaz de reportes"""
    while True:
        mostrar_menu_reportes()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            sistema.generar_reporte_libros()
        
        elif opcion == "2":
            sistema.generar_reporte_usuarios()
        
        elif opcion == "3":
            sistema.mostrar_historial_completo()
        
        elif opcion == "4":
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

def main(sistema):
    """Función principal de la interfaz"""
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "1":
            gestionar_libros(sistema)
        elif opcion == "2":
            gestionar_usuarios(sistema)
        elif opcion == "3":
            gestionar_prestamos(sistema)
        elif opcion == "4":
            gestionar_reservas(sistema)
        elif opcion == "5":
            gestionar_cola(sistema)
        elif opcion == "6":
            gestionar_reportes(sistema)
        elif opcion == "7":
            print("¡Gracias por usar el Sistema de Gestión de Biblioteca!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")