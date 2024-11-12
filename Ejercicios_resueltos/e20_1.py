def redondear(numero):
    parte_decimal = numero - int(numero)
    if parte_decimal >= 0.5:
        return int(numero) + 1
    else: return int(numero)

suma = 0
for i in range(1, 5):
    while True:
        a = float(input("Ingrese un número real positivo "))
        if a >= 0: break
    suma += redondear(a)

print(f"La suma es {suma}")