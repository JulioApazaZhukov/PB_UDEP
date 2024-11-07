def esPar(num):
    if num % 2 == 0:
        return 'par'
    else: return 'impar'

while True:
    n = input('Ingrese un numero entero positivo: ')
    if n.isdigit():
        n = int(n)
        if n > 0:
            break

p = esPar(n)
print(f"El número {n} es {p}")