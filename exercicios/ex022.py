valores = (int(input("Digite um valor: ")), int(input("Digite mais um valor: ")),
           int(input("Digite outro valor: ")), int(input("Digite o ultimo valor: ")),)

print(f"\nVocê digitou os valores: {sorted(valores)}")
print(f"O valor 9 apareceu {valores.count(9)} vez(es)")
print(f"O valor {valores[1]} apareceu na {valores.index(valores[1]) + 1} posição")
print(f"Os valores pares digitados foram: ", end="")

for n in range(0, 4):
    s = valores[n] % 2
    if s == 0:
        print(f"{valores[n]}", end=" ")
