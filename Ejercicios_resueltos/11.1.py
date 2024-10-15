print('Primera fecha')

while True:
    año1 = int(input('Ingrese año:'))
    if año1>=1900 and año1<2100:
        break

bisiesto1 = 0
if año1%4==0 and (año1%100!=0 or año1%400==0):
    bisiesto1 = 1

while True:
    mes1 = int(input('Ingrese mes:'))
    if mes1>=1 and mes1<=12:
        break

if mes1==2:
    numdias1=28+bisiesto1
elif mes1==4 or mes1==6 or mes1==9 or mes1==11:
    numdias1=30
else:
    numdias1=31

while True:
    dia1 = int(input('Ingrese dia:'))
    if dia1>=1 and dia1<=numdias1:
        break

print('segunda fecha')
while True:
    mes2 = int(input('Ingrese mes:'))
    if mes2>=mes1 and mes2<=12:
        break

if mes2==2:
    numdias2=28+bisiesto1
elif mes2==4 or mes2==6 or mes2==9 or mes2==11:
    numdias2=30
else:
    numdias2=31

while True:
    dia2 = int(input('Ingrese dia:'))
    if mes2>mes1 and dia2>=1 and dia2<=numdias2:
        break
    if mes2==mes1 and dia2>dia1 and dia2<=numdias2:
        break

if mes2>mes1:
    sumaDias = numdias1-dia1
    for m in range(mes1+1,mes2):
        if m==2:
            sumaDias += 28 + bisiesto1
        elif m==4 or m==6 or m==9 or m==11:
            sumaDias += 30
        else:
            sumaDias += 31
    sumaDias += dia2
else:
    sumaDias = dia2-dia1
print('entre las fechas hay',sumaDias,'dias')