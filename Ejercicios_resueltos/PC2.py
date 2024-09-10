ultimoNumeroDNI = int(input("Ingrese el último número de su DNI: "))
añoDeNacimiento = int(input("Ingrese su año de nacimiento: "))
montoAhorrado = int(input("Ingrese el monto ahorado en su AFP: "))
edad = 2024 - añoDeNacimiento
if edad >= 40 and montoAhorrado > 5150:
    if ultimoNumeroDNI == 0 or ultimoNumeroDNI == 3 or ultimoNumeroDNI == 6 or ultimoNumeroDNI == 9:
        print("Le corresponde retirar el 10")
    elif ultimoNumeroDNI == 2 or ultimoNumeroDNI == 4 or ultimoNumeroDNI == 8:
        print("Le corresponde retirar el 20")
    elif ultimoNumeroDNI == 1 or ultimoNumeroDNI == 5 or ultimoNumeroDNI == 7:
        print("Le corresponde retirar el 30")
    else:
        print("Entrada invalida (ultimo número del DNI)")
    nuit = montoAhorrado / 5150
    if 2 >= nuit > 1:
        resto = montoAhorrado - 5150
        print("Le corresponde una armada de 5150 y una de", resto)
    elif 3 >= nuit > 2:
        resto = montoAhorrado - 10300
        print("Le corresponde dos armadas de 5150 y una de", resto)
    elif 4 >= nuit > 3:
        resto = montoAhorrado - 5150*3
        print("Le corresponde tres armadas de 5150 y una de", resto)
    elif nuit > 4:
        print("Le corresponde 4 armadas de 5150")
else:
    print("Etrada invalida (edad o monto ahorrado insuficiente)")