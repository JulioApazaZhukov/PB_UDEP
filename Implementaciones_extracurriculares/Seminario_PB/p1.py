def sumaDeNumeros(n):
    suma = 0
    for i in range(1, n):
        if n % i == 0:
            suma += i
    return suma

num = int(input("Ingrese un número entero positivo: "))

if num == sumaDeNumeros(num): 
    print(f"{num} es un número perfecto.")
else: 
    print(f"{num} no es un número perfecto.")

# Números perfectos: 6, 28, 496, 8128