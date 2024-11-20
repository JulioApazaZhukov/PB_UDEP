def leerNum(mensaje, min, max):
    while True:
        x = input(mensaje).strip()

def bisiesto(a):
    bisiesto = 0
    if a % 4 == 0 and (a % 100 != 0 or a % 400 == 0): bisiesto = 1
    return bisiesto

def num_Dias(m, a):
    numDias = [31,28+bisiesto(a),31,30,31,30,31,31,30,31,30,31]
    return numDias(m-1)

def leerFecha(mensage):
    año = leerNum("Ingrese año: ", 1900, 2100)
    mes = leerNum("Ingrese año: ", 1, 12)
    dia = leerNum("Ingrese año: ", 1, num_Dias(mes, año))
    return[dia, mes, año]

def fechaMayor(fecha1, fecha2):
    if fecha1 > fecha2: return fecha1
    else: return fecha2

fecha1 = leerFecha("Ingrese la primera fecha: ")
fecha2 = leerFecha("Ingrese la segunda fecha: ")
if fecha1 != fecha2:
    if fecha1 != fecha2:
        if fecha1 == fechaMayor(fecha1, fecha2):
            fecha1, fecha2 = fecha2, fecha1