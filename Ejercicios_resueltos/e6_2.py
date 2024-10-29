i = 0
while True:
    num = int(input('Ingrese un número de al menos 2 digitos:'))
    if num >= 10:
        break
while num > 0:
    num = num // 10
    i = i+1
print('El número tiene', i, 'digitos')