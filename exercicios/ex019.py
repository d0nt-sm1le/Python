from random import randint
from time import sleep

print("=-" * 26)
print("Vou pensar em um número entre 0 e 5. Tente advinhar!")
print("=-" * 26)

sec = randint(0, 5)
numero = int(input("Em que número eu pensei? "))

print("Processando...")
sleep(3)

if sec == numero:
    print("Parabens você conseguiu me vencer!")
else:
    print(f"Ganhei! Eu pensei no número {sec} e não no {numero}!")
