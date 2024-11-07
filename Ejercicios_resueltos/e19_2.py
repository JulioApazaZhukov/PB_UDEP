def esPar(num):
    if num % 2 == 0:
        return num
    else: 
        num = 0
        return num

def sumOfnumbers(limit):
    sum = 0
    for i in range(limit + 1):
        integer = i
        n = esPar(integer)
        sum += n
    return sum

l = int(input("Ingrese el limite: "))
r = sumOfnumbers(l)
print(f"La suma de los numeros del 1 al {l} es {r}")