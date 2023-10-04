ex = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'deis',
      'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

y = True

while y:
    n = int(input("Digite um número de 0 a 20: "))

    if 0 <= n <= 20:
        print(f"Você digitou o número {ex[n]}")
    else:
        print("Tente novamente.", end=" ")

    x = str(input("\nVocê quer continuar?[S/N] ")).lower()

    if x == 's':
        pass
    elif x == 'n':
        y = False
    else:
        print("tente novamente: ")
