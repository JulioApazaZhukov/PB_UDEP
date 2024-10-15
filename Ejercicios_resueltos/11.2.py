print('primera fecha')

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
	año2 = int(input('Ingrese año:'))
	if año2>año1 and año2<2100:
		break

bisiesto2 = 0
if año2%4==0 and (año2%100!=0 or año2%400==0):
	bisiesto2 = 1

while True:
	mes2 = int(input('Ingrese mes:'))
	if mes2>=1 and mes2<=12:
		break

if mes2==2:
	numdias2=28+bisiesto2
elif mes2==4 or mes2==6 or mes2==9 or mes2==12:
	numdias2=30
else:
	numdias2=31

while True:
	dia2 = int(input('Ingrese dia:'))
	if dia2>=1 and dia2<=numdias2:
			break

sumaDias = numdias1-dia1 
for m in range(mes1+1,13):
	if m==2:
		sumaDias += 28 + bisiesto1
	elif m==4 or m==6 or m==9 or m==11:
		sumaDias += 30
	else:
		sumaDias += 31	

for a in range(año1+1,año2):
	if a%4==0 and (a%100!=0 or a%400==0):
		sumaDias += 366
	else:
		sumaDias += 365


for m in range(1,mes2):
	if m==2:
		sumaDias += 28 + bisiesto2
	elif m==4 or m==6 or m==9 or m==11:
		sumaDias += 30
	else:
		sumaDias += 31
sumaDias = sumaDias + dia2

print('la diferencia de días es:',sumaDias)