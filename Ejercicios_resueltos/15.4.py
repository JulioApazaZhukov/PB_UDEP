n = [19,11,15,16,12,13,17,10,9,20,7,14,18]
index = [0, 0]

sum = 0
for i in range(len(n)):
	sum += n[i]

min1 = n[0]
for i in range(len(n)):
	if n[i] < min1:
		index[0] = i
		min1 = n[i]

if index[0]==0:
	index[1]=1
min2 = n[index[1]]
for i in range(len(n)):
	if n[i] < min2 and n[i] > min1:
		index[1] = i
		min2 = n[i]

print(f"El primer menor es {min1}")
print(f"El segundo menor es {min2}")

print(f"El promedio es {(sum-min1-min2)/(len(n)-2)}")