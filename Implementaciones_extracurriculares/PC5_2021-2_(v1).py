def validar_texto(texto):
    palabras = texto.strip().split()
    if len(palabras) < 20:
        print("El texto debe tener al menos 20 palabras.")
        return False
    return True

def bubbleSort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j][1] < lista[j + 1][1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j] 
    return lista

def contar_palabras(texto):
    palabras = texto.strip().split()
    conteo = {}

    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    palabras_frecuencia = list(conteo.items())
    palabras_ordenadas = bubbleSort(palabras_frecuencia)
    
    palabra_mas_repetida = palabras_ordenadas[0][0]
    segunda_palabra_mas_repetida = palabras_ordenadas[1][0]
    
    return palabra_mas_repetida, segunda_palabra_mas_repetida

texto = input("Ingresa un texto de al menos 20 palabras: ")

# Texto es True o False (boleano)
if validar_texto(texto):
    primera, segunda = contar_palabras(texto)
    print(f"La palabra más repetida es: '{primera}'")
    print(f"La segunda palabra más repetida es: '{segunda}'")