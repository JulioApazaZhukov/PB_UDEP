# escriba un programa que lea 1 fecha 
# y calcule el día del año

while True:
	año = int(input('Ingrese el año:'))
	if año>=1900 and año<2100:
		break

bisiesto=0
if año%4==0 and (año%100!=0 or año%400==0):
	bisiesto = 1

while True:
	mes = int(input('Ingrese el mes:'))
	if mes>=1 and mes<=12:
		break

numDias = 31
if mes==2:
	numDias = 28+bisiesto
elif mes==4 or mes==6 or mes==9 or mes==11:
	numDias = 30

while True:
	dia = int(input('Ingrese el día:'))
	if dia>=1 and dia<=numDias:
		break

# supongamos que la fecha es 15/3/2024
# 31 (enero) + 29 (febrero) + 15 (marzo)

# 20/5/2024
# 31 + 29 + 31 + 30 + 20

sumaDias = 0
for m in range(1,mes):
	if m==2:
		sumaDias = sumaDias + 28 + bisiesto
	elif m==4 or m==6 or m==9 or m==11:
		sumaDias = sumaDias + 30
	else:
		sumaDias = sumaDias + 31
sumaDias = sumaDias + dia

print('El día del año es',sumaDias)