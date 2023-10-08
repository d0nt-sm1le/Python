from random import randint

alunos = [str(input("Primeiro aluno: ")), str(input("Segundo aluno: ")),
          str(input("Terceiro aluno: ")), str(input("Quarto aluno: "))]
sorteado = randint(0, 4)

print(f"O aluno sorteado foi {alunos[sorteado]}")
