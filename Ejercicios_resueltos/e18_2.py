while True:
    t = input("Ingrese el texto: ").strip()
    if t != '' and t.find('  ') == -1 and t.find(' ') != -1: break
while True:
    p = input('Ingrese una palabra: ').strip()
    if t.find(p) != -1: break
c = 0 
while t.find(p) != -1:
    pos  = t.find(p)
    t = t[pos+len(p):]
    c += 1
print(f"La palabra {p} aparece {c} veces")