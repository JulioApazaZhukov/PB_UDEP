programa = input('Ingrese su programa académico: ')

if programa == 'IIS' or programa == 'ADS' or programa == 'PSI' or programa == 'DER' or programa == 'ADE' or programa == 'MED' or programa == 'ECO' or programa == 'HYG':
    if programa == 'IIS' or programa == 'ADS' or programa == 'PSI' or programa == 'DER':
        print('Debe presentarse a las 11am')
    else:
        print('Debe presentarse a las 12pm')
else:
    print('Ingrese un programa valido')