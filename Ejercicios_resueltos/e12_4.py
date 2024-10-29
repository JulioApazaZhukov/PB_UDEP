array = []
nota_min = 20

for i in range(6):
    while True:
        nota = int(input("Ingrese la nota #" + str(i+1) + ":"))
        if nota != '' and 0 <= nota <= 20: break
    array.append(nota)
    if nota_min > array[i]: nota_min = array[i]

print(array)

sum  = 0
for i in range(len(array)):
    sum  = sum + array[i]
sum = sum - nota_min
prom = sum / (len(array) - 1)

print(f"El promedio es : {prom}")