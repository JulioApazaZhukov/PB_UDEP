while True:
    n = int(input('Ingrese un número primo: '))
    if n > 0:
        break
cd = 0
for i in range(1, n+1):
    if n%i == 0:
        cd = cd+1
        if cd > 2:
            break
if cd == 2:
    print(n, 'es primo')
else:
    print(n, 'no es primo')