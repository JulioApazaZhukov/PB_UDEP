while True:
    num = int(input("Ingrese un numero: "))

    if num > 0:
        if num % 2 == 0:
            print("Es positivo y par")
            break
        else:
            print("Es positivo pero no par")
    else:
        print("Es un número negativo")


print("Programa terminado")