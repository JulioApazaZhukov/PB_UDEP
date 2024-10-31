nombres = []
notas = []

for i in range(4):
    print(f"Evaluación #{i+1}")
    while True:
         e = input("Ingrese el nombre de la evaluación: ")
         n = int(input("IIngrese la nota de la evaluación: "))
         if e != '' and 0 <= n <= 20:
              break
    nombres.append(e)
    notas.append(n)

for i in range(len(nombres)):
     print(f"{nombres[i]}: {notas[i]}")

print("---------------")

for i in range(len(nombres)-1):
        for j in range(i+1, len(nombres)):
            if notas[i] < notas[j]:
                aux = nombres[i]
                nombres[i] = nombres[j]
                nombres[j] = aux
                aux = notas[i]
                notas[i] = notas[j]
                notas[j] = aux

for i in range(len(nombres)):
     print(f"{nombres[i]}: {notas[i]}")