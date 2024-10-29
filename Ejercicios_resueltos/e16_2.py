def bubblesort(x):
    for i in range(len(x)-1):
        for j in range(i+1, len(x)):
            if x[i] > x[j]:
                aux = x[i]
                x[i] = x[j]
                x[j] = aux

if __name__ == "__main__":
    x = [20, 15, 12, 9, 7, 6, 13, 7, 8, 9]
    y = [89, 17, 5, 6, 9, 14, 87, 2, 4, 61, 9, 83, 1, 7, 2, 8]
    z = [8, 7, 456, 156, 354, 258, 149, 628, 722, 48]
    print(f"X = {x}, Y = {y}, Z = {z}")
    bubblesort(x)
    bubblesort(y)
    bubblesort(z)
    print(f"X = {x}, Y = {y}, Z = {z}")