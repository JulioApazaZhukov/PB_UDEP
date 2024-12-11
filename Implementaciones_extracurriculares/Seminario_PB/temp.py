def camb(n, b):
    res = ""
    while n > 0:
        res = str(n % b) + res
        n //= b
    return res

n = int(input())
b = int(input())
print(camb(n, b))