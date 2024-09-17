while True:
    a = int(input("Ingrese un numero entero: "))
    if a % 1 == 0 and a > 0:
        break
while True:
    b = int(input("Ingrese un numero entero mayor que el anterior +2: "))
    if b % 1 == 0 and b > a + 2:
        break
while True:
    c = int(input("Ingrese un numero entero: "))
    if (a < b and c > 0) or (a > b and c < 0):
        break

for i in range(a, b, c):
    print(i)