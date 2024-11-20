def leerNum(mensaje,min,max):
	while True:
		x = input(mensaje).strip()
		if x.isdigit():
			x = int(x)
			if x >= min and x <= max:
				return x

def bisiesto(a):
	return a % 4 == 0 and (a % 100 != 0 or a % 400 == 0)

def numDias(m,a):
	numDias = [31,28 + bisiesto(a),31,30,31,30,31,31,30,31,30,31]
	return numDias[m-1]

def leerFecha(mensaje):
    print(mensaje)
    año = leerNum("Ingrese año:",1900,2099)
    mes = leerNum("Ingrese mes:",1,12)
    dia = leerNum("Ingrese dia:",1,numDias(mes,año))
    return [año,mes,dia]

def fechaMayor(fecha1,fecha2):
	if fecha1>fecha2:
		return fecha1
	else:
		return fecha2

def diasEntre(año1,año2):
	dias = 0
	for i in range(año1,año2+1):
		dias += 365 + bisiesto(i)
	return dias

def diasTranscurridos(fecha):
	d = fecha[2]
	m = fecha[1]
	a = fecha[0]
	dias=0
	for i in range(1,m):
		dias += numDias(i,a)
	return dias+d 

fecha1 = leerFecha("Primera fecha")
fecha2 = leerFecha("Segunda fecha")
if fecha1 != fecha2:
	if fecha1 == fechaMayor(fecha1,fecha2):
		fecha1, fecha2 = fecha2, fecha1

if fecha1[0] == fecha2[0]:
	total_dias = diasTranscurridos(fecha2)-diasTranscurridos(fecha1)
else:
	dias1 = 365 + bisiesto(fecha1[0]) - diasTranscurridos(fecha1)
	dias2 = diasEntre(fecha1[0] + 1,fecha2[0] - 1)
	dias3 = diasTranscurridos(fecha2)
	total_dias = dias1 + dias2 + dias3

print(f"La diferencia de dias entre {fecha1} y {fecha2} es {total_dias}")