x = [2, 4, 3, 5, 6, 5, 3, 2, 1, 8]

found = False
while True:
    item = int(input("Item: "))
    for i in range(len(x)):
        if item == x[i]:
            found = True
            break
    if found == True: break
print(f"Item found")