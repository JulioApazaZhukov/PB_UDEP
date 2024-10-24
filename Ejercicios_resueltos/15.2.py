x = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 5]
f = []

for i in range(len(x)):
    found = []
    for j in range(len(x)):
        if x[i] == x[j]:
             found.append(j)
    f.append(len(found))
print(x)
print(f)

max = 0
for i in range(len(f)):
    if f[i] > max:
        max = f[i]
        found = i
print(f"El valor que mas se repite es {x[found]}")