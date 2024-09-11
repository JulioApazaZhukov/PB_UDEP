i=1
while i<=6:
    n=int(input("Ingrese un numero: "))
    if i == 1:
        menor = n
    else:
        if n < menor:
            menor = n
    i = i+1

print("Menor: ",menor)