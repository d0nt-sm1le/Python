aluno = dict()
aluno['nome'] = str(input("Qual é o nome do aluno? ")).capitalize()
aluno['nota'] = float(input(f"Qual é a média de {aluno['nome']}? "))

print("-=" * 20)
print(f"\t- Nome igual a {aluno['nome']}")
print(f"\t- Nota igual a {aluno['nota']}")

if aluno['nota'] > 7:
    aluno['estado'] = 'aprovado'

elif aluno['nota'] >= 5:
    aluno['estado'] = 'recuperação'

elif aluno['nota'] < 5:
    aluno['estado'] = 'reprovado'

print(f"\t- O estado atual é de {aluno['estado']}")
