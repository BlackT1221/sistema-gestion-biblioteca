from grafo_usuarios import GrafoUsuarios

def construir_grafo_usuarios(lista_usuarios):
    """
    Cada usuario debe tener:
    - id
    - libros_prestados (lista de objetos Libro)
    - ratings: { libro_id : rating }
    """
    grafo = GrafoUsuarios()

    for i in range(len(lista_usuarios)):
        for j in range(i + 1, len(lista_usuarios)):
            u1 = lista_usuarios[i]
            u2 = lista_usuarios[j]

            libros_u1 = {l.id for l in u1.libros_prestados}
            libros_u2 = {l.id for l in u2.libros_prestados}

            libros_comunes = libros_u1.intersection(libros_u2)

            if libros_comunes:
                rating_total = 0
                contador = 0

                for libro_id in libros_comunes:
                    if libro_id in u1.ratings and libro_id in u2.ratings:
                        rating_total += (u1.ratings[libro_id] + u2.ratings[libro_id]) / 2
                        contador += 1

                if contador > 0:
                    peso = round(rating_total / contador, 2)
                    grafo.agregar_relacion(u1.id, u2.id, peso)

    return grafo