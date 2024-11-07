while True:
    texto = input("Ingrese una oración: ").strip()
    if texto != '' and texto.find('  ') == -1:break
c = 1
while texto.find(' ') != -1:
    pos = texto.find(' ')
    texto = texto[pos+1:]
    c = c+1
print(f"En el texto hay {c} palabras")