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
    result = 0
    for i in range(len(n)):
        result += n[i] * p[i]
    return result

def menor(n, p, v):
    aux = 21 
    for i in range(len(n)):
        if p[i] == v: 
            if n[i] < aux: 
                aux = n[i]
                index = i
    if index != -1:  
        menor_nota = n[index]  
        n[index] = 0  
        p[index] = 0  

print("Notas: ")
notas = pedirNumeros(4, 0, 20)

print("Pesos: ")
pesos = pedirNumeros(4, 1, 3)

print(notas)
print(pesos)

menor(notas, pesos, 1)

print(notas)
print(pesos)

sumaPesos = suma(pesos)
print(sumaPesos)
sumaNotas = sumaPonderada(notas, pesos)
print(sumaNotas)

promedioP = sumaNotas / sumaPesos if sumaPesos != 0 else 0
print(f"El promedio ponderado menos la menor nota es {promedioP:.2f}")