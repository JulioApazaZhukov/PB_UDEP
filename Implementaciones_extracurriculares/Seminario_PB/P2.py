def palindromo(n):
    strNumero = str(n)
    return strNumero == strNumero[::-1]

numero = int(input("Ingrese un numero mayor a 10"))

if palindromo(numero):
    print(f"{numero} es un palíndromo.")
else:
    print(f"{numero} no es un palíndromo.")