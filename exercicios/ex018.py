from time import sleep

n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo valor: "))
mf = True

while mf:
    print("--" * 20)
    print("""    [1] somar
    [2] multiplicar
    [3] maior número
    [4] novos números
    [5] sair do programa""")

    m1 = int(input(">>> Qual a sua opção? "))

    if m1 == 1:
        print(f"O soma entre {n1} e {n2} é {n1 + n2}")
    elif m1 == 2:
        print(f"O resultado de {n1} x {n2} é {n1 * n2}")
    elif m1 == 3:
        if n1 < n2:
            print(f"Entre os número {n1} e {n2}, o número {n2} é maior!")
        else:
            print(f"Entre os números {n1} e {n2}, o número {n1} é maior!")
    elif m1 == 4:
        n1 = int(input("Digite um novo valor: "))
        n2 = int(input("Digite um segundo novo valor: "))
    elif m1 == 5:
        print("Finalizando o programa...")
        print(f"--" * 20)
        sleep(2)
        mf = False
    else:
        print("Valor invalido! Tente novamente")
