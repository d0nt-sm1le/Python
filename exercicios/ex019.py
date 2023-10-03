while True:
    tabuada = int(input("Digite um número para ver a sua tabua: "))
    if tabuada < 0:
        break
    print("--" * 20)
    for x in range(1, 11):
        print(f"{tabuada} x {x} = {tabuada * x}")
    print("--" * 20)
