#nombre = input()
#print("Hola ", nombre)

data = {2, 3, 5, 4, 8, 9, 7, 4, 1, 4}
array = list(data)
i = 0
j = 0
for j in range (10):
    for i in range (10):
        if (array[i] > array[i+1]):
            aux = array[i]
            array[i] = array[i+1]
            array[i] = aux
i = 0
for i in range (10):
    print(array[i])