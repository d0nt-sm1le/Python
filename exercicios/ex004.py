from datetime import date

nascimento = int(input("Ano de nascimento: "))
genero = str(input("Você é homem ou mulher? "))
print("-=" * 30)
ano = date.today().year
re = ano - nascimento
re1 = 18 - re

if genero == "mulher":
    print("Você não precisa fazer alistamento militar obrigatório!")
    x = str(input("Você deseja fazer mesmo assim? "))
    print("-=" * 30)
    if x == "sim":
        if re == 18:
            print(f"Quem nasceu em {nascimento} tem {re} anos.")
            print(f"Você já pode se alistar")
            print("-=" * 30)

        elif re < 18:
            print(f"Quem nasceu em {nascimento} tem {re} anos.")
            print(f"Ainda faltam {re1} anos para seu alistamento")
            print(f"Seu alistamento será em {ano + re1}")
            print("-=" * 30)

        else:
            print(f"Quem nasceu em {nascimento} tem {re} anos.")
            print(f"Era para você ter se alistado em {ano + re1}")
            print("-=" * 30)

elif genero == "homem":
    if re == 18:
        print(f"Quem nasceu em {nascimento} tem {re} anos.")
        print(f"Você tem que se alistar imediantamente!")
        print("-=" * 30)

    elif re < 18:
        print(f"Quem nasceu em {nascimento} tem {re} anos.")
        print(f"Ainda faltam {re1} anos para seu alistamento")
        print(f"Seu alistamento será em {ano + re1}")
        print("-=" * 30)

    else:
        print(f"Quem nasceu em {nascimento} tem {re} anos.")
        print(f"Já era para você ter se alistado em {ano + re1}")
        print("-=" * 30)

else:
    print(f"Valor invalido, tente novamente")
    print("-=" * 30)
