while True:
    año1 = int(input('Ingrese el año: '))
    if año1 >= 1900 and año1 < 2100:
        break
    else: print("Año no valido")

while True:
    mes1 = int(input('Ingrese el mes: '))
    if mes1 >= 1 and mes1 <= 12:
        break
    else: print("Mes no valido")

while True:
    dia1 = int(input('Ingrese el día: '))
    if mes1 == 2:
        if año1%4 == 0 and (año1%100 != 0 or año1%400 != 0):
            numDias = 29
        else:
            numDias = 28
    elif mes1 == 4 or mes1 == 6 or mes1 == 9 or mes1 == 11:
        numDias = 30
    else: 
            numDias = 31
    if dia1 >= 1 and dia1 <= numDias:
        if mes1 >= 10:
            print("Fecha valida: ", dia1, "-", mes1, "-", año1)
        else: 
            strMes = str(mes1)
            print("Fecha valida: ", dia1, "- 0" + strMes, "-", año1)
        break
    else: print("Día no valido")

while True:
    año2 = int(input('Ingrese el año: '))
    if año2 >= 1900 and año2 < 2100:
        break
    else: print("Año no valido")

while True:
    mes2 = int(input('Ingrese el mes: '))
    if mes2 >= 1 and mes2 <= 12:
        break
    else: print("Mes no valido")

while True:
    dia2 = int(input('Ingrese el día: '))
    if mes2 == 2:
        if año2%4 == 0 and (año2%100 != 0 or año2%400 != 0):
            numDias = 29
        else:
            numDias = 28
    elif mes2 == 4 or mes2 == 6 or mes2 == 9 or mes2 == 11:
        numDias = 30
    else: 
            numDias = 31
    if dia2 >= 1 and dia2 <= numDias:
        if mes2 >= 10:
            print("Fecha valida: ", dia2, "-", mes2, "-", año2)
        else: 
            strMes = str(mes2)
            print("Fecha valida: ", dia2, "- 0" + strMes, "-", año2)
        break
    else: print("Día no valido")

if año1 < año2:
    print("La segunda fecha es mayor que la primera")
elif año1 == año2 and mes1 < mes2:
    print("La segunda fecha es mayor que la primera")
elif año1 == año2 and mes1 == mes2 and dia2 > dia1:
    print("La segunda fecha es mayor que la primera")
else: print("Las fechas son iguales o la fecha 1 es mayor que la fecha dos")