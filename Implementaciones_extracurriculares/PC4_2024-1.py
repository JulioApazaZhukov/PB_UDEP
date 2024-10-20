fechas_entrega = []
fechas_correccion = []
diasMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
cant_de_trabajos = 8

while True:
        año = int(input(f'Ingrese el año de la fecha de entrega del trabajo: '))
        if año >= 1900 and año < 2100:
            break

bisiesto = 0
if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
    bisiesto = 1

for i in range(cant_de_trabajos):
    diasMes[1] = 28 + bisiesto
    while True:
        mes = int(input(f'Ingrese el mes de entrega del trabajo {i+1}:'))
        if mes >= 1 and mes <= 12:
            break

    while True:
        dia = int(input(f'Ingrese el día de entrega del trabajo {i+1}:'))
        if dia >= 1 and dia <= diasMes[mes - 1]:
            break

    fechas_entrega.append([año, mes, dia])

for i in range(cant_de_trabajos):
    while True:
        dias_correccion = int(input(f'Ingrese los días de corrección para el trabajo {i+1} (máx 15 días): '))
        if 1 <= dias_correccion <= 15:
            dia_corregido = fechas_entrega[i][2] + dias_correccion
            mes_corregido = fechas_entrega[i][1]
            año_corregido = fechas_entrega[i][0]

            if dia_corregido > diasMes[mes_corregido - 1]:
                dia_corregido -= diasMes[mes_corregido - 1]
                mes_corregido += 1
                if mes_corregido > 12:
                    mes_corregido = 1
                    año_corregido += 1
            
            fechas_correccion.append([año_corregido, mes_corregido, dia_corregido])
            break

print("\nFechas de entrega y corrección:")
for i in range(cant_de_trabajos):
    print(f"Recibido {fechas_entrega[i][2]}/{fechas_entrega[i][1]}/{fechas_entrega[i][0]} Corregido {fechas_correccion[i][2]}/{fechas_correccion[i][1]}/{fechas_correccion[i][0]}")
