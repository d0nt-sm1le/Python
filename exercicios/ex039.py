soma = 0
cont = 0
for x in range(1, 7):
    z = int(input(f"Digite {x} valor: "))
    if z % 2 == 0:
        soma += z
        cont += 1
print(f"Você informou {cont} números pares,  e a soma de todos os valores é igual a {soma}")
