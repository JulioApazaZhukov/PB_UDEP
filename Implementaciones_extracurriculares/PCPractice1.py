def agregar(arr, cadena):
    arr.append(cadena)
    return arr

def insertar(arr, cadena, posicion):
    if 0 <= posicion <= len(arr):
        arr.insert(posicion, cadena)
    else:
        print("Posición inválida.")
    return arr

def buscar(arr, cadena):
    for i in range(len(arr)):
        if arr[i] == cadena:
            return i
    return -1

x = []

while True:
    print("\nMenú:")
    print("a. Agregar")
    print("b. Insertar")
    print("c. Buscar")
    print("d. Limpiar")
    print("(Deje vacío para salir)")

    opcion = input("Seleccione una opción: ").strip()

    if opcion == "":
        print("Saliendo del programa...")
        break

    if opcion == "a":
        cadena = input("Ingrese la cadena a agregar: ").strip()
        x = agregar(x, cadena)

    elif opcion == "b":
        cadena = input("Ingrese la cadena a insertar: ").strip()
        try:
            posicion = int(input("Ingrese la posición: ").strip())
            x = insertar(x, cadena, posicion)
        except ValueError:
            print("Error: La posición debe ser un número entero.")

    elif opcion == "c":
        cadena = input("Ingrese la cadena a buscar: ").strip()
        posicion = buscar(x, cadena)
        if posicion != -1:
            print(f"Se encontró en la posición {posicion}")
        else:
            print("No se encontró")

    elif opcion == "d":
        x = []
        print("Array limpiado.")

    else:
        print("Opción no válida. Intente de nuevo.")

    print("Array actual:", x)