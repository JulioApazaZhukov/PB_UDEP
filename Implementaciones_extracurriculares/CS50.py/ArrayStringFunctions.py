# Operaciones con listas
array = [1, 2, 3, 4, 5]
print("Lista original:", array)

# Insertar un elemento en un índice específico
a = 2
array.insert(a, 90)  # index, object
print("Lista después de insertar 90 en el índice 2:", array)

# Agregar un elemento al final de la lista
array.append(6)
print("Lista después de agregar 6 al final:", array)

# Extender la lista con otra lista
array.extend([7, 8, 9])  # Agrega múltiples elementos al final
print("Lista después de extender con [7, 8, 9]:", array)

# Acceso por slicing
print("Elementos desde el índice 1 hasta el final:", array[1:])
print("Elementos desde el índice 2 hasta el 5:", array[2:6])
print("Lista invertida:", array[::-1])

# Eliminar elementos de la lista
array.pop()  # Elimina el último elemento
print("Lista después de eliminar el último elemento con pop:", array)

array.pop(3)  # Elimina el elemento en el índice 3
print("Lista después de eliminar el elemento en el índice 3 con pop:", array)

array.remove(90)  # Elimina la primera aparición del valor especificado
print("Lista después de eliminar 90:", array)

# Buscar el índice de un elemento
index = array.index(4)  # Devuelve el índice de la primera aparición del valor
print("Índice del elemento 4:", index)

# Ordenar la lista
array.sort()  # Ordena la lista en orden ascendente
print("Lista ordenada en orden ascendente:", array)

array.sort(reverse=True)  # Ordena la lista en orden descendente
print("Lista ordenada en orden descendente:", array)

# Longitud de la lista
print("Longitud de la lista:", len(array))

# Contar ocurrencias de un elemento
print("Número de veces que aparece el 3 en la lista:", array.count(3))

# Copiar una lista
copia_lista = array.copy()
print("Copia de la lista:", copia_lista)

# Vaciar la lista
array.clear()
print("Lista después de usar clear():", array)

# Operaciones con cadenas
texto = "  PB son las iniciales de programación básica   "
print("\nCadena original:", texto)

# Eliminar espacios al inicio y al final
texto_limpio = texto.strip()
print("Cadena después de usar strip():", texto_limpio)

# Dividir una cadena en una lista de palabras
palabras = texto_limpio.split()
print("Lista de palabras después de usar split():", palabras)

# Unir una lista de palabras en una cadena
texto_unido = " ".join(palabras)
print("Cadena después de unir palabras con join():", texto_unido)

# Cambiar a minúsculas y mayúsculas
print("Texto en minúsculas:", texto.lower())
print("Texto en mayúsculas:", texto.upper())
print("Texto con la primera letra de cada palabra en mayúscula:", texto.title())
print("Texto con la primera letra en mayúscula:", texto.capitalize())

# Reemplazar palabras en una cadena
texto_reemplazado = texto.replace("programación", "Python")
print("Cadena después de reemplazar 'programación' por 'Python':", texto_reemplazado)

# Encontrar una subcadena
indice_programacion = texto.find("programación")  # Devuelve el índice donde comienza la subcadena
print("Índice donde comienza la palabra 'programación':", indice_programacion)

# Verificar si una cadena empieza o termina con algo
print("¿El texto comienza con 'PB'? :", texto.startswith("PB"))
print("¿El texto termina con 'básica'? :", texto.strip().endswith("básica"))

# Contar ocurrencias de una subcadena
print("Número de veces que aparece 'la' en el texto:", texto.count("la"))

# Iterar sobre palabras
print("\nIterando sobre palabras de la lista:")
for i in range(len(palabras)):
    print(palabras[i], end=" ")

# Cadena invertida
cadena_invertida = texto[::-1]
print("\nCadena invertida:", cadena_invertida)

# Cadena sin espacios
sin_espacios = texto.replace(" ", "")
print("Cadena sin espacios:", sin_espacios)

# Verificar si una cadena es numérica
numero = "12345"
print("¿'12345' es numérica?:", numero.isdigit())
print("¿'PB123' es numérica?:", "PB123".isdigit())

# Multiplicar una cadena
print("Repetir texto 3 veces:", texto.strip() * 3)