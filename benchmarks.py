import time
import random
from arboles import ArbolBST
from modelos import Libro

def benchmark_insert_bst(n, aleatorio=True):
    a = ArbolBST()
    claves = list(range(n))
    if aleatorio:
        random.shuffle(claves)
    start = time.time()
    for i in claves:
        isbn = str(i)
        a.insertar(isbn, Libro(f"L{i}", f"Libro {i}", "Autor", isbn, 2020, "Cat"))
    return time.time() - start, a

def benchmark_search_bst(a, n):
    start = time.time()
    for i in range(n):
        _ = a.buscar(str(random.randint(0, n - 1)))
    return time.time() - start

def benchmark_insert_list(n, aleatorio=True):
    lista = []
    claves = list(range(n))
    if aleatorio:
        random.shuffle(claves)
    start = time.time()
    for i in claves:
        lista.append(i)
    return time.time() - start, lista

def benchmark_search_list(lista, n):
    start = time.time()
    for i in range(n):
        _ = (random.randint(0, n - 1) in lista)
    return time.time() - start

if __name__ == "__main__":
    for n in [1000, 5000, 10000]:
        print(f"\nResultados para n = {n}:")
        for tipo in ["aleatorio", "ordenado"]:
            aleatorio = (tipo == "aleatorio")
            t_ins_bst, arbol = benchmark_insert_bst(n, aleatorio)
            t_bus_bst = benchmark_search_bst(arbol, n)
            t_ins_list, lista = benchmark_insert_list(n, aleatorio)
            t_bus_list = benchmark_search_list(lista, n)
            print(f" {tipo.capitalize():<10} | BST -> Inserción: {t_ins_bst:.4f}s | Búsqueda: {t_bus_bst:.4f}s | "
                  f"Lista -> Inserción: {t_ins_list:.4f}s | Búsqueda: {t_bus_list:.4f}s")
