while True:
    año = int(input('Ingrese el año:'))
    if año>=1900 and año<2100:
        break

bisiesto=0
if año%4==0 and (año%100!=0 or año%400==0):
    bisiesto=1
while True:
    mes = int(input('Ingrese el mes:'))
    if mes>=1 and mes<=12:
        break

diasMes = [31,28+bisiesto,31,30,31,30,31,31,30,31,30,31]
while True:
    dia = int(input('Ingrese el día:'))
    if dia>=1 and dia<= diasMes[mes-1]:
        break
