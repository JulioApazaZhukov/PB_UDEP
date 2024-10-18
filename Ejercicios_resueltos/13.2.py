while True:
	año1 = int(input('Ingrese el año:'))
	if año1>=1900 and año1<2100:
		break

bisiesto1=0
if año1%4==0 and (año1%100!=0 or año1%400==0):
	bisiesto1=1

while True:
	mes1 = int(input('Ingrese el mes:'))
	if mes1>=1 and mes1<=12:
		break

diasMes1 = [31,28+bisiesto1,31,30,31,30,31,31,30,31,30,31]

while True:
	dia1 = int(input('Ingrese el día:'))
	if dia1>=1 and dia1<= diasMes1[mes1-1]:
		break


while True:
	año2 = int(input('Ingrese el año:'))
	if año2>=año1 and año2<2100:
		break

bisiesto2=0
if año2%4==0 and (año2%100!=0 or año2%400==0):
	bisiesto2=1

while True:
	mes2 = int(input('Ingrese el mes:'))
	if año1 < año2 and mes2>=1 and mes2<=12:
		break
	if año1 == año2 and mes2>=mes1 and mes2<=12:
		break


diasMes2 = [31,28+bisiesto2,31,30,31,30,31,31,30,31,30,31]

while True:
	dia2 = int(input('Ingrese el día:'))
	if año1<año2 and dia2>=1 and dia2<= diasMes2[mes2-1]:
		break
	if año1==año2 and mes1<mes2 and dia2>=1 and dia2<= diasMes2[mes2-1]:
		break
	if año1==año2 and mes1==mes2 and dia2>=dia1 and dia2<= diasMes2[mes2-1]:
		break

if año1==año2:
	if mes1==mes2:
		if dia1==dia2:
			diferencia = 0
		else:
			diferencia = dia2-dia1
	else:

		d1 = diasMes1[mes1-1] - dia1

		d2=0
		for m in range(mes1+1,mes2):
			d2 += diasMes1[m-1]

		d3 = dia2

		diferencia = d1+d2+d3

else:

	d1 = diasMes1[mes1-1] - dia1
	for m in range(mes1+1,13):
		d1 += diasMes1[m-1]

	d2 = 0
	for a in range(año1+1,año2):
		d2 += 365
		if a%4==0 and (a%100!=0 or a%400==0):
			d2 += 1

	d3 = 0
	for m in range(1,mes2):
		d3 += diasMes2[m-1]
	d3 += dia2

	diferencia = d1+d2+d3

print('La diferencia de dias es',diferencia)