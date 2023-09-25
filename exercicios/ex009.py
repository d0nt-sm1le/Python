from time import sleep
import random

print("Sua opções ")
print("[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura")

jogador = int(input("Qual é a sua jogada? "))
pc = random.randint(1, 3)

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!\n")

print("==" * 20)

if jogador == 1:
    if pc == 1:
        print("O computador escolheu Pedra \nO jogador escolher Pedra")
        print("==" * 20)
        print("EMPATE!")

    elif pc == 2:
        print("O computador escolhou Papel \nO jogador escolheu Pedra")
        print("==" * 20)
        print("O jogador PERDEU!")

    else:
        print("O computador escolheu Tesoura \nO jogador escolheu Pedra")
        print("==" * 20)
        print("O jogador VENCEU")
elif jogador == 2:
    if pc == 1:
        print("O computador escolheu Pedra \nO jogador escolheu Papel")
        print("==" * 20)
        print("O jogador VENCEU!")

    elif pc == 2:
        print("O computador escolheu Papel \nO jogador escolheu Papel")
        print("==" * 20)
        print("EMPATE!")

    else:
        print("O computador escolheu Tesoura \nO jogador escolheu Papel")
        print("==" * 20)
        print("O jogador PERDEU")
elif jogador == 3:
    if pc == 1:
        print("O computador escolheu Pedra \nO jogador escolheu Tesoura")
        print("==" * 20)
        print("O jogador PERDEU")
    elif pc == 2:
        print("O computador escolheu Papel \nO jogador escolheu Tesoura")
        print("==" * 20)
        print("O jogador VENCEU")
    else:
        print("O computador escolheu Tesoura \nO jogador escolheu Tesoura")
        print("==" * 20)
        print("EMPATE!")
