import pytest
from arboles import ArbolBST
from modelos import Libro

@pytest.fixture
def arbol_libros():
    a = ArbolBST()
    libros = [
        Libro(id="L1", titulo="Libro A", autor="Autor 1", isbn="111", año=2020, categoria="Ciencia"),
        Libro(id="L2", titulo="Libro B", autor="Autor 2", isbn="222", año=2019, categoria="Historia"),
        Libro(id="L3", titulo="Libro C", autor="Autor 3", isbn="333", año=2018, categoria="Arte"),
    ]
    for libro in libros:
        a.insertar(libro.isbn, libro)
    return a

def test_buscar_existente(arbol_libros):
    libro = arbol_libros.buscar("111")
    assert libro is not None
    assert libro.titulo == "Libro A"

def test_buscar_inexistente(arbol_libros):
    libro = arbol_libros.buscar("999")
    assert libro is None

def test_insertar_y_eliminar(arbol_libros):
    nuevo = Libro(id="L4", titulo="Libro D", autor="Autor 4", isbn="444", año=2021, categoria="Ficción")
    arbol_libros.insertar(nuevo.isbn, nuevo)
    assert arbol_libros.buscar("444") is not None
    assert arbol_libros.eliminar("444") is True
    assert arbol_libros.buscar("444") is None
