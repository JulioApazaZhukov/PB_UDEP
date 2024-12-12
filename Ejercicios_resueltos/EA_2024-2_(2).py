def reproducir_cancion(canciones, busqueda):
    for cancion in canciones:
        i, j = 0, 0
        while i < len(cancion['nombre']) and j < len(busqueda):
            if cancion['nombre'][i].lower() == busqueda[j].lower():
                j += 1
            i += 1
        if j == len(busqueda):
            cancion['reproducciones'] += 1
            return cancion['nombre']

        i, j = 0, 0
        while i < len(cancion['artista']) and j < len(busqueda):
            if cancion['artista'][i].lower() == busqueda[j].lower():
                j += 1
            i += 1
        if j == len(busqueda):
            cancion['reproducciones'] += 1
            return cancion['nombre']

    return None

def spotify_wrapped(canciones):
    for i in range(len(canciones)):
        for j in range(0, len(canciones) - i - 1):
            if canciones[j]['reproducciones'] < canciones[j + 1]['reproducciones']:
                canciones[j], canciones[j + 1] = canciones[j + 1], canciones[j]

    top_20 = []
    for i in range(min(20, len(canciones))):
        top_20.append(canciones[i]['nombre'])

    return top_20

canciones = [
    {'nombre': 'Song A', 'artista': 'Artist 1', 'reproducciones': 100},
    {'nombre': 'Song B', 'artista': 'Artist 2', 'reproducciones': 200},
    {'nombre': 'Song C', 'artista': 'Artist 3', 'reproducciones': 150},
]

print("Reproduciendo:", reproducir_cancion(canciones, "Song A"))

print("Spotify Wrapped:", spotify_wrapped(canciones))