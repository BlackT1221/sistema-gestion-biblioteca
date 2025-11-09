# tests/test_sistema_arbol.py
import pytest
from arboles import ArbolBST
from modelos import Libro, Usuario
from sistema_core import SistemaBibliotecaArbol

@pytest.fixture
def sistema():
    sistema = SistemaBibliotecaArbol()
    sistema.agregar_libro(Libro("L001", "Libro A", "Autor A", "111", 2020, "Ficción"))
    sistema.agregar_libro(Libro("L002", "Libro B", "Autor B", "222", 2021, "Historia"))
    sistema.registrar_usuario(Usuario("U001", "Ana", "ana@example.com", "123"))
    sistema.registrar_usuario(Usuario("U002", "Luis", "luis@example.com", "456"))
    return sistema

def test_agregar_y_listar_libros(sistema):
    libros = list(sistema.libros.recorrido_inorden())
    assert len(libros) == 2
    assert libros[0][0] == "111"  # ISBN ordenado

def test_buscar_libro(sistema):
    libro = sistema.libros.buscar("111")
    assert libro is not None
    assert libro.titulo == "Libro A"

def test_registrar_usuario(sistema):
    usuario = sistema.usuarios.buscar("U001")
    assert usuario is not None
    assert usuario.nombre == "Ana"

def test_prestar_y_devolver_libro(sistema):
    # Prestar libro
    assert sistema.prestar_libro("U001", "111") is True
    libro = sistema.libros.buscar("111")
    assert libro.estado == "prestado"

    # Devolver libro
    assert sistema.devolver_libro("U001", "111") is True
    libro = sistema.libros.buscar("111")
    assert libro.estado == "disponible"

def test_no_prestar_libro_inexistente(sistema):
    assert sistema.prestar_libro("U001", "999") is False

def test_no_devolver_sin_prestamo(sistema):
    assert sistema.devolver_libro("U002", "222") is False
