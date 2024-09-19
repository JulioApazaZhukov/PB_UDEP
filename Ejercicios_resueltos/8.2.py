while True:
    try:
        num = int(input("Ingrese un número: "))
        if num >= 10 and num % 1 == 0:
            break
    except ValueError as ve:
        print("Floating poit not supported")

num_red=num
num_inv=0
while num_red>0:
    r = num_red%10
    num_inv = num_inv*10 + r
    num_red = num_red//10
if num_inv == num:
    print(num,'es capicúa')
else:
    print(num,'no es capicúa')