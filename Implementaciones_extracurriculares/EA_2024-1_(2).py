nombres = []
pesos = []
valores = []

print("Ingrese el nombre, peso (en kg) y valor (en soles) de 50 objetos:")

for i in range(50):
    print(f"\nObjeto {i+1}:")
    nombre = input("Nombre del objeto: ").strip()

    while True:
        peso = input("Peso (kg): ").strip()
        if peso.isdigit() and int(peso) > 0:
            peso = int(peso)
            break
        else:
            print("Error: Ingrese un peso válido (entero positivo).")
    
    while True:
        valor = input("Valor (S/): ").strip()
        if valor.isdigit() and int(valor) > 0:
            valor = int(valor)
            break
        else:
            print("Error: Ingrese un valor válido (entero positivo).")
    
    nombres.append(nombre)
    pesos.append(peso)
    valores.append(valor)

capacidad = 20  
n = len(nombres)

tabla = [[0 for _ in range(capacidad + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(capacidad + 1):
        if pesos[i - 1] <= w:  
            tabla[i][w] = max(
                valores[i - 1] + tabla[i - 1][w - pesos[i - 1]],
                tabla[i - 1][w]
            )
        else: 
            tabla[i][w] = tabla[i - 1][w]

w = capacidad
objetos_seleccionados = []

for i in range(n, 0, -1):
    if tabla[i][w] != tabla[i - 1][w]:
        objetos_seleccionados.append(i - 1)
        w -= pesos[i - 1] 

print(f"Valor máximo obtenido: S/{tabla[n][capacidad]}")

print("Objetos seleccionados:")
for i in objetos_seleccionados:
    print(f"- {nombres[i]} (Peso: {pesos[i]} kg, Valor: S/{valores[i]})")
