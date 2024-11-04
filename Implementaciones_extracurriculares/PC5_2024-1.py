nombres = []
notas = []
pesos = []
cant_de_evaluaciones = 9 #para las pruebas recomiendo cambiar el valor por 3 o 4

for i in range(cant_de_evaluaciones):
    while True:
        nombre = input(f"Ingrese el nombre de la evaluación #{i+1}: ")
        if (nombre.startswith("Examen") or nombre.startswith("Práctica") or nombre.startswith("Trabajo")) and nombre.split()[-1].isdigit() and 1 <= int(nombre.split()[-1]) <= cant_de_evaluaciones:
            nombres.append(nombre)
            break
        else:
            print("Nombre no válido")

    while True:
        try:
            nota = float(input(f"Ingrese la nota de la evaluación {nombre} (0-20): "))
            if 0 <= nota <= 20:
                notas.append(nota)
                break
            else:
                print("La nota debe estar entre 0 y 20.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")

    while True:
        try:
            peso = int(input(f"Ingrese el peso de la evaluación {nombre} (1, 2 o 3): "))
            if peso in [1, 2, 3]:
                pesos.append(peso)
                break
            else:
                print("El peso debe ser 1, 2 o 3.")
        except ValueError:
            print("Entrada no válida. Ingrese un número.")

notas_peso_1 = [(i, nota) for i, (nota, peso) in enumerate(zip(notas, pesos)) if peso == 1]

if len(notas_peso_1) >= 3:
    for i in range(len(notas_peso_1) - 1):
        for j in range(len(notas_peso_1) - i - 1):
            if notas_peso_1[j][1] > notas_peso_1[j + 1][1]:
                notas_peso_1[j], notas_peso_1[j + 1] = notas_peso_1[j + 1], notas_peso_1[j]
    notas_peso_1 = notas_peso_1[2:]

notas_filtro_peso_1 = [nota for i, nota in notas_peso_1]
promedio_peso_1 = sum(notas_filtro_peso_1) / len(notas_filtro_peso_1) if notas_filtro_peso_1 else 0
print(f"El promedio de las notas de peso 1 (anulando las 2 más bajas) es: {promedio_peso_1:.2f}")

evaluaciones_peso_2_3 = [(nombre, nota) for nombre, nota, peso in zip(nombres, notas, pesos) if peso in [2, 3]]

for i in range(len(evaluaciones_peso_2_3) - 1):
    for j in range(len(evaluaciones_peso_2_3) - i - 1):
        if evaluaciones_peso_2_3[j][1] < evaluaciones_peso_2_3[j + 1][1]:
            evaluaciones_peso_2_3[j], evaluaciones_peso_2_3[j + 1] = evaluaciones_peso_2_3[j + 1], evaluaciones_peso_2_3[j]

if len(evaluaciones_peso_2_3) >= 2:
    print("Las 2 evaluaciones de peso 2 o 3 con la nota más alta son:")
    for nombre, nota in evaluaciones_peso_2_3[:2]:
        print(f"{nombre}: {nota}")
else:
    print("No hay suficientes evaluaciones de peso 2 o 3 para mostrar las dos más altas.")