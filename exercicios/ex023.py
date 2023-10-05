ns = [int(input("Digite um valor para a posição 1: ")),
      int(input("Digite um valor para a posição 2: ")),
      int(input("Digite um valor para a posição 3: ")),
      int(input("Digite um valor para a posição 4: ")),
      int(input("Digite um valor para a posição 5: "))]
x = list()

x.insert(0, ns[0])
x.insert(1, ns[1])
x.insert(2, ns[2])
x.insert(3, ns[3])
x.insert(4, ns[4])

print("==" * 20)
print(f"Você digitou os valores:", x)
print(f"O maior valor digitado foi {max(x)} e está na posição {x.index(max(x)) + 1}")
print(f"O menor valor digitado foi {min(x)} e está na posição {x.index(min(x)) + 1}")
