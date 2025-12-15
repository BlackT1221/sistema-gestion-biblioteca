from grafo_builder import construir_grafo_usuarios

# Suponiendo que ya tienes la lista de usuarios creada por tu sistema
grafo = construir_grafo_usuarios(lista_usuarios)

grafo.mostrar_grafo()

print("\nUsuarios relacionados con U1:")
print(grafo.usuarios_relacionados("U1"))
