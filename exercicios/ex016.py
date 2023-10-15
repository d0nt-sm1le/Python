from random import randint

alunos = [input("Primeiro aluno: "), input("Segundo aluno: "), input("Terceiro aluno: "), input("Quarto aluno: ")]
sorteio = randint(0, 3)

print(f"O aluno sorteado foi {alunos[sorteio]}")
