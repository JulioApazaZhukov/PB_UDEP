while True:
    nombre = input("Ingrese su nombre:").strip()
    if nombre!='':
        if nombre[0] == nombre[0].upper():
            if nombre.find(' ')==-1:
                break
            
print(nombre)