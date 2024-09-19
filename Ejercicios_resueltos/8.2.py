while True:
    try:
        num1 = int(input("Ingrese un número: "))
        if num1 > 9 and num1 % 1 == 0:
            break
    except ValueError as ve:
        print("No floatpoit supported")

i = 1

while :
    res = num1 % 10 * i
    i = i * 10
    print(res)
    if res == 0:
        break

x = num1
cd = 0

while x > 0:
    x = x//10
    cd= cd + 1