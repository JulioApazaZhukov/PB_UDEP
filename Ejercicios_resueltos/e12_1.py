array = []
for i in range(5):
    while True:
        nombre =  str(input("Ingrese el nombre del amigo #" + str(i+1) + ":"))
        if nombre != '':
            break
    array.append(nombre)
print(array)