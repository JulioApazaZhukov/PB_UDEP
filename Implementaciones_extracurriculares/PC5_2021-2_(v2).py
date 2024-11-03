texto = input("Ingresa un texto de al menos 20 palabras: ")

palabras = texto.strip().split()

if len(palabras) < 20:
    print("El texto debe tener al menos 20 palabras.")
else:
    f = []

    for i in range(len(palabras)):
        found = []
        for j in range(len(palabras)):
            if palabras[i] == palabras[j]:
                found.append(j)
        f.append(len(found))

    max1 = 0
    max2 = 0
    idx1 = -1
    idx2 = -1

    for i in range(len(f)):
        if f[i] > max1:
            max2 = max1 
            idx2 = idx1 
            max1 = f[i]
            idx1 = i
        elif f[i] > max2 and palabras[i] != palabras[idx1]:
            max2 = f[i]
            idx2 = i

    print(f"La palabra que más se repite es '{palabras[idx1]}' con {max1} repeticiones.")
    print(f"La segunda palabra más repetida es '{palabras[idx2]}' con {max2} repeticiones.")
