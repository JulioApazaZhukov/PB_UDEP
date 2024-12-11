def convertirBase(numero, base):
    resultado = ""
    while numero > 0:
        resultado = str(numero % base) + resultado
        numero //= base
    return resultado


num = int(input("Ingrese un número entero positivo: "))
base = int(input("Ingrese la base (entre 2 y 16): "))

if 2 <= base <= 16:
    print(f"{num} en base {base} es: {convertirBase(num, base)}")
else:
    print("Base no válida.")