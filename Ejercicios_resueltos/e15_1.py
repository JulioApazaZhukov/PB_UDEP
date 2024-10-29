x = [4, 5, 5, 6, 6, 6, 7, 7, 7, 7, 8, 8, 9, 5]
f = []

for i in range(len(x)):
	found = []
	for j in range(len(x)):
		if x[i]==x[j]:
			found.append(j)
	f.append(len(found))

print(x)

un_val = []
un_val_qy = []

for i in range(len(x)):
    found = -1
    for j in range(len(un_val)):
        if x[i] == un_val[j]:
            found = j
            break
    if found == -1:
        un_val.append(x[i])
        un_val_qy.append(f[i])
        if f[i] > 1:
            print(f"{x[i]} aparece {f[i]} veces")
        else: print(f"{x[i]} aparece 1 vez")
print(f"==> {x}")
print(f"==> {un_val} -> Unique value")
print(f"==> {un_val_qy} -> Unique value quantity")