tamaños = ["mediano", "pequeño", "pequeño", "grande", "mediano", "pequeño", "grande", "mediano", "mediano", "grande"]
dias = [3, 27, 27, 8, 19, 4, 20, 26, 7, 28]
meses = [1, 2, 2, 8, 7, 3, 6, 2, 5, 12]
años = [2020, 2020, 2025, 2024, 2030, 2050, 2080, 2027, 2040, 2000]

for i in range(len(tamaños)):
    if tamaños[i] == "pequeño": tamaños[i] = 2
    elif tamaños[i] == "mediano": tamaños[i] = 4
    elif tamaños[i] == "grande": tamaños[i] = 7

    bisiesto=0
    if años[i]%4 == 0 and (años[i]%100 != 0 or años[i]%400 == 0):
        bisiesto=1
    diasMes = [31,28+bisiesto,31,30,31,30,31,31,30,31,30,31]

    if (dias[i] + tamaños[i]) > diasMes[i]:
        dias[i] = dias[i] + tamaños[i] - diasMes[i]
        meses[i] += 1
    else: dias[i] += tamaños[i]

    if (meses[i]) == 13:
        meses[i] = 1
        años[i] += 1
    print(f"El producto #{i+1} se entregará el {dias[i]}/{meses[i]}/{años[i]}")

min = [40, 13, 3000]
max = [0, 0, 0]
index = [0, 0]
for i in range(len(tamaños)):
    if min[2] > años[i]:
        min[2] = años[i]
        min[1] = meses[i]
        min[0] = dias[i]
        index[0] = i

    if max[2] < años[i]:
        max[2] = años[i]
        max[1] = meses[i]
        max[0] = dias[i]
        index[1] = i
print(f"El producto #{index[0] + 1} primero y el producto #{index[1] + 1} ultimo")