añoDeNacimiento = int(input('Ingrese su año de nacimiento: '))
edad = 2024 - añoDeNacimiento

if edad > 0 and edad < 18:
    print('Primera')
elif edad >=18 and edad < 60:
    print('Segunda')
elif edad >=60 and edad < 100:
    print('Tercera')
else:
    print('Ingrese un valor valido')