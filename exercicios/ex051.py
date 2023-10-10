from datetime import date

trabalhador = dict()
trabalhador['nome'] = str(input("Nome: ")).capitalize()
trabalhador['idade'] = int(input("Ano que você nasceu: "))
trabalhador['Carteira'] = int(input("Carteira de trabalho (0 não tem): "))

if trabalhador['Carteira'] != 0:
    trabalhador['Contratação'] = int(input("Ano de contratação: "))
    trabalhador['salario'] = int(input("Salario: "))

ano = date.today().year
idade = ano - trabalhador['idade']

print("-=" * 20)
print(f"\t - Nome é igual a {trabalhador['nome']}")
print(f"\t - idade tem valor igual a {idade}")
print(f'\t - ctps é igual a {trabalhador['Carteira']}')


if trabalhador['Carteira'] != 0:
    print(f"\t - Contratação feita em {trabalhador['Contratação']}")
    print(f'\t - sálario tem o valor de {trabalhador['salario']}')