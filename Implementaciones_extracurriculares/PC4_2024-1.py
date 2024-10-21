fechas_entrega = []
fechas_correccion = []
cant_de_trabajos = 8 #Sugiero cambiar el valor por 2 o 3 para las pruebas

'''
Los requerimientos finales son:
1. Todas las fechas leídas deben pertenecer al mismo año.
2. El año está definido por la primera fecha que se lee.
3. Todas las fechas se deben pedir completas (año, mes y día).
4. Todos los datos leídos deben validarse.
Lo normal, considerando los req. 1 y 2, sería recibir la entrada "año" y validar si es bisiesto fuera del bucle de mes y día de entrega de datos. Sin embargo, el requerimiento 3 indica que se debe de solicitar el año en cada entrada de fecha y asegurarse de que sea el mismo siempre.
'''

for i in range(cant_de_trabajos):
    while True:
            año = int(input(f'Ingrese el año de entrega del trabajo: '))
            if i == 0:
                aux = año
                if año >= 1900 and año < 2100:
                    break
            else:
                if año >= 1900 and año < 2100 and año == aux:
                    break

    bisiesto = 0
    if año%4 == 0 and (año%100 != 0 or año%400 == 0):
        bisiesto = 1

    diasMes = [31, 28+bisiesto, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    while True:
        mes = int(input(f'Ingrese el mes de entrega del trabajo #{i+1}:'))
        if mes >= 1 and mes <= 12:
            break

    while True:
        dia = int(input(f'Ingrese el día de entrega del trabajo #{i+1}:'))
        if dia >= 1 and dia <= diasMes[mes - 1]:
            break
    #En cada entrada de datos, mes y día son agregados a la matriz "fechas_entrega" en su respectivo arreglo
    fechas_entrega.append([año, mes, dia])
    # "append" agrega un elemento al final del arreglo; en este caso el elemento es un arreglo que contiene "año", "mes" y "dia".
    print(fechas_entrega) #Esta línea no es parte del código original; la agrego únicamente por motivos de depuración (para visualizar los arreglos y asegurarme de que esté todo en orden)

for i in range(cant_de_trabajos):
    while True:
        dias_correccion = int(input(f'Ingrese los días de corrección para el trabajo #{i+1} (máx 15 días): '))
        if 1 <= dias_correccion <= 15:
            dia_corregido = fechas_entrega[i][2] + dias_correccion
            mes_corregido = fechas_entrega[i][1]
            año_corregido = fechas_entrega[i][0]
            #La matriz es bidimencional; el primer índice le corresponde al número de fila (m de matriz m*n).
            #En este caso, el número de fila representa el número de trabajo (i = 0 -> trabajo 1, i = 6 -> trabajo 7).

            #El siguiente código se encargará de incrementar el mes y el año en el caso de que sea necesario: Se entrega cerca al fin de mes y se corrige al mes siguiente, o se entrega a fin de año y se corrige el primer mes del año siguiente.
            #Recibido 1/12/2020 Corregido 16/12/2020
            #Recibido 29/5/2020 Corregido 12/6/2020
            #Recibido 28/2/2020 Corregido 12/3/2020
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