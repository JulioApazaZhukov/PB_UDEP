def swap(array, i, j):
    aux = array[i]
    array[i] = array[j]
    array[j] = aux

países = ["Perú", "Argentina", "Chile", "Brasil", "Bolivia", "Ecuador", "Uruguay", "Colombia", "Venezuela", "Paraguay"]
pg = [6, 4, 4, 4, 4, 4, 2, 2, 1, 1]
pe = [1, 4, 3, 1, 3, 0, 5, 4, 3, 2]
pp = [2, 1, 2, 4, 2, 5, 2, 3, 5, 6]
gf = [6, 9, 2, 4, 3, 5, 4, 8, 7, 9]
gc = [5, 4, 8, 7, 5, 6, 9, 2, 4, 3]

puntos = []
for i in range(len(pg)):
    p = pg[i] * 3 + pe[i]
    puntos.append(p)

dif_de_goles = []
for i in range(len(pg)):
    d = gf[i] - gc[i]
    dif_de_goles.append(d)

for i in range(len(puntos)-1):
        for j in range(i+1, len(puntos)):
            if puntos[i] < puntos[j]:
                swap(países, i , j)
                swap(pg, i , j)
                swap(pe, i , j)
                swap(pp, i , j)
                swap(gf, i , j)
                swap(gc, i , j)
            elif puntos[i] == puntos[j] and dif_de_goles[i] < dif_de_goles[j]:
                swap(países, i , j)
                swap(pg, i , j)
                swap(pe, i , j)
                swap(pp, i , j)
                swap(gf, i , j)
                swap(gc, i , j)
            elif puntos[i] == puntos[j] and dif_de_goles[i] == dif_de_goles[j] and gf[i] < gf[j]:
                swap(países, i , j)
                swap(pg, i , j)
                swap(pe, i , j)
                swap(pp, i , j)
                swap(gf, i , j)
                swap(gc, i , j)

for i in range(len(pe)):
    print(f"#{i+1} {países[i]} {puntos[i]}")

print("\nPaises clasificados: ")
for i in range(6):
    print(f"#{i+1} {países[i]} {puntos[i]}")
print("\nEn repechaje: ")
print(f"#7 {países[6]} {puntos[6]}")

goln = []
golp = []
for i in range(len(gf)):
    goln.append(países[i])
    golp.append(gf[i])
for i in range(len(puntos)-1):
        for j in range(i+1, len(puntos)):
            if golp[i] < golp[j]:
                swap(golp, i , j)
                swap(goln, i , j)
print("\nGoleadores:")
print(f"{goln[0]} ==> {golp[0]}")
for i in range(1, 6):
    if golp[i] == golp[0]:
        print(f"{goln[i]} ==> {golp[i]}")

while True:
    seguir = True
    s = input("Ingrese el nombre de un país: ")
    for i in range(len(países)):
        if s == países[i]:
            index = i
            seguir = False
            break
    if seguir == False: break
    else: print("Sin resultados")

print(f"Puesto #{index+1}, {puntos[index]} puntos")