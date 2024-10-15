array = []

arrsize = int(input("Cantidad de elementos a ingresar: "))
for i in range(arrsize):
    while True:
        nota = int(input("Ingrese la nota #" + str(i+1) + ":"))
        if nota != '': break
    array.append(nota)

print(array)

sum  = 0
for i in range(len(array)):
    sum  = sum + array[i]

prom = sum/len(array)
print(f"El promedio es : {prom}")