# arboles_avl.py
class NodoAVL:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.izq = None
        self.der = None
        self.altura = 1

class ArbolAVL:
    def __init__(self):
        self.raiz = None

    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    def _balance(self, nodo):
        return self._altura(nodo.izq) - self._altura(nodo.der) if nodo else 0

    def _rotar_derecha(self, y):
        x = y.izq
        T2 = x.der
        x.der = y
        y.izq = T2
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        return x

    def _rotar_izquierda(self, x):
        y = x.der
        T2 = y.izq
        y.izq = x
        x.der = T2
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        return y

    def insertar(self, clave, valor):
        def _insertar(nodo, clave, valor):
            if not nodo:
                return NodoAVL(clave, valor)
            if clave < nodo.clave:
                nodo.izq = _insertar(nodo.izq, clave, valor)
            elif clave > nodo.clave:
                nodo.der = _insertar(nodo.der, clave, valor)
            else:
                nodo.valor = valor
                return nodo

            nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
            balance = self._balance(nodo)

            if balance > 1 and clave < nodo.izq.clave:
                return self._rotar_derecha(nodo)
            if balance < -1 and clave > nodo.der.clave:
                return self._rotar_izquierda(nodo)
            if balance > 1 and clave > nodo.izq.clave:
                nodo.izq = self._rotar_izquierda(nodo.izq)
                return self._rotar_derecha(nodo)
            if balance < -1 and clave < nodo.der.clave:
                nodo.der = self._rotar_derecha(nodo.der)
                return self._rotar_izquierda(nodo)

            return nodo

        self.raiz = _insertar(self.raiz, clave, valor)

    def buscar(self, clave):
        nodo = self.raiz
        while nodo:
            if clave == nodo.clave:
                return nodo.valor
            elif clave < nodo.clave:
                nodo = nodo.izq
            else:
                nodo = nodo.der
        return None
