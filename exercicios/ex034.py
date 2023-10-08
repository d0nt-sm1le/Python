from time import sleep
import random

print("Sua opções ")
print("[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura")

pl = int(input("Qual é a sua jogada? "))
jogada = ('Pedra', 'Papel', 'Tesoura')
pc = random.randint(0, 2)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")

print("=-" * 20)
print(f"O computador jogou {jogada[pc]}")
print(f"O jogador jogou {jogada[pl]}")
print("=-" * 20)

if pl == 0:
    if pc == 0:
        print("\033[33mEMPATE!\033[m")

    elif pc == 1:
        print("O jogador \033[31mPERDEU\033[m!")

    else:
        print("O jogador \033[32mVENCEU\033[m!")
elif pl == 1:
    if pc == 0:
        print("O jogador \033[32mVENCEU\033[m!")

    elif pc == 1:
        print("\33[33mEMPATE!\033[m")

    else:
        print("O jogador \033[31mPERDEU\033[m")
elif pl == 2:
    if pc == 0:
        print("O jogador \033[31mPERDEU\033[m")
    elif pc == 1:
        print("O jogador \033[32mVENCEU\033[m!")
    else:
        print("\033[33mEMPATE!\033[m")
