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

dp = [0] * (capacidad + 1)
objeto_incluido = [-1] * (capacidad + 1) 

for i in range(n):
    for w in range(capacidad, pesos[i] - 1, -1):
        if dp[w - pesos[i]] + valores[i] > dp[w]:
            dp[w] = dp[w - pesos[i]] + valores[i]
            objeto_incluido[w] = i

w = capacidad
objetos_seleccionados = []

while w > 0 and objeto_incluido[w] != -1:
    i = objeto_incluido[w]
    objetos_seleccionados.append(i)
    w -= pesos[i]

print(f"\nValor máximo obtenido: S/{dp[capacidad]}")
print("Objetos seleccionados:")
for i in objetos_seleccionados:
    print(f"- {nombres[i]} (Peso: {pesos[i]} kg, Valor: S/{valores[i]})")
