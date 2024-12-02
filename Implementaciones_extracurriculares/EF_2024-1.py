def obtener_datos_fase_grupos():
    equipos = []
    for grupo in ['A', 'B', 'C', 'D', 'E', 'F']:
        print(f"\nIngrese datos para el grupo {grupo}")
        for i in range(4):
            print(f"\nEquipo {i+1}:")
            pais = input("Nombre del país: ").strip()
            partidos_ganados = int(input("Partidos ganados: "))
            partidos_empatados = int(input("Partidos empatados: "))
            goles_a_favor = int(input("Goles a favor: "))
            goles_en_contra = int(input("Goles en contra: "))

            puntos = partidos_ganados * 3 + partidos_empatados
            diferencia_goles = goles_a_favor - goles_en_contra

            equipos.append([grupo, pais, puntos, diferencia_goles, goles_a_favor])
    return equipos

def clasificar_a_octavos(equipos):
    clasificados = []
    terceros = []
    
    for grupo in ['A', 'B', 'C', 'D', 'E', 'F']:
        equipos_grupo = [equipo for equipo in equipos if equipo[0] == grupo]
        
        for i in range(len(equipos_grupo)):
            for j in range(len(equipos_grupo) - 1):
                if (equipos_grupo[j][2] < equipos_grupo[j + 1][2] or
                    (equipos_grupo[j][2] == equipos_grupo[j + 1][2] and
                     equipos_grupo[j][3] < equipos_grupo[j + 1][3]) or
                    (equipos_grupo[j][2] == equipos_grupo[j + 1][2] and
                     equipos_grupo[j][3] == equipos_grupo[j + 1][3] and
                     equipos_grupo[j][4] < equipos_grupo[j + 1][4])):
                    equipos_grupo[j], equipos_grupo[j + 1] = equipos_grupo[j + 1], equipos_grupo[j]

        clasificados.extend(equipos_grupo[:2])
        terceros.append(equipos_grupo[2])

    for i in range(len(terceros)):
        for j in range(len(terceros) - 1):
            if (terceros[j][2] < terceros[j + 1][2] or
                (terceros[j][2] == terceros[j + 1][2] and
                 terceros[j][3] < terceros[j + 1][3]) or
                (terceros[j][2] == terceros[j + 1][2] and
                 terceros[j][3] == terceros[j + 1][3] and
                 terceros[j][4] < terceros[j + 1][4])):
                terceros[j], terceros[j + 1] = terceros[j + 1], terceros[j]

    clasificados.extend(terceros[:4])
    return clasificados

def programar_partidos_octavos(clasificados):
    print("\nProgramación de partidos de octavos de final")
    partidos = []
    fechas_usadas = []

    for i in range(8):
        while True:
            print(f"\nPartido {i+1}: {clasificados[i][1]} vs {clasificados[15-i][1]}")
            fecha = int(input("Ingrese la fecha (día en julio 2024, entre 1 y 15): "))
            hora = input("Ingrese la hora (11am, 12pm, 1pm, 2pm, 3pm o 4pm): ").strip()
            clave_partido = (fecha, hora)

            if clave_partido in fechas_usadas:
                print("Error: Ya hay un partido programado en esa fecha y hora. Intente nuevamente.")
            else:
                fechas_usadas.append(clave_partido)
                partidos.append([clasificados[i][1], clasificados[15-i][1], fecha, hora])
                break
    return partidos

while True:
    equipos = obtener_datos_fase_grupos()
    clasificados = clasificar_a_octavos(equipos)
    
    print("\nEquipos clasificados a octavos de final:")
    for equipo in clasificados:
        print(f"{equipo[1]} - Puntos: {equipo[2]} - Diferencia de goles: {equipo[3]} - Goles a favor: {equipo[4]}")
    
    partidos_octavos = programar_partidos_octavos(clasificados)
    print("\nCalendario de partidos de octavos de final:")
    for partido in partidos_octavos:
        print(f"{partido[0]} vs {partido[1]} - Fecha: {partido[2]} - Hora: {partido[3]}")
    break