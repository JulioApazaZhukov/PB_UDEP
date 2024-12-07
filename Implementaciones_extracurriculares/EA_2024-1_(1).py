precios = [4, 5, 10, 16, 20]
nombres_desayunos = ["Económico", "Universitario", "Americano", "Continental", "Completo"]

ventas_semanales = [0] * len(precios)
ventas_diarias = []

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes"]

for dia in dias_semana:
    print(f"\n--- Ventas del {dia} ---")
    ventas_dia = [0] * len(precios)
    for i in range(len(precios)):
        valido = False
        while not valido:
            cantidad = input(f"Ingrese la cantidad de desayunos {nombres_desayunos[i]} vendidos: ")
            if cantidad.isdigit():
                cantidad = int(cantidad)
                if cantidad >= 0:
                    valido = True
                    ventas_dia[i] = cantidad
                else:
                    print("Error: La cantidad no puede ser negativa. Intente nuevamente.")
            else:
                print("Error: Ingrese un número válido. Intente nuevamente.")
    ventas_diarias.append(ventas_dia)
    for i in range(len(precios)):
        ventas_semanales[i] += ventas_dia[i]

total_por_dia = []
for ventas_dia in ventas_diarias:
    total_dia = 0
    for i in range(len(precios)):
        total_dia += ventas_dia[i] * precios[i]
    total_por_dia.append(total_dia)

total_semanal = 0
for total in total_por_dia:
    total_semanal += total

promedio_por_dia = total_semanal / len(dias_semana)

print("\nVentas semanales por desayuno:")
for i in range(len(precios)):
    print(f"{nombres_desayunos[i]}: {ventas_semanales[i]} unidades")

print("\nTotal vendido (en soles) por día:")
for i in range(len(dias_semana)):
    print(f"{dias_semana[i]}: S/{total_por_dia[i]:.2f}")

print(f"\nTotal vendido en la semana: S/{total_semanal:.2f}")
print(f"Promedio diario de ventas: S/{promedio_por_dia:.2f}")

print("\nDesayuno más vendido y segundo más vendido por día:")
for dia_idx in range(len(dias_semana)):
    ventas_dia = ventas_diarias[dia_idx]
    
    ordenados_idx = []
    for _ in range(len(ventas_dia)):
        mayor_idx = -1
        mayor_venta = -1
        for i in range(len(ventas_dia)):
            if i not in ordenados_idx and ventas_dia[i] > mayor_venta:
                mayor_idx = i
                mayor_venta = ventas_dia[i]
        ordenados_idx.append(mayor_idx)

    mas_vendido = nombres_desayunos[ordenados_idx[0]]
    segundo_mas_vendido = "Ninguno" if ventas_dia[ordenados_idx[1]] == 0 else nombres_desayunos[ordenados_idx[1]]

    print(f"{dias_semana[dia_idx]}:")
    print(f"- Más vendido: {mas_vendido}")
    print(f"- Segundo más vendido: {segundo_mas_vendido}")
