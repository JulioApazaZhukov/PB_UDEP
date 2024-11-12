def contar_palabras(t):
    c = 1
    while t.find(' ') != -1:
        pos = t.find(' ')
        t = t[pos+1:]
        c += 1
    return c

def texto_valido(t):
    return t!= '' and t.find('  ') == -1 and contar_palabras(t) >= 3

while True:
    texto = input("Ingrese un texto de al menos 10 palabras: ").strip()
    if texto_valido(texto): break
print(f"El texto contiene {contar_palabras(texto)} palabras")