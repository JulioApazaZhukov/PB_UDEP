from e16_2 import bubblesort

x = []

for i in range(10):
    x.append(int(input("Ingrese un numero: ")))

bubblesort(x)

x[0] = x[1] = x[2] = 0
sum = 0

for i in range(len(x)):
    sum += x[i]
prom = sum / (len(x)-3)

print(f"El promedio de las 7 mayores notas es {prom}")