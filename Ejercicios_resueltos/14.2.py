x = [2, 4, 3, 5, 6, 5, 3, 2, 1, 8]

while True:
    try:
        item = int(input("Item: "))
        t = True
    except ValueError:
        print("Only numerical data")
        t = False
    if t == True: break
found = False
index = []

for i in range(len(x)):
    if x[i] == item:
        index.append(i)
        found = True

if found == False: print("Item not found")
else: print(f"Item found at index #{index}")