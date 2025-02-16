def palabra_mas_larga(texto):
    palabras = texto.split()
    max_palabra = palabras[0]
    for palabra in palabras:
        if len(palabra) > len(max_palabra):
            max_palabra = palabra
    return max_palabra

def encontrar_palabra_rec(texto, palabra, index=None, pos=-1):
    palabras = texto.split()
    if index is None:
        index = len(palabras) - 1 
    if index < 0:
        return pos 
    if palabras[index] == palabra:
        pos = index
    return encontrar_palabra_rec(texto, palabra, index - 1, pos)

def insertar_palabra(texto, palabra, posicion):
    palabras = texto.split()
    if 0 <= posicion < len(palabras):
        palabras.insert(posicion, palabra)
        return " ".join(palabras)
    else:
        print("Posición inválida.")
        return texto

def eliminar_palabra_rec(texto, palabra):
    palabras = texto.split()
    if not palabras:
        return ""
    if palabras[0] == palabra:
        return eliminar_palabra_rec(" ".join(palabras[1:]), palabra)
    else:
        return palabras[0] + " " + eliminar_palabra_rec(" ".join(palabras[1:]), palabra)

while True:
    texto = input("Ingrese un texto con al menos 100 palabras:\n").strip()
    if len(texto.split()) >= 100:
        break
    print("El texto debe tener al menos 100 palabras. Intente nuevamente.")

while True:
    print("\n¿Qué desea hacer?")
    print("1. Palabra más larga")
    print("2. Encontrar palabra")
    print("3. Insertar palabra")
    print("4. Eliminar palabra")
    print("5. Volver a imprimir el menú")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        print("Palabra más larga:", palabra_mas_larga(texto))
        break

    elif opcion == "2":
        palabra = input("Ingrese la palabra a buscar: ").strip()
        posicion = encontrar_palabra_rec(texto, palabra)
        if posicion != -1:
            print(f"La palabra '{palabra}' se encuentra en la posición {posicion}.")
        else:
            print("No se encontró la palabra.")
        break

    elif opcion == "3":
        palabra = input("Ingrese la palabra a insertar: ").strip()
        try:
            posicion = int(input("Ingrese la posición (no puede ser al final): ").strip())
            texto = insertar_palabra(texto, palabra, posicion)
            print("Texto actualizado:", texto)
        except ValueError:
            print("Error: La posición debe ser un número entero.")
        break

    elif opcion == "4":
        palabra = input("Ingrese la palabra a eliminar: ").strip()
        texto = eliminar_palabra_rec(texto, palabra)
        print("Texto actualizado:", texto)
        break

    elif opcion == "5":
        continue

    else:
        print("Opción no válida. Intente de nuevo.")