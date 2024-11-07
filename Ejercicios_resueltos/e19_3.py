def suma(x):
    suma = 0
    for i in range(len(x)):
        suma += x[i]
    return suma

def pedirNumeros(limite, min, max):
    array = []
    for i in range(limite):
        while True:
            val = int(input("Ingrese un valor: "))
            if min <= val <= max: break
        array.append(val)
    return array

def sumaPonderada(n, p):
    for i in range(len(n)):
        result = n[i] * p[i]
    return(result)

def menor(n, p, v):
    aux = 21
    index = -1
    for i in range(len(n)):
        if p == v:
            if n[i] < aux: 
                aux = n[i]
                index = i
    n[index] = 0
    p[index] = 0

notas = pedirNumeros(4, 0, 20)
print(notas)
pesos = pedirNumeros(4, 1, 3)
print(pesos)
menorNota = menor(notas, pesos, 1)
print(menorNota)
sumaPesos = suma(pesos)
print(sumaPesos)
sumaNotas = sumaPonderada(notas, pesos)
print(sumaNotas)

promedioP = sumaNotas / sumaPesos
print(f"El promedio ponderado menos la menor nota es {promedioP}")