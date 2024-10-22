x = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9]
f = []

for j in range(len(x)):
    a = x[j]
    f.append(0)
    for i in range(len(x)):
        if a == x[i]:
            f[j] += 1
print(x)
print(f)