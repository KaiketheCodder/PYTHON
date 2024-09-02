turno = str(input("Em que turno você estuda? Digite V para vespertino, M para matutino e N para noturno: "))

if (turno == "M" or turno == "m"):
    print("Bom dia!")
elif (turno == "V" or turno == "v"):
    print("Boa tarde!")
elif (turno == "N" or turno == "n"):
    print("Boa noite!")
else:
    print(turno,"....Quando você estuda mano? Que horário é esse???")