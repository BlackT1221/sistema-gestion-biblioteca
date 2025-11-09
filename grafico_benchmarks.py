"""
grafico_benchmarks.py
Genera gráficos comparativos de rendimiento entre BST, AVL y Lista
Autor: Christian Martinez
Fecha: 11/9/25
"""

import random
import time
import matplotlib.pyplot as plt
from modelos import Libro
from arboles import ArbolBST
from arboles_avl import ArbolAVL

# =====================
# Funciones de prueba
# =====================

def medir_insercion(arbol_class, n, aleatorio=True):
    """Mide tiempo de inserción para un árbol o lista"""
    arbol = arbol_class() if arbol_class != list else []
    claves = list(range(n))
    if aleatorio:
        random.shuffle(claves)
    start = time.time()
    for i in claves:
        if arbol_class == list:
            arbol.append(i)
        else:
            arbol.insertar(str(i), Libro(f"L{i}", f"Libro {i}", "Autor", str(i), 2020, "Cat"))
    return time.time() - start, arbol

def medir_busqueda(estructura, n, arbol_class):
    """Mide tiempo de búsqueda"""
    start = time.time()
    for _ in range(n):
        key = str(random.randint(0, n - 1))
        if arbol_class == list:
            _ = (key in estructura)
        else:
            _ = estructura.buscar(key)
    return time.time() - start

# =====================
# Ejecución de pruebas
# =====================

def ejecutar_pruebas():
    tamaños = [1000, 5000, 10000]
    estructuras = {"BST": ArbolBST, "AVL": ArbolAVL, "Lista": list}
    modos = {"Aleatorio": True, "Ordenado": False}

    resultados = {modo: {estr: {"insercion": [], "busqueda": []} for estr in estructuras} for modo in modos}

    for modo, aleatorio in modos.items():
        print(f"\nEjecutando modo {modo}...")
        for n in tamaños:
            print(f"  n = {n}")
            for nombre, clase in estructuras.items():
                t_ins, estructura = medir_insercion(clase, n, aleatorio)
                t_bus = medir_busqueda(estructura, n, clase)
                resultados[modo][nombre]["insercion"].append(t_ins)
                resultados[modo][nombre]["busqueda"].append(t_bus)

    return tamaños, resultados

# =====================
# Gráficos
# =====================

def graficar(tamaños, resultados):
    for modo in resultados:
        fig, axs = plt.subplots(1, 2, figsize=(12, 5))
        fig.suptitle(f"Comparativa de rendimiento ({modo})", fontsize=14, fontweight="bold")

        for nombre, datos in resultados[modo].items():
            axs[0].plot(tamaños, datos["insercion"], marker="o", label=nombre)
            axs[1].plot(tamaños, datos["busqueda"], marker="o", label=nombre)

        axs[0].set_title("Tiempo de Inserción")
        axs[0].set_xlabel("Número de elementos (n)")
        axs[0].set_ylabel("Segundos")
        axs[0].grid(True)
        axs[0].legend()

        axs[1].set_title("Tiempo de Búsqueda")
        axs[1].set_xlabel("Número de elementos (n)")
        axs[1].set_ylabel("Segundos")
        axs[1].grid(True)
        axs[1].legend()

        plt.tight_layout()
        plt.savefig(f"grafico_{modo.lower()}.png", dpi=300)
        print(f"✅ Gráfico generado: grafico_{modo.lower()}.png")

# =====================
# Main
# =====================

if __name__ == "__main__":
    tamaños, resultados = ejecutar_pruebas()
    graficar(tamaños, resultados)
