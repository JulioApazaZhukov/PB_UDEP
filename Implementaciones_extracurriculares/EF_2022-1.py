def contar_palabras(x):
    palabras = x.strip().split()  # Elimina espacios extra y divide en palabras
    c = len(palabras) 
    return c

def pasarAunaLista(x):
    lista = x.strip().split() 
    return lista

def Palabramaslarga(x):
    palabras = pasarAunaLista(x)  
    palabralarga = max(palabras, key=len)  
    return palabralarga

def encontrar(x, palabra):
    lista = pasarAunaLista(x)  
    posiciones = [i for i, p in enumerate(lista) if p == palabra] 
    return posiciones

def insertar(x, a, d):
    lista = pasarAunaLista(x)
    lista.insert(a, d)  
    return " ".join(lista)  

def eliminar(x, palabra):
    lista = pasarAunaLista(x) 
    lista = [p for p in lista if p != palabra]  # Elimina todas las ocurrencias de la palabra
    return " ".join(lista)  # Convierte la lista de regreso a una cadena

while True:
    x = input('Ingrese una oración de al menos 5 palabras: ')
    if contar_palabras(x) >= 5:
        break

while True:
    print('\n¿Qué desea hacer?')
    print('1. Palabra más larga')
    print('2. Encontrar una palabra')
    print('3. Insertar una palabra')
    print('4. Eliminar una palabra')
    print('5. Salir')

    g = int(input('Ingresa un número (1, 2, 3, 4 o 5): '))
    
    if g == 1:
        print('La palabra más larga es:', Palabramaslarga(x))

    elif g == 2:
        palabra = input('Ingresa una palabra para buscar: ')
        posiciones = encontrar(x, palabra)
        if posiciones:
            print(f'Se encontró la palabra "{palabra}" en las posiciones: {posiciones}')
        else:
            print(f'La palabra "{palabra}" no se encontró en la cadena.')

    elif g == 3:
        palabra = input('Ingresa la palabra que quieres insertar: ')
        posicion = int(input('¿En qué posición quieres insertarla? '))
        x = insertar(x, posicion, palabra)
        print('Nueva oración:', x)

    elif g == 4:
        palabra = input('Ingresa la palabra que quieres eliminar: ')
        x = eliminar(x, palabra)
        print('Nueva oración después de eliminar la palabra:', x)

    elif g == 5:
        print('¡Adiós!')
        break

    else:
        print('Opción no válida. Intenta de nuevo.')