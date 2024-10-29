x = [5, 4, 1, 5, 5, 6, 1, 5, 6, 1, 7, 5, 5, 1, 6, 
	 9, 7, 5, 1, 6, 7, 6, 1, 8, 1, 8, 1, 9, 6, 6]
f = []

for i in range(len(x)):
	pos = []
	for j in range(len(x)):
		if x[i]==x[j]:
			pos.append(j)
	f.append(len(pos))

print(x)
print(f)

mayor=0
for i in range(len(f)):
	if f[i]>mayor:
		mayor = f[i]

mas_frecuentes = []
for i in range(len(f)):
	if f[i] == mayor:
		pos=-1
		for j in range(len(mas_frecuentes)):
			if x[i] == mas_frecuentes[j]:
				pos = j
				break
		if pos==-1: 
			mas_frecuentes.append(x[i])

print(f"Los valores más frecuentes son: {mas_frecuentes}")
print(f"Cada uno se repite {mayor} veces")