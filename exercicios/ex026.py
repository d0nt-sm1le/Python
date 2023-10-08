casa = int(input("Quanto é o valor da casa? "))
s1 = int(input("Salario do comprador: "))
a1 = int(input("Quantos anos de financiamento? "))
re1 = casa / (a1 * 12)
re2 = (30 * s1) / 100

if re1 >= re2:
    print(f"Para pagar uma casa de \033[34R${casa}\033[m em \033[34m{a1}\033[m a prestação será de \033[34mR${re1:.2f}\033[m!")
    print(f"Empréstimo \033[31mNEGADO\033[m")
else:
    print(f"Para pagar uma casa de \033[34mR${casa}\033[m em \033[34m{a1}\033[m a prestação será de \033[34mR${re1:.2f}\033[m!")
    print(f"Empréstimo pode ser \033[32mCONCEDIDO\033[m")
