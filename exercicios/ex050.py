from random import randint
from time import sleep
from operator import itemgetter

pl = {'jogador 1': randint(0, 5),
      'jogador 2': randint(0, 5),
      'jogador 3': randint(0, 5),
      'jogador 4': randint(0, 5)}
ranking = list

print("Resultados: ")
for x in range(1, 5):
    print(f"Jogador {x} tirou {pl[f'jogador {x}']}")
    sleep(1)

ranking = sorted(pl.items(), key=itemgetter(1), reverse=True)


print("=-" * 20)
print("\t== RANKING DO JOGADORES == ")
for p, v in enumerate(ranking):
    print(f"\t{p + 1}° lugar,{v[0]} tirou {v[1]}")
    sleep(1)
