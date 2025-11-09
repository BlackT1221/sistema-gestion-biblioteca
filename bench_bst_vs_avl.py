import time
import random
from modelos import Libro
from arboles import ArbolBST
from arboles_avl import ArbolAVL

def benchmark_insert(arbol_class, n, aleatorio=True):
    arbol = arbol_class()
    claves = list(range(n))
    if aleatorio:
        random.shuffle(claves)
    start = time.time()
    for i in claves:
        isbn = str(i)
        arbol.insertar(isbn, Libro(f"L{i}", f"Libro {i}", "Autor", isbn, 2020, "Cat"))
    return time.time() - start, arbol

def benchmark_search(arbol, n):
    start = time.time()
    for i in range(n):
        _ = arbol.buscar(str(random.randint(0, n - 1)))
    return time.time() - start

if __name__ == "__main__":
    for n in [1000, 5000, 10000]:
        for tipo in ["aleatorio", "ordenado"]:
            aleatorio = (tipo == "aleatorio")
            t_ins_bst, bst = benchmark_insert(ArbolBST, n, aleatorio)
            t_bus_bst = benchmark_search(bst, n)
            t_ins_avl, avl = benchmark_insert(ArbolAVL, n, aleatorio)
            t_bus_avl = benchmark_search(avl, n)
            print(f"\nResultados n={n} ({tipo}):")
            print(f"BST -> Inserción: {t_ins_bst:.4f}s | Búsqueda: {t_bus_bst:.4f}s")
            print(f"AVL -> Inserción: {t_ins_avl:.4f}s | Búsqueda: {t_bus_avl:.4f}s")
