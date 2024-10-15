values = []
weights = []

arrsize = int(input("Cantidad de elementos a ingresar: "))
for i in range(arrsize):
    while True:
        value = int(input("Ingrese la nota #" + str(i+1) + ":"))
        if value != '': break
    values.append(value)
    while True:
        weight = int(input("Ingrese el peso de la nota #" + str(i+1) + ":"))
        if weight != '' or weight  >= 1 or weight <= 3: break
    weights.append(weight)

sum  = 0
sweights = 0
for i in range(len(values)):
    sum  = sum + values[i] * weights[i]
    sweights = sweights + weights[i]

prom = sum/sweights
print(f"El promedio es : {prom}")