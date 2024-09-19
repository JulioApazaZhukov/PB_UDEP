while True:
    try:
        num1 = int(input("Ingrese un número: "))
        if num1 > 9 and num1 % 1 == 0:
            break
    except ValueError as ve:
        print("Floating poit not supported")

x = num1
cd = 0

while x > 0:
    x = x//10
    cd= cd + 1
x = num1
s = 0
while x > 0:
    r = x % 10
    s = s + r**cd
    x = x//10
if s == num1:
    print(num1, "Es narcisista")
else:
    print(num1, "No es narcisista")