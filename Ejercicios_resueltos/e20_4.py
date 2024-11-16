def correo_valido(correo):
    
    arroba_pos = -1
    for i in range(len(correo)):
        if correo[i] == "@":
            if arroba_pos != -1:
                return False
            arroba_pos = i 
    if arroba_pos == -1: 
       return False
    
    usuario=correo[:arroba_pos]
    dominio=correo[arroba_pos+1:]

    if len(usuario) < 3 or not usuario[0].isalpha():
        return False

    if len(dominio) < 6 or not dominio[0].isalpha():
        return False

    extensiones_validas = [".com", ".net", ".org", ".edu", ".pe"]

    if not all(c.isalpha() or c.isdigit() or c == "." for c in dominio):
        return False

    if dominio[-4:] in extensiones_validas or dominio[-3:] == ".pe":
        return True
    
    return False

while True:
    correo = input("Ingrese un correo electronico: ").strip()
    if correo_valido(correo):
        print("El correo es valido")
    else:
        print("El correo no es valido")