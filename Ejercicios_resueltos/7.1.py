#in range(start, stop, step)

while True:
    número = int(input("Ingrese un numero entero: "))
    if número % 1 == 0 and número > 0:
        break

f = 1

for i in range(1, número+1):
    f = f * i
print(f)