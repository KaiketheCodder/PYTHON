sex = int(input("Qual o seu salário atual?: "))

if (sex <= 280):
    print("Seu salário é:", sex, "Portanto você receberá 20% de aumento, ou seja, Seu novo salário é:", sex*1.20)
elif (sex > 280 and sex < 700):
    print("Seu salário é:", sex, "Portanto você receberá 15% de aumento, Seu novo salário é:", sex*1.15)
elif (sex > 700 and sex < 1500):
    print("Seu salário é:", sex, "Portanto você receberá 10% de aumento, Seu novo salário é:", sex*1.10)
elif (sex > 1500):
    print("Seu salário é:", sex, "Portanto você receberá 5% de aumento, Seu novo salário é:", sex*1.05)


