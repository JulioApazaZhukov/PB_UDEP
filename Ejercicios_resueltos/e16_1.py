x = [20, 15, 12, 9, 7, 6, 13, 7, 8, 9]
index = [0,0]

menor = x[index[0]]
for i in range(len(x)):
    if x[i] < menor:
        menor = x[i]
        index[0] = i

if index[0] == 0:
    index[1] = 1
menor2 = x[index[1]]

for i in range(len(x)):
    if x[i] < menor2 and x[i] >= menor and i!=index[0]:
        menor2 = x[i]
        index[1] = i
print(f"El menor valor es {menor}, y el segundo menor es {menor2}")