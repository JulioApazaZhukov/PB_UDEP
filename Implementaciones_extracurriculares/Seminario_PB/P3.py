def secCollatz(n):
    collatz = [n]
    while n != 1:
        if n % 2 == 0: n //= 2
        else: n = (n * 3) + 1
        collatz.append(n)
    return collatz

num = int(input("Número: "))
print(secCollatz(num))