curso = input('Ingrese el curso en el que desea matricularse:')
if curso == 'AGT':
    curso_req = 'PB'
    ciclo_req = 4
    creditos_req = 50
    creditos = 4
elif curso == 'BD':
    curso_req = 'PB'
    ciclo_req = 6
    creditos_req = 90
    creditos = 5
elif curso == 'ADS':
    curso_req = 'PB'
    ciclo_req = 7
    creditos_req = 90
    creditos = 4
elif curso == 'ID':
    curso_req = 'BD'
    ciclo_req = 8
    creditos_req = 140
    creditos = 4
elif curso == 'DTI':
    curso_req = 'ID'
    ciclo_req = 10
    creditos_req = 190
    creditos = 6
else:
    print('Puede matricularse en',curso)
    curso = 'otro'
if curso != 'otro':
    ciclo = int(input('En qué ciclo está?'))
    creditos_aprobados = int(input('Cuántos créditos aprobados tiene?'))
    llevo_req = input('Ya llevó el requisito ' + curso_req + '?')
    if llevo_req == 'si':
        promedio_req = int(input('Con qué promedio lo dejó?'))
    else:
        promedio_req = 0
        hay_cruce = input('Hay cruce de horas?')
    if hay_cruce == 'si':
        horas_cruce = int(input('Cuántas horas hay de cruce?'))
    else:
        horas_cruce = 0
    if promedio_req >= 10 and ciclo >= ciclo_req and creditos_aprobados >= creditos_req and horas_cruce < 0.5*creditos :
        print('Puede matricularse en',curso)
else:
    print('No puede matricularse en',curso)