def cadena_mas_larga(arr):
    if not arr:
        return "El array está vacío."
    max_cadena = arr[0]
    for cadena in arr:
        if len(cadena) > len(max_cadena):
            max_cadena = cadena
    return max_cadena

def encontrar_ultima_posicion(arr, cadena):
    posicion = -1
    for i in range(len(arr)):
        if arr[i] == cadena:
            posicion = i
    return posicion

def insertar(arr, cadena, posicion):
    if 0 <= posicion <= len(arr):
        arr.insert(posicion, cadena)
    else:
        print("Posición inválida.")
    return arr

def eliminar(arr, cadena):
    return [x for x in arr if x != cadena]

x = [] 

while True:
    print("\n¿Qué desea hacer?")
    print("1. Cadena más larga")
    print("2. Encontrar")
    print("3. Insertar")
    print("4. Eliminar")
    print("5. Salir")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "5":
        print("Saliendo del programa...")
        break

    if opcion == "1":
        print("Cadena más larga:", cadena_mas_larga(x))

    elif opcion == "2":
        cadena = input("Ingrese la cadena a buscar: ").strip()
        posicion = encontrar_ultima_posicion(x, cadena)
        if posicion != -1:
            print(f"Última aparición en la posición {posicion}")
        else:
            print("No se encontró la cadena.")

    elif opcion == "3":
        cadena = input("Ingrese la cadena a insertar: ").strip()
        try:
            posicion = int(input("Ingrese la posición: ").strip())
            x = insertar(x, cadena, posicion)
        except ValueError:
            print("Error: La posición debe ser un número entero.")

    elif opcion == "4":
        cadena = input("Ingrese la cadena a eliminar: ").strip()
        x = eliminar(x, cadena)
        print(f"Se eliminaron todas las apariciones de '{cadena}'.")

    else:
        print("Opción no válida. Intente de nuevo.")

    print("Array actual:", x)