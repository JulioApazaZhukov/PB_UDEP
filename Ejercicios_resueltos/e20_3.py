def es_placa_valida(placa):
    contador_letras = 0
    contador_numeros = 0
    for i in range(len(placa)):
        if placa[i].isalpha(): contador_letras += 1
        elif placa[i].isdigit(): contador_numeros += 1

    return len(placa) == 6 and placa[0].isalpha() and placa[3:].isdigit() and (placa[1].isalpha() or placa[2].isalpha()) and contador_letras + contador_numeros == 6

while True:
    placa = input("Ingrese la placa del auto: ").strip()
    if es_placa_valida(placa): break

print(f"{es_placa_valida(placa)}")