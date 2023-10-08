from datetime import date

idade = int(input("Ano de nascimento: "))
ano = date.today().year
re = ano - idade

if re <= 9:
    print(f"O atleta tem {re} ano(s)")
    print(f"Classificação: MIRIM")

elif re <= 14:
    print(f"O atleta tem {re} ano(s)")
    print(f"Classificação: INFANTIL")

elif re <= 19:
    print(f"O atleta tem {re} ano(s)")
    print(f"Classificação: JÚNIOR")

elif re <= 25:
    print(f"O atleta tem {re} ano(s)")
    print(f"Classificação: SÊNIOR")

else:
    print(f"O atleta tem {re} ano(s)")
    print(f"Classificação: MASTER")
