from time import sleep


def contagem(a, b, c):
    print("--" * 20)
    print(f"Contagem de {a} até {b}, pulando de {c} em {c}")
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont}', end=" ")
            sleep(0.5)
            cont += c
    else:
        cont = a
        while cont >= b:
            print(f"{cont}", end=" ")
            sleep(0.5)
            cont -= c

    print(f"FIM!")


contagem(0, 10, 1)
contagem(10, 0, 2)

print("Agora é sua vez de personalizar as contagens!")
n1 = float(input("Inicio: "))
n2 = float(input("Fim: "))
n3 = float(input("Passo: "))

contagem(int(n1), int(n2), int(n3))
