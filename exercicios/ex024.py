lista = list()

while True:
    lista.append(int(input("Digite um número: ")))
    s_n = str(input("Deseja continuar?[S/N] ")).upper()

    if s_n == "S":
        pass
    elif s_n == "N":
        break
    else:
        break

lista.sort()
lista.reverse()

print("==" * 20)
print(f"Você digitou {len(lista)} elementos!")
print(f"A ordem descrescente dessa lista é: {lista}")

print(f"O numero 5 ", end="")
for x in lista:
    if 5 in lista:
        print('está na lista. ')
        break
    else:
        print('não está na lista')
        break
