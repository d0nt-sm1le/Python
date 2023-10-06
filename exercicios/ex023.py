lista = list()
while True:
    n = int(input("Digite um número: "))
    if n not in lista:
        lista.append(n)
    else:
        print("valor duplicado não vou adicionar")

    sn = str(input("Deseja continuar?[S/N] ")).lower()
    if sn == 's':
        pass
    elif sn == 'n':
        break
print(f"Você digitou os valores {lista}")
