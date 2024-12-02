def validarAños():
    año = int(input("Año: "))
    if año >= 1900 and año < 2100:
        return año
    else: 
        print("Año no valido")
        return validarAños()

def validarMes():
    mes = int(input("Mes: "))
    if mes >= 1 and mes <= 12:
        return mes
    else: 
        print("Mes no valido")
        return validarMes()

def validarDias(mes, año):
    dia = int(input("Día: "))
    if mes == 2:
        if año%4 == 0 and (año%100 != 0 or año%400 != 0):
            numDias = 29
        else:
            numDias = 28
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        numDias = 30
    else: 
            numDias = 31
    if dia >= 1 and dia <= numDias:
        if mes >= 10:
            print("Fecha valida: ", dia, "-", mes, "-", año)
        else: 
            strMes = str(mes)
            print("Fecha valida: ", dia, "- 0" + strMes, "-", año)
    else: 
        print("Día no valido")
        return validarDias(mes, año)

a = validarAños()
m = validarMes()
validarDias(m, a)