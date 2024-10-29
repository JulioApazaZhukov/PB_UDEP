x = [2, 4, 3, 5, 6, 5, 3, 2, 1, 8]

item = input("Item: ")
found = False
index = []

for i in range(len(x)):
    if str(x[i]) == item:
        index.append(i)
        found = True

if found == False: print("Item not found")
else: print(f"Item found at index #{index}")