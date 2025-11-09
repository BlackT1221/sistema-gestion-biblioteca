# arboles.py
# Implementación de árboles binarios de búsqueda (BST) para libros y usuarios

from dataclasses import dataclass
from typing import Any, Optional, List, Tuple


# Nodo base del árbol
class NodoBST:
    def __init__(self, clave: Any, valor: Any):
        self.clave = clave
        self.valor = valor
        self.izq: Optional["NodoBST"] = None
        self.der: Optional["NodoBST"] = None


class ArbolBST:
    """Árbol binario de búsqueda genérico (sin balancear)."""

    def __init__(self):
        self.raiz: Optional[NodoBST] = None
        self._tam = 0

    def insertar(self, clave: Any, valor: Any) -> None:
        def _insertar(nodo: Optional[NodoBST], clave, valor) -> NodoBST:
            if nodo is None:
                return NodoBST(clave, valor)
            if clave < nodo.clave:
                nodo.izq = _insertar(nodo.izq, clave, valor)
            elif clave > nodo.clave:
                nodo.der = _insertar(nodo.der, clave, valor)
            else:
                nodo.valor = valor
            return nodo

        if self.buscar(clave) is None:
            self._tam += 1
        self.raiz = _insertar(self.raiz, clave, valor)

    def buscar(self, clave: Any) -> Optional[Any]:
        nodo = self.raiz
        while nodo:
            if clave == nodo.clave:
                return nodo.valor
            elif clave < nodo.clave:
                nodo = nodo.izq
            else:
                nodo = nodo.der
        return None

    def _minimo(self, nodo: NodoBST) -> NodoBST:
        while nodo.izq:
            nodo = nodo.izq
        return nodo

    def eliminar(self, clave: Any) -> bool:
        eliminado = False

        def _eliminar(nodo: Optional[NodoBST], clave) -> Optional[NodoBST]:
            nonlocal eliminado
            if nodo is None:
                return None
            if clave < nodo.clave:
                nodo.izq = _eliminar(nodo.izq, clave)
            elif clave > nodo.clave:
                nodo.der = _eliminar(nodo.der, clave)
            else:
                eliminado = True
                if nodo.izq is None:
                    return nodo.der
                if nodo.der is None:
                    return nodo.izq
                sucesor = self._minimo(nodo.der)
                nodo.clave, nodo.valor = sucesor.clave, sucesor.valor
                nodo.der = _eliminar(nodo.der, sucesor.clave)
            return nodo

        self.raiz = _eliminar(self.raiz, clave)
        if eliminado:
            self._tam -= 1
        return eliminado

    def recorrido_inorden(self) -> List[Tuple[Any, Any]]:
        resultado = []

        def _inorden(nodo: Optional[NodoBST]):
            if nodo:
                _inorden(nodo.izq)
                resultado.append((nodo.clave, nodo.valor))
                _inorden(nodo.der)

        _inorden(self.raiz)
        return resultado

    def __len__(self):
        return self._tam
