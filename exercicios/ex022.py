ns = (int(input("Digite um número: ")), int(input("Digite outro número: ")),
      int(input("Digite mais um número: ")), int(input("Digite um último número: ")))

print(f"""Você digitou os valores: {ns[0]}, {ns[1]}, {ns[2]} e {ns[3]}
O número 9 aparece {ns.count(9)} vezes""")

if 3 in ns:
      print(f"O valor 3 aparece na {ns.index(3) + 1} posição")
else:
      print("O valor 3 não aparece")
print("Os valores pares foram ",end=" ")

for n in ns:
      if n % 2 == 0:
            print(n, end="")