class GrafoUsuarios:
    def __init__(self):
        # { usuario_id : { usuario_vecino : peso } }
        self.grafo = {}

    # ---------- NODOS ----------
    def agregar_usuario(self, usuario_id):
        if usuario_id not in self.grafo:
            self.grafo[usuario_id] = {}

    def eliminar_usuario(self, usuario_id):
        if usuario_id in self.grafo:
            for vecino in self.grafo[usuario_id]:
                self.grafo[vecino].pop(usuario_id, None)
            del self.grafo[usuario_id]

    # ---------- ARISTAS ----------
    def agregar_relacion(self, u1, u2, peso):
        if u1 == u2:
            return

        self.agregar_usuario(u1)
        self.agregar_usuario(u2)

        # Grafo NO dirigido
        self.grafo[u1][u2] = peso
        self.grafo[u2][u1] = peso

    def eliminar_relacion(self, u1, u2):
        if u1 in self.grafo and u2 in self.grafo[u1]:
            del self.grafo[u1][u2]
            del self.grafo[u2][u1]

    # ---------- CONSULTAS ----------
    def usuarios_relacionados(self, usuario_id):
        return self.grafo.get(usuario_id, {})

    def mostrar_grafo(self):
        for usuario, relaciones in self.grafo.items():
            print(f"{usuario} -> {relaciones}")
