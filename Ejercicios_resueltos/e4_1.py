nombre = str(input("Ingrese su nombre"))
apellido = str(input("Ingrese su apellido"))
edad = int(input("Ingrese su edad"))
añoDeGraduacion = int(input("Ingrese el año en el que termino el colegio"))
certificacion = str(input("Su colegio esta certificado?"))
quintoSup = str(input("Es quinto superior?"))

if añoDeGraduacion >= 2025:
    print('Le corresponde simulacion de examen de admición')
else:
    if edad >= 18:
        print('Requisitos')
        print('Antecedentes penales')
        print('Libreta de secundaria')
        print('Le corresponde el de examen de admición')
    else: 
        if añoDeGraduacion == 2022:
            print('Requisitos')
            print('Libreta de secundaria')

        elif añoDeGraduacion == 2023:
            
            if certificacion == 'si' and quintoSup == 'si':
                print('Ingreso directo')
            elif certificacion == 'si' and quintoSup == 'no':
                print('Le corresponde el de examen de admición')
            elif certificacion == 'no':
                print('Le corresponde el de examen de admición')

        elif añoDeGraduacion == 2024:
            if certificacion == 'si' and quintoSup == 'si':
                print('Ingreso directo')
            elif certificacion == 'si' and quintoSup == 'no':
                print('Le corresponde el de examen de admición')
            elif certificacion == 'no':
                print('Le corresponde el de examen de admición')