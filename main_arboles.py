"""
Pruebas del sistema de biblioteca usando árboles (BST)
"""

from sistema_core import SistemaBibliotecaArbol
from modelos import Libro, Usuario

def main():
    sistema = SistemaBibliotecaArbol()

    sistema.agregar_libro(Libro(
        id="L001",
        titulo="The C Programming Language",
        autor="Kernighan & Ritchie",
        isbn="978-0131103627",
        año=1988,
        categoria="Programación"
    ))

    sistema.agregar_libro(Libro(
        id="L002",
        titulo="The Pragmatic Programmer",
        autor="Hunt & Thomas",
        isbn="978-0201616224",
        año=1999,
        categoria="Programación"
    ))

    sistema.agregar_libro(Libro(
        id="L003",
        titulo="Clean Code",
        autor="Robert C. Martin",
        isbn="978-0132350884",
        año=2008,
        categoria="Programación"
    ))

    # --- Agregar usuarios ---
    sistema.registrar_usuario(Usuario(
        id="U001",
        nombre="Ana Pérez",
        email="ana@example.com",
        telefono="555-1111"
    ))

    sistema.registrar_usuario(Usuario(
        id="U002",
        nombre="Luis Gómez",
        email="luis@example.com",
        telefono="555-2222"
    ))

    print("\n📚 Libros en el sistema (ordenados por ISBN):")
    sistema.listar_libros()

    print("\n👥 Usuarios registrados:")
    sistema.listar_usuarios()

    # --- Préstamos y devoluciones ---
    print("\n🔹 Operaciones de préstamo y devolución:")
    sistema.prestar_libro("U001", "978-0132350884")  # Clean Code
    sistema.prestar_libro("U002", "978-0131103627")  # The C Programming Language
    sistema.devolver_libro("U001", "978-0132350884")

    print("\n📚 Libros después de las operaciones:")
    sistema.listar_libros()

if __name__ == "__main__":
    main()
