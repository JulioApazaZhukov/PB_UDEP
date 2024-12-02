array = [1, 2, 3, 4, 5]
print(array)

a = 2
array.insert(a, 90) # index, object 
print(array)

array.append(6)      # inserta al final de la lista
print(array)

print(array[1:])    # del indice en adelante

texto = "  PB son las iniciales de programacion basica   "
palabras = texto.strip().split() # strip elimina espacios al inicio y al final y split divide la cadena
print(palabras)

for i in range(len(palabras)):
    print(palabras[i], end=" ")