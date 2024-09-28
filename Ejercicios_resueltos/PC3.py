def printf(string="c/c++>python", number=""):
    if number:
        print(f"{string} {number}")
    else:
        print(f"{string}")

def process_names():
    x = 0
    y = 0
    while True:
        nombre = input("Nombre: ")
        if nombre == "":
            break
        peso = 10                                   # valor por defecto para evitar el NameError
        while peso < 50 or peso > 120:
            peso = float(input("Peso: "))
        if peso < 80:
            x = x + 1
        elif peso >= 80:
            y = y + 1
    if x == 0:
        printf("Llave vacía")
    else:
        i = 1
        j = 2
        while True:
            if i >= x:
                printf("Categoría -80: llave de", j)
                break
            i = i * 2
            j = i

    if y == 0:
        printf("Llave vacía")
    else:
        i = 1
        j = 2
        while True:
            if i >= y:
                printf("Categoría +80: llave de", j)
                break
            i = i * 2
            j = i
process_names()