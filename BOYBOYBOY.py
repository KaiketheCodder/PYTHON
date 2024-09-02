n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())

media = (n1 + n2 + n3 + n4)/4

if (media == 10):
    print("Aluno passou com distinção! TA DE FERIAS PORRA")
elif (media >= 7 and media < 10):
    print("Passou, ta bão")
else:
    print("Reprovado meu consagrado, de volta para os estudos!")