i = 0
notaT = 0
notaM = 20
nota = 1
while i < 6:
    while True:
        nota = int(input('Ingrese la nota #' + str(i+1) + ':'))
        if nota >= 0 and nota <= 20:
            break
    notaT = notaT + nota
    if nota < notaM:
        notaM = nota
    i = i+1
resp = (notaT - notaM) / 5
print(resp)