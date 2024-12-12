def contar_involucrados(denuncia):
    dnis = []
    palabra = ""

    for caracter in denuncia:
        if caracter.isdigit():
            palabra += caracter
        else:
            if len(palabra) == 8 and palabra[0] in '01467':
                if palabra not in dnis:
                    dnis.append(palabra)
            palabra = ""

    if len(palabra) == 8 and palabra[0] in '01467':
        if palabra not in dnis:
            dnis.append(palabra)

    return len(dnis)

denuncia = input("Ingrese el texto de denuncia: ")
print(f"Total de involucrados: {contar_involucrados(denuncia)}")
