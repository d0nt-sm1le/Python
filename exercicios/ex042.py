from random import randint
cp = randint(0, 10)

print("""Seu computador: 
Acabei de pensar em número entre 0 e 10!
Será que você consegue adivinhar qual foi? """)
pl = int(input("Qual é o seu palpite? "))

while pl != cp:
    if pl < cp:
        print("Mais... Tente mais uma vez.")
        pl = int(input("Qual é o seu palpite? "))
    else:
        print("Menos...Tente mais uma vez.")
        pl = int(input("Qual é o seu palpite? "))

print("Acetou miseravi!")
