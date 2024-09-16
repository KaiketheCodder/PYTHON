def some(n1,n2):##As duas entradas entre os parenteses ditam quantos inputs possiveis podem ser utilizados pela variavel, entretanto, eles não são obrigatoriamente iguais os nomes das variaveis a serem usadas.
    resultado = n1 + n2
    print(resultado)

num1 = int (input())
num2 = int (input())
some(num1, num2)##Aqui por exemplo, criamos as duas vars: Num1 e Num2, e usaremos essas duas para executar a função(Temos dois slots disponiveis para a função usar)




def analise(n1,n2):
    resultado = n1 + n2
    if n1 == n2:
        print("São iguais")
    elif n1 > n2:
        print("PQP")
    else:
        print("cu")

num1 = int (input())
num2 = int (input())
analise(num1, num2)




valor = str (input("Qual o Tipo de combustível gostaria? :"))
Litros = float(input("Quantos litros foram comprados? "))

Gas = 3.30 * 0.97 
Al = 2.90 * Litros


if valor == "g" or valor == "G" and Litros < 20:
    print("Seu total é: ", Gas*Litros)
elif valor == "g" or valor == "G" and Litros > 20:
    print("Seu total é: ", Gas, "Seu desconto é de 5%, portanto você deve: ", Gas - (0.05 * 100))
elif valor == "a" or valor == "A" and Litros < 20:
    print("Seu total é: ", Al, "Seu desconto é de 3%, portanto você deve: ", Al - (0.04 * 100))
elif valor == "a" or valor == "A" and Litros > 20:
    print("Seu total é: ", Al, "Seu desconto é de 5%, portanto você deve: ", Al - (0.06 * 100)) 

Homem1 = int(input()) 
Homem2 = int(input()) 
Mulher1 = int(input())
Mulher2 = int(input())

if Homem1 > Homem2: 
    print(Homem1)
    if Homem1 < Homem2: 
        print(Homem2)

elif Mulher1 > Mulher2: 
    print(Mulher1)
    if Mulher2 > Mulher1:
        print(Mulher2)

if Homem1 > Homem2 and Mulher1 > Mulher2:
    print(Homem2 * Mulher1)
    
elif Homem2 > Homem1 and Mulher2 > Mulher1:
        print(Homem1 * Mulher2)
