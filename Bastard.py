def funcional(): #Para criarmos uma função, usamos def (Nome da função)():
    print("Hello World!")

def jorge(num1m, num2):
    print("OH PORRA CARALHO")
    funcional()#Uma função pode ser chamada de dentro de uma outra função

nome = input("Qual o seu nome?")
print(nome)

print("HAHAHHAHHAA")
funcional()#Para chamarmos uma função, apenas devemos copiar o nome dela com () e sem def.
print("Sua CALCINHA caiu!")
funcional()#temos a possibilidade de usar uma mesma função várias vezes, o quanto quisermos 
jorge(nome)

