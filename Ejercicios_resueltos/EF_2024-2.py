def bisiesto(año):
  return año%4==0 and (año%100!=0 or año%400==0)
def diasAño(año):
  return 365+bisiesto(año)
def diasMes(mes,año):
  diasMes = [31,28+bisiesto(año),31,30,31,30,31,31,30,31,30,31]
  return diasMes[mes-1]
def diasEmpezoAño(dia,mes,año):
  d = dia
  for m in range(1,mes):
    d += diasMes(m,año)
  return d
def diasFinAño(dia,mes,año):
  return diasAño(año)-diasEmpezoAño(dia,mes,año)

def calculoFecha(dias):
  años = dias//365
  if años>0:
    dias -= años*365
  meses = dias//30
  if meses>0:
    dias -= meses*30
  return [años,meses,dias]

def separarFecha(fecha):
  # fecha en formato año-mes-dia
  datosFecha = []
  while fecha.find('-')>-1:
    pos = fecha.find('-')
    dato = int(fecha[:pos])
    datosFecha.append(dato)
    fecha = fecha[pos+1:]
  datosFecha.append(int(fecha))
  return datosFecha

def pregunta1(fecha1,fecha2):

  lista1 = separarFecha(fecha1)
  lista2 = separarFecha(fecha2)

  if lista1>lista2:
    lista1,lista2 = lista2,lista1

  año1,mes1,dia1 = lista1[0],lista1[1],lista1[2]
  año2,mes2,dia2 = lista2[0],lista2[1],lista2[2]

  if año1==año2:
    if mes1==mes2:
      d = dia2-dia1
    else:
      d = diasMes(mes1,año1)-dia1
      for m in range(mes1+1,mes2):
        d += diasMes(m,año1)
      d += dia2

  else:
    d = diasFinAño(dia1,mes1,año1) + diasEmpezoAño(dia2,mes2,año2)
    for a in range(año1+1,año2):
      d += 365+bisiesto(a)

  return calculoFecha(d)

def pregunta2(fecha,e,c):

  fecha = separarFecha(fecha)
  año,mes,dia = fecha[0],fecha[1],fecha[2]

  if c=='d':
    dia = dia+e
    while dia>diasMes(mes,año):
      dia -= diasMes(mes,año)
      mes += 1
      if mes>12:
        mes = 1
        año += 1
  elif c=='m':
    mes = mes+e
    while mes>12:
      mes -= 12
      año += 1
  elif c=='a':
    año = año+e
  return [año,mes,dia]

def pedirNum(msj,min,max):
  while True:
    num = input(msj)
    if num.isdigit():
      num = int(num)
      if num>=min and num<=max:
        return num
def pedirFecha(msj):
  print(msj)
  año = pedirNum('Ingrese año:',1900,2099)
  mes = pedirNum('Ingrese mes:',1,12)
  dia = pedirNum('Ingrese día:',1,diasMes(mes,año))
  return str(año)+"-"+str(mes)+"-"+str(dia)
def pedirTexto(msj,valores):
  while True:
    texto = input(msj).strip()
    if texto in valores:
      return texto

# pregunta 3

while True:
  print()
  print('MENÚ')
  print('a. Diferencia de fechas')
  print('b. Suma de fechas')
  print('c. Salir')
  op = input('Ingrese una opción: ')
  if op == 'c':
    break
  elif op == 'a':
    print('Diferencia de fechas')
    fecha1 = pedirFecha('Fecha 1')
    fecha2 = pedirFecha('Fecha 2')
    diferencia = pregunta1(fecha1,fecha2)
    print('La diferencia de fechas es',diferencia)
  elif op == 'b':
    print('Suma de fechas')
    fecha = pedirFecha('Fecha')
    cantidad = pedirNum('Ingrese cantidad a sumar:',1,1000)
    unidades = pedirTexto('Ingrese unidades (d,m o a):',['d','m','a'])
    nuevaFecha = pregunta2(fecha,cantidad,unidades)
    print('La nueva fecha es',nuevaFecha)
  else:
    print('Opción inválida')