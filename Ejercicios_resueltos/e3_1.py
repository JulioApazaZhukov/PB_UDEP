age = int(input("Ingrese su edad: "))

if age >=30:
    dosis = int(input("Ingrese el numero de dosis: "))
    if dosis == 1:
        print("Le toca Sinopharm")
    elif dosis == 2:
        userInput = str(input("Ingrese vacuna: "))
        if userInput == "Pfizer" or userInput == "Sinopharm":
            print("Le toca 2da dosis de ", userInput)
        else:
            print("No es una vacuna valida")
    else:
        print("No es una dosis valida")