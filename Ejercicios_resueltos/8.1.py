while True:
    try:
        num1 = int(input("Ingrese un número: "))
        if num1 > 1 and num1 % 1 == 0:
            break
    except ValueError as ve:
        print("Floating poit not supported")
while True:
    try:
        num2 = int(input("Ingrese un número: "))
        if num2 > 1 and num2 % 1 == 0:
            break
    except ValueError as ve:
        print("Floating poit not supported")

sum1 = 0
sum2 = 0

for i in range(1, num1-1, 1):
    if num1 % i == 0:
        sum1 = sum1 + i


for i in range(1, num2-1, 1):
    if num2 % i == 0:
        sum2 = sum2 + i
    
if sum1 == num2 or sum2 == num1:
    print("Son números amigos")
else:
    print("No son números amigos")