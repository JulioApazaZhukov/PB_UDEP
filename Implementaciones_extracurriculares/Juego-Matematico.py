import random

n = int(input("Cuantos ejercicios quiere resolver:"))
operador = input("Qué tipo de operación quieres practicar: suma, resta o multiplicación: ")

for i in range(n):

    nu1 = random.randint(1, 50)
    nu2 = random.randint(1, 50)
    num1 = random.randint(2, 12)
    num2 = random.randint(1, 12)

    # Por lo visto, Python no tiene case/swith
    if (operador == '+'):
        print("Cuanto es " + format(nu1) + ' + ' + format(nu2))
        respuesta = int(input())
        sum = nu1 + nu2
        if (respuesta == sum):
            print("Correcto")
        else:
            print("Incorrecto, la respuesta correcta es: " + format(sum))
    elif (operador == '-'):
        print("Cuanto es " + format(nu1) +' - '+ format(nu2))
        respuesta = int(input())
        res = nu1 - nu2
        if (respuesta == res):
            print("Correcto")
        else:
            print("Incorrecto, la respuesta correcta es: " + format(res))
    elif (operador == '*'):
        print("Cuanto es " + format(num1) +' * '+ format(num2))
        respuesta = int(input())
        mul = num1 * num2
        if (respuesta == mul):
            print("Correcto")
        else:
            print("Incorrecto, la respuesta correcta es: " + format(mul))
input()

#       Desenredar el espaguetti:
#           Buscar alternativa en python a case/switch                                                      ?
#           Implementar funciones abstractas para limpiar este desorden                                     ?
#           Probar una clase "operación" y objetos "suma", "resta" y "multiplicación" (encapsulamiento).    ?
#       Reimplementar el sistema de puntaje